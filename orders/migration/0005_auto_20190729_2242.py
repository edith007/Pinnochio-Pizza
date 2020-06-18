from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190729_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_fullfilled',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_placed',
            field=models.DateTimeField(null=True),
        ),
    ]
