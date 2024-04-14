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

    @staticmethod
    def tag_id():
        return '1'

    # RESTFUL URL
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

    def test_tag_list_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/tags/')
        view = reverse('tag-list', kwargs={'you_know_customuser_pk': self.you_know_customuser_pk()})
        self.assertEqual(view, t.substitute(you_know_customuser_pk=self.you_know_customuser_pk()))

    # other URL
    def test_library_multi_delete_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/multi_delete/')
        view = reverse('library-multi-delete', kwargs={
            'you_know_customuser_pk': self.you_know_customuser_pk()
        })
        self.assertEqual(
            view,
            t.substitute(
                you_know_customuser_pk=self.you_know_customuser_pk()
            )
        )

    def test_library_search_by_content_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/search_by_content/')
        view = reverse('library-search-by-content', kwargs={
            'you_know_customuser_pk': self.you_know_customuser_pk()
        })
        self.assertEqual(
            view,
            t.substitute(
                you_know_customuser_pk=self.you_know_customuser_pk()
            )
        )

    def test_library_search_by_tag_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/search_by_tag/')
        view = reverse('library-search-by-tag', kwargs={
            'you_know_customuser_pk': self.you_know_customuser_pk()
        })
        self.assertEqual(
            view,
            t.substitute(
                you_know_customuser_pk=self.you_know_customuser_pk()
            )
        )

    def test_category_multi_delete_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/${library_id}/categories/multi_delete/')
        view = reverse('category-multi-delete', kwargs={
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

    def test_category_search_by_content_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/${library_id}/categories/search_by_content/')
        view = reverse('category-search-by-content', kwargs={
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

    def test_category_search_by_tag_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/${library_id}/categories/search_by_tag/')
        view = reverse('category-search-by-tag', kwargs={
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

    def test_keyword_move_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/${library_id}/categories/${category_id}/keywords/${keyword_id}/move/')
        view = reverse('keyword-move', kwargs={
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

    def test_keyword_multi_delete_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/${library_id}/categories/${category_id}/keywords/multi_delete/')
        view = reverse('keyword-multi-delete', kwargs={
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

    def test_keyword_search_by_content_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/${library_id}/categories/${category_id}/keywords/search_by_content/')
        view = reverse('keyword-search-by-content', kwargs={
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

    def test_keyword_search_by_tag_url(self):
        t = Template('/api/users/${you_know_customuser_pk}/libraries/${library_id}/categories/${category_id}/keywords/search_by_tag/')
        view = reverse('keyword-search-by-tag', kwargs={
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

    # Swagger UI
    def test_docs_url(self):
        view = reverse('swagger-ui')
        self.assertEqual(view, '/api/docs/')

    def test_schema_url(self):
        view = reverse('redoc')
        self.assertEqual(view, '/api/redoc/')

    def test_schema_url(self):
        view = reverse('schema')
        self.assertEqual(view, '/api/schema/')

    # duplicate check
    def test_email_duplicated_url(self):
        view = reverse('customuser-email-duplicated')
        self.assertEqual(view, '/api/users/email_duplicated/')

    def test_username_duplicated_url(self):
        view = reverse('customuser-username-duplicated')
        self.assertEqual(view, '/api/users/username_duplicated/')
