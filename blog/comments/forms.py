from django import forms


class CommentForm(forms.Form):
    # hidden inputs means they are not visible to the user
    content_type = forms.CharField(widget=forms.HiddenInput)
    obj_id = forms.IntegerField(widget=forms.HiddenInput)
    # parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label=" ", widget=forms.Textarea)
