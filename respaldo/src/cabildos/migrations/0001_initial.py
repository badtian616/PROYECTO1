# Generated by Django 3.1.3 on 2020-12-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrearCabildo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etiquetas', models.CharField(max_length=200, null=True)),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('fecha', models.DateTimeField()),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
