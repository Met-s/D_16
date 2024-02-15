from django.contrib import admin
from .models import Post, Reply


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_author', 'post_title', 'post_category',
                    'post_text', 'post_date')
    list_filter = ('post_author', 'post_category', 'post_date')


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('reply_author', 'reply_post', 'reply_text',
                    'reply_text', 'reply_date', 'status')
    list_filter = ('reply_author', 'reply_post', 'reply_date', 'status')


admin.site.register(Post, PostAdmin)
admin.site.register(Reply, ReplyAdmin)
