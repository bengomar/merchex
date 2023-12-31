# Generated by Django 4.2.4 on 2023-08-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0007_remove_band_like_new"),
    ]

    operations = [
        migrations.AlterField(
            model_name="band",
            name="genre",
            field=models.CharField(
                choices=[
                    ("FK", "Funk"),
                    ("HH", "Hip Hop"),
                    ("SP", "Synth Pop"),
                    ("AR", "Alternative Rock"),
                    ("RA", "Rai"),
                ],
                max_length=5,
            ),
        ),
    ]
