from django import forms
from portals.models import Discussions


CHOICES = (('QA', 'QA'), ('BA', 'BA'), ('DEV', 'DEV'), ('Others', 'Others'))


class CreateForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CHOICES, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Discussions
        fields = ('name', 'description', 'category')
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
                   'description': forms.Textarea(attrs={'class':'form-control', 'rows':10, 'cols':10}),
                   }

