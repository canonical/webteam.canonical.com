import unittest
from webapp.app import app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        """
        Set up Flask app for testing
        """
        app.testing = True
        self.client = app.test_client()

    def test_homepage(self):
        """
        When given the index URL,
        we should return a 200 status code
        """

        self.assertEqual(self.client.get("/").status_code, 200)

    def test_not_found(self):
        """
        When given a non-existent URL,
        we should return a 404 status code
        """

        self.assertEqual(self.client.get("/not-found-url").status_code, 404)

    def test_domain_info(self):
        """
        When requesting domain-info data with domain and repo params
        we should return a 200 status code
        we should return data that contains staging and production keys
        """
        endpoint = self.client.get(
            "/domain-info.json?domain=ubuntu.com"
            + "&repo=canonical-web-and-design/ubuntu.com"
        )
        self.assertEqual(endpoint.status_code, 200)
        self.assertIn("staging", endpoint.json)
        self.assertIn("production", endpoint.json)


if __name__ == "__main__":
    unittest.main()
