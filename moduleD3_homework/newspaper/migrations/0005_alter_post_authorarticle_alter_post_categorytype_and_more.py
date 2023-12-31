

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='authorArticle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspaper.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoryType',
            field=models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], default='AR', max_length=2, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.SmallIntegerField(default=0, verbose_name='Рейтинг поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, unique=True, verbose_name='Заголовок'),
        ),
    ]
