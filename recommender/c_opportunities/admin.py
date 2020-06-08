from django.contrib import admin
from .models import ContractOpportunities

# Register your models here.
# source: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site

# define admin class for contract opportunities model
class ContractOpportunitiesAdmin(admin.ModelAdmin):
    pass

# register the admin class with the associated model
admin.site.register(ContractOpportunities, ContractOpportunitiesAdmin)
