from django.contrib import admin

from .models import District,Person,Branch

# Register your models here.


# admin.site.register(Accessories)
admin.site.register(Branch)

admin.site.register(District)




class PersonTable(admin.ModelAdmin):
    list_display = ('id','name','dob','mobile','email','district','branch')

admin.site.register(Person,PersonTable)

