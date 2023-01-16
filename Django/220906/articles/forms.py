from django import forms
from .models import Article

# Form 상속
# class ArticleForm(forms.Form):
#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATION_CHOICES = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATION_CHOICES)
    # nation = forms.ChoiceField(choices=NATION_CHOICES, widget=forms.RadioSelect)

# ModelForm 상속 (모델을 기반으로 한 Form)
class ArticleForm(forms.ModelForm):
    # 모델의 해당 필드가 이러이러한 form에 들어갈 것이다
    # form 형식 설정
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',   # form-control은 bootstrap custom form layout을 위함
                'placeholder': 'Enter the title',
                'max-length': 10    # 페이지에서 10글자 이상을 입력할 수 없다뿐이지 유효성 검사와는 무관
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        # 유효성 검사 관련 출력한 에러 메세지 커스텀 정의
        error_messages={
            'required': 'Please enter your content'
        }
    )

    # form 정보
    class Meta:
        model = Article         # 어떤 모델을 기반으로 할지 (참조값)
        fields = '__all__'      # 모델 필드 중 어떤 것을 출력할지
        # exclude = ('title',)  # 그 중 어떤 필드를 제외할 것인지
