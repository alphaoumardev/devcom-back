from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Devcom  password reset Notice"),
        # message:
        email_plaintext_message,
        # from:
        "devalphaoumar@gmail.com",
        # to:
        [reset_password_token.user.email]
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="devcom", blank=True)
    bio = models.TextField()

    # @property
    # def my_posts(self):
    #     return self.feed_set.all()

    def __str__(self):
        return self.user.username
