from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from random import randint

# Create your views here.

def Indexpage(request):
    return render(request,"app/index.html")


def DoctorRegisterPage(request):
    return render(request,"app/doctorregister.html")


def PharmacyRegisterPage(request):
    return render(request,"app/pharmaregister.html")


def PaitentRegisterPage(request):
    return render(request,"app/paitentregister.html")

def Loginpage(request):
    return render(request,"app/login.html")




#def PaitentProfilePage(request):
 #   return render(request,"app/patient-profile.html")

#def DoctorProfilePage(request):
 #   return render(request,"app/doctor-profile.html")

def InsertData(request):
    try:
        if request.POST['role']=="Doctor":
            role = request.POST['role']
            fname = request.POST['fname']   
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['pass']
            cpassword = request.POST['cpass']
            
            user = User.objects.filter(Email=email)
            if user:
                message = "Email already exits"
                return render(request,"app/doctorregister.html",{'msg':message})
            else:
                if password==cpassword:
                    otp = randint(10000,99999)
                    newuser = User.objects.create(Email=email,Password=password,Role=role,Otp=otp)
                    newdoc = Doctor.objects.create(user_id=newuser,Firstname=fname,Lastname=lname)
                    return render(request,"app/login.html")
                else:
                    message = "password and conform password does not match"
                    return render(request,"app/doctorregister.html",{'msg':message})

        elif request.POST['role']=="Patient":
                    role = request.POST['role']
                    fname = request.POST['fname']   
                    lname = request.POST['lname']
                    email = request.POST['email']
                    password = request.POST['pass']
                    cpassword = request.POST['cpass']

                    user = User.objects.filter(Email=email)
                    if user:
                        message = "Email already exits"
                        return render(request,"app/paitentregister.html",{'msg':message})
                    else:
                        if password==cpassword:
                            otp = randint(10000,99999)
                            newuser = User.objects.create(Email=email,Password=password,Role=role,Otp=otp)
                            newpat = Patient.objects.create(user_id=newuser,Firstname=fname,Lastname=lname)
                            return render(request,"app/login.html")
                        else:
                            message = "password and conform password does not match"
                            return render(request,"app/paitentregister.html",{'msg':message}) 
        else: 
                if request.POST['role']=="Pharmacy":
                    role = request.POST['role']
                    fname = request.POST['fname']   
                    lname = request.POST['lname']
                    email = request.POST['email']
                    password = request.POST['pass']
                    cpassword = request.POST['cpass']

                    user = User.objects.filter(Email=email)
                    if user:
                        message = "Email already exits"
                        return render(request,"app/pharmaregister.html",{'msg':message})
                    else:
                        if password==cpassword:
                            otp = randint(10000,99999)
                            newuser = User.objects.create(Email=email,Password=password,Role=role,Otp=otp)
                            newpat = Pharmacy.objects.create(user_id=newuser,Firstname=fname,Lastname=lname)
                            return render(request,"app/login.html")
                        else:
                            message = "password and conform password does not match"
                            return render(request,"app/pharmaregister.html",{'msg':message})
                  
    except Exception as e:
        print("Regitration exception ------------>",e)

def Loginuser(request):
    try:
        if request.POST['role']=="Doctor":
            email = request.POST['email']
            password = request.POST['pass']

            user =User.objects.get(Email=email)
            if user:
                if user.Password==password and user.Role=="Doctor":
                    doc =Doctor.objects.get(user_id=user)
                    request.session['Firstname'] = doc.Firstname
                    request.session['Lastname'] = doc.Lastname
                    request.session['Email'] = user.Email
                    request.session['Role'] = user.Role
                    request.session['id'] = user.id
                    return render(request,"app/index-2.html")
                else:
                    message = "password doesnot match"
                    return render(request,"app/login.html",{'msg':message})
            else:
                message = "password doesnot match"
                return render(request,"app/login.html",{'msg':message})

        elif request.POST['role']=="Patient":
            email = request.POST['email']
            password = request.POST['pass']

            user =User.objects.get(Email=email)
            if user:
                if user.Password==password and user.Role=="Patient":
                    pat =Patient.objects.get(user_id=user)
                    request.session['Firstname'] = pat.Firstname
                    request.session['Lastname'] = pat.Lastname
                    request.session['Email'] = user.Email
                    request.session['Role'] = user.Role
                    request.session['id'] = user.id
                    return render(request,"app/index-2.html")
                else:
                    message = "password doesnot match"
                    return render(request,"app/login.html",{'msg':message})
            else:
                message = "password doesnot match"
                return render(request,"app/login.html",{'msg':message})

        else:
            if request.POST['role']=="Pharmacy":
                email = request.POST['email']
                password = request.POST['pass']

                user =User.objects.get(Email=email)
                if user:
                    if user.Password==password and user.Role=="Pharmacy":
                        pha =Pharmacy.objects.get(user_id=user)
                        request.session['Firstname'] = pha.Firstname
                        request.session['Lastname'] = pha.Lastname
                        request.session['Email'] = user.Email
                        request.session['Role'] = user.Role
                        request.session['id'] = user.id
                        return render(request,"app/index-2.html")
                    else:
                        message = "password doesnot match"
                        return render(request,"app/login.html",{'msg':message})
                else:
                    message = "password doesnot match"
                    return render(request,"app/login.html",{'msg':message})

    except Exception as e:
        print("Regitration exception ------------>",e)

def ProfilePage(request,pk):

    udata = User.objects.get(id=pk)
    print("Udata------------>",udata)

    if udata.Role=="Patient":
        pdata = Patient.objects.get(user_id=udata)
        print("Paitemt DATA -------------->",pdata)
        return render(request,"app/patient-profile.html",{"key2":pdata})
    else:
        if udata.Role == "Doctor":
            pdata = Doctor.objects.get(user_id=udata)
            print("Paitemt DATA -------------->",pdata)
        return render(request,"app/doctor-profile.html",{"key2":pdata})



def Logout(request,pk):
    udata = User.objects.get(id=pk)

    if udata.Role=="Patient":
        del request.session['Email']
        del request.session['Firstname']
        del request.session['Role']
        del request.session['id']
    else:
        if udata.Role=="Patient":
            del request.session['Email']
            del request.session['Firstname']
            del request.session['Role']
            del request.session['id']
    return HttpResponseRedirect(reverse('loginpage'))



def AllDoctorShow(request):
    all_doc = Doctor.objects.all()
    return render(request,"app/doctors-1.html",{'key3':all_doc})