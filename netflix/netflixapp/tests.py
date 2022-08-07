from django.test import TestCase, Client

from .models import Movie


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:

        self.movie = Movie.objects.create(
            name="Secret",
            year="2016-01-02",
            genre="Drama",
            imdb=8.9,

        )
        self.client = Client()

    def test_get_all_movies(self):
        response = self.client.get('/movie/')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]["id"])
        self.assertEqual(data[0]["name"], "Secret")

    def test_search(self):
        response = self.client.get('/movie/?search=Secret')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]["id"])
        self.assertEqual(data[0]["name"], "Secret")

    def test_ordering(self):
        response = self.client.get('/movie/?ordering=-imdb')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]["id"])
        self.assertEqual(data[0]["name"], "Secret")
