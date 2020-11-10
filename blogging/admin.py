from django.contrib import admin
from blogging.models import Post, Category


class ThemesInline(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ThemesInline]


class PostAdmin(admin.ModelAdmin):
    inlines = [ThemesInline]
    exclude = ('posts',)

# and a new admin registration
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

