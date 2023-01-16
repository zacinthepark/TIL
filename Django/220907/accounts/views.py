from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    # 로그인된 유저라면 login 함수를 마저 실행하지 않고 index page로 이동시킴
    if request.user.is_authenticated:
        return redirect('articles:index')
    # 로그인 정보 입력 후 제출 버튼 눌렀을 때
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)    # AuthenticationForm은 Form을 상속받고, ModelForm과 다르게 Form은 첫번째 인자가 request
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인 (로그인은 Session을 만드는 것이기에 save는 아님)
            auth_login(request, form.get_user())   # request.POST을 받은 form에 유저정보가 있을 것 # AuthenticationForm에서 .get_user()라는 인스턴스 메서드를 제공함
            # url querystring에 next 키 값이 있는 경우는 로그인이 안된 경우에 비정상적으로 article을 create 혹은 update하려는 경우의 url
            # 비정상적 접근의 경우 로그인 후 next 키 값에 있는 /articles/create/ 혹은 /articles/pk/update/로 이동
            # 로그인 버튼을 통한 정상적 로그인은 index 화면으로 이동
            return redirect(request.GET.get('next') or 'articles:index')    # 단축평가
    # 로그인 페이지 렌더링
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    # 로그아웃
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    # 유저 생성
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)     # ModelForm의 성격을 띠기에 data가 첫번째 인자
        if form.is_valid():
            user = form.save()                          # save()는 데이터에 유저생성, 그와 동시에 공식문서에서 확인해보면 user를 리턴해줌 / 이를 user에 할당하여 로그인 인자에 넣어줌
            # 회원가입 후 redirect전에 로그인시킨 상태로 전환
            auth_login(request, user)
            return redirect('articles:index')
    # 회원가입 페이지 렌더링
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        # 탈퇴 - 로그아웃 순서 (로그아웃을 먼저 하면 session이 사라져서 request.user에서 접근할 수 없음)
        # request.user에 유저 데이터가 있음
        request.user.delete()
        # 어차피 회원탈퇴하면 죽은 세션이 되어서 필수는 아니지만 session을 지우고 탈퇴하고자 한다면 추가
        auth_logout(request)
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    # 회원정보 수정 DB에 요청
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    # 회원정보 수정 페이지 렌더링
    else:
        form = CustomUserChangeForm(instance=request.user)  # 내용 채운 form
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    # 비밀번호 변경 요청
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)   # 첫번째 인자 user, 두번째 인자 data
        if form.is_valid():
            form.save()                                         # 비밀번호 변경됨
            # user = form.save() 후 (request, user)도 가능함
            update_session_auth_hash(request, form.user)        # 세션 sync
            return redirect('articles:index')
    # 비밀번호 변경 페이지 렌더링
    else:
        # PasswordChangeForm은 SetPasswordForm의 하위 클래스로, SetPasswordForm은 첫번째 인자로 user를 받음
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)
