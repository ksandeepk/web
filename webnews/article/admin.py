
# Register your models here.
from django.contrib import admin

from .models import Article,Reporter

class ArticleDetails(admin.ModelAdmin):
    list_display=('id','heading','body','image','created','reporter')
    search_fields=('heading','created','reporter__name')

admin.site.register(Article,ArticleDetails) 

class ReporterDetails(admin.ModelAdmin):
    list_display=('id','name','n_articles')
    search_fields=('name',)


admin.site.register(Reporter,ReporterDetails)    
