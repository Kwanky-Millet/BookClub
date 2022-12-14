# Generated by Django 4.1 on 2022-11-15 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("comment", models.CharField(max_length=300)),
                ("created_on", models.DateField(auto_now_add=True)),
                ("last_modified", models.DateField(auto_now=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="books.book",
                    ),
                ),
            ],
            options={
                "db_table": "book_comments",
            },
        ),
    ]
