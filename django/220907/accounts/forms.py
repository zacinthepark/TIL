from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User                          # 직접 참조 (Django에서는 권장하지 않음)

class CustomUserCreationForm(UserCreationForm):
    # Meta 부분만 overriding
    class Meta(UserCreationForm.Meta):
        # model = User                              # 직접 참조 (Django에서는 권장하지 않음)
        model = get_user_model()
        # 기본적으로 UserCreationsForm.Meta에 있는 fields는 ('username',)
        # DB의 accounts_user를 확인해보면 username만 있고 password1, password2는 없음
        # password1, password2는 UserCreationForm에서 인증용으로 fields 밖에 따로 설정되어 있음 (Django 문서에서 확인)
        fields = UserCreationForm.Meta.fields + ('email',)  # 추가할 수 있는 필드명은 accounts_user에 있는 컬럼만 가능 (migrations 파일에서 확인 가능)

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # admin에서 보여주는 UserChangeForm을 다 보여주면 안되므로 선택적으로 보여주기 위해 필드 재정의
        # 비밀번호는 유저 모델이 아닌 다른 form에서 변경하는 것이 일반적
        fields = ('email', 'first_name', 'last_name',)
