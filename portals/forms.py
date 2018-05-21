from django import forms
from portals.models import Discussions, Replies
from django.contrib.auth.forms import AuthenticationForm


CHOICES = (('QA', 'QA'), ('BA', 'BA'), ('DEV', 'DEV'), ('Others', 'Others'))


class CreateForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CHOICES, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Discussions
        fields = ('name', 'description', 'category')
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
                   'description': forms.Textarea(attrs={'class':'form-control', 'rows':10, 'cols':10}),
                   }


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Replies
        fields = ('content','replied_by')
        widgets = {'content':forms.Textarea(attrs={'class':'form-control', 'rows':5})}


class UserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

