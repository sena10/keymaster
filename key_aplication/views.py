from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Chave, AluguelChave, Funcionario
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import (CreateView)
from .forms import  User, UserRegistrationForm
from django.urls import reverse_lazy






def principal(request):
    return render(request,'principal.html')

def agradecimento(request):
    return render(request, 'agradecimento.html')

def alugado(request):
    return render(request,'alugado.html')

def principalpage(request):
    chaves = Chave.objects.all()
    usuario_atual = request.user
    contexto = {
        'chaves': chaves,
        'usuario_atual': usuario_atual
    }

    return render(request, 'principal2.html', contexto)

@login_required
def list_chaves(request):
    chaves = Chave.objects.all()
    context = {'chaves': chaves}
    return render(request, 'list_chaves.html', context)

@login_required
def devolver(request):
    chaves = Chave.objects.all()
    usuario_atual = request.user
    contexto = {
        'chaves': chaves,
        'usuario_atual': usuario_atual
    }

    return render(request, 'devolver.html', contexto)


@login_required
def alugar_chave(request, chave_id):
    funcionario = request.user.funcionario

    chave = Chave.objects.get(id=chave_id)
    
    if chave.disponivel:
        chave.disponivel = False
        chave.save()

        AluguelChave.objects.create(chave=chave, funcionario=funcionario)
        return redirect('alugado')
    else:
        return redirect('list_chaves')
    


@login_required
def devolver_chave(request, chave_id):
    chave = Chave.objects.get(id=chave_id)
    alugueis = chave.alugueis.all()

    if alugueis.exists():
        aluguel = alugueis.first()
        chave.disponivel = True
        chave.save()

        aluguel.data_devolucao = timezone.now()
        aluguel.save()

        return redirect('agradecimento')
    else:
        # Trate a situação em que não há aluguéis para a chave
        # Você pode redirecionar para uma página de erro ou exibir uma mensagem de erro

        return HttpResponse("Não foi possível devolver a chave. Não há aluguéis registrados.")



def loginpage(request):
    if request.method == 'GET':
        return render(request, template_name='login.html')
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect ('principal2')
        else:
            return redirect ('login')
    
def logoutpage(request):
    logout(request)
    return redirect ('principal')


class Registration(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("principal2")

    def form_valid(self, form):
        response = super().form_valid(form)
        funcionario = Funcionario(user=self.object)
        funcionario.save()
        return response
