from celery import shared_task
import datetime
from .models import Category, SubscribersCAT, Post, User

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

@shared_task
def notification_about_new_post(name, sub, html_content):
    subject = f'Новая статья в любимой категории!'

    msg = EmailMultiAlternatives(
        subject=subject,
        body=name,
        from_email='p.seregina2015@yandex.ru',
        to=sub)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

@shared_task
def notification_about_all_posts_week():
    categories = Category.objects.all()
    for i in categories:
        list_of_sub = SubscribersCAT.objects.filter(rel_cat=i.id).values('rel_user')
        news = Post.objects.filter(time_in__range=[datetime.date.today() - datetime.timedelta(days=7),
                                                   datetime.date.today()], post_cat=i)

        if list_of_sub and news:
            sub = []

            for k in list_of_sub:
                user_email = User.objects.get(id=k['rel_user']).email
                sub.append(user_email)

            html_content = render_to_string('posts_week.html', {
                'news': news
            })

            msg = EmailMultiAlternatives(
                subject=f'Категория {i.name_cat}',
                body='New posts!',
                from_email='p.seregina2015@yandex.ru',
                to=sub)


            msg.attach_alternative(html_content, "text/html")
            msg.send()