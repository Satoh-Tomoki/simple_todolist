from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import *

from django.utils import timezone

#Viewを継承してGET文、POST文の関数を作る
class TodoView(View):

    def get(self, request, *args, **kwargs):

        data  = Todolist.objects.order_by("deadline")
        context     = { "data"  : data }

        return render(request,"todo/index.html",context)

    def post(self, request, *args, **kwargs):


        #TODOリストの作成
        if "deadline" in request.POST and "content" in request.POST:

            posted  = Todolist( deadline    = request.POST["deadline"],
                                content     = request.POST["content"],
                                )
            posted.save()
        

        #TODOリストの削除
        if "todo_delete" in request.POST:
            target_id   = request.POST["todo_delete"].replace("-","")

            posted  = Todolist.objects.filter(id=target_id)
            posted.delete()


        data  = Todolist.objects.order_by("deadline")
        context     = { "data"  : data }

        return render(request,"todo/index.html",context)

index       = TodoView.as_view()


