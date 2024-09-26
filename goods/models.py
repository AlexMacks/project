from django.db import models

# class Card(models.Model):       
#     class status(models.IntegerChoices):       
#         UNCHECKED = 0, 'не проверено'
#         CHECKED = 1, 'проверено'

#     id = models.AutoField(primary_key=True, db_column='CardID')
#     name = models.CharField(max_length=255, db_column='Name', verbose_name='Наименование')
#     description = models.TextField(max_length=5000, db_column='Description', verbose_name='Описание')
#     price = models.IntegerField(db_column='Price', verbose_name='Цена')
#     category = models.ForeignKey('Category', on_delete=models.CASCADE, db_column='CategoryID', verbose_name='Категория')
#     upload_date = models.DateTimeField(auto_now_add=True, db_column='UploadDate', verbose_name='Дата загрузки')
#     views = models.IntegerField(default=0, db_column='Views', verbose_name='Просмотры')
#     adds = models.IntegerField(default=0, db_column='Favorites', verbose_name='Добавления в избранное')
#     tags = models.ManyToManyField('Tag', through='CardTag', related_name='cards', verbose_name='Теги')
#     status = models.BooleanField(default=0, choices=(map(lambda x: (bool(x[0]), x[1]), status.choices)), verbose_name='Проверено')

#     class Meta:
#         db_table = 'Cards'
#         verbose_name = 'Карточка товара'
#         verbose_name_plural = 'Карточки товаров'

#     def __str__(self):
#         return f'Товар "{self.name}"'


#     def get_absolute_url(self):
#         return f'/goods/{self.id}/detail/'
  
