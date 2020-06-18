from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_auto_20190728_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeritem',
            old_name='name',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='datetime_placed',
            new_name='cart_created',
        ),
        migrations.RemoveField(
            model_name='order',
            name='datetime_fullfilled',
        ),
        migrations.AddField(
            model_name='customeritem',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='order_fullfilled',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='order',
            name='order_placed',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('cart', 'In Cart'), ('progress', 'In Progress'), ('transit', "On it's Way"), ('complete', 'Complete')], default='cart', max_length=15),
        ),
    ]
