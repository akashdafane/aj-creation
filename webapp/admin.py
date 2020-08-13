from django.contrib import admin
from webapp.models import ContactForm

# Register your models here.
class modelAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','message']
admin.site.register(ContactForm,modelAdmin)
