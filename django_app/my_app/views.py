from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TestModal
from django.http import HttpResponse
from .tasks import incrementModal,scheduledIncrementModal
from datetime import datetime, timedelta

# Create your views here.


def index(request):
  return HttpResponse("<h1>Your app is running !!</h1>")


class API(APIView):
  def get(self,request):
    
    return Response({'message','Website is running Modal value is :'+str(TestModal.objects.first().count)})

class CeleryTask(APIView):
  def get(self,request):
    incrementModal.apply_async()
    return Response({'Work assigned to Celery check model to verify '})
class ScheduleCeleryTask(APIView):
  def get(self,request):
    eta = datetime.utcnow() + timedelta(seconds=10)
    scheduledIncrementModal.apply_async(eta=eta)
    return Response({'Work assigned to Celery check model to verify '})
  