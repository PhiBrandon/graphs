from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .forms import loginForm

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def blog(request):
	return render(request, 'personal/post_index.html',{'success':'great success'})

class loginView(View):
	def get(self, request):
		form = loginForm()
		context = {'form': form}
		return render(request, 'personal/post_index.html', context)

	def post(self, request):
		form = loginForm(request.POST)
		context  = {'form':form, 'success':"success"}
		return render(request, 'personal/post_index.html',context)

def get_data(request, *args, **kwargs):
	data = {
		"sales": 100,
		"customers": 10
	}
	return JsonResponse(data)

class ChartData(APIView):
   
    authentication_classes = []
    permission_classes = []
    labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
    default_items = [1234,1234,231,100,1230,2901]
    def get(self, request, format=None):
        data = {
				"labels": self.labels,
				"default": self.default_items,
				"customers": 10
	}
        return Response(data)