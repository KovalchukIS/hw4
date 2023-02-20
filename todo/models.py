from django.db import models
from django.conf import Settings

from django.db import models
from django.utils import timezone


class List(models.Model):

    name = models.CharField(help_text="Имя задачи", max_length=300)
    is_done = models.BooleanField(default=False, help_text="Выполнена ли задача")
    start_dt = models.DateTimeField(
        default=timezone.now, help_text="Дата и время создания"
    )
    end_dt = models.DateTimeField(
        default=timezone.now, blank=True, null=True, help_text="Дата и время завершения"
    )

    def save(self, *args, **kwargs) -> None:
        """Переопределение сохранения.

        Убирается галочка активности корзины если нет привязанного пользователя.
        """
        if self.is_done is False and self.end_dt:
            self.end_dt = None
        if self.is_done is True:
            self.end_dt = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"Task {self.id}|{self.name}|{self.start_dt}|{self.end_dt}"
