from django.contrib import admin
from . models import Post, PostCategory, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'publishedon',
        'status',
    )
    list_filter = ('status', 'created', 'publishedon', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'url': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publishedon'
    ordering = ('status', 'publishedon')
admin.site.register(PostCategory)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')