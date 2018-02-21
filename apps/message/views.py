from django.shortcuts import render
from .models import UserMessage

# Create your views here.
def getform(request):
    # 实例化一个对象
    # umsg = UserMessage()
    # umsg.name = '王五'
    # umsg.email = 'wangwu@123.com'
    # umsg.address = '江苏南京'
    # umsg.message = '放假了！'
    # umsg.save()

    # umsg = UserMessage()
    # 接收页面传送值
    # if request.method == 'POST':
    #     umsg.name = request.POST.get('name', '')
    #     umsg.email = request.POST.get('email', '')
    #     umsg.address = request.POST.get('address', '')
    #     umsg.message = request.POST.get('message', '')
    #     umsg.save()

    # 删除处理
    # del_messages = UserMessage.objects.filter(address='安徽宿州')
    # 一次性全部删除
    # del_messages.delete()
    # 也可以循环删除
    # for dm in del_messages:
    #     dm.delete()

    # 全部列出
    # all_messages = UserMessage.objects.all()
    # 按照指定条件过滤
    # all_messages = UserMessage.objects.filter(address='安徽宿州')
    # for message in all_messages:
    #     print(message.name)

    msg = None
    if request.method == 'GET':
        all_msg = UserMessage.objects.filter(address='江苏南京')
        if all_msg:
            msg = all_msg[0]
    elif request.method == 'POST':
        msg = UserMessage()
        msg.id = 3
        msg.name = request.POST.get('name', '')
        msg.email = request.POST.get('email', '')
        msg.address = request.POST.get('address', '')
        msg.message = request.POST.get('message', '')
        msg.save()
    else:
        pass
    # 将数据回填到表单中
    return render(request, 'message_form.html', {'my_msg': msg})