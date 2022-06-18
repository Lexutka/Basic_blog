from django.contrib import admin
from .models import Post, Comment


admin.site.register(Post)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('author', 'body')
admin.site.register(Comment, CommentAdmin)