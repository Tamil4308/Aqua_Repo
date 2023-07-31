from django import forms
from django.contrib.auth.models import User
from cartfish.models import Post

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

# define the class of a form
class PostForm(forms.ModelForm):
	class Meta:
		# write the name of models for which the form is made
		model = Post	

		# Custom fields
		fields =["NAME", "MOBILE_NO", "ENQUIRE"]

	# this function will be used for the validation
	def clean(self):

		# data from the form is fetched using super function
		super(PostForm, self).clean()
		
		# extract the username and text field from the data
		username = self.cleaned_data.get('NAME')
		text = self.cleaned_data.get('ENQUIRE')

		# conditions to be met for the username length
		if len(username) < 5:
			self._errors['NAME'] = self.error_class([
				'Minimum 5 characters required'])
		if len(text) <10:
			self._errors['ENQUIRE'] = self.error_class([
				'Post Should Contain a minimum of 10 characters'])

		# return any errors if found
		return self.cleaned_data