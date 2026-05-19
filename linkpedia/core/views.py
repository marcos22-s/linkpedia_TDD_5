from django.shortcuts import render, redirect, get_object_or_404
from core.forms import LoginForm, LinkModelForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import LinkModel 

def login(request):
    if request.user.id is not None:
        return redirect("home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("home")
        context = {'acesso_negado': True}
        return render(request, 'login.html', {'form':form})
    return render(request, 'login.html', {'form':LoginForm()})

        
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'logout.html')
    return redirect("home")


@login_required
def home(request):
    context = {
        'links': LinkModel.objects.all()
    }
    return render(request, 'index.html', context)



@login_required
def cadastrar_link(request):
    if request.method == 'POST':
        form = LinkModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LinkModelForm()
    return render(request, 'cadastrar.html', {'form': form})

@login_required
def listar_links(request):
    links = LinkModel.objects.all()
    return render(request, 'listar.html', {'links': links})

@login_required
def atualizar_link(request, pk):
    link = get_object_or_404(LinkModel, pk=pk)
    if request.method == 'POST':
        form = LinkModelForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LinkModelForm(instance=link)
    return render(request, 'atualizar.html', {'form': form})

@login_required
def remover_link(request, pk):
    link = get_object_or_404(LinkModel, pk=pk)
    if request.method == 'POST':
        link.delete()
        return redirect('home')
    return render(request, 'remover.html', {'link': link})