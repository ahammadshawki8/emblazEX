from django import forms

class SendMsgForm(forms.Form):
    username = forms.CharField(max_length = 256)
    number = forms.CharField(max_length = 24)
    body = forms.CharField(widget = forms.Textarea)