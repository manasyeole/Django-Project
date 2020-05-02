from django.shortcuts import render
from django.http import JsonResponse
import requests
import random
from datetime import datetime

# Create your views he
def index(request):
	return render(request,'index.html')

def coronaupdates(request):
	data = random.randint(100,900)
	label =  str(datetime.now())
	
	print(label)
	context = {
		'data':data,
		'label':label,

	}
	return JsonResponse(context)