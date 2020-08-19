from django.shortcuts import render,get_object_or_404
from .models import Post
# Importar la vistas genericas(class)
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
# Para verificar si esta logeado para crear post se importa el siguiente decorador,
# para usar en una clase.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Se importa el model User para la pagination de los posts del usuario,
# con el shorcut get_object_or_404 en arriba en shortcuts.
from django.contrib.auth.models import User


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
    # Pagination de cuantos articulos mostrar
    paginate_by = 4


# Pagination de los post de los usarios solamente.
class UserPostView(ListView):
  
    model = Post
    # Con cual template va a mostrar
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # Pagination de cuantos articulos mostrar
    paginate_by = 4

    def get_queryset(self):
        # Se obtiene al user si existe sino da un error 404
        user =get_object_or_404(User, username=self.kwargs.get('username'))
        # returna los posts del usuario y ordenado por fecha
        return Post.objects.filter(autor=user).order_by('-date')

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