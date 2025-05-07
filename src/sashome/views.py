import pathlib

from django.shortcuts import render
from django.http import HttpResponse #render is also present in django.http

from visits.models import PageVisit

this_dir= pathlib.Path(__file__).resolve().parent


def my_home_page_view(request, *args, **kwargs):

    qs=PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=request.path)
    my_title="nothing here go back home"
    my_context={
        "page_title":my_title,
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count()*100)/qs.count(),
        "total_visit_count": qs.count()
    }
    path=request.path
    print("path", path)
    html_template="home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)



def my_old_home_page_view2(request, *args, **kwargs):
    my_title="My page"
    my_context={
        "page_title":my_title
    }
    html__=f"""
        <!DOCTYPE html>
        <html>
        <body>
            <h1> {my_title} has anything? </h1>
        </body>
        </html>
        """.format(**my_context)   #page_title=my_title
    return HttpResponse(html__)


def my_old_home_page_view1(request, *args, **kwargs):
    print(this_dir)
    html_=""
    html_file_path=this_dir/ "home.html"
    html_=html_file_path.read_text()
    return HttpResponse(html_)
    # return "Hello world"



def my_old_home_page_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")
    # return "Hello world"