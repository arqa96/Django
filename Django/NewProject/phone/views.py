from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Phone
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class PhoneListView(ListView):
    model = Phone
    template_name = 'phone/home.html'
    context_object_name = 'phones'
    ordering = ['-pub_date']
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):

        context = super(PhoneListView, self).get_context_data(*args, **kwargs)
        context['apple_count'] = str(Phone.objects.filter(phone__iexact='apple').count())
        context['samsung_count'] = str(Phone.objects.filter(phone__iexact='samsung').count())
        context['xiaomi_count'] = str(Phone.objects.filter(phone__iexact='xiaomi').count())
        context['lg_count'] = str(Phone.objects.filter(phone__iexact='lg').count())

        return context


class UserPhoneListView(ListView):
    model = Phone
    template_name = 'phone/user_phones.html'
    context_object_name = 'phones'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Phone.objects.filter(user=user).order_by('-pub_date')


class PhoneDetailView(DetailView):
    model = Phone


class PhoneCreateView(CreateView, LoginRequiredMixin):
    model = Phone
    fields = ['phone', 'phone_model', 'image_field', 'price', 'name', 'metro', 'phone_number', 'comments']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PhoneUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Phone
    fields = ['phone', 'phone_model', 'image_field', 'price', 'name', 'metro', 'phone_number', 'comments']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        phone = self.get_object()
        if self.request.user == phone.user:
            return True
        return False


class PhoneDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Phone
    success_url = '/'

    def test_func(self):
        phone = self.get_object()
        if self.request.user == phone.user:
            return True
        return False
