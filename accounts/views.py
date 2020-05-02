from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import requests
from .models import City
from .models import CSRD
from simple_search import search_filter

# Create your views 
def getin (request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username,password)
		user = authenticate(username=username,password=password)

		if user is not None:
			login(request, user)
			return redirect(reverse("index"))
		else:
			messages.info(request,'Invalid Credentials')
			return redirect('getin')
	else:
		return render(request,'getin.html')


def register (request):
	if request.method == 'POST':
		first_name =request.POST.get('first_name',None)
		last_name =request.POST.get('last_name',None)
		username =request.POST.get('username')
		password =request.POST.get('password1')
		password2 =request.POST.get('password2')
		email =request.POST.get('email',None)

		if password == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Taken')
				return redirect('accounts:register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email Taken')
				return redirect('accounts:register')
			else:
				user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name,last_name=last_name )
				user.save()
				return redirect('accounts:getin')
		else:
			messages.info(request,'Password Not Matching...')
			return redirect('accounts:register')
		return redirect('/')
	else:
		return render(request,'register.html')


def getout(request):
	logout(request)
	return redirect('/')


def wheather (request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b6ad5f15e50893832b94dcc1fc951cc5'
	
	if(request.method=="GET"):

	# cities = City.objects.all()

		cities=City.objects.all().order_by("-pk")
		wheather_data = []
		city_wheather={}
		for city in cities:
			r=requests.get(url.format(city)).json()
			city_wheather = {
			'city' : city.name,
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'icon' : r['weather'][0]['icon'],
			}
			wheather_data.append(city_wheather)
		context = {'wheather_data' : wheather_data}
		return render(request,'wheather.html',context)
	
	if(request.method=="POST"):
		city=request.POST.get("city_name")
		new_city=City(name=city)
		new_city.save()
		return redirect(reverse('accounts:wheather'))

def csrd (request):
	if(request.method == "POST"):
		if("delete" in request.POST):
			name=request.POST.get("delete")
			user =  CSRD.objects.get(username=name)
			user.delete()
			return redirect(reverse("accounts:csrd"))
		elif("search" in request.POST):
			search=request.POST.get("search")
			print(request.POST)
			obj = CSRD.objects.filter(username=search)
			print(obj)
			context = {
				"object_list": obj 
		
			}
			return render(request,'csrd.html',context)
		elif("edit" in request.POST):
			edit=request.POST.get("edit")
			user= CSRD.objects.get(username=edit)
			return redirect(reverse("accounts:edit",kwargs={"username":user.username}))
	return render(request,'csrd.html',{})

def create (request):
	if(request.method == 'POST'):
		username=request.POST.get("username")
		first_name=request.POST.get("first_name")
		last_name=request.POST.get("last_name")
		password=request.POST.get("password")
		new_csrd=CSRD(username=username,first_name=first_name,last_name=last_name,password=password)
		new_csrd.save()
		return redirect(reverse('accounts:csrd'))
	else:
		return render(request,"create.html",{})



def edit (request,username):
	user=CSRD.objects.get(username=username)

	if(request.method == 'POST'):
		username=request.POST.get("username")
		first_name=request.POST.get("first_name")
		last_name=request.POST.get("last_name")
		password=request.POST.get("password")
		
		user.username=username
		user.first_name=first_name
		user.last_name=last_name
		user.password=password
		user.save()
		return redirect(reverse('accounts:csrd'))
	else:
		return render(request,"edit.html",{"user":user})



