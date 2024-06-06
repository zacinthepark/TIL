## Related Manager

---

### Related Manager

- related manager는 N:1 혹은 M:N 관계에서 사용가능한 context

- 장고는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조할 때 사용할 수 있는 manager를 생성
    - 모델 생성 시 `objects`라는 매니저를 통해 queryset api를 사용할 수 있는 것처럼
    - related manager를 통해 queryset api를 사용할 수 있음

- N:1 관계에서 생성되는 related manager 이름은 참조하는 `modelName_set` 이름 규칙으로 만들어짐
    - ForeignKey 설정 시 `related_name` 옵션을 통해 역참조 시 사용할 manager 이름 설정 가능
    - 작성 후 migration 과정 필요
    - 설정 시 기존의 `modelName_set`은 더이상 사용할 수 없으며, 대체됨

### 역참조

- 나를 참조하는 테이블을 참조하는 것
    - 나를 외래 키로 참조 중인 다른 테이블에 접근하는 것
    - N:1에서 1이 N을 참조하는 것

- Aritlce(1):Comment(N)
    - `article.comment` 형식으로는 댓글 객체를 참조할 수 없음
    - `article.comment_set` 형식으로 댓글 객체를 참조할 수 있음
    - 참조 상황에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기에 `comment.article` 형태로 작성 가능

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    ...

```

- related_name 설정
    - migration 진행
    - `article.comments`를 통해 역참조

### Referencing User Model

- Django에서 User Model을 참조하는 방법
    - `settings.AUTH_USER_MODEL`
    - `get_user_model()`

- `settings.AUTH_USER_MODEL`
    - 문자열을 반환
    - 반환값은 'accounts.User'
    - models.py의 모델 필드에서 User 모델을 참조할 때 사용
    - 장고의 내부적인 동작 순서에 따라 아직 유저 객체가 생성되지 않은 시점에서 models.py가 임시로 참조할 수 있도록 문자열을 주는 것

- `get_user_model()`
    - 객체를 반환
    - 반환값은 User Object
    - 현재 활성화된 User 모델을 반환
    - 커스터마이징한 User 모델이 있을 경우엔 Custom User 모델, 그렇지 않으면 User를 반환
    - models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용
