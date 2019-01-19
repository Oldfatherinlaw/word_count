#编写函数传递指令给各个页面
from django.shortcuts import render


def home(request):
	'''主页'''
	return render(request, 'home.html')

def count(request):
	'''显示统计结果'''
	text_req = request.GET['text']
	total_count = len(text_req)
	
	count_dic = {}
	for word in text_req:
		if word not in count_dic:
			count_dic[word] = 1
		else:
			count_dic[word] += 1
	sorted_dic = sorted(count_dic.items(), key=lambda w:w[1], reverse=False)			#排序
	
	return render(request, 'count.html',
				 {'count':total_count, 'text':text_req, 
				 'countdic':count_dic, 'sorted':sorted_dic})