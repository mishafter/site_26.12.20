from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Region, Filial, Cekh
from .forms import FilialForm, RegionForm, CekhForm
from django.shortcuts import redirect
# Главная страница----------------------------------------------------------------
def index(request):
    filials = Filial.objects.all().values()
    regions = Region.objects.all().values()
    cekhs = Cekh.objects.all().values()
    return render(request,'base/index.html', {'regions': regions,'filials': filials, 'cekhs': cekhs})


# Филиал----------------------------------------------------------------
def AddFilial(request):

    if request.method == "POST":
        form = FilialForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:

        form = FilialForm()
        data = {'Form': form}
        return render(request, 'base/add.html', data, )

# Вывести инфо по филиалу недоделана----------------------------------------------------------------
def filial(request, id):
    try:
        filial = Filial.objects.get(id=id)
        filials = Filial.objects.all().values()
        if request.method == "POST":
            filial.name = request.POST.get('name')
            filial.save()
            return HttpResponseRedirect('/4444')
        else:
            return render(request,'base/cart.html', {'filials': filials})
    except Filial.DoesNotExist:
        return HttpResponseNotFound('<h2>filial not found</h2>')

# Добавить Регион----------------------------------------------------------------
def AddRegion(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = RegionForm()
        data = {'Form': form}

        return render(request, 'base/add.html', data)

# Добавить Цех----------------------------------------------------------------
def AddCekh(request):
    if request.method == "POST":
        form = CekhForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = CekhForm()
        data = {'Form': form}

        return render(request, 'base/add.html', data)

# Добавить ПУО----------------------------------------------------------------
def AddPuo(request):
    return HttpResponse('Вьюха добавления ПУО')

# Добавить Группа----------------------------------------------------------------
def AddGroupItems(request):
    return HttpResponse('Вьюха добавления групп устройств')

# Добавить Устройство----------------------------------------------------------------
def AddItem(request):
    return HttpResponse('Вьюха добавления устройства')

# Добавить Программа----------------------------------------------------------------
def AddProgram(request):
    return HttpResponse('Вьюха добавления программы')

# Добавить Вещание----------------------------------------------------------------
def AddBroadcast(request):
    return HttpResponse('Вьюха добавления вещания')

# Добавить Связь----------------------------------------------------------------
def AddLink(request):
    return HttpResponse('Вьюха добавления связей')