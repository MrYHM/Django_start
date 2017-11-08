from django.shortcuts import render

# Create your views here.
def getform(request):
    return render(request,'message_form.html')
# 不能用form.html名称 因为jango内部有这个