from django import forms
from .models import Post

# class PostCreationForm(forms.Form):
#     title=forms.CharField(max_length=225)
#     content=forms.CharField(max_length=500)
#     author=forms.CharField(max_length=255)

class PostCreationForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id": "title"}))
    content=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "id": "content", "rows":5}))
    author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id": "author"}))

    class Meta:
        model=Post
        fields="__all__"
        # fields=['title', 'content']
