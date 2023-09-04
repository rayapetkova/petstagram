from django.core.exceptions import ValidationError


def validate_files_size(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 5.0

    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Max file size is {megabyte_limit}MB")