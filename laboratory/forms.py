from django import forms
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):

    full_name = forms.CharField(
        label="ФИО",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ФИО сотрудника',
            'required': 'required'
        })
    )

    age = forms.IntegerField(
        label="Возраст",
        min_value=18,
        max_value=100,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'required': 'required'
        })
    )

    position = forms.CharField(
        label="Должность",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите должность сотрудника',
            'required': 'required'
        })
    )

    academic_degree = forms.CharField(
        label="Ученая степень",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Например: кандидат наук, доктор наук'
        })
    )

    class Meta:
        model = Employee
        fields = [
            'full_name',
            'gender',
            'age',
            'marital_status',
            'has_children',
            'position',
            'academic_degree'
        ]
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'marital_status': forms.Select(attrs={'class': 'form-select'}),
            'has_children': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'gender': 'Пол',
            'marital_status': 'Семейное положение',
            'has_children': 'Есть дети',
        }

    def clean_full_name(self):

        full_name = self.cleaned_data['full_name'].strip()
        if len(full_name.split()) < 2:
            raise forms.ValidationError("ФИО должно содержать как минимум имя и фамилию")
        return full_name

    def clean_age(self):

        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Сотрудник должен быть совершеннолетним")
        if age > 100:
            raise forms.ValidationError("Некорректный возраст")
        return age


class SimpleRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    user_type = forms.ChoiceField(
        choices=[
            ('hr', 'Отдел кадров'),
            ('trade_union', 'Профком'),
        ],
        required=True,
        label='Тип пользователя'
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']