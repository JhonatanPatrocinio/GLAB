import os
import uuid

from django.utils.deconstruct import deconstructible


@deconstructible
class UploadToFactory:

    def __init__(self, prefix=None):
        self.prefix = prefix

    def __call__(self, instance, filename):
        instance.original_file_name = filename
        filename, extension = os.path.splitext(filename)
        path = [str(uuid.uuid4())]
        if self.prefix:
            path.insert(0, self.prefix)
        return os.path.join(*path) + extension.lower()
