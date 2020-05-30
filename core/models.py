from django.db import models

# Create your models here.


class Skills(models.Model):
    name = models.CharField(max_length=30)
    skillLevel = models.IntegerField()
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "habilidad"
        verbose_name_plural = "habilidades"
        ordering = ["createTime"]

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    startDate = models.DateField()
    endDate = models.DateField(blank=True, null=True)
    shortDescription = models.CharField(max_length=255)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "experiencia"
        verbose_name_plural = "experiencias"
        ordering = ["createTime"]

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=30)
    grade = models.CharField(max_length=30)
    startDate = models.DateField()
    endDate = models.DateField(blank=True, null=True)
    shortDescription = models.CharField(max_length=255)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "estudio"
        verbose_name_plural = "estudios"
        ordering = ["createTime"]

    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(verbose_name="imagen", upload_to="projects")
    urlGithub = models.URLField()
    urlLive = models.URLField()
    shortDescription = models.CharField(max_length=255)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["createTime"]

    def __str__(self):
        return self.name
