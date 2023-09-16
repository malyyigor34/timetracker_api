from django.db.models import CharField, FileField, FloatField, DateTimeField, Model


class Track(Model):
    time = DateTimeField(auto_now_add=True)
    screen = FileField(upload_to='screens/')
    window_name = CharField(max_length=500)

    def __str__(self):
        return f"{self.time} - {self.window_name}"

    def __repr__(self):
        return f"{self.time} - {self.window_name}"
