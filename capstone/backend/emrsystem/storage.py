from django.conf import settings
from django.core.files.storage import FileSystemStorage


class OverwriteMediaStorage(FileSystemStorage):
    """Local media storage that replaces existing files (same name as profile re-uploads)."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('location', settings.MEDIA_ROOT)
        kwargs.setdefault('base_url', settings.MEDIA_URL)
        super().__init__(*args, **kwargs)

    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            self.delete(name)
        return name
