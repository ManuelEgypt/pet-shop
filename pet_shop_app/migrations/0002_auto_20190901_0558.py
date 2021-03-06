# Generated by Django 2.2.4 on 2019-09-01 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='pet',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='price',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=6),
            preserve_default=False,
        ),
    ]
