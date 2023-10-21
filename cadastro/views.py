from django.shortcuts import render , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Aluno

@login_required
def base(request):
    return render(request,'base.html')
    

def index(request):
    alunos = Aluno.objects.all()
    return render(request,'index.html',{'alunos':alunos})

@login_required
def aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    return render(request, 'aluno.html',{'aluno':aluno})

# Create your views here.

@login_required
def entrada(request):
    return render(request,'entrada.html')