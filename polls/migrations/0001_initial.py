# Generated by Django 4.0 on 2022-07-29 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database', models.CharField(max_length=100)),
                ('table', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('definir', models.CharField(max_length=100)),
                ('script_conf', models.CharField(max_length=200)),
            ],
        ),
    ]
