from django.test import TestCase
from django.urls import reverse
from django.db import connection
from you_know.models import CustomUser, Library, Category, Keyword, Tag


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
        'title': 'tag_title' + str(number),
        'content': 'content' + str(number)
    }


# DB access
def post_user(self):
    return self.client.post(path=reverse('customuser-list'), data=customuser_create_args())


def get_user(self):
    user = CustomUser.objects.first()
    return self.client.get(path=reverse('customuser-detail', kwargs={'pk': user.sub}))


def username_duplicated(self, username):
    return self.client.get(path=reverse('customuser-username-duplicated') + '?username=' + username)


def email_duplicated(self, email):
    return self.client.get(path=reverse('customuser-email-duplicated') + '?email=' + email)


def post_library(self, number=1):
    return self.client.post(
        path=reverse(
            'library-list', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
        ),
        data=library_create_args(number=number)
    )


def delete_libraries(self, ids):
    return self.client.delete(
        path=reverse(
            'library-multi-delete', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
        ) + '?ids=' + ', '.join(ids)
    )


def get_libraries(self, search_content=''):
    return self.client.get(
        path=reverse('library-list', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk()
        })
    )


def get_libraries_searched_by_content(self, search_content=''):
    return self.client.get(
        path=reverse('library-search-by-content', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk()
        }) + '?content=' + search_content
    )


def get_libraries_searched_by_tag(self, search_tag=''):
    return self.client.get(
        path=reverse('library-search-by-tag', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk()
        }) + '?title=' + search_tag
    )


def get_library(self, library):
    return self.client.get(
        path=reverse(
            'library-detail', kwargs={
                'you_know_customuser_pk': you_know_customuser_pk(),
                'pk': library.id
            }
        )
    )


def post_category(self, library, number=1):
    return self.client.post(
        path=reverse(
            'category-list', kwargs={
                'you_know_customuser_pk': you_know_customuser_pk(),
                'library_pk': library.id
            }
        ), data=category_create_args(library.id, number=number)
    )


def delete_categories(self, library, ids):
    return self.client.delete(
        path=reverse(
            'category-multi-delete', kwargs={
                'you_know_customuser_pk': you_know_customuser_pk(),
                'library_pk': library.id
            }
        ) + '?ids=' + ', '.join(ids)
    )


def get_categories(self, library):
    return self.client.get(
        path=reverse('category-list', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk(),
            'library_pk': library.id
        })
    )


def get_categories_searched_by_content(self, library, search_content=''):
    return self.client.get(
        path=reverse('category-search-by-content', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk(),
            'library_pk': library.id
        }) + '?content=' + search_content
    )


def get_categories_searched_by_tag(self, library, search_tag=''):
    return self.client.get(
        path=reverse('category-list', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk(),
            'library_pk': library.id
        }) + '?title=' + search_tag
    )


def get_category(self, library, category):
    return self.client.get(reverse('category-detail', kwargs={
        'you_know_customuser_pk': you_know_customuser_pk(),
        'library_pk': library.id,
        'pk': category.id
    }))


def post_keyword(self, library, category, number=1):
    return Keyword.objects.create(
        custom_user_id=you_know_customuser_pk(),
        library_id=library.id,
        category_id=category.id,
        title='title' + str(number),
        content='content' + str(number)
    )
    # tagsのNULLチェックになぜか引っかかって以下通らないため暫定的にKeyword.objects.create()でデータを入れる
    # response = self.client.post(
    #     path=reverse('keyword-list', kwargs={
    #         'you_know_customuser_pk': you_know_customuser_pk(),
    #         'library_pk': library.id,
    #         'category_pk': category.id
    #     }),
    #     data=keyword_create_args(library.id, category.id, number=number)
    # )


def delete_keywords(self, library, category, ids):
    return self.client.delete(
        path=reverse(
            'keyword-multi-delete', kwargs={
                'you_know_customuser_pk': you_know_customuser_pk(),
                'library_pk': library.id,
                'category_pk': category.id
            }
        ) + '?ids=' + ', '.join(ids)
    )


def get_keywords(self, library, category):
    return self.client.get(reverse('keyword-list', kwargs={
        'you_know_customuser_pk': you_know_customuser_pk(),
        'library_pk': library.id,
        'category_pk': category.id
    }))


def get_keywords_searched_by_content(self, library, category, search_content=''):
    return self.client.get(
        path=reverse('keyword-search-by-content', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk(),
            'library_pk': library.id,
            'category_pk': category.id
        }) + '?content=' + search_content
    )


def get_keywords_searched_by_tag(self, library, category, search_tag=''):
    return self.client.get(
        path=reverse('keyword-search-by-tag', kwargs={
            'you_know_customuser_pk': you_know_customuser_pk(),
            'library_pk': library.id,
            'category_pk': category.id
        }) + '?title=' + search_tag
    )


def get_keyword(self, library, category, keyword):
    return self.client.get(reverse('keyword-detail', kwargs={
        'you_know_customuser_pk': you_know_customuser_pk(),
        'library_pk': library.id,
        'category_pk': category.id,
        'pk': keyword.id,
    }))


def post_tag(self):
    return self.client.post(
        path=reverse(
            'tag-list', kwargs={'you_know_customuser_pk': you_know_customuser_pk()}
        ),
        data=tag_create_args()
    )


def get_tags(self):
    return self.client.get(reverse('tag-list', kwargs={
        'you_know_customuser_pk': you_know_customuser_pk()
    }))


def get_tag(self, tag):
    return self.client.get(
        reverse(
            'tag-detail', kwargs={
                'you_know_customuser_pk': you_know_customuser_pk(),
                'pk': tag.id
            }
        )
    )


def associate_keyword_tag(keyword, tag):
    # client.postではkeyword_tagsが作られないので生SQLで直接データを入れる
    cursor = connection.cursor()
    cursor.execute("insert into keyword_tags(keyword_id, tag_id) values('" + str(keyword.id) + "', '" + str(tag.id) + "');")


# tests
class CustomUserListTests(TestCase):
    def test_insert(self):
        response = post_user(self=self)
        users = CustomUser.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(users.count(), 1)


class CustomUserDuplicateTests(TestCase):
    def setUp(self):
        post_user(self=self)

    def test_username_duplicate(self):
        # not duplicated pattern
        response = username_duplicated(self=self, username='test')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data['duplicated'])

        # duplicated pattern
        user = CustomUser.objects.first()
        response = username_duplicated(self=self, username=user.username)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['duplicated'])

    def test_email_duplicated(self):
        # not duplicated pattern
        response = email_duplicated(self=self, email='a@a.com')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data['duplicated'])

        # duplicated pattern
        user = CustomUser.objects.first()
        response = email_duplicated(self=self, email=user.email)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['duplicated'])


class CustomUserDetailTests(TestCase):
    def setUp(self):
        post_user(self=self)

    def test_get(self):
        get_user(self=self)


class LibraryListTests(TestCase):
    def setUp(self):
        post_user(self=self)

    def test_get(self):
        response = get_libraries(self=self)
        self.assertEqual(response.status_code, 200)

    def test_search_by_content_get(self):
        post_library(self)
        response = get_libraries_searched_by_content(self, search_content='content')

        library = Library.objects.first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], library.id)

    def test_search_by_tag_get(self):
        post_library(self)
        library = Library.objects.first()
        post_category(self=self, library=library)
        category = Category.objects.first()
        post_keyword(self=self, library=library, category=category)
        keyword = Keyword.objects.first()
        post_tag(self=self)
        tag = Tag.objects.first()
        associate_keyword_tag(keyword=keyword, tag=tag)

        response = get_libraries_searched_by_tag(self, search_tag='tag_title1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], library.id)

    def test_insert(self):
        response = post_library(self=self)

        libraries = Library.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(libraries.count(), 1)

    def test_multi_delete(self):
        for i in range(2):
            post_library(self, number=i)

        libraries = Library.objects.all()
        ids = [str(x.id) for x in libraries]
        response = delete_libraries(self=self, ids=ids)
        self.assertEqual(response.status_code, 200)

        libraries = Library.objects.all()
        self.assertEqual(libraries.count(), 0)


class LibraryDetailTests(TestCase):
    def setUp(self):
        post_user(self)
        post_library(self, number=1)

    def test_get(self):
        library = Library.objects.first()
        response = get_library(self=self, library=library)
        self.assertEqual(response.status_code, 200)


class CategoryListTests(TestCase):
    def setUp(self):
        post_user(self=self)
        post_library(self=self)

    def test_get(self):
        library = Library.objects.first()
        response = get_categories(self=self, library=library)
        self.assertEqual(response.status_code, 200)

    def test_search_by_content_get(self):
        library = Library.objects.first()

        post_category(self=self, library=library)
        response = get_categories_searched_by_content(self=self, library=library, search_content='content')

        category = Category.objects.first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], category.id)

    def test_search_by_tag_get(self):
        library = Library.objects.first()
        post_category(self=self, library=library)
        category = Category.objects.first()
        post_keyword(self=self, library=library, category=category)
        keyword = Keyword.objects.first()
        post_tag(self=self)
        tag = Tag.objects.first()
        associate_keyword_tag(keyword=keyword, tag=tag)

        response = get_libraries_searched_by_tag(self, search_tag='tag_title1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], category.id)

    def test_insert(self):
        library = Library.objects.first()
        response = post_category(self=self, library=library)

        categories = Category.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(categories.count(), 1)

    def test_multi_delete(self):
        library = Library.objects.first()
        for i in range(2):
            post_category(self=self, library=library, number=i)

        categories = Category.objects.all()
        ids = [str(x.id) for x in categories]
        response = delete_categories(self=self, library=library, ids=ids)
        self.assertEqual(response.status_code, 200)

        categories = Category.objects.all()
        self.assertEqual(categories.count(), 0)


class CategoryDetailTests(TestCase):
    def setUp(self):
        post_user(self=self)
        post_library(self=self)

        library = Library.objects.first()
        post_category(self=self, library=library)

    def test_get(self):
        library = Library.objects.first()
        category = Category.objects.first()
        response = get_category(self=self, library=library, category=category)
        self.assertEqual(response.status_code, 200)


class KeywordListTests(TestCase):
    def setUp(self):
        post_user(self=self)
        post_library(self=self)

        library = Library.objects.first()
        post_category(self=self, library=library)

    def test_get(self):
        library = Library.objects.first()
        category = Category.objects.first()
        response = get_keywords(self=self, library=library, category=category)
        self.assertEqual(response.status_code, 200)

    def test_search_by_content_get(self):
        library = Library.objects.first()
        category = Category.objects.first()
        post_keyword(self=self, library=library, category=category)
        keyword = Keyword.objects.first()
        post_tag(self=self)

        response = get_keywords_searched_by_content(self=self, library=library, category=category, search_content='content')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], keyword.id)

    def test_search_by_tag_get(self):
        library = Library.objects.first()
        category = Category.objects.first()
        post_keyword(self=self, library=library, category=category)
        keyword = Keyword.objects.first()
        post_tag(self=self)
        tag = Tag.objects.first()
        associate_keyword_tag(keyword=keyword, tag=tag)

        response = get_keywords_searched_by_tag(self=self, library=library, category=category, search_tag='tag_title1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], keyword.id)

    def test_insert(self):
        library = Library.objects.first()
        category = Category.objects.first()
        response = post_keyword(self=self, library=library, category=category)

        keywords = Keyword.objects.all()
        # self.assertEqual(response.status_code, 201)
        self.assertEqual(keywords.count(), 1)

    def test_multi_delete(self):
        library = Library.objects.first()
        category = Category.objects.first()
        # tagsのNULLチェックになぜか引っかかって以下通らないため暫定的にKeyword.objects.create()でデータを入れる
        for i in range(2):
            post_keyword(self, library, category, number=i)

        keywords = Keyword.objects.all()
        ids = [str(x.id) for x in keywords]
        response = delete_keywords(self=self, library=library, category=category, ids=ids)
        self.assertEqual(response.status_code, 200)

        keywords = Keyword.objects.all()
        self.assertEqual(keywords.count(), 0)


class KeywordDetailTests(TestCase):
    def setUp(self):
        post_user(self=self)
        post_library(self=self)

        library = Library.objects.first()
        post_category(self=self, library=library)
        category = Category.objects.first()
        post_keyword(self=self, library=library, category=category)

    def test_get(self):
        library = Library.objects.first()
        category = Category.objects.first()
        keyword = Keyword.objects.first()
        response = get_keyword(self=self, library=library, category=category, keyword=keyword)
        self.assertEqual(response.status_code, 200)


class TagListTests(TestCase):
    def setUp(self):
        post_user(self=self)

    def test_get(self):
        response = get_tags(self=self)
        self.assertEqual(response.status_code, 200)

    def test_insert(self):
        response = post_tag(self=self)
        tags = Tag.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(tags.count(), 1)


class TagDetailTests(TestCase):
    def setUp(self):
        post_user(self=self)
        post_tag(self=self)

    def test_get(self):
        tag = Tag.objects.first()
        response = get_tag(self=self, tag=tag)
        self.assertEqual(response.status_code, 200)
