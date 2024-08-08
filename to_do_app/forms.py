from django import forms

from to_do_app.models import Test, Todo

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = "__all__"
class ToDo(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

