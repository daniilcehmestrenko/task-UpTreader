from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MainMenu(models.Model):
    name = models.CharField(
                max_length=50,
                verbose_name='Название меню'
            )

    def __str__(self):
        return self.name


class Menu(MPTTModel):
    mainmenu = models.ForeignKey(
                'MainMenu',
                on_delete=models.CASCADE,
                null=True,
                blank=True,
            )
    name = models.CharField(
                max_length=50,
                unique=True,
                verbose_name='Название'
            )
    parent = TreeForeignKey(
                'self',
                on_delete=models.CASCADE,
                null=True,
                blank=True,
                related_name='children'
            )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ('name',)
