from django import forms
class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    telefone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
