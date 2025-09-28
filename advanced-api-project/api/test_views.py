from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Book, Author
from django.contrib.auth.models import User
class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        
        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")
        
        # Create books
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author2)
        
        # API client
        self.client = APIClient()
    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # we created 2 books

    def test_book_detail(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_book_create_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse('book-create')
        data = {"title": "Book Three", "publication_year": 2022, "author": self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_book_create_unauthenticated(self):
        url = reverse('book-create')
        data = {"title": "Book Three", "publication_year": 2022, "author": self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_book_update_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse('book-update', args=[self.book1.id])
        data = {"title": "Book One Updated", "publication_year": 2020, "author": self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Book One Updated")

    def test_book_delete_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
    def test_book_filtering_by_author(self):
        url = reverse('book-list') + f"?author={self.author1.id}"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    def test_book_search_by_title(self):
        url = reverse('book-list') + "?search=Two"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book2.title)

    def test_book_ordering_by_year(self):
        url = reverse('book-list') + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.data[0]['publication_year'], 2021)  # latest first

