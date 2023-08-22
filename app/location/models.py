from django.db import models
from django.urls import reverse


class Location(models.Model):
    name = models.CharField(
        'Название локации',
        max_length=20,
        help_text='Здесь содержится название вашей локации'
    )

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('location', kwargs={'location_slug': self.slug})

    class Meta:
        verbose_name = 'Location'


class Hood(models.Model):
    location = models.ForeignKey(
        Location,
        related_name='Location',
        on_delete=models.PROTECT,
    )
    name = models.CharField(
        'Название худа',
        max_length=50
    )
    description = models.TextField(
        'Описание локации',
        max_length=1000
    )
    status_zone = (
        ('Красная зона', 'Красная зона'),
        ('Желтая зона', 'Желтая зона'),
        ('Зелёная зона', 'Зелёная зона'),
    )
    status = models.CharField(
        verbose_name='Зона',
        choices=status_zone,
        max_length=30,
    )
    color_code = (
        ('bg-red', 'bg-red'),
        ('bg-yellow', 'bg-yellow'),
        ('bg-green', 'bg-green'),
    )
    color = models.CharField(
        verbose_name='Зона',
        choices=color_code,
        max_length=12,
    )
    fraction_name = models.CharField(
        'Название фракции',
        max_length=120,
        default='Неизвестно'
    )
    fraction_link = models.CharField(
        'Ссылка на фракцию',
        null=True,
        max_length=300,
        default='#'
    )
    image = models.ImageField(
        upload_to='images'
    )

    def __str__(self):
        return f'{self.name} - {self.status}'

    class Meta:
        verbose_name = 'Hood'
