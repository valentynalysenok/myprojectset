from django.db import models
from django.utils.text import slugify

from apps.companies.models import Company


class Project(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE)
    technologies = models.ManyToManyField('Technology',
                                          related_name='projects')
    industries = models.ManyToManyField('Industry',
                                        related_name='projects')
    description = models.TextField()
    notes = models.TextField(blank=True,
                             null=True)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Technology(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Technology, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Industry(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Industry'
        verbose_name_plural = 'Industries'
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Industry, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
