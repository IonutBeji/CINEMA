from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from companies.forms import CompanyForm
from companies.models import Company


class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


class CompaniesView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'companies/companies_index.html'


class EditCompanyView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/edit_company.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Company, id=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('companies:lista_companii')
