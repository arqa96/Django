from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Phone
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context = {
        'phones': Phone.objects.all().order_by('-pub_date'),
        'apple_count': str(Phone.objects.filter(phone__iexact='apple').count()),
        'samsung_count': str(Phone.objects.filter(phone__iexact='samsung').count()),
        'xiaomi_count': str(Phone.objects.filter(phone__iexact='xiaomi').count()),
        'lg_count': str(Phone.objects.filter(phone__iexact='lg').count())
    }
    return render(request, ('phone/home.html','phone/base.html'), context)


class PhoneDetailView(DetailView):
    model = Phone

class PhoneCreateView(CreateView, LoginRequiredMixin,  UserPassesTestMixin):
    model = Phone
    fields = ['phone', 'phone_model', 'image', 'price', 'name', 'metro', 'phone_number']

    def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)

class PhoneUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Phone
    fields = ['phone', 'phone_model', 'image', 'price', 'name', 'metro', 'phone_number']

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
