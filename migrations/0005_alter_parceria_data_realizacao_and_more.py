# Generated by Django 5.0.2 on 2024-03-24 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_alter_parceria_data_realizacao_alter_parceria_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceria',
            name='data_realizacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 20, 20, 41, 995049)),
        ),
        migrations.AlterField(
            model_name='parceria2',
            name='data_realizacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 20, 20, 41, 996047)),
        ),
        migrations.AlterField(
            model_name='parceria3',
            name='data_realizacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 20, 20, 41, 997044)),
        ),
    ]