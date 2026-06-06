from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.

def home(req):
    # return HttpResponse("<h1>Hello World..........!!!!!!!!!!!!</h1> <h2>Hello World..........!!!!!!!!!!!!</h2>")
    # return HttpResponse('''
    #                     <!doctype html>
    #                     <html lang="en">
    #                     <head>
    #                         <!-- Required meta tags -->
    #                         <meta charset="utf-8">
    #                         <meta name="viewport" content="width=device-width, initial-scale=1">

    #                         <!-- Bootstrap CSS -->
    #                         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    #                         <title>Hello, world!</title>
    #                     </head>
    #                     <body>
    #                         <nav class="navbar navbar-expand-lg navbar-light bg-light">
    #                     <div class="container-fluid">
    #                         <a class="navbar-brand" href="#">Navbar</a>
    #                         <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    #                         <span class="navbar-toggler-icon"></span>
    #                         </button>
    #                         <div class="collapse navbar-collapse" id="navbarSupportedContent">
    #                         <ul class="navbar-nav me-auto mb-2 mb-lg-0">
    #                             <li class="nav-item">
    #                             <a class="nav-link active" aria-current="page" href="#">Home</a>
    #                             </li>
    #                             <li class="nav-item">
    #                             <a class="nav-link" href="#">Link</a>
    #                             </li>
    #                             <li class="nav-item dropdown">
    #                             <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
    #                                 Dropdown
    #                             </a>
    #                             <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
    #                                 <li><a class="dropdown-item" href="#">Action</a></li>
    #                                 <li><a class="dropdown-item" href="#">Another action</a></li>
    #                                 <li><hr class="dropdown-divider"></li>
    #                                 <li><a class="dropdown-item" href="#">Something else here</a></li>
    #                             </ul>
    #                             </li>
    #                             <li class="nav-item">
    #                             <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
    #                             </li>
    #                         </ul>
    #                         <form class="d-flex">
    #                             <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
    #                             <button class="btn btn-outline-success" type="submit">Search</button>
    #                         </form>
    #                         </div>
    #                     </div>
    #                     </nav>

    #                         <!-- Optional JavaScript; choose one of the two! -->

    #                         <!-- Option 1: Bootstrap Bundle with Popper -->
    #                         <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    #                         <!-- Option 2: Separate Popper and Bootstrap JS -->
    #                         <!--
    #                         <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    #                         <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    #                         -->
    #                     </body>
    #                     </html>
    #                     ''')
    
    return render(req, 'app1/home.html')
    # return redirect("https://www.google.com/") # external url
    # return redirect("home1") # internal url

def home1(req):
    return HttpResponse("<h1>From redirect response...............</h1>")

# def landing(req):
#     xyz = {
#         "name":"Neeraj",
#         "age": 37,
#         "hobbies": ["coding","playing","travelling"]
#     }
#     return render(req,'landing.html', xyz)

# def landing(req):
#     return render(req,'landing.html', {"name":"Neeraj",
#                                        "age": 37,
#                                        "hobbies": ["coding","playing","travelling"]})

def landing(req):
    user = [
        {"name":"Neeraj",
            "email": "neeraj@example.com",
            "hobbies": ["coding","playing","travelling"]
        }]
    return render(req,'app1/landing.html', {"user": user})


# { key : [{"name":"Neeraj","email": "neeraj@example.com","hobbies": ["coding","playing","travelling"]},{"name":"Neeraj","email": "neeraj@example.com","hobbies": ["coding","playing","travelling"]}] }

# { key : [ value1, value2]}

# for i in [value1, value2]:
#     print(i)

# output value1
#        value2

def my_json_response(req):
    # recomended to return dict object in JsonResponse
    # data = {'name': "Neeraj", "age": 37, 'hobbies': ['coding', 'playing', 'travelling'],'x':True,'y':False,'z':None}
    # return JsonResponse(data)

    ## list_of_dict = [{},{},{},...........]
    data = [{'name': "Neeraj", "age": 37, 'hobbies': ['coding', 'playing', 'travelling']},{'name':"Rahul","age": 25, 'hobbies': ['reading', 'swimming']}]
    return JsonResponse(data, safe=False)

    # data = 10
    # return JsonResponse(data,safe=False) #In order to allow non-dict objects to be serialized set the safe parameter to False.

    # data = "Python language"
    # return JsonResponse(data,safe=False)
    
    # data = ['Python','Java','C++','JavaScript']
    # return JsonResponse(data,safe=False)
    
    # data = ('Python','Java','C++','JavaScript')
    # return JsonResponse(data,safe=False)

    ## Object of type set is not JSON serializable (Due to unordered collection)
    # data = {'Python','Java','C++','JavaScript'}
    # return JsonResponse(data,safe=False)
    
    ## Object of type frozenset is not JSON serializable (Due to unordered collection)
    # data = frozenset({'Python','Java','C++','JavaScript'})
    # return JsonResponse(data,safe=False)
    
    # return JsonResponse({'name': True, "age": False, '''hobbies''': None})


def dynamic_url1(req, age):
    print(age)
    print(type(age))
    # return HttpResponse(f"<h1>Dynamic URL with age: {age}</h1>")
    return render(req,'app2/dynamic_url1.html',{"data": age})

def dynamic_url2(req, name):
    print(name)
    print(type(name))
    # return HttpResponse(f"<h1>Dynamic URL with name: {name}</h1>")
    return render(req,'app2/dynamic_url2.html',{"data": name})

def dynamic_url3(req, xyz):
    print(xyz)
    print(type(xyz))
    # return HttpResponse(f"<h1>Dynamic URL with slug: {xyz}</h1>")
    return render(req,'app1/dynamic_url3.html',{"data": xyz})

# def my_redirect(req):
#     # return redirect("https://www.google.com/",name) # external url
#     name="Neeraj"
#     return redirect("home2",name) # internal url

def my_redirect(req):
    # return redirect("https://www.google.com/",name) # external url
    name="Neeraj"
    # redirect(to, *args, **kwargs)
    # redirection dose not support both *args and **kwargs at a time.
    # return redirect("home2",10,data=name) # Don't mix *args and **kwargs in call to reverse()!
    return redirect("home2",data=name)


# def home2(req,xyz):
#     return HttpResponse(f"<h1>Value {xyz} comes from redirect response...............</h1>")

def home2(req,data):
    return HttpResponse(f"<h1>Value {data} comes from redirect response...............</h1>")