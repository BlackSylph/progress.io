from django import forms


class StringForm(forms.Form):
    input_string = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
    output_string = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5, "readonly": True}))


class StringParametersForm(forms.Form):
    input_string = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
    input_parameters = forms.CharField(widget=forms.Textarea(attrs={"rows": 1}))
    output_string = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5, "readonly": True}))