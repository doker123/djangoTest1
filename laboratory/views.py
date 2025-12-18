from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Employee
from .forms import EmployeeForm


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'laboratory/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(full_name__icontains=search_query) | \
                       queryset.filter(position__icontains=search_query) | \
                       queryset.filter(academic_degree__icontains=search_query)
        return queryset


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'laboratory/employee_detail.html'
    context_object_name = 'employee'


class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'laboratory/employee_form.html'
    success_url = reverse_lazy('employee_list')
    permission_required = 'laboratory.add_employee'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'laboratory/employee_form.html'
    success_url = reverse_lazy('employee_list')
    permission_required = 'laboratory.change_employee'


class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Employee
    template_name = 'laboratory/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')
    permission_required = 'laboratory.delete_employee'
