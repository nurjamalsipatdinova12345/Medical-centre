from django import forms
from .models import Appointment, Contact

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Atiniz'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailiniz'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefoniniz'}),
            # MUHIM: datetime-local va formatni belgilash
            'date': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Xabar...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Select menyularida birinchi tanlovni ko'rsatish
        self.fields['department'].empty_label = "Bolimdi tanlan"
        self.fields['doctor'].empty_label = "shipakerdi tanlan"
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Atiniz'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailiniz'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tema'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Xabariniz...'}),
        }