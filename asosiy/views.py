from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# from .forms import *

def home(request):
    qidiruv_sozi = request.GET.get("qidiruv_sozi")
    if qidiruv_sozi != "" and qidiruv_sozi is not None:
        t_s = Togri.objects.filter(soz=qidiruv_sozi)
        if t_s:
            n_s = Xato.objects.filter(t_soz=t_s[0])

        elif Xato.objects.filter(notogri=qidiruv_sozi):
            n_s = Xato.objects.filter(notogri=qidiruv_sozi)
            t_s = [n_s[0].t_soz]
            n_s = Xato.objects.filter(t_soz=t_s[0])

        else:
            t_s = [f"Siz kiritgan {qidiruv_sozi} so'zi mavjud emas."]
            n_s = ["So'z omborda yo'q"]
    else: t_s, n_s = [""], []
    data = {"togrisi": t_s[0], "notogrilar": n_s}
    return render(request, 'result.html', data)
