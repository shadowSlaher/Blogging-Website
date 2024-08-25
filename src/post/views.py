from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
      
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context = super().get_context_data(**kwargs)
        context["total_likes"] = total_likes
        context["liked"] = liked
         
        return context
    
        
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
         
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={"pk":self.kwargs["pk"]})
    # success_url = reverse_lazy('home')

