from django.conf import settings
from django.db import models

from django_extensions.db.models import TimeStampedModel


class Author(TimeStampedModel):
    """저자"""
    name = models.CharField('이름', db_index=True, max_length=30)
    birth_date = models.DateField('출생일', null=True, blank=True)

    def __str__(self):
        return '{}_{}'.format(self.name, self.birth_date)


class Book(TimeStampedModel):
    """도서"""
    author = models.ForeignKey(Author, related_name='books')
    title = models.CharField('제목', db_index=True, max_length=100)
    # TODO - 표준 언어코드로(https://ko.wikipedia.org/wiki/ISO_639#.EC.96.B8.EC.96.B4_.EB.B6.80.ED.98.B8_.EB.AA.A9.EB.A1.9D)
    language = models.CharField('언어', max_length=10, blank=True)
    publisher = models.CharField('출판사', max_length=50, blank=True)
    date_of_publication = models.DateField('출판일', null=True, blank=True)
    cover_img = models.ImageField('표지그림', blank=True)

    def __str__(self):
        return '{}_{}'.format(self.title, self.author.name)


class BookMark(TimeStampedModel):
    """책갈피"""
    reader = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bookmarks')
    book = models.ForeignKey(Book, related_name='bookmarks')
    page = models.IntegerField('페이지')

    def __str__(self):
        return '{}_{}'.format(self.reader.email, self.book.title)


class Comment(TimeStampedModel):
    """서평"""
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')
    book = models.ForeignKey(Book, related_name='comments')
    contents = models.CharField('내용', max_length=500)

    def __str__(self):
        return '{}_{}'.format(self.writer.email, self.book.title)

