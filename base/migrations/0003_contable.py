# Generated by Django 4.1.2 on 2022-10-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_dyngt'),
    ]

    operations = [
        migrations.CreateModel(
            name='conTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etape2', models.IntegerField(null=True)),
                ('column', models.IntegerField(default=1)),
                ('type', models.TextField(choices=[('charfield', 'Text'), ('date', 'Date'), ('integer', 'number')], max_length=100, null=True)),
                ('champs', models.CharField(default='', max_length=100, null=True)),
            ],
        ),
    ]
