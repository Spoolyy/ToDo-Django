# Generated by Django 5.1.2 on 2024-10-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_List', '0004_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('work', 'Work'), ('family', 'Family'), ('personal', 'Personal'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
