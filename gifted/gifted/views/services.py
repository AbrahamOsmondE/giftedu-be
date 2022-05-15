from gifted.models import Donator, Donee, Child, Subscription, Post
from datetime import datetime, timedelta

def get_donator():
    donator_list = []
    donators = Donator.objects.all()
    for donator in donators:
        donator_detail = {
            'id': donator.id,
            'name': donator.name,
            'phone_number': donator.phone_number,
            'photo': donator.photo
        }
        donator_list.append(donator_detail)
    return donator_list

def post_donator(name, phone_number, photo):
    donator = Donator(name=name, phone_number=phone_number, photo=photo)
    donator.save()
    donator_id = {
        "id": donator.id
    }
    return donator_id

def get_donator_int(donator_id):
    donator = Donator.objects.filter(id=donator_id).first()
    if not donator:
        raise ValueError("Donator not found")
    donator_detail = {
        'id': donator.id,
        'name': donator.name,
        'phone_number': donator.phone_number,
        'photo': donator.photo
    }
    return donator_detail

def get_donator_from_name(donator_name):
    donator = Donator.objects.filter(name=donator_name).first()
    if not donator:
        raise ValueError("Donator not found")
    donator_detail = {
        'id': donator.id,
        'name': donator.name,
        'phone_number': donator.phone_number,
        'photo': donator.photo
    }
    return donator_detail

def get_donee():
    donee_list = []
    donees = Donee.objects.all()
    for donee in donees:
        donee_detail = {
            'id': donee.id,
            'name': donee.name,
            'description': donee.description,
            'phone_number': donee.phone_number,
            'photo': donee.photo
        }
        donee_list.append(donee_detail)
    return donee_list

def post_donee(name, phone_number, photo, description):
    donee = Donee(name=name, phone_number=phone_number, photo=photo, description=description)
    donee.save()
    donee_id = {
        "id": donee.id
    }
    return donee_id

def get_donee_int(donee_id):
    donee = Donee.objects.filter(id=donee_id).first()
    if not donee:
        raise ValueError("Donee not found")
    
    child_list = []
    children = Child.objects.filter(donee_id=donee_id)
    for child in children:
        donee = Donee.objects.filter(id=child.donee_id.id).first()
        child_detail = {
            'id': child.id,
            'name': child.name,
            'description': child.description,
            'photo': child.photo,
            'subscription_cost': child.subscription_cost,
            'donee': donee.name
        }
        child_list.append(child_detail)
    
    donee_detail = {
        'id': donee.id,
        'name': donee.name,
        'description': donee.description,
        'phone_number': donee.phone_number,
        'photo': donee.photo,
        'children': child_list
    }
    return donee_detail

def get_donee_from_name(donee_name):
    donee = Donee.objects.filter(name=donee_name).first()
    if not donee:
        raise ValueError("Donee not found")
    donee_detail = {
        'id': donee.id,
        'name': donee.name,
        'description': donee.description,
        'phone_number': donee.phone_number,
        'photo': donee.photo
    }
    return donee_detail


def get_donee_fund(donee_id):
    donee = Donee.objects.filter(id=donee_id).first()
    if not donee:
        raise ValueError("Donee not found")
    enddate = datetime.today()
    startdate = enddate - timedelta(days=30)
    fund = 0
    children = Child.objects.filter(donee_id=donee)
    for child in children:
        subscription = Subscription.objects.filter(child_id=child.id, created__range=[startdate, enddate]).count()
        fund += subscription*child.subscription_cost
    donee_detail = {
        'fund': fund
    }
    return donee_detail

def get_child():
    child_list = []
    children = Child.objects.all()
    for child in children:
        donee = Donee.objects.filter(id=child.donee_id.id).first()
        child_detail = {
            'id': child.id,
            'name': child.name,
            'description': child.description,
            'photo': child.photo,
            'subscription_cost': child.subscription_cost,
            'donee': donee.name
        }
        child_list.append(child_detail)
    return child_list

def post_child(name, description, photo, subcription_cost, donee_id):
    donee = Donee.objects.filter(id=donee_id).first()
    if not donee:
        raise ValueError("Donee not found")
    child = Child(name=name, description=description, photo=photo, subscription_cost=subcription_cost, donee_id=donee)
    child.save()
    child_id = {
        "id": child.id
    }
    return child_id

def get_child_int(child_id):
    child = Child.objects.filter(id=child_id).first()
    if not child:
        raise ValueError("Child not found")
    donee = Donee.objects.filter(id=child.donee_id.id).first()
    enddate = datetime.today()
    startdate = enddate - timedelta(days=30)
    posts = Post.objects.filter(child_id=child.id, created__range=[startdate, enddate])
    subscription = Subscription.objects.filter(child_id=child.id, created__range=[startdate, enddate]).count()
    post_detail = []
    for post in posts:
        post_detail.append({
            'id': post.id,
            'title': post.title,
            'text': post.text,
            'created': post.created
        })
    child_detail = {
        'id': child.id,
        'name': child.name,
        'description': child.description,
        'photo': child.photo,
        'subscription_cost': child.subscription_cost,
        'fund': subscription*child.subscription_cost,
        'donee': donee.name,
        'posts': post_detail
    }
    return child_detail

def get_child_fund(child_id):
    child = Child.objects.filter(id=child_id).first()
    if not child:
        raise ValueError("Child not found")
    enddate = datetime.today()
    startdate = enddate - timedelta(days=30)
    fund = 0
    subscriptions = Subscription.objects.filter(child_id=child, created__range=[startdate, enddate])
    subscription_count = subscriptions.count()
    subscription_list = []
    for subscription in subscriptions:
        subscription_list.append({
            'id': subscription.id,
            'name': subscription.donator_id.name,
            'created': subscription.created
        })
    fund += subscription_count*child.subscription_cost
    subscription_detail = {
        'fund': fund,
        'subscriptions': subscription_list
    }
    return subscription_detail 

def get_subscription(donator_id, child_id):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=30)
    subscription = Subscription.objects.filter(donator_id=donator_id, child_id=child_id, created__range=[startdate, enddate]).first()
    if subscription:
        connected = True
    else:
        connected = False
    connection = {
        'connected': connected
    }
    return connection

def get_subscription_donator(donator_id):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=30)
    subscriptions = Subscription.objects.filter(donator_id=donator_id, created__range=[startdate, enddate])
    subscription_list = []
    for subscription in subscriptions:
        child = Child.objects.filter(id=subscription.child_id.id).first()
        subscription_list.append({
            'id': subscription.id,
            'name': child.name,
            'created': subscription.created
        })
    return subscription_list

def get_subscription_child(child_id):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=30)
    subscriptions = Subscription.objects.filter(child_id=child_id, created__range=[startdate, enddate])
    subscription_list = []
    for subscription in subscriptions:
        donator = Donator.objects.filter(id=subscription.donator_id.id).first()
        subscription_list.append({
            'id': subscription.id,
            'name': donator.name,
            'created': subscription.created
        })
    return subscription_list

def get_subscription_donee(donee_id):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=30)
    children = Child.objects.filter(donee_id=donee_id)
    subscription_list = []
    for child in children:
        subscriptions = Subscription.objects.filter(child_id=child, created__range=[startdate, enddate])
        for subscription in subscriptions:
            donator = Donator.objects.filter(id=subscription.donator_id.id).first()
            subscription_list.append({
                'id': subscription.id,
                'name': donator.name,
                'created': subscription.created
            })
    return subscription_list

def post_subscription(child_id, donator_id):
    child = Child.objects.filter(id=child_id).first()
    if not child:
        raise ValueError('Child not found')
    donator = Donator.objects.filter(id=donator_id).first()
    if not donator:
        raise ValueError("Donator not found")
    subscription = Subscription(child_id=child, donator_id=donator)
    subscription.save()
    subscription_id = {
        "id": subscription.id
    }
    return subscription_id

def get_post():
    post_list = []
    posts = Post.objects.all()
    for post in posts:
        post_detail = {
            'id': post.id,
            'title': post.title,
            'text': post.text,
            'created': post.created,
        }
        post_list.append(post_detail)
    return post_list

def post_post(title, text, child_id):
    child = Child.objects.filter(id=child_id).first()
    if not child:
        raise ValueError("Child not found")
    post = Post(title=title, text=text, child_id=child)
    post.save()
    post_id = {
        "id": post.id,
        "date_created": post.created
    }
    return post_id

def get_post_int(post_id):
    post = Post.objects.filter(id=post_id).first()
    post_detail = {
        'id': post.id,
        'title': post.title,
        'text': post.text,
        'created': post.created
    }
    return post_detail
