from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=150, unique=True)
    code = models.CharField(max_length=15, unique=True)
    description = models.TextField(blank=True, default='')
    established_year = models.PositiveIntegerField(default=2000)
    head_of_department = models.CharField(max_length=120, blank=True, default='')
    building_block = models.CharField(max_length=50, blank=True, default='Main Block')
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return f"{self.code} - {self.name}"
