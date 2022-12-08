from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Criteria


@receiver(post_save, sender=CustomUser)
def post_save_create_criteria(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', instance)
    print('created', created)
    if created:
        Criteria.objects.create(user_id=instance)

