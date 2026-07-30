import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Copy seed PDFs into PDF_ROOT, skipping files that already exist."

    def handle(self, *args, **options):
        seed_root = Path(settings.BASE_DIR) / 'seed_data' / 'pdf'
        pdf_root = Path(settings.PDF_ROOT)

        if not seed_root.is_dir():
            self.stdout.write(self.style.WARNING(f"No seed PDF directory at {seed_root}"))
            return

        copied = 0
        skipped = 0
        for src in seed_root.rglob('*.pdf'):
            dest = pdf_root / src.relative_to(seed_root)
            if dest.exists():
                skipped += 1
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            copied += 1

        self.stdout.write(self.style.SUCCESS(
            f"Seed PDFs: {copied} copied, {skipped} skipped (already present)."
        ))
