from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomAuthenticationForm, AvatarForm, BioForm, UserProfileSearchForm, BlogEntryForm, MessageForm
from django.contrib.auth import login, logout
from .models import UserProfile, BlogEntry, Message
from django.contrib.auth import get_user_model


def inicio(request):
    return render(request,"inicio.html")
def blog(request):
    return render(request,"blog.html")
def success(request):
    return render(request,"success.html")
def sobremi(request):
    return render(request,"sobremi.html")

def view_registrarse(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, "registrarse.html", context)

def view_iniciar_sesion(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = CustomAuthenticationForm()
    return render(request, "iniciar_sesion.html", {'form': form})

def view_cerrar_sesion(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")

def view_bio_avatar(request):
    user_profile, created = UserProfile.objects.get_or_create(username=request.user)

    if request.method == 'POST':
        if 'avatar_form' in request.POST:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=user_profile)

            if avatar_form.is_valid():
                avatar_form.save()
                return redirect('miperfil') 

        elif 'bio_form' in request.POST:
            # Procesar el formulario de bio
            bio_form = BioForm(request.POST, instance=user_profile)

            if bio_form.is_valid():
                bio_form.save()
                return redirect('miperfil')

    else:
        avatar_form = AvatarForm(instance=user_profile)
        bio_form = BioForm(instance=user_profile)
    
    bio_actual = user_profile.bio

    return render(request, 'miperfil.html', {'avatar_form': avatar_form, 'bio_form': bio_form, 'user_profile': user_profile, 'bio_actual': bio_actual})

def view_userprofilesearch(request):
    if request.method == 'GET':
        search_form = UserProfileSearchForm(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            resultados = UserProfile.objects.filter(username__icontains=query)
            return render(request, 'resultados.html', {'resultados': resultados, 'search_form': search_form})
    else:
        search_form = UserProfileSearchForm()

    return render(request, '/', {'search_form': search_form})

def view_blogandlikes(request):
    if request.method == 'POST':
        blog_form = BlogEntryForm(request.POST, request.FILES)
        if blog_form.is_valid():
            entry = blog_form.save(commit=False)
            entry.author = request.user
            entry.save()
            return redirect('blog') 
    else:
        blog_form = BlogEntryForm()

    entries = BlogEntry.objects.all()

    if 'like_entry_id' in request.POST:
        entry_id = request.POST['like_entry_id']
        entry = get_object_or_404(BlogEntry, pk=entry_id)
        user = request.user

        if user in entry.likes.all():
            entry.likes.remove(user)
        else:
            entry.likes.add(user)

        return redirect('blog')

    return render(request, 'blog.html', {'entries': entries, 'blog_form': blog_form})

def blog_detail(request, blog_id):
    entry = get_object_or_404(BlogEntry, id=blog_id)
    return render(request, 'blog_detail.html', {'entry': entry})

def profile_detail(request, username):
    profile = get_object_or_404(UserProfile, username=username)
    return render(request, 'profile_detail.html', {'profile': profile})

def view_mensajes(request):
    return render(request,"mensajes.html")

def send_message(request, recipient_username):
    recipient = get_object_or_404(get_user_model(), username=recipient_username)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Message.objects.create(sender=request.user, recipient=recipient, content=content)
            return redirect('inbox')
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form, 'recipient': recipient})

def select_recipient(request):
    users = get_user_model().objects.exclude(username=request.user.username)
    return render(request, 'select_recipient.html', {'users': users})

def inbox(request):
    received_messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    users = get_user_model().objects.all()

    return render(request, 'inbox.html', {'received_messages': received_messages, 'users': users})