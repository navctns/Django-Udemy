
from django import forms
from .models import Category

# class AddCategoryForm(forms.Form):
#     """Form to create category"""
#     title = forms.CharField()
#
#     def create_category(self):
#         """Create category from form"""
#         newCat = Category(title= self.title)
#         newCat.save()
#         print("New Category Created")

class AddCategoryForm(forms.ModelForm):
    """Form to create category ModelForm"""
    # title = forms.CharField()
    class Meta:
        model = Category
        fields = ['title']

        widgets = {
            'title':forms.TextInput(attrs= {'class':'form-control'}),
        }
