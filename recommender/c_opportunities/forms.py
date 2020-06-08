from django import forms

class SearchForm(forms.Form):
    search_term = forms.CharField(label='Search term here', max_length=200)


class SimilarsForm(forms.Form):
    base_document_idx = forms.IntegerField()
