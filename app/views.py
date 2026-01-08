from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.db.models import Q
from django.db import connection
from django.http import JsonResponse
from django.db.models import Sum
import datetime
def home(request):
	return render(request,'index.html',{})
def dashboard(request):
	return render(request,'dashboard.html',{})
def customer_register(request):
	if request.method == 'POST':
		cname = request.POST.get('cname')
		mail = request.POST.get('mail')
		num = request.POST.get('num')
		uname = request.POST.get('uname')
		psw = request.POST.get('psw')
		country = request.POST.get('country')
		state = request.POST.get('state')
		city = request.POST.get('city')
		addr = request.POST.get('addr')
		lic = Customer_Detail.objects.filter(username=uname)
		if lic:
			messages.success(request,'User Alredy Exist')
		else:
			crt = Customer_Detail.objects.create(name=cname,email=mail,username=uname,
			phone_number=num,country=country,state=state,city=city,address=addr,password=psw)
			if crt:
				messages.success(request,'Registered Successfully')
	return render(request,'customer_register.html',{})
def customer_login(request):
	if request.session.has_key('customer'):
		return redirect("customer_dashboard")
	else:
		if request.method == 'POST':
			username = request.POST.get('uname')
			password =  request.POST.get('psw')
			post = Customer_Detail.objects.filter(username=username,password=password)
			if post:
				username = request.POST.get('uname')
				request.session['customer'] = username
				a = request.session['customer']
				sess = Customer_Detail.objects.only('id').get(username=a).id
				request.session['cus_id']=sess
				return redirect("customer_dashboard")
			else:
				messages.success(request, 'Invalid Username or Password')
	return render(request,'customer_login.html',{})
def hospital_login(request):
	if request.session.has_key('username'):
		return redirect("dashboard")
	else:
		if request.method == 'POST':
			username = request.POST.get('uname')
			password =  request.POST.get('psw')
			post = Hospital_Register.objects.filter(username=username,password=password,status='Approved')
			if post:
				username = request.POST.get('uname')
				request.session['username'] = username
				a = request.session['username']
				sess = Hospital_Register.objects.only('id').get(username=a).id
				request.session['hospital_id']=sess
				return redirect("dashboard")
			else:
				messages.success(request, 'Admin need to Approve or Invalid Username or Password')
	return render(request,'hospital_login.html',{})
def logout(request):
    try:
        del request.session['username']
    except:
     pass
    return render(request, 'hospital_login.html', {})
def customer_logout(request):
    try:
        del request.session['customer']
    except:
     pass
    return render(request, 'customer_login.html', {})
def customer_dashboard(request):
	return render(request,'customer_dashboard.html',{})
def hospital_register(request):
	a = Area.objects.all()
	if request.method == 'POST':
		hospital_name = request.POST.get('hname')
		d_name = request.POST.get('dname')
		hlnum = request.POST.get('hlnum')
		email = request.POST.get('email')
		uname = request.POST.get('uname')
		psw = request.POST.get('psw')
		pnum = request.POST.get('pnum')
		country = request.POST.get('country')
		state = request.POST.get('state')
		city = request.POST.get('city')
		addr = request.POST.get('addr')
		area = request.POST.get('area')
		area_id=Area.objects.get(id=int(area))
		image=request.FILES['image']
		specialist = request.POST.get('specialist')
		crt = Hospital_Register.objects.create(hospital_name=hospital_name,
		mail=email,mobile=pnum,specialist=specialist,
		hospital_license_no=hlnum,username=uname,
		password=psw,area=area_id,image=image,status='Waiting',
		country=country,state=state,city=city,hospital_address=addr)
		if crt:
			messages.success(request,'Registered Successfully')
		else:
			messages.success(request,'Invalid License Number')

	return render(request,'hospital_register.html',{'a':a})
def add_facilities(request):
	hospital_id = request.session['hospital_id']
	uid= Hospital_Register.objects.get(id=int(hospital_id))
	if request.method == 'POST':
		doctor_detail = request.POST.get('doctor_detail')
		bed_detail = request.POST.get('bed_detail')
		blood_bank = request.POST.get('blood_bank')
		medical_detail = request.POST.get('medical_detail')
		ambulance = request.POST.get('ambulance')
		other = request.POST.get('other')
		cylinder_count = request.POST.get('cylinder_count')
		crt = Facilities.objects.create(doctor_detail=doctor_detail,
		bed_detail=bed_detail,blood_bank=blood_bank,medical_detail=medical_detail,
		ambulance=ambulance,other=other,hospital_id=uid,cylinder_count=cylinder_count)
		if crt:
			messages.success(request,'Detail Added Successfully')

	return render(request,'add_facilities.html',{})
def search(request):
	a = Area.objects.all()
	if request.session.has_key('customer'):
		if request.GET.get('area'):
			s = request.GET.get('area')
			bed = request.GET.get('bed_count')
			cylinder = request.GET.get('cylinder_count')
			detail = Facilities.objects.filter(hospital_id__in=Hospital_Register.objects.filter(area=int(s)),
			bed_detail__gte=int(bed),cylinder_count__gte=int(cylinder))
			return render(request,'search.html',{'detail':detail,'a':a})
		return render(request,'search.html',{'a':a})
	else:
		return render(request,'customer_login.html',{})
def detail(request,pk):
	if request.session.has_key('customer'):
		detail = Facilities.objects.filter(hospital_id=pk)
		return render(request,'detail.html',{'detail':detail})
	else:
		return render(request,'customer_login.html',{})
def view_facilities(request):
	if request.session.has_key('username'):
		user_id = request.session['hospital_id']
		detail = Facilities.objects.filter(hospital_id=int(user_id))
		return render(request,'view_facility.html',{'detail':detail})
	else:
		return render(request,'customer_login.html',{})