# Generated by Django 4.1 on 2022-11-15 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("offers", "0001_initial"),
        ("books", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="offer",
            name="buyer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="buyer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="offer",
            name="exchange_book",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exchange_book",
                to="books.book",
            ),
        ),
        migrations.AddField(
            model_name="offer",
            name="posted_book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posted_book",
                to="books.book",
            ),
        ),
        migrations.AddConstraint(
            model_name="offer",
            constraint=models.CheckConstraint(
                check=models.Q(("status__in", ["processing", "rejected", "accepted"])),
                name="possible_offer_status",
            ),
        ),
    ]
