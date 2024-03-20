from  utils.setup_test import TestSetup
from authentication.models import User
from todo.models import Todo
from django.urls import reverse


class TestModel(TestSetup):

    def test_should_create_a_todo(self):
        user = self.create_test_user()
        
        response = self.client.post(reverse('create-todo'),{
            'owner':user,
            'title':"coding",
            'description':"remembert to write some code today"
        })

        self.assertEqual(response.status_code, 302)