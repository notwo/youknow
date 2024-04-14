from django.test import TestCase
from django.urls import reverse
from string import Template


class TestsUrls(TestCase):
    # define constant value methods
    @staticmethod
    def you_know_customuser_pk():
        return 'aaaa'

    @staticmethod
    def library_id():
        return '1'

    @staticmethod
    def category_id():
        return '1'

    @staticmethod
    def keyword_id():
        return '1'

    def test_library_list_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/')
        view = reverse('library-list', kwargs={'you_know_customuser_pk': self.you_know_customuser_pk()})
        self.assertEqual(view, t.substitute(you_know_customuser_pk=self.you_know_customuser_pk()))

    def test_category_list_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/${library_id}/categories/')
        view = reverse('category-list', kwargs={
            'you_know_customuser_pk': self.you_know_customuser_pk(),
            'library_pk': self.library_id()
        })
        self.assertEqual(
            view,
            t.substitute(
                you_know_customuser_pk=self.you_know_customuser_pk(),
                library_id=self.library_id()
            )
        )

    def test_keyword_list_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/${library_id}/categories/${category_id}/keywords/')
        view = reverse('keyword-list', kwargs={
            'you_know_customuser_pk': self.you_know_customuser_pk(),
            'library_pk': self.library_id(),
            'category_pk': self.category_id()
        })
        self.assertEqual(
            view,
            t.substitute(
                you_know_customuser_pk=self.you_know_customuser_pk(),
                library_id=self.library_id(),
                category_id=self.category_id()
            )
        )

    def test_keyword_detail_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/${library_id}/categories/${category_id}/keywords/${keyword_id}/')
        view = reverse('keyword-detail', kwargs={
            'you_know_customuser_pk': self.you_know_customuser_pk(),
            'library_pk': self.library_id(),
            'category_pk': self.category_id(),
            'pk': self.keyword_id()
        })
        self.assertEqual(
            view,
            t.substitute(
                you_know_customuser_pk=self.you_know_customuser_pk(),
                library_id=self.library_id(),
                category_id=self.category_id(),
                keyword_id=self.keyword_id()
            )
        )

