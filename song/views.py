from django.shortcuts import render
import pafy
import youtube_dl
from .forms import songForm
# Create your views here.

def downloadsong(response):
    if response.method == "POST":
        print(response.POST)
        form = songForm(response.POST)
        if form.is_valid():
            yurl = form.cleaned_data['songurl']
            url = yurl
            video = pafy.new(url)
            bestaudio = video.getbestaudio()
            bestaudio.download()
            print("download complete")
            form.save()
            print("Form Data saved")
    else: 
        form = songForm()
    return render(response, 'song/downloadsong.html',{"form":form})