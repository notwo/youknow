from django.test import TestCase
from you_know.models import CustomUser, Library, Category, Keyword, Tag



class CustomUserModelTests(TestCase):
    def test_single_record(self):
        user = CustomUser(username='username', email='test@example.com', sub='subsubsub')
        user.save()
        users = CustomUser.objects.all()
        self.assertEqual(users.count(), 1)


class LibraryModelTests(TestCase):
    def test_single_record(self):
        CustomUser.objects.create(username='username', email='test@example.com', sub='subsubsub')
        user = CustomUser.objects.first()
        library = Library(custom_user_id=user.sub, title='l_title1', content='l_content1')
        library.save()
        libraries = Library.objects.all()
        self.assertEqual(libraries.count(), 1)


class CategoryModelTests(TestCase):
    def test_single_record(self):
        CustomUser.objects.create(username='username', email='test@example.com', sub='subsubsub')
        user = CustomUser.objects.first()
        Library.objects.create(custom_user_id=user.sub, title='l_title1', content='l_content1')
        library = Library.objects.first()
        category = Category(custom_user_id=library.custom_user.sub, library_id=library.id, title='c_title1', content='c_content1')
        category.save()
        categories = Category.objects.all()
        self.assertEqual(categories.count(), 1)


class KeywordModelTests(TestCase):
    def test_single_record(self):
        CustomUser.objects.create(username='username', email='test@example.com', sub='subsubsub')
        user = CustomUser.objects.first()
        Library.objects.create(custom_user_id=user.sub, title='l_title1', content='l_content1')
        library = Library.objects.first()
        Category.objects.create(custom_user_id=library.custom_user.sub, library_id=library.id, title='c_title1',
                                content='c_content1')
        category = Category.objects.first()
        keyword = Keyword(custom_user_id=library.custom_user.sub, library_id=library.id, category_id=category.id, title='c_title1', content='c_content1')
        keyword.save()
        keywords = Keyword.objects.all()
        self.assertEqual(keywords.count(), 1)


class TagModelTests(TestCase):
    def test_single_record_only_tag(self):
        CustomUser.objects.create(username='username', email='test@example.com', sub='subsubsub')
        user = CustomUser.objects.first()
        tag = Tag(custom_user_id=user.sub, title='t_title1', content='t_content1')
        tag.save()
        tags = Tag.objects.all()
        self.assertEqual(tags.count(), 1)
