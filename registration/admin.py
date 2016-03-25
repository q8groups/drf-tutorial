from django.contrib import admin
from    .models import Company,Customer

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','active')
    search_fields = ('name',)
    filter_horizontal = ['users',]
    list_filter = ('active',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Customer)