# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20181231_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='courses.Question')),
                ('shuffle_answer', models.BooleanField(default=False)),
            ],
            bases=('courses.question',),
        ),
    ]
