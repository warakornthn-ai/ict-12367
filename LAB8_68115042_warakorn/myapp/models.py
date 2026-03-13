from django.db import models


class Population(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ชื่อ-นามสกุล')
    age = models.IntegerField(verbose_name='อายุ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='วันที่บันทึก')

    class Meta:
        verbose_name = 'ข้อมูลประชากร'
        verbose_name_plural = 'ข้อมูลประชากร'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} ({self.age} ปี)'


class Employee(models.Model):
    POSITION_CHOICES = [
        ('Manager', 'Manager'),
        ('Supervisor', 'Supervisor'),
        ('Staff', 'Staff'),
        ('Intern', 'Intern'),
    ]

    full_name = models.CharField(max_length=200, verbose_name='ชื่อ-นามสกุล')
    email = models.EmailField(unique=True, verbose_name='อีเมล')
    position = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES,
        verbose_name='ตำแหน่งงาน'
    )
    phone = models.CharField(max_length=20, verbose_name='เบอร์โทรศัพท์')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='วันที่บันทึก')

    class Meta:
        verbose_name = 'พนักงาน'
        verbose_name_plural = 'ข้อมูลพนักงาน'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} ({self.position})'
