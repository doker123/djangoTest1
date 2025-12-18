from django.apps import AppConfig
from django.db.models.signals import post_migrate


class LaboratoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'laboratory'

    def ready(self):
        post_migrate.connect(create_groups, sender=self)


def create_groups(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from .models import Employee


    hr_group, _ = Group.objects.get_or_create(name='Отдел кадров')
    trade_union_group, _ = Group.objects.get_or_create(name='Профком')


    content_type = ContentType.objects.get_for_model(Employee)
    permissions = Permission.objects.filter(content_type=content_type)


    for perm in permissions:
        hr_group.permissions.add(perm)


    view_permissions = permissions.filter(codename__startswith='view')
    for perm in view_permissions:
        trade_union_group.permissions.add(perm)
