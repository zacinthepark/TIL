from django import forms
from .models import Question, Comment


class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = '__all__'


class CommentForm(forms.ModelForm):
    # 댓글에서 둘 중 하나 선택하는 form 작성
    PICK_A = False
    PICK_B = True
    PICKS = [
        (PICK_A, 'BLUE'),
        (PICK_B, 'RED'),
    ]
    pick = forms.ChoiceField(choices=PICKS)
    # pick = forms.ChoiceField(choices=PICKS, widget=forms.RadioSelect())
    
    class Meta:
        model = Comment
        fields = ('pick', 'content',)
