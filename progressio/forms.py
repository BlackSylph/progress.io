from django import forms


class StringForm(forms.Form):
    input_string = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
    output_string = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5, "readonly": True}))


class CaesarCipherForm(forms.Form):

    CAESAR_CIPHER_AVAILABLE_SHIFTS = [
        (1, 1),     (2, 2),
        (3, 3),     (4, 4),
        (5, 5),     (6, 6),
        (7, 7),     (8, 8),
        (9, 9),     (10, 10),
        (11, 11),   (12, 12),
        (13, 13),   (14, 14),
        (15, 15),   (16, 16),
        (17, 17),   (18, 18),
        (19, 19),   (20, 20),
        (21, 21),   (22, 22),
        (23, 23),   (24, 24),
    ]

    input_string = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
    shift = forms.ChoiceField(choices=CAESAR_CIPHER_AVAILABLE_SHIFTS)
    output_string = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5, "readonly": True}))