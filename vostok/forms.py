from .models import Post, Comment
from django import forms
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','text','photo']
        widgets = {'title': forms.TextInput(attrs={
           'class': 'form-control-title',
           'placeholder': 'Тема думы'

        }),'text': forms.Textarea(attrs={
           'class': 'form-control',
           'placeholder': 'Место для изливания души'

        }),'photo': forms.FileInput(attrs={
           'class': 'form-control-photo',
            
        })}


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {'email':forms.EmailInput(attrs={'required':'true'})}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body','photo')
        widgets = {'body': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Опишите свое впечатление от поста'}),
            'photo': forms.FileInput(attrs={
                'class': 'form-control-photo'})}
