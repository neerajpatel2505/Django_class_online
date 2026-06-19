from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def set_cookies(req):
    if req.method == 'POST':
        # print(req.POST)
        n = req.POST.get('fname')
        e = req.POST.get('my_email')
        a = req.POST.get('my_age')
        print(n,e,a)
        response = render(req,'landing.html',{'set_done':True})
        response.set_cookie('name',n,secure=True)
        response.set_cookie('email',e,max_age=60*60*24)
        response.set_cookie('age',a,httponly=True)
        return response
    return render(req,'landing.html',{'set':True})

def get_cookies(req):
    print("get_cookies function called..........")
    print(req.COOKIES)
    # n = req.COOKIES.get('name')
    # e = req.COOKIES.get('email')
    # a = req.COOKIES.get('age')
    # t = req.COOKIES.get('csrftoken')

    # print(n,e,a,t)
    # data = {
    #     'name':n,
    #     'email':e,
    #     'age':a,
    #     'token':t
    # }
    data = {
        'name':req.COOKIES.get('name'),
        'email':req.COOKIES.get('email'),
        'age':req.COOKIES.get('age'),
        'token':req.COOKIES.get('csrftoken')
    }
    return render(req,'landing.html',{'data':data})


