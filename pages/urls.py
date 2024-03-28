from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about.html", views.about, name='about'),
    path("botanical.html", views.botanical, name='botanical'),
    path("brooks.html", views.brooks, name='brooks'),
    path("cmom.html", views.cmom, name='cmom'),
    path("crosstown.html", views.crosstown, name='crosstown'),
    path("exhibits.html", views.exhibits, name='exhibits'),
    path("metal.html", views.metal, name='metal'),
    path("mosh.html", views.mosh, name='mosh'),
    path("ncrm.html", views.ncrm, name='ncrm'),
    path("rocknsoul.html", views.rocknsoul, name='rocknsoul'),
    path("stax.html", views.stax, name='stax'),
    path("sun.html", views.sun, name='sun'),
]
