from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'snippet', 'header_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'elder', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the content'}),
            'snippet': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the content'}),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'snippet', )
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the content'}),
            'snippet': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the content'}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }