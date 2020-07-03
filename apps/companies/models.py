from django.db import models
from django.utils.text import slugify

from apps.accounts.models import User


class Company(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200,
                                null=True)
    hourly_rate = models.CharField(max_length=100)
    employees = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    website = models.URLField()
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(models.Model):
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='reviews')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Comment by {self.user.name} on {self.company}'
