# Generated by Django 2.2.4 on 2019-08-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('assunto', models.CharField(max_length=30)),
                ('editora', models.CharField(max_length=20)),
                ('isbn', models.CharField(max_length=20)),
                ('ano_publicacao', models.DateField()),
            ],
        ),
    ]