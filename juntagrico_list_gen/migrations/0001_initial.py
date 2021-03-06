# Generated by Django 3.0.1 on 2020-02-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    def insert_default(apps, schema_editor):
        ListGeneration = apps.get_model("juntagrico_list_gen", "ListGeneration")
        ListGeneration.objects.create()

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListGeneration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generating', models.BooleanField(default=False)),
            ],
        ),
        migrations.RunPython(insert_default),
    ]
