from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.views.generic import TemplateView

class Profile(TemplateView):
    template_name = 'accounts/profile.html'

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render(request=request, template_name='accounts/register.html', context={"register_form":form})
