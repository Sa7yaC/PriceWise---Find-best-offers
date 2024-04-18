from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def index(request):
    return render(request,'extension.html')

def getLink(request):
    url = request.GET.get('text','default')
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    Name = soup.find('span',class_='VU-ZEz').text.strip()
    Image = soup.find('img', class_='_0DkuPH').get('src') 
    params = {'productImage':Image,'productName':Name}
    return render(request,'extension.html',params)
    