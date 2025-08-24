from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=100,
        required=False,
        strip=True
    )

    def clean_q(self):
        data = self.cleaned_data["q"]
        # أي فلترة إضافية أو validation—مثلاً منع رموز ضارة
        return data