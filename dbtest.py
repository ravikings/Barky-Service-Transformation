import sqlite3
import unittest
from unittest import result, mock
from app import *


con = sqlite3.connect('Barky/bookmarks.db')
cur = con.cursor()

class FlaskTest(unittest.TestCase):

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
