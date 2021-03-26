import unittest
import sqlite3
from unittest import result, mock
from app import *
from flask.templating import render_template
from app import app



con = sqlite3.connect('Barky/bookmarks.db')
cur = con.cursor()


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

# Testing field variable type
    def field_type(self):

        cur.execute("select * from bookmarks")
        x = cur.fetchone()
        assert type(x[0]) == "<class 'int'>"
        assert type(x[1]) == "<class 'str'>"
        assert type(x[2]) == "<class 'str'>"
        assert type(x[3]) == "<class 'str'>"

# Testing select from database
    def db_selectby(self):
        cur.execute("select * from bookmarks where id = 1")
        x = cur.fetchone()
        assert x == (1, 'aboki', 'aboki', 'aboki', '2021-03-24T06:00:49.843401')

# Testing orderby from database
    def db_orderby(self):

        row = cur.execute('SELECT * FROM bookmarks ORDER BY title')
        result_list = row.fetchone()
        assert result_list == (9, 'Kapoor', 'www', 'notes', '12.3.34')

# Testing delect function by using mocking method
    @mock.patch('app.bk_delete')
    def db_delete(self, test_mock):
        test_mock = bk_delete
        assert test_mock is bk_delete


if __name__ == "__main__":
    unittest.main()
