# Generated by Django 5.0.4 on 2024-07-08 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_item_blood_type_item_citizenship_item_civil_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='address',
        ),
        migrations.AddField(
            model_name='item',
            name='barangay',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='fatherext',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='fatherl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='fatherm',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='fathern',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='house_no',
            field=models.IntegerField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='motherext',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='motherl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='motherm',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='mothern',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ext',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='postal',
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='province',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='subd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='height',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
