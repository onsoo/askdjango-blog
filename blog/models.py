import re
from django.urls import reverse
from django.db import models
from django.forms import ValidationError

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')



class Post(models.Model):

    STATUS_CHOICE = (
        ('d', 'Draft'),
        ('p', 'Pubplished'),
        ('w', 'Withdrawn'),
    )

    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name="제목",
        help_text="제목을 입력해주세요. 최대 100자 이내")
    content = models.TextField(verbose_name="내용")               # 길이 제한이 없는 문자열
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=100, blank=True,
        validators=[lnglat_validator],
        help_text="경도, 위도 포맷으로 입력") 
    tag_set = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)  # 최초 설정시 값 
    updated_at = models.DateTimeField(auto_now=True)      # 업데이트 될 때마다 업데이트됨

    class Meta:
        ordering = ['-id']  #1차 기준, 2차 기준 가능함 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])



class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
 
