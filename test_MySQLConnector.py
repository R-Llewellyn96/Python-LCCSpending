from unittest import TestCase

from MySQLConnector import connectToMySQL

class Test(TestCase):
    def test_connect_to_my_sql(self):
        connectToMySQL()


