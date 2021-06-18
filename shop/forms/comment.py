from django import forms
from shop.models.Comment import Comment

class CommentForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['message', 'name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customer class css
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control'})