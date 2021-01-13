from django.shortcuts import render
from django import forms
# Create your views here.
class NewForm(forms.Form):
    text=forms.CharField(label="", widget=forms.Textarea(attrs={'rows': 11, 'cols':50}))
def countword(request):
    if request.method=="POST":
        form=NewForm(request.POST)
        if form.is_valid():
            text=form.cleaned_data["text"]
            t=text.split()
            c=len(t)
            return render(request,"wordcount/countword.html",{"form": form, "count":c})
        else:
            return render(request,"wordcount/countword.html",{"form": form})
    return render(request,"wordcount/countword.html",{"form": NewForm(), "count":0})