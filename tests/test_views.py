from django.test import TestCase
from django.urls import reverse

from you_know.models import CustomUser, Library, Category, Keyword, Tag
from django.db import connection


def you_know_customuser_pk():
    return 'subsubsub'


def customuser_create_args():
    return {
        'username': 'username',
        'email': 'test@example.com',
        'sub': you_know_customuser_pk()
    }


def library_create_args(number=1):
    return {
        'custom_user': you_know_customuser_pk(),
        'title': 'title' + str(number),
        'content': 'content' + str(number)
    }


def category_create_args(library_id, number=1):
    return {
        'custom_user': you_know_customuser_pk(),
        'library': library_id,
        'title': 'title' + str(number),
        'content': 'content' + str(number)
    }


def keyword_create_args(library_id, category_id, number=1):
    return {
        'custom_user': you_know_customuser_pk(),
        'library': library_id,
        'category': category_id,
        'title': 'title' + str(number),
        'content': 'content' + str(number)
    }


def tag_create_args(number=1):
    return {
        'custom_user': you_know_customuser_pk(),
        'title': 'title' + str(number),
        'content': 'content' + str(number)
    }


class CustomUserListTests(TestCase):
    def test_get(self):
        self.client.get(path=reverse('customuser-list'))

    def test_insert(self):
        response = self.client.post(
            path=reverse('customuser-list'),
            data=customuser_create_args()
        )
        users = CustomUser.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(users.count(), 1)


class CustomUserDetailTests(TestCase):
    def setUp(self):
        self.client.post(path=reverse('customuser-list'), data=customuser_create_args())

    def test_get(self):
        user = CustomUser.objects.first()
        self.client.get(path=reverse('customuser-detail', kwargs={'pk': user.sub}))


class LibraryListTests(TestCase):
    def setUp(self):
        self.client.post(path=reverse('customuser-list'), data=customuser_create_args())

    def test_get(self):
        response = self.client.get(reverse('library-list', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}))
        self.assertEqual(response.status_code, 200)

    def test_search_by_content_get(self):
        self.client.post(
            path=reverse(
                'library-list', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
            ),
            data=library_create_args()
        )
        response = self.client.get(reverse('library-search-by-content', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}) + '?content=content')

        library = Library.objects.first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], library.id)

    def test_insert(self):
        response = self.client.post(
            path=reverse(
                'library-list', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
            ),
            data=library_create_args()
        )

        libraries = Library.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(libraries.count(), 1)

    def test_multi_delete(self):
        for i in range(2):
            self.client.post(
                path=reverse(
                    'library-list', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
                ),
                data=library_create_args(number=i)
            )

        libraries = Library.objects.all()
        ids = [str(x.id) for x in libraries]
        response = self.client.delete(
            path=reverse(
                'library-multi-delete', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
            ) + '?ids=' + ', '.join(ids)
        )
        self.assertEqual(response.status_code, 200)

        libraries = Library.objects.all()
        self.assertEqual(libraries.count(), 0)


class LibraryDetailTests(TestCase):
    def setUp(self):
        self.client.post(path=reverse('customuser-list'), data=customuser_create_args())
        self.client.post(
            path=reverse('library-list', kwargs={
                'you_know_customuser_pk': you_know_customuser_pk()
            }),
            data=library_create_args()
        )

    def test_get(self):
        library = Library.objects.first()
        response = self.client.get(
            reverse(
                'library-detail', kwargs={
                    'you_know_customuser_pk': you_know_customuser_pk(),
                    'pk': library.id
                }
            )
        )
        self.assertEqual(response.status_code, 200)


class CategoryListTests(TestCase):
    def setUp(self):
        self.client.post(path=reverse('customuser-list'), data=customuser_create_args())
        self.client.post(path=reverse(
            'library-list', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
        ), data=library_create_args())

    def test_get(self):
        library = Library.objects.first()
        response = self.client.get(reverse('category-list', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk(),
            'library_pk': library.id
        }))
        self.assertEqual(response.status_code, 200)

    def test_search_by_content_get(self):
        library = Library.objects.first()
        self.client.post(
            path=reverse(
                'category-list', kwargs={
                    'you_know_customuser_pk': you_know_customuser_pk(),
                    'library_pk': library.id
                }
            ), data=category_create_args(library.id)
        )
        response = self.client.get(
            reverse('category-search-by-content', kwargs={
                'you_know_customuser_pk': you_know_customuser_pk(),
                'library_pk': library.id
            }) + '?content=content')

        category = Category.objects.first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], category.id)

    def test_insert(self):
        library = Library.objects.first()
        response = self.client.post(
            path=reverse(
                'category-list', kwargs={
                    'you_know_customuser_pk': you_know_customuser_pk(),
                    'library_pk': library.id
                }
            ), data=category_create_args(library.id)
        )

        categories = Category.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(categories.count(), 1)

    def test_multi_delete(self):
        library = Library.objects.first()
        for i in range(2):
            self.client.post(
                path=reverse(
                    'category-list', kwargs={
                        'you_know_customuser_pk': you_know_customuser_pk(),
                        'library_pk': library.id
                    }
                ),
                data=category_create_args(library.id, number=i)
            )

        categories = Category.objects.all()
        ids = [str(x.id) for x in categories]
        response = self.client.delete(
            path=reverse(
                'category-multi-delete', kwargs={
                    'you_know_customuser_pk': you_know_customuser_pk(),
                    'library_pk': library.id
                }
            ) + '?ids=' + ', '.join(ids)
        )
        self.assertEqual(response.status_code, 200)

        categories = Category.objects.all()
        self.assertEqual(categories.count(), 0)


class CategoryDetailTests(TestCase):
    def setUp(self):
        self.client.post(path=reverse('customuser-list'), data=customuser_create_args())
        self.client.post(path=reverse(
            'library-list', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
        ), data=library_create_args())

        library = Library.objects.first()
        self.client.post(
            path=reverse(
                'category-list', kwargs={
                    'you_know_customuser_pk': you_know_customuser_pk(),
                    'library_pk': library.id
                }
            ), data=category_create_args(library.id)
        )

    def test_get(self):
        library = Library.objects.first()
        category = Category.objects.first()
        response = self.client.get(reverse('category-detail', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk(),
            'library_pk': library.id,
            'pk': category.id
        }))
        self.assertEqual(response.status_code, 200)


class KeywordListTests(TestCase):
    def setUp(self):
        self.client.post(path=reverse('customuser-list'), data=customuser_create_args())

        self.client.post(path=reverse(
            'library-list', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
        ), data=library_create_args())

        library = Library.objects.first()
        self.client.post(path=reverse(
            'category-list', kwargs={
                    'you_know_customuser_pk': you_know_customuser_pk(),
                    'library_pk': library.id
                }
            ), data=category_create_args(library.id)
        )

    def test_get(self):
        response = self.client.get(reverse('keyword-list', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk(),
            'library_pk': 1,
            'category_pk': 1
        }))
        self.assertEqual(response.status_code, 200)

    def test_insert(self):
        library = Library.objects.first()
        category = Category.objects.first()
        Keyword.objects.create(
            custom_user_id=you_know_customuser_pk(),
            library_id=library.id,
            category_id=category.id,
            title='title',
            content='content')
        # response = self.client.post(
        #     path=reverse('keyword-list', kwargs={
        #         'you_know_customuser_pk': you_know_customuser_pk(),
        #         'library_pk': library.id,
        #         'category_pk': category.id
        #     }),
        #     data=keyword_create_args(library.id, category.id)
        # )

        keywords = Keyword.objects.all()
        # self.assertEqual(response.status_code, 201)
        self.assertEqual(keywords.count(), 1)


class TagListTests(TestCase):
    def setUp(self):
        self.client.post(path=reverse('customuser-list'), data=customuser_create_args())

    def test_get(self):
        response = self.client.get(reverse('tag-list', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk()
        }))
        self.assertEqual(response.status_code, 200)

    def test_insert(self):
        response = self.client.post(
            path=reverse(
                'tag-list', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
            ),
            data=tag_create_args()
        )

        tags = Tag.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(tags.count(), 1)


class TagDetailTests(TestCase):
    def setUp(self):
        self.client.post(path=reverse('customuser-list'), data=customuser_create_args())
        self.client.post(
            path=reverse(
                'tag-list', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
            ),
            data=tag_create_args()
        )

    def test_get(self):
        tag = Tag.objects.first()
        response = self.client.get(
            reverse(
                'tag-detail', kwargs={
                    'you_know_customuser_pk': you_know_customuser_pk(),
                    'pk': tag.id
                }
            )
        )
        self.assertEqual(response.status_code, 200)
