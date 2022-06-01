# Generated by Django 4.0.4 on 2022-06-01 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0002_alter_student_profile'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('students', models.ManyToManyField(related_name='courses', to='students.student')),
                ('teachers', models.ManyToManyField(related_name='courses', to='teachers.teacher')),
            ],
        ),
    ]
