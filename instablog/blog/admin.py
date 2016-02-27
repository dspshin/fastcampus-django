from django.contrib import admin
from .models import Post, Comment, Category
# inline comment 기능추가
class CommentInlineAdmin(admin.StackedInline):
	model = Comment
	extra = 1
class PostAdmin(admin.ModelAdmin):
	# 컬럼 추가
	list_display = ('pk', 'title', 'created_at',)
	# 링크가 걸리는 컬럼 정릐
	list_display_links = ('pk', 'title',)
	ordering = ('-id',)
	# inline comment 추가
	inlines = [CommentInlineAdmin,]
	# 검색기능 추가
	search_fields = ('title', 'content',)
	# 우측에 필터 추가
	list_filter = ('title','created_at',)
	# 계층적으로 보여주기 기능 추가
	date_hierarchy = 'created_at'
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)