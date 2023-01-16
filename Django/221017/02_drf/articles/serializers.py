from rest_framework import serializers  # DRF 패키지에서 serializers 기능을 차용
from .models import Article, Comment    # ModelSerializer에 사용할 모델 import


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) # 최종적으로 조회는 되나, 유효성 검사에서 제외됨


# 게시글의 목록(게시글들의 QuerySet)을 serialize해서 나눌 것이기에 이름을 ArticleListSerializer로 명명
class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article                         # 해당 모델 정보에 맞춰 자동으로 필드 생성
        # 전체 게시글 목록에서는 생성일, 수정일은 빼고 보여주기
        fields = ('id', 'title', 'content',)    # 어떤 필드를 serialize할지 결정 (사용자에게 최종적으로 JSON에 보여질 것을 결정)


# 단일 게시글에 대한 상세 정보를 제공하는 serializer
# serialize하는 fields가 달라지면 다른 serializer를 만들어줘야함
class ArticleSerializer(serializers.ModelSerializer):
    # article 입장에서 comment는 N이기에 many=True 필요, 또한 유효성 검사에서 제외되어야 함
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # 기존 역참조용 필드를 override
    comment_set = CommentSerializer(many=True, read_only=True)  # 역참조할 시 pk말고 CommentSerializer에서 출력하는 모든 정보 출력 가능
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)    # 새로운 필드 추가
    
    class Meta:
        model = Article
        fields = '__all__'
