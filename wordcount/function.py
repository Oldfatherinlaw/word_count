#新建一个home函数存储首页内容
#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')