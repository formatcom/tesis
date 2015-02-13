from django.contrib import admin
from .models        import Dewey

class DeweyAdmin(admin.ModelAdmin):
	list_display  = ('description', )
	search_fields = ('id', 'description', )

admin.site.register(Dewey, DeweyAdmin)
