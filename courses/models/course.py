from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, null= False)
    description = models.CharField(max_length=300, null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to = "files/thumbnail")
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to = "files/resource")
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name


# this is inheritance model because same fields
# are used in three models then we create a parent model
# and inherit parent model to the child models
class CourseProperty(models.Model):
    description = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    # means for this parent model table will not create in database
    class Meta:
        abstract = True


class Tag(CourseProperty):
    pass


class Prerequisite(CourseProperty):
    pass


class Learning(CourseProperty):
    pass

