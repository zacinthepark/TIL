from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

    # 영화제목 위젯
    title = forms.CharField(
        label='영화 제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요.',
                'max_length': 20,
            }
        ),
    )

    # 관객수 위젯
    audience = forms.CharField(
        label='관객 수',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '관객 수를 입력하세요.',
            }
        ),
    )

    # 개봉일 위젯
    release_date = forms.DateField(
        label='개봉일',
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control',
                'type': 'date',
            }
        ),
    )

    # 장르 위젯
    GENRE = [
        ('Comedy', '코미디'),
        ('Horror', '호러'),
        ('Romance', '로맨스'),
        ('Drama', '드라마'),
        ('Action', '액션'),
        ('SF', 'SF'),
        ('Noir', '느와르'),
    ]
    genre = forms.ChoiceField(
        choices=GENRE,
        label='장르',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    # 평점 위젯
    score = forms.CharField(
        label='평점',
        widget=forms.NumberInput(
            attrs={
                'step': 0.5,
                'min': 0,
                'max': 5,
                'class': 'form-control',
                'placeholder': '0점~5점 중 평점을 입력하세요.',
            }
        ),
    )

    # 포스터 경로 위젯
    poster_url = forms.CharField(
        label='포스터 경로',
        initial='https://web.yonsei.ac.kr/_ezaid/board/_skin/albumRecent/3/no_image.gif',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    # 줄거리 위젯
    description = forms.CharField(
        label='줄거리',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '줄거리를 입력하세요.',
            }
        ),
    )
