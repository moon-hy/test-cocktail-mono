from django.db import models
from django.utils.translation import gettext_lazy as _


class Ingredient(models.Model):
    '''
    # 재료 테이블
    [FK] 대표
    이름
    설명
    알코올도수
    (구매방법)
    '''
    representation = models.ForeignKey(
        to="Representation",
        related_name="ingredients",
        verbose_name=_("Representation"),
        on_delete=models.CASCADE)

    name = models.CharField(
        verbose_name=_("Ingredient Name"),
        max_length=50,
        unique=True,
        db_index=True)

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True)

    alcohol_by_volume = models.DecimalField(
        verbose_name=_("ABV"),
        max_digits=5,
        decimal_places=2,
        default=0.0)

    created_by = models.IntegerField(
        verbose_name=_("Created User Id"),
        blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '1_Ingredient'


class Representation(models.Model):
    '''
    - 어떤 재료를 대표하는 명칭. ex) Triple Sec, Cointreau => Orange Liqueur
    # 대표 테이블
    [FK] 카테고리
    대표이름
    '''
    category = models.ForeignKey(
        to="Category",
        verbose_name=_("Category"),
        on_delete=models.CASCADE)

    name = models.CharField(
        verbose_name=_("Representation Name"),
        max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '2_Representation'


class Category(models.Model):
    '''
    # 카테고리 테이블
    카테고리이름
    '''
    name = models.CharField(
        verbose_name=_("Category Name"),
        max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '3_Category'
