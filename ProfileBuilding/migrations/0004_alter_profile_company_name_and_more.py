# Generated by Django 4.0.5 on 2022-07-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileBuilding', '0003_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='course_duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='course_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='duration_project',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='project_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
