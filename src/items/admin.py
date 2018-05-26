from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Item, Category, OptionGroup, Option, ItemOptions
from .forms import ItemModelForm
class ItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    #readonly_fields = ['updated', 'timestamp', 'added_by', 'last_edited_by']
    readonly_fields = ['updated', 'timestamp']
    form = ItemModelForm
    class Meta:
        model = Item


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(OptionGroup)
admin.site.register(Option)
admin.site.register(ItemOptions)
