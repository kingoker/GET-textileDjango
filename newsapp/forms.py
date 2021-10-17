from django import forms
from .models import Comment
from django.core.validators import RegexValidator

PHONE = r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{2}[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{2}[-\s\.]?[0-9]{2}$'


class ContactForm(forms.ModelForm):
	phone = forms.CharField(max_length=255, validators=[RegexValidator(PHONE, message="Invalid Phone number")])
	class Meta:
		model = Comment
		fields = ("name", "phone", "email", "comment")

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.label = ""
		self.fields["name"].widget.attrs.update({"class" : "contacts__form-name input", "placeholder" : "Name"})	
		self.fields["phone"].widget.attrs.update({"class" : "contacts__form-phone input", "placeholder" : "Phone: e.g: +998991234567"})
		self.fields["email"].widget.attrs.update({"class" : "contacts__form-email input", "placeholder" : "Email"})
		self.fields["comment"].widget.attrs.update({"class" : "contacts__form-text input", "placeholder" : "Comment", "cols" : "30", "rows" : "10"})
