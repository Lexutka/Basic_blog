from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import UserRegistrationForm
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail


def index(request):
    posts = Post.objects.filter(date__lte=timezone.now()).order_by('-date')
    return render(request,'home.html', {'posts': posts})


@login_required
def create_post(request):
    error = ''
    photo_url = ''
    if  request.method == 'POST' and request.FILES:
        photo_file = request.FILES['photo']
        ps = FileSystemStorage()
        photo_name = ps.save(photo_file.name, photo_file)
        photo_url = ps.url(photo_name)
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.photo = photo_file
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            error = 'Что-то пошло не так'
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            error = 'Что-то пошло не так'
    form = PostForm()
    context = {'form': form,'error':error,'photo_url': photo_url}
    return render(request,'newpost.html',context)


@login_required
def edit_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST, instance=post)
    photo_url = ''
    if  request.method == 'POST' and request.FILES:
        photo_file = request.FILES['photo']
        ps = FileSystemStorage()
        photo_name = ps.save(photo_file.name, photo_file)
        photo_url = ps.url(photo_name)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.photo = photo_file
            post.save()
            return redirect('post_detail', pk=post.pk)
    elif request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    context = {'form': form,'photo_url':photo_url}
    return render(request, 'postedit.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    title = post.title
    item = Post.objects.get(pk=pk)
    comments = post.comments.filter(active=True)
    photo_url = ''
    if request.method == 'POST' and request.FILES:
        photo_file = request.FILES['photo']
        ps = FileSystemStorage()
        photo_name = ps.save(photo_file.name, photo_file)
        photo_url = ps.url(photo_name)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.photo = photo_file
            new_comment.post = post
            new_comment.save()
    elif request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
    check_author = False
    if request.user == item.author:
        check_author = True
    comment_form = CommentForm()
    context = {'post': post,
               'title': title,
               'check_author': check_author,
               'comments': comments,
               'comment_form': comment_form,
               'photo-url':photo_url,
               }
    return render(request, 'postdetail.html', context)


def cabinet (request):
    return render (request,'cabinet.html')


def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.email
            form.save()
            subject_template_name = 'password_reset_subject'
            email_template_name = 'password_reset_email'
            context = None
            from_email = 'ebonist123@gmail.com'
            send_mail(subject_template_name, 
                      email_template_name, 
                      context, from_email, 
                      to_email,
                      html_email_template_name=None)
            return redirect('password_reset_done.html')
    else:
        form = PasswordResetForm()
    return render(request,'password_reset_form.html', {'form': form})
