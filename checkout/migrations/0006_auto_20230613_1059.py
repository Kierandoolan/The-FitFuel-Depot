# Generated by Django 3.2.18 on 2023-06-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20230613_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='coupon',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='product_size',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]
