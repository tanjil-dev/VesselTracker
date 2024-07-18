from django import template
from django.utils import timezone

register = template.Library()

@register.filter(name='is_past')
def is_past(value):
    """Check if a datetime value is in the past."""
    value = timezone.make_aware(value) if timezone.is_naive(value) else value
    return value < timezone.now()

@register.filter(name='is_future')
def is_future(value):
    """Check if a datetime value is in the future."""
    value = timezone.make_aware(value) if timezone.is_naive(value) else value
    return value > timezone.now()