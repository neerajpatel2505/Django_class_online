from django.shortcuts import render
from django.contrib.sessions.models import Session
from .models import Student

# Create your views here.
def landing(req):
    # data = Student.objects.all()
    # print(data)

    # data = Student.objects.filter(stu_name="Raj")
    # data = Student.objects.filter(stu_city="Indore")
    # data = Student.objects.exclude(stu_city="Indore")
    # data = Student.objects.values()
    # data = Student.objects.values_list()
    # data = Student.objects.values("stu_name",'stu_city')
    # data = Student.objects.values_list("stu_name",'stu_city')
    # data = Student.objects.order_by("-stu_name")  # decending order
    data = Student.objects.order_by("stu_name")     # assending order


    print(data)
    return render(req,'landing.html')

    # 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 , 9, 10   10,9,8,7,6,5,4,3,2,1   10,9,8,7,6   6,7,8,9,10
    # Query syntex :- Model_name.objects.query() 
    
    # Student.objects.create(stu_name="Neeraj",stu_email="n@gmail.com", stu_city="Bhopal") 
    # Student.objects.bulk_create([Student(stu_name="Raj",stu_email="r@gmail.com", stu_city="Indore"),
    #                              Student(stu_name="Jai",stu_email="j@gmail.com", stu_city="Jabalpur"),
    #                              Student(stu_name="Vishnu",stu_email="v@gmail.com", stu_city="Dehli")
    #                              ])

    # data = Student.objects.earliest('stu_name')
    # print("Earliest:",data)

    # data = Student.objects.latest('stu_name')
    # print("Latest:",data)

    # data = Student.objects.earliest('stu_city')
    # print("Earliest_city:",data)
    
    # data = Student.objects.latest('stu_city')
    # print("Latest_city:",data)
    # return render(req,'landing.html')

   
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

