from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import FormularioRegistro, FormularioPerfilUsuario, FormularioPerfilAvatar
from .models import Perfil


def registro(request):
    if request.user.is_authenticated:
        return redirect('blog:inicio')

    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(user=user)
            login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}! Tu cuenta ha sido creada.")
            return redirect('blog:inicio')
    else:
        form = FormularioRegistro()
    return render(request, 'cuentas/registro.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'cuentas/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('blog:inicio')


@login_required
def editar_perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = FormularioPerfilUsuario(request.POST, instance=request.user)
        perfil_form = FormularioPerfilAvatar(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, "Perfil actualizado con éxito.")
            return redirect('cuentas:perfil')
    else:
        user_form = FormularioPerfilUsuario(instance=request.user)
        perfil_form = FormularioPerfilAvatar(instance=perfil)

    return render(request, 'cuentas/perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form,
    })