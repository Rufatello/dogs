from django import template

register = template.Library()
@register.filter()
def load_image(val):
    if val:
        return f'/media/{val}'
