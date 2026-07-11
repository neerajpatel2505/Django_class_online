from django.shortcuts import render,redirect
from .models import Register

# Create your views here.

def landing(req):
    return render(req,'landing.html')

def register(req):
    if req.method == "POST":
        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('city')
        p = req.POST.get('password')
        cp = req.POST.get('con_password')
        i = req.FILES.get('image')  
        r = req.FILES.get('resume')
        g = req.POST.get('gender')
        q = req.POST.get('qualification')
        d = req.POST.get('description')
        # print(n,e,c,i,r,g,q,d)
        user = Register.objects.filter(email=e)
        if user:
            msg = "User already exist"
            return render(req,'landing.html',{'msg':msg,'register':True})
        else:
            if p == cp:
                Register.objects.create(name=n,email=e,city=c,image=i,resume=r,password=p,gender=g,qualification=q,description=d)
                msg = "Registration Done........"
                return render(req,'landing.html',{'msg':msg,'login':True})
            else:
                msg = "Password and Conform+password not matched....."
                return render(req,'landing.html',{'msg':msg,'register':True})
    return render(req,'landing.html',{'register':True})

def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')

        user = Register.objects.filter(email=e)
        if not user:
            msg = "Email id is not register... Please register first..!!!!!!"
            return render(req,'landing.html',{'login':True,'msg':msg})
        else:
            user_data = Register.objects.get(email=e)
            db_user_pass = user_data.password 
            if db_user_pass == p :
                req.session['name'] = user_data.name
                req.session['email'] = user_data.email
                req.session['city'] = user_data.city
                # req.session['image'] = user_data.image
                # req.session['resume'] = user_data.resume
                req.session['password'] = user_data.password
                req.session['gender'] = user_data.gender
                req.session['qualification'] = user_data.qualification
                req.session['description'] = user_data.description
                # req.session['created_at'] = user_data.created_at
                # req.session['updated_at'] = user_data.updated_at
                return redirect('dashboard')
    return render(req,'landing.html',{'login':True})

def dashboard(req):
    if 'email' in req.session and 'password' in req.session :
        user_data = {
            'name':req.session['name'],
            'email':req.session['email'],
            'city':req.session['city'],
            # 'image':req.session['image'],
            # 'resume':req.session['resume'],
            'password':req.session['password'],
            'gender':req.session['gender'],
            'qualification':req.session['qualification'],
            'description':req.session['description'],
            # 'created_at':req.session['created_at'],
            # 'updated_at':req.session['updated_at'],
        }
        return render(req,'dashboard.html',{'data':user_data})
    msg = "Please login first"
    return render(req,'landing.html',{'login':True,'msg':msg})

def logout(req):
    if 'email' in req.session and 'password' in req.session :
        req.session.flush()
        return redirect('login')
    return redirect('login')