from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def pqr(req):
    # print("Hello....")
    # print(req.method)       # req kis method ke sath aa rahi hai....
    # print(req.GET)          # GET method ke sath koi data hai kya...
    # print(req.POST)         # POST method ke sath koi data hai kya...
    # print(req.FILES)        # Koi binary data hai kya (image,audio,vedio, files.... )
    # print(req.COOKIES)      # cookies me koi data hai kya.....
    # print(req.META)
    if req.method == "POST":
        x = req.POST.get('data') # <input type="text" name="data" id="">
        print(x)
        return render(req,'landing.html',{'data':x})

    