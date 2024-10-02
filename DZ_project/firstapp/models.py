from django.db import models

# Create your models here.
class clients(models.Model):
    nickname = models.CharField(max_length = 100, verbose_name = "Никнейм")
    name = models.CharField(max_length = 50, verbose_name = "Имя")
    lastname = models.CharField(default=None, max_length = 100, verbose_name = "Фамилия")
    purchase_history = models.CharField(default=None, max_length = 500, verbose_name = "История покупок")
    date_of_last_purchase = models.DateTimeField(default=None, verbose_name = "Дата и время последней покупки")
    dor = models.DateField(auto_now=True, verbose_name = "Дата регистрации")
    email = models.EmailField(verbose_name = "E-mail")
    city = models.CharField(default = "Санкт-Петербург", max_length = 100, verbose_name = "Город")

class products(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Наименование")
    count = models.IntegerField(verbose_name = "Кол-во поступившее")
    count_left = models.IntegerField(verbose_name = "Кол-во оставшееся")
    price_selling = models.FloatField(verbose_name = "Цена продажи")
    price_purchase = models.FloatField(verbose_name = "Цена закупки")
    tags = models.CharField(default = "game_PC", max_length = 100, verbose_name= "Тэги")
    doc = models.DateTimeField(auto_now=True, verbose_name = "Дата и время изменения")
    discount2 = models.IntegerField(verbose_name = "Скидка %", blank=True, default=10)
    pic = models.ImageField(upload_to = "firstapp/static/img", blank = True)

    def discount(self):
        cost = self.price_selling - (self.price_selling * self.discount2 * 0.01)
        return cost


class tags(models.Model):
    tag = models.CharField(max_length = 100, verbose_name = "Тэг")
    tag_RU = models.CharField(max_length = 100, verbose_name = "Тэг на русском")
