from django.shortcuts import render
from django.contrib.sessions.models import Session


# Create your views here.
def landing(req):
    return render(req,'landing.html')

def set(req):
    if req.method == 'POST':
        # print(req.POST)
        n = req.POST.get('fname')
        e = req.POST.get('my_email')
        a = req.POST.get('my_age')
        print(n,e,a)
        req.session['name'] = n
        req.session['email'] = e
        req.session['age'] = a
        # req.session.set_expiry(31536000) # 1-year
        req.session.set_expiry(10) # 1-year
        return render(req,'landing.html',{'set_data':True})
    return render(req,'landing.html',{'set':True})

def get(req):
    data = {
        'name':req.session.get('name','Guest'),
        'email':req.session.get('email','guest@gmail.com'),
        'age':req.session.get('age','0'),
    }
    return render(req,'landing.html',{'data':data})

def delete(req):
    # if 'name' in req.COOKIES:
    #     response = render(req,'landing.html',{'msg':" name data deleted from cookies..."})
    #     response.delete_cookie('name')
    #     return response
    n = req.session.get('name')
    e = req.session.get('email')
    a = req.session.get('age')
    print(n,e,a)
    if 'name' in req.session and 'age' in req.session and 'email' in req.session:
        # del req.session['name']
        # del req.session['age']
        # del req.session['email']
        # req.session.clear() # all session data clear. dose not remove session id.
        req.session.flush() # remove session id.

        return render(req,'landing.html',{'msg':"Sessions are deleted...."})
    
    else:
        req.session.clear_expired() # remove expired sessionid from database
        # Session.objects.all().delete() # delete all session object from database
        return render(req,'landing.html',{'msg':"Sessions are not found"})   

