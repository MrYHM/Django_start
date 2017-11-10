from django.shortcuts import render
import pymysql
from .models import UserMessage
import MySQLdb

# Create your views here.
def getform(request):
    # all_messages = UserMessage.objects.all()  # 返回数据库的所有数据  类型是QuerySet  可以进行迭代
    # print(type(all_messages))
    # for message in all_messages:  # message 是一个类
    #     print(message.name)

    # all_messages = UserMessage.objects.filter(name='bobby', address='北京') #filter 函数可以写默认参数进行搜索
    # for message in all_messages:  # message 是一个类
    #     print(message.name)


    # if request.method == "POST":  # 判断是get还是post请求
    #     name = request.POST.get("name", "")  # 如果取不到 默认值为空
    #     message = request.POST.get("message", "")
    #     address = request.POST.get("address", "")
    #     email = request.POST.get("email", "")
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.email = email
    #     user_message.address = address
    #     user_message.object_id = "helloworld3"
    #
    #     user_message.save()

    #删除数据
    message = None
    all_messages = UserMessage.objects.filter(name="bobbytest")
    if all_messages:
        message = all_messages[0]

    return render(request, 'message_form.html',{"my_message":message})

# 不能用form.html名称 因为jango内部有这个
