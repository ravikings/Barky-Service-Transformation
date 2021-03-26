import unittest

from flask.templating import render_template
from app import app


class FlaskTest(unittest.TestCase):

    # Testing home page route
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Add a bookmark', response.data)

    # Testing new bookmark add route
    def test_new(self):
        tester = app.test_client(self)
        response = tester.get('addnew')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Add new Bookmark Information', response.data)


    # Testing recent page route
    def test_recent(self):
        tester = app.test_client(self)
        response = tester.get('/addfilter')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Retrieve book by Id', response.data)


  # Testing update page route
    def test_update(self):
        tester = app.test_client(self)
        response = tester.get('/updates')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Please enter Bookmark Information', response.data)



    # Testing delete page route
    def test_delete(self):
        tester = app.test_client(self)
        response = tester.get('/record_delete')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Delete Bookmark Information', response.data)


    # Query testing



if __name__ == "__main__":
    unittest.main()
