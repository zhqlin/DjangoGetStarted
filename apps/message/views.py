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

    umsg = UserMessage()
    # 接收页面传送值
    if request.method == 'POST':
        umsg.name = request.POST.get('name', '')
        umsg.email = request.POST.get('email', '')
        umsg.address = request.POST.get('address', '')
        umsg.message = request.POST.get('message', '')
        umsg.save()

    # 删除处理
    del_messages = UserMessage.objects.filter(address='安徽宿州')
    # 一次性全部删除
    # del_messages.delete()
    # 也可以循环删除
    for dm in del_messages:
        dm.delete()

    # 全部列出
    all_messages = UserMessage.objects.all()
    # 按照指定条件过滤
    # all_messages = UserMessage.objects.filter(address='安徽宿州')
    for message in all_messages:
        print(message.name)
    return render(request, 'message_form.html')