from __future__ import absolute_import,unicode_literals
from celery import shared_task
from celery.task import periodic_task
from webservices.scrapeitems.fetch import update_products



@periodic_task(run_every=crontab(minute=0, hour='*/12'),
    queue='nonsdepdb3115', options={'queue': 'nonsdepdb3115'})
def update_products_task():
    update_products()