from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import pre_save, post_save

from engine.utils import unique_referral_code_generator


# Create your models here.

class UserQueryset(models.query.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class UserManager(BaseUserManager):
    def get_queryset(self):
        return UserQueryset(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def create_user(self, username, mobile, email=None, password=None):
        # check user exists
        user_qs = self.filter(username=username, mobile=mobile)
        if user_qs.exists():
            return user_qs.first()
        # create user if not exist
        user_obj = self.model(
            username=username,
            mobile=mobile,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.is_active = True
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, mobile, password=None):
        user = self.create_user(
            username,
            mobile,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=60, blank=True, unique=True)

    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=16, unique=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    mobile_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    referral_code = models.CharField(max_length=60, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    # USERNAME_FIELD and password are required by default.
    REQUIRED_FIELDS = ['mobile', ]

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # def is_admin(self):
    #     return self.is_admin

    # def is_staff(self):
    #     return self.is_staff

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class UserVerification(models.Model):
    STATUS = (
        ("pending", "Pending"),
        ("verified", "Verified"),
        ("unverified", "unVerified"),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="verification")
    nin = models.CharField(max_length=60, blank=True, null=True)
    status = models.CharField(max_length=60, choices=STATUS, default="unverified")
    
    objects = models.Manager()

    def __str__(self):
        return f"{self.user} - {self.status}"
    


def user_pre_save_receiver(instance, *args, **kwargs):
    # Generate referral code
    if not instance.referral_code:
        instance.referral_code = unique_referral_code_generator(instance)

    # Get or Create UserVerification object
    UserVerification.objects.get_or_create(user=instance)
        

pre_save.connect(user_pre_save_receiver, sender=User)
