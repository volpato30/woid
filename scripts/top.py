# coding: utf-8

from unipath import Path
import sys
import os

PROJECT_DIR = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(PROJECT_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'woid.settings')

import django
from django.utils import timezone
django.setup()


from twisted.internet import task
from twisted.internet import reactor
from woid.apps.services.models import Service
from woid.apps.services import crawlers


FIVE_MINUTES = 5 * 60
THIRTY_MINUTES = 30 * 60

def prepare_service():
    hn_service, created = Service.objects.get_or_create(slug='hn')
    if created:
        hn_service.save()
    nytimes_service, created = Service.objects.get_or_create(slug='nytimes')
    if created:
        nytimes_service.story_url = 'https://www.nytimes.com/'
        nytimes_service.save()
    github_service, created = Service.objects.get_or_create(slug='github')
    if created:
        github_service.story_url = 'https://github.com/'
        github_service.save()
    mingjing_service, created = Service.objects.get_or_create(slug='mingjing')
    if created:
        mingjing_service.save()

def main():
    service_crawlers = [
        #(crawlers.RedditCrawler(), FIVE_MINUTES),
        #(crawlers.MediumCrawler(), FIVE_MINUTES),
        #(crawlers.DiggCrawler(), FIVE_MINUTES),
        (crawlers.HackerNewsCrawler(), FIVE_MINUTES),
        (crawlers.GithubCrawler(), THIRTY_MINUTES),
        (crawlers.NyTimesCrawler(), THIRTY_MINUTES),
        (crawlers.MingjingNewsCrawler(), THIRTY_MINUTES)
    ]

    for crawler in service_crawlers:
        task.LoopingCall(crawler[0].run).start(crawler[1])

    reactor.run()

if __name__ == '__main__':
    prepare_service()
    main()
