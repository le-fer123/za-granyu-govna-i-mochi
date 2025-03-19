from django.db import models, IntegrityError
from django.urls import reverse
from django.utils.text import slugify
from .services import gen_str, file_upload_path




class File(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.SlugField(unique=True, blank=True)
    content = models.FileField(upload_to=file_upload_path, blank=True, null=True)
    content_text = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.url:
            try:
                if self.title:
                    slug = slugify(self.title, allow_unicode=True)
                    print(File.objects.filter(url=slug).count())
                    if File.objects.filter(url=slug).count() > 1:
                        raise ValueError("Файл с таким названием уже существует")
                else:
                    slug = gen_str()

                self.url = slug
            except Exception as e:
                raise ValueError("Файл с таким названием уже существует")
        try:
            super().save(*args, **kwargs)
        except IntegrityError as e:
            if "UNIQUE constraint failed: main_file.url" in str(e):
                raise ValueError("Файл с таким названием уже существует.") from e
            else:
                raise ValueError("Unknown error")

    def get_absolute_url(self):
        return reverse('filegetview', kwargs={'url': self.url})