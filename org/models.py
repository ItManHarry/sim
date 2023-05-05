from django.db import models
from db import BaseModel
from django.contrib.auth.models import User
class School(BaseModel):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table = 'school'

class SchoolZone(BaseModel):
    name = models.CharField(max_length=256)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table = 'school_zone'

class Department(BaseModel):
    name = models.CharField(max_length=128)
    code = models.CharField('Department code', max_length=32, null=True)
    school_zone = models.ForeignKey(SchoolZone, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table = 'department'

class Employee(BaseModel):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table = 'employee'

class Supervisor(Employee):
    post = models.CharField(max_length=128)
    school_zones = models.ManyToManyField(SchoolZone, through='SchoolZoneSupervisor')

    def __str__(self):
        return self.post

    class Meta(Employee.Meta):
        db_table = 'supervisor'

class SchoolZoneSupervisor(BaseModel):
    school_zone = models.ForeignKey(SchoolZone, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    assume_start_date = models.DateField()                  # 任职开始日期
    assume_end_date = models.DateField(null=True)           # 任职结束日期

    class Meta(BaseModel.Meta):
        db_table = 'school_zone_supervisor'