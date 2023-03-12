import datetime

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.signals import m2m_changed, post_save, pre_save, pre_init
from django.dispatch import receiver

from .models import Post, SubscribersCAT, User
from .tasks import notification_about_new_post


@receiver(m2m_changed, sender=Post.post_cat.through)
def notify_new_post(sender, instance, **kwargs):

    if kwargs['action'] == 'pre_add':
        html_content = render_to_string('email_about_creating.html', {
            'news': instance
        })

        for i in kwargs['pk_set']:
            cat_id = i

        list_of_sub = SubscribersCAT.objects.filter(rel_cat=cat_id).values('rel_user')
        sub = []

        name = instance.post_name

        for i in list_of_sub:
            user_email = User.objects.get(id=i['rel_user']).email
            sub.append(user_email)

        notification_about_new_post.delay(name, sub, html_content)



@receiver(post_save, sender=Post)
def notify_new_post(sender, instance, **kwargs):
    all_posts = Post.objects.filter(post_author=instance.post_author.id, time_in__range=[datetime.date.today(),
                                                                                         datetime.date.today() +
                                                                                         datetime.timedelta(days=1)])
    print(all_posts)
    if len(all_posts) >= 3:
        print('if > 3')
        raise ValueError('В день можно публиковать только 3 поста!')