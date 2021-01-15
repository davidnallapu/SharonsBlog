from django.contrib import admin

from .models import Article, Podcast, Contact

class ArticleAdmin(admin.ModelAdmin):
    list_display=('id','title','author')
    list_display_links = ('id','title')
    search_fields = ('name','email')
    list_per_page =15
admin.site.register(Article,ArticleAdmin)

class PodcastAdmin(admin.ModelAdmin):
    list_display=('id','title','author')
    list_display_links = ('id','title')
    search_fields = ('title','author')
    list_per_page =15
admin.site.register(Podcast,PodcastAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','website', 'message')
    list_display_links = ('id','name')
    search_fields = ('name','email')
    list_per_page =15
admin.site.register(Contact,ContactAdmin)

# Register your models here.
