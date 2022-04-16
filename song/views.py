from turtle import down
from django.shortcuts import render
import pafy
import youtube_dl
import os 
from .forms import songForm
from django.shortcuts import redirect
from django.contrib import messages

os.chdir(r'C:\Users\Venom\Desktop\django\youtube download songs')
# Create your views here.

def downloadsong(response):
    if response.method == "POST":
        print(response.POST)
        form = songForm(response.POST)
        if form.is_valid():
            yurl = form.cleaned_data['songurl']
            if executedownload(yurl):
                print("Song Downloaded") 
                messages.success(response, 'Song Downloaded Successfully')
                redirect("downloadsong")    
            else:
                print("Please Try again")
                redirect("downloadsong")    
            form.save()
            print("Form Data saved")
            
    else: 
        form = songForm()
        
    return render(response, 'song/index.html',{"form":form})

def executedownload(yurl):
    try:
        url = yurl
        video = pafy.new(url)
        bestaudio = video.getbestaudio()
        bestaudio.download()
        return True
    except:
        return False
        
    