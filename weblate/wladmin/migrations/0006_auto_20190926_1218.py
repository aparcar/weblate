# Generated by Django 2.2.5 on 2019-09-26 12:18

from django.db import migrations, models

import weblate.utils.backup


class Migration(migrations.Migration):

    dependencies = [("wladmin", "0005_auto_20190926_1332")]

    operations = [
        migrations.AddField(
            model_name="backupservice",
            name="paperkey",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="backupservice",
            name="passphrase",
            field=models.CharField(
                default=weblate.utils.backup.make_password, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="backuplog",
            name="event",
            field=models.CharField(
                choices=[
                    ("backup", "Backup performed"),
                    ("prune", "Deleted the oldest backups"),
                    ("init", "Repository initialization"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="backupservice",
            name="repository",
            field=models.CharField(
                default="", max_length=500, verbose_name="Backup repository"
            ),
        ),
    ]
