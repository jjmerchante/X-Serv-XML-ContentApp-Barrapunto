from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseForbidden
from models import Page, News
from barrapunto_parser import getNews

# Create your views here.


def update(request):
    news = News(content=getNews())
    News.objects.all().delete()
    news.save()
    return HttpResponse(news.content)


def mostrar(request, resource):
    if request.method == "GET":
        try:
            news_content = News.objects.all()[0].content
        except (News.DoesNotExist, IndexError):
            news_content = "You must first /update to get the news"
        try:
            fila = Page.objects.get(name=resource)
            return HttpResponse(fila.page + "<br><hr>" + news_content)
        except Page.DoesNotExist:
            return HttpResponseNotFound('Page not found: ' + resource +
                                        "<br><hr>" + news_content)
        except Page.MultipleObjectsReturned:
            return HttpResponseNotFound('Server allocated more than \
                    one page for that resource')
    elif request.method == "PUT":
        newpage = Page(name=resource, page=request.body)
        newpage.save()
        return HttpResponse("New page added:\n" + request.body)
    else:
        return HttpResponseForbidden("Method not allowed")
