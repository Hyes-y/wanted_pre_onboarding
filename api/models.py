from django.db import models


class Company(models.Model):
    NATIONAL_CHOICES = (
        ('KR', '대한민국'),
        ('US', '미국'),
        ('JP', '일본'),
        ('CN', '중국'),
        ('DE', '독일'),
    )

    name = models.CharField('회사명', max_length=30)
    country = models.CharField(max_length=2, choices=NATIONAL_CHOICES)
    location = models.CharField(max_length=30)


class User(models.Model):
    uid = models.CharField('회원아이디', max_length=30, unique=True)
    password = models.CharField(max_length=32)


class Post(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)

    uid = models.CharField('채용공고_id', unique=True, max_length=30)
    position = models.CharField('채용포지션', max_length=30)
    reward = models.PositiveIntegerField('채용보상금', default=0)
    skill = models.CharField('사용기술', max_length=30)
    description = models.TextField('채용내용')

    company = models.ForeignKey(Company, on_delete=models.CASCADE, db_column="c_id", related_name='company')


class Apply(models.Model):
    p_id = models.ForeignKey(Post, on_delete=models.CASCADE, db_column="p_id")
    u_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="u_id")