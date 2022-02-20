from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = { 
            'name': forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Name',
            }),
            'email': forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Email',
            }),
            'subject': forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Subject',
            }),
            'message': forms.Textarea(attrs={
                'class' : 'form-control', 
                'rows' : '4',
                'placeholder' : 'Message',
            }) 
        }

    custom_names = {
        'name': 'Your Name', 
        'email': 'Your Email', 
        'subject': 'Subject', 
        'message': 'Message'
    }

    def add_prefix(self, field_name):
        field_name = self.custom_names.get(field_name, field_name)
        return super(ContactForm, self).add_prefix(field_name)

