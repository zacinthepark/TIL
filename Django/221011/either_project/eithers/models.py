from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    issue_a = models.CharField(max_length=50)
    issue_b = models.CharField(max_length=50)


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    pick = models.BooleanField()    # 댓글 중 좌,우를 선택할 때 컬럼을 무엇으로 할지 (값이 2개이므로 Boolean 활용, 0과 1의 값이 들어감)
    # pick = models.IntegerField()
