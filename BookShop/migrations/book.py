from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', 'initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('isbn', models.CharField(help_text='13 character <a href=', max_length=13, verbose_name='ISBN')),
                ('genre', models.ManyToManyField(help_text='select a genre for this book', to='app.Genre')),
            ],
        ),
    ]