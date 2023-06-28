from django.shortcuts import render, redirect

from Adminside.models import catdb, prodb, contactdb
from Frontendapp.models import Customerdb, checkoutdetailsdb
from django.contrib import messages


# Create your views here.
def homepage(request):
    data = catdb.objects.all()
    return render(request, "Home.html", {'data': data})


def aboutpage(request):
    data = catdb.objects.all()
    return render(request, "Aboutus.html", {'data': data})


def contactpage(request):
    data = catdb.objects.all()
    return render(request, "Contact.html", {'data': data})


def productdisplay(request, itemCatg):
    data = catdb.objects.all()
    if itemCatg == "PROTEIN":
        itemCatg = "Protein"
    elif itemCatg == "PRE-WORKOUT":
        itemCatg = "Pre-Workout"
    elif itemCatg == "CREATINE":
        itemCatg = "Creatine"
    elif itemCatg == "MASS GAINERS":
        itemCatg = "Mass Gainers"
    elif itemCatg == "FAT LOSS":
        itemCatg = "Fat loss"
    elif itemCatg == "TEST BOOSTERS":
        itemCatg = "Test Boosters"

    products = prodb.objects.filter(Category=itemCatg)
    context = dict(products=products, catg=itemCatg, data=data)
    return render(request, "Productdisplay.html", context)


def productdetails(request, dataid):
    products = prodb.objects.get(id=dataid)
    data = catdb.objects.all()
    context = {
        'data': data,
        'pro': products
    }
    return render(request, 'Singleproduct.html', context)


def reglogdisplay(req):
    data = catdb.objects.all()

    return render(req, "Registration&login.html", {'data': data})


def customerdata(request):
    if request.method == "POST":
        na = request.POST.get('uname')
        em = request.POST.get('email')
        ps = request.POST.get('password')
        cp = request.POST.get('cpassword')

        obj = Customerdb(username=na, email=em, password=ps, confirmpassword=cp)
        obj.save()
        return redirect(reglogdisplay)


def customerlogin(request):
    if request.method == 'POST':
        username_r = request.POST.get("uname")
        password_r = request.POST.get("password")
        if Customerdb.objects.filter(username=username_r, password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r

            return redirect(homepage)
        else:
            return render(request, 'Registration&login.html', {'msg': "sorry....invalid password or username"})


def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(homepage)


def contactsave(arg):
    if arg.method == "POST":
        na = arg.POST.get('name')
        em = arg.POST.get('email')
        sub = arg.POST.get('subject')
        msg = arg.POST.get('message')

        obj = contactdb(Name=na, Email=em, Subject=sub, Message=msg)
        obj.save()
        return redirect(contactpage)


def displaycontact(request):
    data = contactdb.objects.all()
    return render(request, "Display Contactus.html", {'data': data})


def Addtocart(request, dataid):
    data = catdb.objects.all()
    products = prodb.objects.get(id=dataid)
    context = {
        'data': data,
        'pro': products
    }

    return render(request, "Add Cart.html", context)


def CheckOut(req):
    data = catdb.objects.all()
    return render(req, "Checkout.html", {'data': data})


def Checkoutsave(req):
    if req.method == "POST":
        fn = req.POST.get('fname')
        ln = req.POST.get('lname')
        ad = req.POST.get('address')
        ct = req.POST.get('tcity')
        ps = req.POST.get('pst')
        ph = req.POST.get('phn')
        em = req.POST.get('email')
        obj = checkoutdetailsdb(Firstname=fn, Lastname=ln, Address=ad, City=ct, Postcode=ps, Phone=ph, Email=em)
        obj.save()
        messages.success(req, "Order Placed Succesfully")
        return redirect(homepage)
