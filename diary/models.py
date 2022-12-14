from django.db import models

class Memory(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #쿼리셋에서 order_by를 지정하지 않았을 때
        ordering = ['-id']
    def get_absolute_url(self):
        return f"/diary/{self.pk}/"
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'