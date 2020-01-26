from django.db import models as m

# Create your models here.

class Author(m.Model):
    first_name = m.CharField(max_length=50)
    last_name = m.CharField(max_length=50)
    image_url = m.CharField(max_length=150)

    def __str__(self):
        return self.first_name
    

class Book(m.Model):
    WHITE = 'WT'
    YELLOW = 'YW'
    BLACK='BK'
    RED='RD'
    GREEN='GN'
    PURPLE='PL'
    BOOK_COLOR_CHOICES = [
        (WHITE, 'White'),
        (YELLOW, 'Yellow'),
        (BLACK,'Black'),
        (RED,'Red'),
        (GREEN,'Green'),
        (PURPLE,'Purple'),
    ]
    title= m.CharField(max_length=100)
    available= m.BooleanField()
    color = m.CharField(choices = BOOK_COLOR_CHOICES, max_length=5)
    author=m.ForeignKey(Author, on_delete=m.CASCADE)


    def __str__(self):
        return self.title