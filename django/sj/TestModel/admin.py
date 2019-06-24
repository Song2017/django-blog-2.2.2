from django.contrib import admin
# Register your models here.
from TestModel.models import Test, Contact, Tag


# 内联(Inline)显示
class TagInLine(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name', )
    inlines = [TagInLine]
    # fields = ('name', 'email')
    fieldsets = (
        ['main', {
            'fields': ('name', 'email')
        }],
        [
            'advance',
            {
                'classes': ('collapse', ),  # CSS
                'fields': ('age', ),
            }
        ])


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
