# Generated by Django 4.1.1 on 2023-05-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Management", "0008_primaryuser_phone_no_primaryuser_profile_img_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="primaryuser",
            name="profile_img",
            field=models.ImageField(null=True, upload_to="profile_image/"),
        ),
    ]
