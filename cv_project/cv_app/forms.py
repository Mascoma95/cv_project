from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50)	#da specificare name = "name" nell'input del form
	email = forms.EmailField(max_length = 150)
	subject = forms.CharField(max_length = 50)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)