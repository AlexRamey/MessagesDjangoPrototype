from django import forms

class MessageForm(forms.Form):
    sender_id = forms.IntegerField(label = 'sender')
    receiver_id = forms.IntegerField(label='receiver')
    message_text = forms.CharField(label='message: ', max_length = 100)