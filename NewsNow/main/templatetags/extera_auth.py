from django import template
from django.contrib.auth.models import Group

register=template.Library()

#codes executes when you wants to checkin

@register.filter(name='has_group')
def has_group(user,group__name):
    return user.groups.filter(name=group__name).exists()#check the group exists for the user