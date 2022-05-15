"""gifted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gifted.views import donator, donee, child, subscription, post

urlpatterns = [
    path('admin/', admin.site.urls),

    path('donator_api', donator.DonatorList.as_view(), name="donator_api"),
    path('donator_api/get_id/<donator_name>', donator.DonatorFromName.as_view(), name="donator_api_from_name"),
    path('donator_api/<int:donator_id>', donator.DonatorListInt.as_view(), name="donator_api_int"),

    path('donee_api', donee.DoneeList.as_view(), name="donee_api"),
    path('donee_api/get_id/<donee_name>', donee.DoneeFromName.as_view(), name="donee_api_from_name"),
    path('donee_api/<int:donee_id>', donee.DoneeListInt.as_view(), name="donee_api_int"),
    path('donee_api/fund/<int:donee_id>', donee.DoneeListFund.as_view(), name="donee_api_int"),

    path('child_api', child.ChildList.as_view(), name="child_api"),
    path('child_api/<int:child_id>', child.ChildListInt.as_view(), name="child_api_int"),
    path('child_api/subscription/<int:child_id>', child.ChildListFund.as_view(), name="child_api_int"),

    path('subscription_api', subscription.SubscriptionList.as_view(), name="subscription_api"),
    path('subscription_api/donator/<int:donator_id>', subscription.SubscriptionListDonator.as_view(), name="subscription_api_donator"),
    path('subscription_api/child/<int:child_id>', subscription.SubscriptionListChild.as_view(), name="subscription_api_child"),
    path('subscription_api/donee/<int:donee_id>', subscription.SubscriptionListDonee.as_view(), name="subscription_api_donee"),

    path('post_api', post.PostList.as_view(), name="post_api"),
    path('post_api/<int:post_id>', post.PostListInt.as_view(), name="post_api_int"),
]
