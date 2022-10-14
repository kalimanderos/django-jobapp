from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description"
]



# Create your views here.
# def hello(request):
#     return HttpResponse("<h3>Hello World</h3>")

def job_list(request):
    # <ul><li>Job 1</li> <li>Job 2</li> <li>Job 3</li></ul>
    list_of_jobs = "<ul>"
    for j in job_title:
        job_id = job_title.index(j)
        list_of_jobs += f"<li><a href='job/{job_id}'>{j}</a></li>"
    list_of_jobs += "</ul>"
    return HttpResponse(list_of_jobs)


def job_detail(request, id):
    print(type(id))

    if id == 0:
        return redirect("/")
    return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
    return HttpResponse(return_html)

    # "<domain>/job/1" --> Job detail page