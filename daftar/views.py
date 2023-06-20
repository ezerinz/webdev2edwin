from django.shortcuts import render, redirect
from .forms import PendaftaranForm
from .models import Pendaftaran


def delete(request, id):
    tamu = Pendaftaran.objects.get(id=id)
    tamu.delete()
    return redirect("crud")


def update(request, id):
    tamu = Pendaftaran.objects.get(id=id)

    if request.method != "POST":
        form = PendaftaranForm(instance=tamu)
    else:
        form = PendaftaranForm(data=request.POST, instance=tamu)
        if form.is_valid():
            form.save()
            return redirect("crud")
    return render(request, "update.html", {"form": form, "tamu": tamu})


# Create your views here.
def add(request):
    if request.method == "POST":
        form = PendaftaranForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("crud")
            except:
                pass
    else:
        form = PendaftaranForm()
    return render(request, "add.html", {"form": form})


def index(request):
    pendaftaran = Pendaftaran.objects.all()
    context = {"daftar": pendaftaran}

    return render(request, "crud.html", context)
