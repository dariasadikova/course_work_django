from django.db import models
from django.urls import reverse

class Genre(models.Model):

    name = models.CharField(max_length=200, help_text="Введите название жанра (например, драма или комедия)", verbose_name="Название")
    
    class Meta:
      verbose_name = "жанр"
      verbose_name_plural = "Жанры"
      

    def __str__(self):
        return self.name


class Play(models.Model):

    name = models.CharField(max_length=200, help_text="Введите название спектакля", verbose_name="Название")
    genre = models.ManyToManyField(Genre, help_text="Выбери жанр", verbose_name="Жанр")
    director = models.CharField(max_length=200, help_text="Введите ФИ режиссера", verbose_name="Режиссер")
    datetime = models.DateTimeField(help_text="Введите дату и время", verbose_name="Дата и время")
    
    class Meta:
      verbose_name = "спектакль"
      verbose_name_plural = "Спектакли"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):

        return reverse('play-detail', args=[str(self.id)])
        
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ]) 
    display_genre.short_description = 'Жанр'
        
        
class Actor(models.Model):

    name = models.CharField(max_length=200, help_text="Введите имя актера", verbose_name="Имя")
    surname = models.CharField(max_length=200, help_text="Введите фамилию актера", verbose_name="Фамилия")
    date_of_birth = models.DateField(help_text="Введите дату рождения актера", verbose_name="Дата рождения")
    contact = models.CharField(max_length=200, help_text="Введите номер телефона актера", verbose_name="Номер телефона")
    
    class Meta:
      verbose_name = "актер"
      verbose_name_plural = "Актеры"

    def __str__(self):
    
        return f"{self.name} {self.surname}"
    
    def get_absolute_url(self):

        return reverse('actor-detail', args=[str(self.id)])

class Ticket(models.Model):

    play = models.ForeignKey('Play', on_delete=models.CASCADE, verbose_name="Спектакль")
    seatkind = models.CharField(max_length=200, help_text="Введите название категории места", verbose_name="Категория места")
    seatnum = models.PositiveIntegerField(null=False, help_text="Введите номер места", verbose_name="Номер места")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Введите стоимость билета", verbose_name="Цена")
    status = models.BooleanField(default=True, help_text="Укажите, доступен ли к продаже билет", verbose_name="Доступен (не продан)")
    
    class Meta:
      verbose_name = "билет"
      verbose_name_plural = "Билеты"

    def __str__(self):

        return f"Ticket #{self.id}"

class Viewer(models.Model):

    name = models.CharField(max_length=200, help_text="Введите имя зрителя", verbose_name="Имя")
    surname = models.CharField(max_length=200, help_text="Введите фамилию зрителя", verbose_name="Фамилия")
    contact = models.CharField(max_length=200, help_text="Введите номер телефона зрителя", verbose_name="Номер телефона")
    visits = models.PositiveIntegerField(default=0, help_text="Введите кол-во предыдущих посещений театра", verbose_name="Кол-во посещений")
    
    class Meta:
      verbose_name = "зритель"
      verbose_name_plural = "Зрители"

    def __str__(self):
        return f"{self.name} {self.surname}"

class Review(models.Model):

    viewer = models.ForeignKey('Viewer', on_delete=models.CASCADE, verbose_name="Зритель")
    play = models.ForeignKey('Play', on_delete=models.CASCADE, verbose_name="Спектакль")
    text = models.TextField(help_text="Введите текст отзыва", verbose_name="Текст")
    mark = models.PositiveIntegerField(help_text="Поставьте оценку спектаклю (от 1 до 10)", verbose_name="Оценка")
    
    class Meta:
      verbose_name = "отзыв"
      verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Review #{self.id}"

class Booking(models.Model):

    viewer = models.ForeignKey('Viewer', on_delete=models.CASCADE, verbose_name="Зритель")
    play = models.ForeignKey('Play', on_delete=models.CASCADE, verbose_name="Спектакль")
    amount = models.PositiveIntegerField(help_text="Введите кол-во бронируемых билетов", verbose_name="Кол-во билетов")
    status = models.BooleanField(default=False, help_text="Укажите, подтверждена ли бронь", verbose_name="Подтверждено")
    
    class Meta:
      verbose_name = "бронь"
      verbose_name_plural = "Бронирования"

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return f"Booking #{self.id}"
