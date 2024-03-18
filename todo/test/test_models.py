from django.test import TestCase
from authentication.models import User
from todo.models import Todo

class TestModel(TestCase):

    def test_should_create_todo(self):
        user = User.objects.create_user(username = 'username',email='email@app.com')
        user.set_password('password12!')
        user.save()
        todo = Todo(owner=user ,tittle="buy salt",description = 'do it by evening')
        todo.save()
        self.assertEqual(str(todo), 'buy salt')
