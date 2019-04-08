from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Alumno
from .forms import AlumnoForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['txtuser']
        password = request.POST['txtpass']
        user = authenticate(request,username = username, password=password)
        if user:
            login(request,user)
            
            return HttpResponseRedirect(reverse('registro'))
        else:
            context['error'] = "Credenciales incorrectas"
            
            return render(request, 'citt/login.html',context)
    else:
        return render(request,'citt/login.html',context)  
@login_required(login_url='login')
def logout_view(request):
  
    if request.method == 'POST':
        logout(request)
    return redirect('login')
@login_required(login_url='login')
def registro_view(request):
    context = {}
    ruts = Alumno.objects.all()
    if request.method == 'POST':
        rutAlumno = request.POST.get('txtrut',True)
        elrutexiste = False
        for i in ruts:
            if rutAlumno == i.rut_alumno:
                elrutexiste = True
        if elrutexiste == False:
            atributos = Alumno(rut_alumno =rutAlumno) 
            atributos.save()
        else:
            return redirect('error')
        


    return render(request,'citt/registro.html',context)
@login_required(login_url='login')  
def error_view(request):
    context = {}
    return render(request,'citt/error.html',context) 
 
@login_required(login_url='login')
def listar_view(request):
    todos_ruts = Alumno.objects.all()
    query = request.GET.get('q')
    if query:
        
        todos_ruts = todos_ruts.filter(
                                        Q(rut_alumno__icontains=query)
                                    )
    context = {'todos_ruts':todos_ruts}
    return render(request,'citt/listar.html',context)
@login_required(login_url='login')
def modificar_view(request,pk):
    alumno = get_object_or_404(Alumno,pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST,instance=alumno)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.save()
            return redirect('listar')
    else:
        form = AlumnoForm(instance = alumno)
    context = {'form':form}
    return render(request,'citt/modificar.html',context)
@login_required(login_url='login')
def eliminar_view(request,pk):
    alumno = get_object_or_404(Alumno,pk=pk)
    alumno.delete()

    return redirect('listar')



        
