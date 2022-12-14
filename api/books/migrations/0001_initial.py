# Generated by Django 4.1 on 2022-11-15 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=120)),
                ("author", models.CharField(max_length=30, null=True)),
                ("description", models.TextField()),
                ("isbn", models.TextField(null=True)),
                ("publisher", models.CharField(max_length=30, null=True)),
                ("for_sale", models.BooleanField(default=0)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
                ),
                ("address", models.CharField(max_length=150)),
                ("city", models.CharField(max_length=40)),
                ("state", models.CharField(max_length=40)),
                ("country", models.CharField(max_length=40)),
                ("created_on", models.DateField(auto_now_add=True)),
                ("last_modified", models.DateField(auto_now=True)),
            ],
            options={
                "db_table": "books",
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("url", models.TextField(default=None)),
                ("filename", models.TextField(default=None)),
            ],
            options={
                "db_table": "book_images",
            },
        ),
        migrations.CreateModel(
            name="WishList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="books.book"
                    ),
                ),
            ],
            options={
                "db_table": "user_wishlist",
            },
        ),
    ]
