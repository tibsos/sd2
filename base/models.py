from django.db import models as m

from uuid import uuid4

class Customer(m.Model):

    uid = m.UUIDField(default = uuid4)

    name = m.TextField()
    phone = m.TextField()

    sent_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return self.name