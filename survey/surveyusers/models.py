from django.db import models


class User(models.Model):
    userid = models.UUIDField(primary_key=True, editable=False)

    def __str__(self):
        return self.userid

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Survey(models.Model):
    name = models.CharField("Опрос", max_length=30)
    description = models.TextField("Описание")
    start_date = models.DateTimeField(editable=False, auto_now=True)
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Опроы"
        verbose_name_plural = "Опросы"


class Questions(models.Model):
    name = models.CharField("Вопрос", max_length=30)
    description = models.TextField("Текст вопроса")
    type = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
    question = models.ForeignKey(Questions, on_delete=models.PROTECT)
    name = models.CharField("Ответ", max_length=30)
    answer = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
