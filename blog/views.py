from django.shortcuts import render

posts = [
    {
        'autor' : 'Ruben C',
        'titulo' : 'Primer blog',
        'contenido' : 'Primer post',
        'date' : '12/08/2020',
    },
    {
        'autor' : 'Gloria C',
        'titulo' : 'segundo blog',
        'contenido' : 'segundo post',
        'date' : '12/08/2020',
    }
]

def home(request):
    
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})