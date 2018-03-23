from django.db import models

Kind = (
    ('h', 'Хищник'),
    ('t', 'Травоядное'),
    ('v', 'Всеядный')
)


class Animal(models.Model):
    name = models.CharField("Кличка", max_length=30)
    kind = models.CharField("Вид", choices=Kind, max_length=1)
    img = models.ImageField("Изображение", upload_to='animals', blank=True, null=True)

    def get_img_url(self):
        if self.img:
            return self.img.url
        return ''

    def get_kind(self):
        if self.kind == 'h':
            return 'ХИЩНИК'
        return self.kind

    def __str__(self):
        return self.name
