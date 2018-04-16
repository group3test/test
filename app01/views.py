from django.shortcuts import render, HttpResponse, redirect, render


# Create your views here.


def denglu(request):
    return render(request, "denglu.html")


def submit(request):
    res = {"is_reg": True}
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    if len(user) == 0 or user == "ck":
        res["is_reg"] = "zh"
    elif len(pwd) == 0:
        res["is_reg"] = "mm"
    else:
        res["is_reg"] = False

    import json
    return HttpResponse(json.dumps(res))
