from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.task.models import Task
from apps.task.mail import notify_by_mail

@receiver(post_save, sender=Task)
def notify_task_updated(sender, instance, created, **kwargs):
    # 僅修改時(非新建)
    if not created:
        if not notify_by_mail(instance):
            "mail Error."