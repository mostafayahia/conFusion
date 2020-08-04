import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Dish

class ConfusionTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "confusion_test"
        # TODO: setup you database url for testing here
        self.database_path = "postgres://{}:{}@{}/{}".format('yahia', 'password', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_retrieve_all_dishes(self):
        res = self.client().get('/dishes')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['dishes']))

    def test_400_create_dish_with_missing_args(self):
        res = self.client().post('/dishes', json={'name': 'test_dish'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

    def test_create_dish(self):
        res = self.client().post('/dishes', json={
            'name': 'tname', 
            'image': 'timage',
            'category': 'tcategory',
            'price': 2.55
            }
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['created'])
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['dishes']))

    def test_405_creation_dish_not_allowed(self):
        res = self.client().post('/dishes/10', json={
            'name': 'tname', 
            'image': 'timage',
            'category': 'tcategory',
            'price': 2.55
            })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 405)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_404_update_price_for_not_exist_book(self):
        res = self.client().patch('/dishes/1000', json={'price': 500})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_update_dish_price(self):
        res = self.client().patch('/dishes/1', json={'price': 1.23})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['dish']['price'], 1.23)

    def test_422_delete_dish_not_exist(self):
        res = self.client().delete('/dishes/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Processable')
        self.assertEqual(data['error'], 422)

    def test_delete_dish(self):
        res = self.client().delete('/dishes/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], 2)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['dishes']))


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()