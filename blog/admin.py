from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['id', 'title','content_size','status',
                    'created_at', 'updated_at']
    actions = ['make_published', 'make_draft']

    def content_size(self, post):
        return mark_safe('<strong>{}글자</strong>'.format(len(post.content)))
    content_size.short_description = '글자수'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 Pusblished 상태로 변경'.format(updated_count))
    make_published.short_description = 'Published 상태로 변경하기'
    
    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft 상태로 변경'.format(updated_count))
    make_draft.short_description = 'Draft 상태로 변경하기'


#admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_id', 'author', 'message']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ['name', ]
