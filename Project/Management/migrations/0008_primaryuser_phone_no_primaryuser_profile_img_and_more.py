# Generated by Django 4.1.1 on 2023-05-07 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Management", "0007_alter_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="primaryuser",
            name="phone_no",
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="primaryuser",
            name="profile_img",
            field=models.ImageField(null=True, upload_to="profile_image"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(null=True, upload_to="product_images/"),
        ),
    ]
