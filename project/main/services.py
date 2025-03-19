import os
import random
import string


def gen_str(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def file_upload_path(instance, filename):
    return os.path.join('uploads', instance.url, filename)