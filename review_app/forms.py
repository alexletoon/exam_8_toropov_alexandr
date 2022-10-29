from django import forms
from django.forms import widgets
from review_app.models import Product, Choice, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description','category', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']

    # def save(self, commit=True):
    #     if commit:
    #         Review.author.add(self.request.user)
    #     return super().save(commit)


    # def save(self, commit=True):
    #     self.object.author
    #     review = super().save(commit=False)
    #     user.set_password(self.cleaned_data.get('password'))
    #     user.groups.add('user')
    #     if commit:
    #         user.save()
    #         user.profile = Profile.objects.get_or_create(user=user)
    #     return user

