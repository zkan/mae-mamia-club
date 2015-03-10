from django.contrib import admin

from .models import Member
#from import_export.admin import ExportMixin
#from import_export import resources

#class MemberResource(resources.ModelResource):
#    class Meta:
#        model = Member
#        fields = (
#            'id',
#            'nickname',
#            'firstname',
#            'lastname',
#            'birthdate',
#            'gender',
#            'dad_name',
#            'mom_name',
#            'address',
#            'province',
#            'facebook_account',
#        )

#class MemberAdmin(ExportMixin, admin.ModelAdmin):
class MemberAdmin(admin.ModelAdmin):
    #resource_class = MemberResource
    list_per_page = 30
    list_display = ('nickname', 'firstname', 'lastname', 'birthdate', 'gender', 'province')
    #list_display_links = ('first_name', 'last_name')
    search_fields = ['nickname', 'firstname', 'lastname', 'birthdate', 'gender', 'province']
    list_filter = ('gender', )

admin.site.register(Member, MemberAdmin)
