# Generated by Django 2.2.7 on 2019-11-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('userpic', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('Contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]