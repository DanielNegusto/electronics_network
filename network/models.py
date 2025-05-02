from django.db import models


class Contact(models.Model):
    """Модель контактов поставщика."""
    name = models.CharField(max_length=255, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель продукта."""
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.name} ({self.model})"


class NetworkNode(models.Model):
    """Модель сетевого узла."""
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название')
    contacts = models.OneToOneField(Contact, on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='supplied_by', verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность', default=0.00)
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Уровень')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Сетевой узел'
        verbose_name_plural = 'Сетевые узлы'

    def __str__(self):
        return self.name
