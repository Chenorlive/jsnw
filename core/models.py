from django.db import models
from django.utils import timezone

# Create your models here.


# Base model
class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


Gender = [
    ("Male", "Male"),
    ("Female", "Female"),
]


FileType = [
    ("Image", "Image"),
    ("Video", "Video"),
    ("Audio", "Audio"),
]

InitiativeStatue = [
    ("Pending", "Pending"),
    ("Ongoing", "Ongoing"),
    ("Completed", "Completed"),
]

InitiativeType = [
    ("Community", "Community"),
    ("Women", "Women"),
    ("Youth", "Youth"),
]

class Initiative(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    beneficiary = models.TextField(blank=True, null=True)
    statue = models.CharField(max_length=100, choices=InitiativeStatue)
    type = models.CharField(max_length=100, choices=InitiativeType)
    lrd = models.DecimalField(decimal_places=2, max_digits=9)
    usd = models.DecimalField(decimal_places=2, max_digits=9)


    def __str__(self):
        return self.name
    
    

class BlogCategory(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Blog(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="Blog cover", blank=True, null=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class DistrictA(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class DistrictE(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Town(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    districtE = models.ForeignKey(DistrictE, on_delete=models.CASCADE)
    districtA = models.ForeignKey(DistrictA, on_delete=models.CASCADE)


    def __str__(self):
        return self.name





class BlogFile(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    file = models.FileField(upload_to="Blog File")
    type = models.CharField(max_length=100, choices=FileType)

    def __str__(self):
        return self.blog.tittle


class Member(BaseModel):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ReportCategory(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Report(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to="Report File")
    download_count = models.IntegerField(default=0)
    category = models.ForeignKey(ReportCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    is_fqa = models.BooleanField(default=False)
    is_suggestion = models.BooleanField(default=False)
    answer_time = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=255, choices=Gender, blank=True, null=True)

    def __str__(self):
        return self.name


class MediaCategory(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Media(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="Media File")
    category = models.ForeignKey(MediaCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    



