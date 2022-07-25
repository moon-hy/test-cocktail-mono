from django.db import models
from django.utils.translation import gettext_lazy as _


class Recipe(models.Model):
    '''
    # 칵테일 재료 중간 테이블
    [FK] 칵테일
    [~FK] 재료
    용량
    단위
    '''
    cocktail = models.ForeignKey(
        to="cocktail.Cocktail",
        related_name="recipe",
        verbose_name=_("Cocktail"),
        blank=True,
        on_delete=models.CASCADE)

    ingredient = models.ForeignKey(
        to="ingredient.Ingredient",
        related_name="recipe",
        verbose_name=_("Ingredient"),
        blank=True,
        on_delete=models.CASCADE)

    volume = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        verbose_name=_("Ingredient Volume"))

    unit = models.CharField(
        verbose_name=_("Ingredient Unit"),
        max_length=16)

    optional = models.BooleanField(
        verbose_name=_("Optional"),
        default=False)
    
    class Meta:
        ordering = [ 'cocktail' ]
        db_table = 'COCKTAIL_RECIPE'

    def __str__(self):
        return f'{self.cocktail.name} | {self.ingredient.name} | {str(self.volume)} {self.unit}'
