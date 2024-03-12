# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model
# from clients.models import Client
# from employees.models import Employee
# from employers.models import Employer
#
# User = get_user_model()
#
#
# @receiver(post_save, sender=Client)
# def update_user_role_to_client(sender, instance, **kwargs):
#     instance.user.role = 'client'
#     instance.user.save()
#
#
# @receiver(post_save, sender=Employee)
# def update_user_role_to_employee(sender, instance, **kwargs):
#     instance.user.role = 'employee'
#     instance.user.save()
#
#
# @receiver(post_save, sender=Employer)
# def update_user_role_to_employer(sender, instance, **kwargs):
#     instance.user.role = 'employer'
#     instance.user.save()
