from django.shortcuts import render
from .models import Post
# Importar la vistas genericas(class)
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
# Para verificar si esta logeado para crear post se importa el siguiente decorador,
# para usar en una clase.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# def home(request):
    
#     context = {
#         'posts' : Post.objects.all()
#     }
#     return render(request,'blog/home.html', context)

class PostListView(ListView):
  
    # Declaramos con que model trabajar
    model = Post
    # Con cual template va a mostrar
    template_name = 'blog/home.html'
    # Variable para mostrar la informacion del model Post
    context_object_name = 'posts'
    # Para ordenar por fecha los posts
    ordering = ['-date']

class PostDetailView(DetailView):
    model = Post

# Se agrega el decorador clase LoginRequiredMixin en las herencias primero
class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['titulo', 'contenido']

    # Para que pueda crear el articulo con el id del usuario
    def form_valid(self,form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# Ademas del LoginRequiredMixin para chequear si esta logaeado se agrega,
# UserPassesTestMixin de segundo en jerarquia para verificar que sea el mismo usuario que pueda
# actualizar solo sus articulos o post.
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['titulo', 'contenido']

    # Para que pueda actualizar el articulo con el id del usuario
    def form_valid(self,form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    # Se crea el metodo test_func para confirmar el usuario.
    def test_func(self):
        post =self.get_object()
        if self.request.user == post.autor:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
    model = Post
    # Para luego de borrar haga redirect.
    success_url = '/'

       # Se crea el metodo test_func para confirmar el usuario.
    def test_func(self):
        post =self.get_object()
        if self.request.user == post.autor:
            return True
        return False




def about(request):
    return render(request, 'blog/about.html', {'title':'About'})