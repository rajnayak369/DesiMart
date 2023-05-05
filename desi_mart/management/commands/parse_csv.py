import csv
from decimal import Decimal
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from desi_mart.models import Category, Product


# We use the command tools so that we gain access to our models and database connections
# https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/


class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # drop the data from the table so that if we rerun the file, we don't repeat values
        Category.objects.all().delete()
        Product.objects.all().delete()

        print("table dropped successfully")
        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(
                str(base_dir) + '/desi_mart/data_set/data.csv',
                newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line

            # parsing each row and inserting the values in appropriate model attribute.
            category_list = []
            for row in reader:
                print(row)
                category_name = row[4]
                if category_name in category_list:
                    category_obj = Category.objects.filter(name=category_name).first()
                else:
                    category_obj = Category.objects.create(
                        name=category_name
                    )
                    category_obj.save()
                    category_list.append(category_name)
                product = Product.objects.create(
                    category=category_obj,
                    title=row[0],
                    price=int(Decimal(row[2])),
                    discount_price=int(Decimal(row[1])),
                    imageLink=row[3]
                )
                product.save()

        print("data parsed successfully")


