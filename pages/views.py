from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "pages/home.html", {})

def about(request):
    return render(request, "pages/about.html", {})

def exhibits(request):
    return render(request, "pages/exhibits.html", {})

def botanical(request):
    return render(request, "pages/botanical.html", {})

def brooks(request):
    return render(request, "pages/brooks.html", {})

def cmom(request):
    return render(request, "pages/cmom.html", {})

def crosstown(request):
    return render(request, "pages/crosstown.html", {})

def metal(request):
    return render(request, "pages/metal.html", {})

def mosh(request):
    return render(request, "pages/mosh.html", {})

def ncrm(request):
    return render(request, "pages/ncrm.html", {})

def rocknsoul(request):
    return render(request, "pages/rocknsoul.html", {})

def stax(request):
    return render(request, "pages/stax.html", {})

def sun(request):
    return render(request, "pages/sun.html", {})