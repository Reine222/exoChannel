from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','image',)
    readonly_fields = ['detail_image']

    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))

    def detail_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))




@admin.register(models.Tchater)
class TchaterAdmin(admin.ModelAdmin):
    list_display = ('utilisateur','message')
    



