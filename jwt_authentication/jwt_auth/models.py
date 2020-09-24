from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Role(models.Model):
    role_name = models.CharField(null=True, blank=True, max_length=30)
    role_description = models.CharField(null=True, blank=True, max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        ordering = ['pk']

    def __str__(self):
        """Return role name."""
        return str(self.role_name)


class UserPermissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)

    class Meta:
        managed = True
        ordering = ['pk']
        unique_together = ('role', 'user')

    def __str__(self):
        """Return role id and user id."""
        return str(self.role) + " | " + str(self.user)


class UserInfo(UserPermissions):
    GENDER_OPTIONS = (
        ('male', 'male'),
        ('female', 'female')
    )
    mobile = models.CharField(max_length=20, blank=False, null=False, unique=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_OPTIONS, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_active = models.BooleanField(null=True)

    class Meta:
        managed = True
        ordering = ['pk']

    def __str__(self):
        """Return user id."""
        return str(self.user)














