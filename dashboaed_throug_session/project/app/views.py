from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,"landing.html")


def register(req):
    if req.method=='POST':
        print(req.POST)
        n = req.POST.get('name')
        e = req.POST.get('email')
        ph = req.POST.get('phone')
        p = req.POST.get('password')
        cp = req.POST.get('confirm_password')
        d = req.POST.get('dob')
        g = req.POST.get('gender')
        c = req.POST.get('country')
        req.session['name'] = n
        req.session['email'] = e
        req.session['phone'] = ph
        req.session['password'] = p
        req.session['confirm_password'] = cp
        req.session['dob'] = d
        req.session['gender'] = g
        req.session['country'] = c
        return render(req,"landing.html",{'login':True})

    return render(req,'landing.html',{'register':True})