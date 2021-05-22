from unittest import TestCase

from MySQLConnector import connectToMySQL
from MySQLConnector import checkDbExists

class Test(TestCase):
    def test_connect_to_my_sql(self):
        myDb = connectToMySQL()


class Test(TestCase):
    def test_check_db_exists(self):
        myDb = connectToMySQL()
        checkDbExists(myDb)


