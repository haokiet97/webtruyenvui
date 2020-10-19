from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Tiêu đề", blank=False)
    description = models.TextField(max_length=250, verbose_name="Mô tả", blank=True)

    def __str__(self):
        return self.name


class Story(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Tiêu đề", blank=False)
    composed_in = models.DateField(auto_now_add=True, blank=True)
    description = models.TextField(max_length=500, verbose_name="Mô tả", blank=True)
    thumbnail = models.FileField(upload_to="thumbnail", blank=True)
    category = models.ForeignKey("Story", related_name="stories", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Chapter(BaseModel):
    file = models.FileField(upload_to="chapter", blank=True, verbose_name="Hình ảnh")
    content = models.TextField(max_length=2500, blank=True, verbose_name="Nội dung")
    story = models.ForeignKey("Story", related_name="chapters", on_delete=models.CASCADE)
