# C:\Users\Corland\PycharmProjects\Django_tutorial\mysite\polls\models.py
import os, sys
os.chdir(r'C:\Users\Corland\PycharmProjects\Django_tutorial')
sys.path.append(r'C:\Users\Corland\PycharmProjects\Django_tutorial\mysite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()

from polls.models import Question, Choice
print(Question.objects.all())
