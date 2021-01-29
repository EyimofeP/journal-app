import uuid
from django.contrib.auth import get_user_model 
from django.db import models

# ALERTS = (
#     ("primary", "Blue"),  # Key, Value
#     ("secondary", "Grey"),
#     ("danger", "Red"),
#     ("info", "Sky Blue"),
#     ("success", "Green"),
#     ("warning", "Yellow"),
#     ("dark", "Black"),
# )

# # Model for Category Objects
# class Category(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     name = models.CharField(max_length=100, verbose_name="Category Name")
#     color = models.CharField(null=True, max_length=50, choices=ALERTS)

#     def __str__(self):
#         return f"{self.name} by {self.user}"

#     class Meta:
#         verbose_name_plural = "Categories"  # Plural Form of Model

#     # Redirect User to this url, if form is created or updated
#     # def get_absolute_url(self):
#         # return reverse("cat", kwargs={"pk": self.pk, "name": self.name})

class Diary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text="Title of Journal Log")
    body = models.TextField(help_text="Write Info Here")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.email}"
    
    class Meta:
        verbose_name_plural = "Diaries"