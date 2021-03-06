#borre todo lo que habia aqui y lo deje en web_views
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from posts.models import Post, PostView, Like, Comment, Profile, Dislike
from .forms import PostForm, CommentForm, ProfileUpdateForm

from django.views.generic.edit import FormView 
from django.http import HttpResponseRedirect

from django.contrib import messages

#cabildos
import json
from cabildos.forms import CrearCabildo
from cabildos.models import Cabildo, get_conceptos_Valores, get_conceptos_Derechos, get_conceptos_Deberes, get_conceptos_Instituciones 



class PostListView(ListView):
    model = Post
    form_class = CrearCabildo
    #initial = {'key': 'value'}
    #template_name = "post_list.html"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        context['cabildo_form'] = CrearCabildo()

        conceptos_Valores = get_conceptos_Valores()
        conceptos_Derechos = get_conceptos_Derechos()
        conceptos_Deberes = get_conceptos_Deberes()
        conceptos_Instituciones = get_conceptos_Instituciones()

        json_conceptos_Valores = json.dumps(conceptos_Valores)
        json_conceptos_Derechos =json.dumps(conceptos_Derechos)
        json_conceptos_Deberes = json.dumps(conceptos_Deberes)
        json_conceptos_Instituciones = json.dumps(conceptos_Instituciones)

        context['json_conceptos_Valores'] = json_conceptos_Valores
        context['json_conceptos_Derechos'] = json_conceptos_Derechos
        context['json_conceptos_Deberes'] = json_conceptos_Deberes
        context['json_conceptos_Instituciones'] = json_conceptos_Instituciones

        return context

    #def get(self, request, *args, **kwargs):
    #    form = self.form_class(initial=self.initial)
    #    return render(request, self.template_name, {'form': form})

    # Handle POST GTTP requests
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            return HttpResponseRedirect('/')

        #return render(request, self.template_name, {'form': form})
    #def post(self, request, *args, **kwargs):
    #    form = self.get_form_class()
    #    if form.is_valid(self):
    #        return self.form_valid(form)
    #    else:
    #        return self.form_invalid(form)

    #def form_valid(self, form):
    #    if form.is_valid():
    #        form.save()


class PostDetailView(DetailView):
    model = Post

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm(),
            'all_posts': Post.objects.all(),
        })
        return context
    

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)

        return object

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['view_type'] = 'create'
        context['post_form'] = PostForm()

        conceptos_Valores = get_conceptos_Valores()
        conceptos_Derechos = get_conceptos_Derechos()
        conceptos_Deberes = get_conceptos_Deberes()
        conceptos_Instituciones = get_conceptos_Instituciones()

        json_conceptos_Valores = json.dumps(conceptos_Valores)
        json_conceptos_Derechos =json.dumps(conceptos_Derechos)
        json_conceptos_Deberes = json.dumps(conceptos_Deberes)
        json_conceptos_Instituciones = json.dumps(conceptos_Instituciones)

        context['json_conceptos_Valores'] = json_conceptos_Valores
        context['json_conceptos_Derechos'] = json_conceptos_Derechos
        context['json_conceptos_Deberes'] = json_conceptos_Deberes
        context['json_conceptos_Instituciones'] = json_conceptos_Instituciones

        return context

    # Handle POST GTTP requests
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if request.method == "POST":
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                # <process form cleaned data>
            
            #print(form)
            return HttpResponseRedirect('/blog')

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)

def profile(request):
    context = super().get_context_data(**kwargs)
    model = Profile
    context['image_form'] = ProfileUpdateForm() 

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES) #, instance=request.user.profile.image
        if form.is_valid():
            form.save()
            messages.success(request, f'Tu cuenta ha sido actualizada!')
            return redirect('perfil')

        else:
            print(form.errors)

    #else:
    #    form = ProfileUpdateForm(instance=request.user.profile.image)

    
    #context = {
    #    'form': form
    #}
    return render(request, 'perfil.html', context)



'''
views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post, PostView, Like, Comment, Profile, Dislike
from .forms import PostForm, CommentForm

from django.views.generic.edit import FormView 
from django.http import HttpResponseRedirect


#cabildos
import json
from articulos.forms import CrearArticulo
from articulos.models import Articulo, get_conceptos_Valores, get_conceptos_Derechos, get_conceptos_Deberes, get_conceptos_Instituciones 



class PostListView(ListView):
    model = Post
    form_class = PostForm
    #initial = {'key': 'value'}
    #template_name = "post_list.html"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        context['post_form'] = PostForm()

        conceptos_Valores = get_conceptos_Valores()
        conceptos_Derechos = get_conceptos_Derechos()
        conceptos_Deberes = get_conceptos_Deberes()
        conceptos_Instituciones = get_conceptos_Instituciones()

        json_conceptos_Valores = json.dumps(conceptos_Valores)
        json_conceptos_Derechos =json.dumps(conceptos_Derechos)
        json_conceptos_Deberes = json.dumps(conceptos_Deberes)
        json_conceptos_Instituciones = json.dumps(conceptos_Instituciones)

        context['json_conceptos_Valores'] = json_conceptos_Valores
        context['json_conceptos_Derechos'] = json_conceptos_Derechos
        context['json_conceptos_Deberes'] = json_conceptos_Deberes
        context['json_conceptos_Instituciones'] = json_conceptos_Instituciones

        return context

    #def get(self, request, *args, **kwargs):
    #    form = self.form_class(initial=self.initial)
    #    return render(request, self.template_name, {'form': form})

    # Handle POST GTTP requests
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            return HttpResponseRedirect('/')
            

        #return render(request, self.template_name, {'form': form})
    #def post(self, request, *args, **kwargs):
    #    form = self.get_form_class()
    #    if form.is_valid(self):
    #        return self.form_valid(form)
    #    else:
    #        return self.form_invalid(form)

    #def form_valid(self, form):
    #    if form.is_valid():
    #        form.save()


class PostDetailView(DetailView):
    model = Post

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm(),
            'all_posts': Post.objects.all(),
        })
        return context
    

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)

        return object

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)

        context['post_form'] = PostForm()

        conceptos_Valores = get_conceptos_Valores()
        conceptos_Derechos = get_conceptos_Derechos()
        conceptos_Deberes = get_conceptos_Deberes()
        conceptos_Instituciones = get_conceptos_Instituciones()

        json_conceptos_Valores = json.dumps(conceptos_Valores)
        json_conceptos_Derechos =json.dumps(conceptos_Derechos)
        json_conceptos_Deberes = json.dumps(conceptos_Deberes)
        json_conceptos_Instituciones = json.dumps(conceptos_Instituciones)

        context['json_conceptos_Valores'] = json_conceptos_Valores
        context['json_conceptos_Derechos'] = json_conceptos_Derechos
        context['json_conceptos_Deberes'] = json_conceptos_Deberes
        context['json_conceptos_Instituciones'] = json_conceptos_Instituciones

        return context

    # Handle POST GTTP requests
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            return HttpResponseRedirect('/')

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)

def dislike(request, slug):
    post = get_object_or_404(Post, slug=slug)
    dislike_qs = Dislike.objects.filter(user=request.user, post=post)
    if dislike_qs.exists():
        dislike_qs[0].delete()
        return redirect('detail', slug=slug)
    Dislike.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)
'''
