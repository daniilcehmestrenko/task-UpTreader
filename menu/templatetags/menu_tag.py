from django import template

from menu.models import Menu


register = template.Library()

@register.simple_tag()
def draw_menu(name):

    return Menu.objects.filter(mainmenu__name=name)
