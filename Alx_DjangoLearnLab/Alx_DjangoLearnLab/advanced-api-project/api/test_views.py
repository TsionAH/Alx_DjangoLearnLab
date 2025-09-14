from models import Book
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class BookTest(APITestCase):
    def setUp(self):
        """
        Set up a user and log them in before each test method runs.
        """
        # Log the client in with the created user
        self.client.login(username='testuser', password='password123')
 
    def test_create_book(self):
        
        """
        Ensure a book can be created
        """

        url = reverse('create-book')
        data = {
                'title': 'Dune', 
                'author': 'Frank Herbert', 
                'publication_year': '1965'
            }
        
        response = self.client.post(url, data, format='json')

        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)

        self.assertEqual(response.data['title'], 'Dune')
        self.assertEqual(response.data['author'], 'Frank Herbert')
        self.assertEqual(response.data['publication_year'], '1965')

    def test_update_book(self):
        """
        Ensure a book is updated
        """

        # define the test book
        book = Book.object.create(title='Dune', author='Frank Herbert', publication_year='1965')

        # find the url and use the pk of the book
        url = reverse('update-book', kwargs={'pk': book.pk})

        update_data = {
            'title': 'Children of Dune',
            'author': 'Frank Herbert',
            'publication_year': '1975'
        }

        response = self.client.put(url, update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_book = Book.objects.get(pk=book.pk)

        self.assertEqual(response.data['title'], 'Children of Dune')
        self.assertEqual(response.data['publication_year'], 1975)

    def test_delete_book(self):
        """
        Ensure a book is deleted
        """

        book = Book.objects.create(title='Dune', author='Frank Herbert', publication_year='1965')

        url = reverse('delete-book', kwargs={'pk': book.pk})

        response = self.client.delete(url)

        # check if the book still exists
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=book.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Book.objects.count, 0)