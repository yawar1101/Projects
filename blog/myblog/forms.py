from dataclasses import fields
from django import forms
from .models import Post, Category

# choices = [('coding', 'coding'), ('space', 'space'), ('sports', 'sports'),]

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
        choice_list.append(item) 


class PostForm(forms.ModelForm):
    # def get_context_data(self, **kwargs):
    #     """Insert the form into the context dict."""
    #     if 'form' not in kwargs:
    #         kwargs['form'] = self.get_form()
            


    #     return super().get_context_data(**kwargs)

  
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Title Tag here'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list ,attrs={'class': 'form-control'}), 
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content here'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Title Tag here'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content here'}),
        }