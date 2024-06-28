import logging
from typing import Any, Type

from django.db.models import Model
from django.db.models.signals import post_save
from django.dispatch import receiver

from config.settings.base import AUTH_USER_MODEL
from core_apps.profiles.models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender: Type[Model], instance: Model, created: bool, **kwargs: Any) -> None:

    if created:
        Profile.objects.create(user=instance)
        logger.info(f"Created profile for {instance.first_name} {instance.last_name}")
    else:
        logger.info(f"Profile for {instance.first_name} {instance.last_name} already exists")
