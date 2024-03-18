from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .models import Commander


def home(request):
    if 'commander' not in request.GET:
        commanders = Commander.objects.all()
        return render(request,'generals.html',context={'commanders': commanders})
    else:
        commanders = Commander.objects.filter(name__contains=request.GET['commander'])
        return render(request,'generals.html',context={'commanders': commanders})


def about(request):
    return render(request,'about.html')


def commander_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        year = request.POST['year']
        did = request.POST['did']
        area = request.POST['area']
        image = request.FILES.get('image')

        if image:
            new_commander = Commander(name=name,year=year,did=did,area=area,image=image)
        else:
            new_commander = Commander(name=name,year=year,did=did,area=area)
        new_commander.save()
        return redirect('/',pk=new_commander.pk)
    else:
        return render(request,'add_commanders.html')


def edit_commander(request, pk):
    this_commander = get_object_or_404(Commander, id=pk)
    if request.method == 'POST':
        this_commander.name = request.POST['name']
        this_commander.year = request.POST['year']
        this_commander.did = request.POST['did']
        this_commander.area = request.POST['area']
        image = request.FILES.get('image')
        if image:
            this_commander.image = image
        this_commander.save()
        return redirect('/', pk=this_commander.pk)
    else:
        return render(request, 'edit_commanders.html', context={'commander': this_commander})





def delete_commanders(request, pk):
    delete_commander = get_object_or_404(Commander, id=pk)
    if request.method == "POST":
        if 'confirm_delete' in request.POST:
            delete_commander.delete()
            return redirect('home')
        else:
            return redirect('home')
    else:
        return render(request, 'delete_commanders.html', {'delete_commander': delete_commander})

