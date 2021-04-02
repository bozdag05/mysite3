from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Fact, Category
from .forms import Factsform, UserRegisterForm, UserLoginForm, ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'Ощибка регистраций :(')
    else:
        form = UserRegisterForm()
    return render(request, 'fact/register.html', {"form": form})


def user_login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    else:
        form = UserLoginForm()

    return render(request, 'fact/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'muhammadosmanov02@gmail.com',
                             ['makhmydosmanov@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Сообщение успешно отправленно')
                return redirect('contact')
            else :
                messages.error(request, 'Ошибка отправки  :(')

        else:
            messages.error(request, 'Ошибка валитаци :(')
    else:
        form = ContactForm()

    return render(request, 'fact/test.html', {'form': form})


class HomeFact(ListView):
    model = Fact
    template_name = 'fact/home_fact_list.html'
    context_object_name = 'fact'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная Страница'
        return context

    def get_queryset(self):
        return Fact.objects.filter(is_published=True)


class FactByCategory(ListView):
    model = Fact
    template_name = 'fact/home_fact_list.html'
    context_object_name = 'fact'
    allow_empty = False
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Fact.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewContent(DetailView):
    model = Fact
    context_object_name = 'content_item'
    # template_name = 'fact/fact_detail.html'
    # pk_url_kwarg = 'content_id'


class CreateFact(LoginRequiredMixin, CreateView):
    form_class = Factsform
    template_name = 'fact/add_fact.html'
    # login_url = '/admin/'
    raise_exception = True


'''def index(request) :
    fact = Fact.objects.all()

    context = {
        'fact': fact,
        'title': 'Список новостей',
    }
    return render(request , 'fact/index.html' , context=context)'''

'''def get_category(request , category_id):
    fact = Fact.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)

    return render(request, 'fact/category.html', {'fact': fact , 'category': category})'''

'''def get_content (request , content_id):
    #content_item = Fact.objects.get(pk=content_id)
    content_item = get_object_or_404(Fact , pk=content_id)
    return render(request, 'fact/content.html', {'content_item': content_item})'''

'''def add_fact(request):
    if request.method == 'POST':
        form = Factsform(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # fact = Fact.objects.create(**form.cleaned_data)
            fact = form.save()
            return redirect(fact)
    else :
        form = Factsform()
    return render(request, 'fact/add_fact.html', {'form':form})'''
