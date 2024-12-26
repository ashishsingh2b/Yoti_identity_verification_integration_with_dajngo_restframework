from django.db import models

class YotiSession(models.Model):
    session_id = models.CharField(max_length=255)
    user_tracking_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Yoti Session {self.session_id}"
