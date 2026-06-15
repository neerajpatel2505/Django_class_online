from django.shortcuts import render

# Create your views here.
def landing(req):
    data = {"name":"Neeraj","city":"Bhopal"}
    # return render(req,'landing.html')
    # return render(req,'landing.html',{"xyz":data})
    # return render(req,'landing.html',{"pqr":[10,20,30,40,50]}) # for with list of object
    # return render(req,'landing.html',{"pqr":"Hello World"})

    # forloop.counter
    return render(req,'landing.html',{"pqr":"Hello World"})
    

