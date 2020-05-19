from django import forms


class StringForm(forms.Form):
    input_string = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
    output_string = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5, "readonly": True}))
