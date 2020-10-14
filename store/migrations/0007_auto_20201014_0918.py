# Generated by Django 3.1.1 on 2020-10-14 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20201012_1916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'verbose_name': 'Скидка', 'verbose_name_plural': 'Скидки'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Вещь', 'verbose_name_plural': 'Вещи'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='tax',
            options={'verbose_name': 'Налог', 'verbose_name_plural': 'Налоги'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='currency',
        ),
        migrations.AddField(
            model_name='discount',
            name='percentage_price',
            field=models.BooleanField(default=False, verbose_name='Цена скидки указана в процентах'),
        ),
        migrations.AddField(
            model_name='tax',
            name='percentage_price',
            field=models.BooleanField(default=False, verbose_name='Цена скидки указана в процентах'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='condition_price',
            field=models.PositiveIntegerField(verbose_name='Цена для условия'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='keyword',
            field=models.CharField(choices=[('FDV', 'Бесплатная доставка'), ('BO', 'Большой заказ')], max_length=3, verbose_name='Вид налога'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='order_price_condition',
            field=models.CharField(choices=[('LTE', '<='), ('LT', '<'), ('GTE', '>='), ('GT', '>'), ('EQ', '=')], help_text='Условный оператор, который должен выполниться, для использования этой скидки, например, если в этом поле указан знак ">", то если "цена заказа" > "цена скидки", то скидка активируется относительно данного заказа', max_length=3, verbose_name='Оператора условия'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='discounts', to='store.Order', verbose_name='Заказы'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='orders', to='store.Item', verbose_name='Вещи'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='condition_price',
            field=models.PositiveIntegerField(verbose_name='Цена для условия'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='keyword',
            field=models.CharField(choices=[('DV', 'Доставка'), ('AC', 'НДС')], max_length=3, verbose_name='Вид налога'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='order_price_condition',
            field=models.CharField(choices=[('LTE', '<='), ('LT', '<'), ('GTE', '>='), ('GT', '>'), ('EQ', '=')], help_text='Условный оператор, который должен выполниться, для использования этого налога, например, если в этом поле указан знак ">", то если "цена заказа" > "цена налога", то налог активируется относительно данного заказа', max_length=3, verbose_name='Оператор условия'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='taxes', to='store.Order', verbose_name='Заказы'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
    ]