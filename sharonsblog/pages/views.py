from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.http import HttpResponse
from django.contrib import messages
from . models import Article, Podcast, Contact

def index(request):
    articles= Article.objects.order_by('-date')
    paginator =Paginator(articles,4)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)
    context = {
        'articles':paged_articles
    }
    return render(request,'pages/index.html', context)

def about(request):
    return render(request,'pages/about.html')

def support(request):
    if request.method =='POST':
        name = request.POST['cName']
        email = request.POST['cEmail']
        website = request.POST['cWebsite']
        message = request.POST['cMessage']
        contact = Contact(name=name, email=email, website=website, message=message)
        contact.save()
    return render(request,'pages/support.html')

def podcasts(request):
    podcasts= Podcast.objects.order_by('-date')
    paginator =Paginator(podcasts,5)
    page = request.GET.get('page')
    paged_podcasts = paginator.get_page(page)
    context = {
        'podcasts':paged_podcasts
    }
    return render(request,'pages/podcasts.html', context)

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context={
        'article':article
    }
    return render(request,'pages/article.html',context)


