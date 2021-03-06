# Generated by Django 2.1.5 on 2019-02-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0002_team_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('job_des', models.CharField(max_length=500)),
                ('qualification', models.CharField(max_length=200)),
            ],
        ),
    ]
