import re
import shutil
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand

User = get_user_model()
FILENAME_PATTERN = re.compile(r'^(\d+)_(.+)\.[^.]+$')


class Command(BaseCommand):
    help = 'Copy seed profile images into media storage and link matching users.'

    def handle(self, *args, **options):
        seed_root = Path(settings.BASE_DIR) / 'seed_data' / 'media'
        if not seed_root.is_dir():
            self.stdout.write(self.style.WARNING(f'No seed media directory at {seed_root}'))
            return

        copied = 0
        skipped = 0
        linked = 0

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

        self.stdout.write(self.style.SUCCESS(
            f'Seed media: {copied} copied, {skipped} skipped, {linked} user(s) linked.'
        ))
