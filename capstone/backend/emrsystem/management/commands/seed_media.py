import re
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand

User = get_user_model()
FILENAME_PATTERN = re.compile(r'^(\d+)_(.+)\.[^.]+$')


class Command(BaseCommand):
    help = 'Copy seed profile images into media storage, link users, and drop missing uploads.'

    def handle(self, *args, **options):
        seed_root = Path(settings.BASE_DIR) / 'seed_data' / 'media'
        copied = 0
        skipped = 0
        linked = 0
        cleared = 0

        if seed_root.is_dir():
            for src in sorted(seed_root.iterdir()):
                if not src.is_file():
                    continue

                name = src.name
                if default_storage.exists(name):
                    skipped += 1
                else:
                    with src.open('rb') as handle:
                        default_storage.save(name, ContentFile(handle.read()))
                    copied += 1

                match = FILENAME_PATTERN.match(name)
                if not match:
                    continue

                user_id, username = match.groups()
                try:
                    user = User.objects.get(id=user_id, username=username)
                except User.DoesNotExist:
                    self.stdout.write(self.style.WARNING(
                        f'No user for seed image {name} (expected id={user_id}, username={username}).'
                    ))
                    continue

                current_name = user.profilePic.name if user.profilePic else ''
                if current_name != name:
                    user.profilePic = name
                    user.save(update_fields=['profilePic'])
                    linked += 1
        else:
            self.stdout.write(self.style.WARNING(f'No seed media directory at {seed_root}'))

        # Ephemeral disk (e.g. Render sleep/wake): DB outlives files — clear stale refs.
        for user in User.objects.all():
            if not user.profilePic:
                continue
            if not default_storage.exists(user.profilePic.name):
                user.profilePic = ''
                user.save(update_fields=['profilePic'])
                cleared += 1

        self.stdout.write(self.style.SUCCESS(
            f'Seed media: {copied} copied, {skipped} skipped, {linked} linked, {cleared} stale cleared.'
        ))
