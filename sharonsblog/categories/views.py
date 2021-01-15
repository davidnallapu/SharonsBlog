from django.shortcuts import render
from pages.models import Article
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

def category(request, category):
    if '-' in category:
        category=category.replace('-',' ')
    articles = Article.objects.order_by('-date').filter(category1=category)
    articles|=Article.objects.order_by('-date').filter(category2=category)
    articles|=Article.objects.order_by('-date').filter(category3=category)
    paginator =Paginator(articles,4)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)
    context = {
        'articles':paged_articles
    }
    if(articles):
        return render(request,'pages/index.html', context)
    else:
        return render(request,'pages/comingsoon.html')




