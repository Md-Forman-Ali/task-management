from django.db.models.signals import pre_save,post_save,post_delete,pre_delete,m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from tasks.models import Task


@receiver(m2m_changed, sender = Task.assigned_to.through)

def notify_employees_on_task_creation(sender, instance,action, **kwargs):
    if action == 'post_add':
        print(instance, instance.assigned_to.all())
        assigned_emails = [emp.email for emp in instance.assigned_to.all()]
        print("Checking....", assigned_emails)
        send_mail(
            "New Task Assign",
            f'You Have Been Assign To The Task :{instance.title}',
            "ridoykhanna634@gmail.com",
            assigned_emails,
            fail_silently = False
        )

@receiver(post_delete, sender= Task)

def delete_associate_details(sender, instance, **kwargs):
    if instance.details:
        print(instance)
        instance.details.delete()

        print("Delete Successfully ")

