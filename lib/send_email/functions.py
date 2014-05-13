# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from threading import Thread
from django.conf import settings
from HTMLParser import HTMLParser

def remove_tags(html):
    class MLStripper(HTMLParser):
        def __init__(self):
            self.reset()
            self.fed = []
        def handle_data(self, d):
            self.fed.append(d)
        def get_data(self):
            return ''.join(self.fed)

    s = MLStripper()
    s.feed(html)
    return s.get_data()


def send_template_mail(subject, html_content, from_email, to, files=[], fail_silently=not settings.DEBUG):
    text_content = remove_tags(html_content)
    
    def send_template_mail_thread(subject, text_content, html_content, from_email, to, files, fail_silently):
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        for f in files:
            msg.attach(f.name, f.read(), f.content_type)
        try: msg.send()
        except Exception as ex:
            if not fail_silently: raise ex

    th = Thread(target=send_template_mail_thread, args=(subject, text_content, html_content, from_email, to, files, fail_silently))
    th.start()