from django.contrib import admin
from .models import Post, Reply

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'body', 'author')
	list_filter = ('title', 'author', 'added')
	search_fields = ('title', 'author')
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Reply)
# Register your models here.
