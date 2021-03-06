# Generated by Django 3.1.7 on 2021-04-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('generateddate', models.DateTimeField()),
                ('expirydate', models.DateField()),
                ('expirytime', models.TimeField()),
                ('file', models.FileField(upload_to='notice/')),
            ],
        ),
    ]
