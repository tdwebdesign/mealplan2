from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Recipe, RecipeIngredient, Ingredient
from .forms import IngredientForm

from django.views import generic

# Create your views here.
class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class ProtectedAboutView(PermissionRequiredMixin, View):
    permission_required = 'recipes.view_protected_data'
    login_url = 'login'

    def get(self, request):
        # Render the protected view
        return render(request, 'recipes/about.html', {})


def IndexView(request):
    return render(request, 'recipes/index.html', {})

'''
def AboutView(request):
    return render(request, 'recipes/about.html', {})
'''

def create_view(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = IngredientForm()
    return render(request, 'recipes/create_ingredient.html', {'form': form})
