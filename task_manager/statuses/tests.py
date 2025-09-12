from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse_lazy as reverse

from task_manager.statuses.models import Status
from task_manager.test_db import TestDB


class TestStatus(TestDB, TestCase):
    def test_status_index_page(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("statuses"))
        self.assertEqual(response.status_code, 200)

    def test_create_status(self):
        test_status_data = {
            "name": "status_test",
        }
        status_count = Status.objects.all().count()
        self.client.force_login(user=self.user)
        response = self.client.post(reverse("status_create"), test_status_data)

        self.assertRedirects(response, reverse("statuses"))
        test_status = Status.objects.last()
        self.assertEqual(test_status.name, test_status_data.get("name"))
        self.assertEqual(Status.objects.all().count(), status_count + 1)

    def test_read_status(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("statuses"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.status.name)

    def test_update_status(self):
        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse("status_update", kwargs={"pk": self.status.id}),
            self.status_data,
        )
        self.assertRedirects(response, reverse("statuses"))
        status = Status.objects.get(pk=self.status.id)
        self.assertEqual(status.name, self.status_data.get("name"))

    def test_delete_task_status(self):
        status_count = Status.objects.all().count()
        self.client.force_login(user=self.user)

        response = self.client.post(
            reverse("status_delete", kwargs={"pk": self.status.id})
        )
        self.assertRedirects(response, reverse("statuses"))
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Cannot delete busy status")

        self.assertRedirects(response, reverse("statuses"))
        self.assertEqual(Status.objects.all().count(), status_count)

    def test_delete_status(self):
        test_status_data = {"name": "status_test_2"}
        test_status = Status.objects.create(**test_status_data)
        status_count = Status.objects.all().count()

        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse("status_delete", kwargs={"pk": test_status.id})
        )
        self.assertRedirects(response, reverse("statuses"))
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Status was deleted successfully")

        self.assertEqual(Status.objects.all().count(), status_count - 1)
