from django.db import models
from django.utils.translation import gettext_lazy as _


class Cocktail(models.Model):
    '''
    # 칵테일 테이블
    이름
    설명
    도수
    베이스
    [M2M]재료 리스트
    제조 방법
    색상
    [M2M]태그
    '''
    name = models.CharField(
        verbose_name=_("Cocktail Name"), 
        max_length=50)

    description = models.TextField(
        verbose_name=_("Cocktail Description"),
        blank=True)
        
    alcohol_by_volume = models.DecimalField(
        verbose_name=_("Cocktail ABV"), 
        max_digits=5, 
        decimal_places=2,
        blank=True,
        default=0)
    
    base = models.CharField(
        verbose_name=_("Cocktail Base"),
        max_length=16)

    detail = models.TextField(
        verbose_name=_("Cocktail Detail"),
        blank=True)
    
    color = models.CharField(
        verbose_name=_("Cocktail Color"),
        max_length=16)

    tags = models.ManyToManyField(
        to="Tag", 
        verbose_name=_("Cocktail Tag"),
        blank=True)

    created_by = models.IntegerField(
        verbose_name=_("Created User Id"))

    class Meta:
        ordering = [ 'name' ]

    def __str__(self):
        return self.name


class Tag(models.Model):
    '''
    # 태그 테이블
    이름
    '''
    name = models.CharField(
        verbose_name=_("Tag Name"), 
        max_length=50,
        primary_key=True)

    class Meta:
        ordering = [ 'name' ]

    def __str__(self):
        return self.name
