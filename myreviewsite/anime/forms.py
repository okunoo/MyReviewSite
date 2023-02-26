from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='検索キーワードを入力', max_length=100)
    
