from django.contrib import admin
from django.urls import path,include
from preciseweb import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',views.index,name='index'),
    path('privacypolicy/',views.privacypolicy,name='privacypolicy'),
    path('getstarted/',views.getstarted,name='getstarted'),
    path('ecommerce/',views.ecommerce,name='ecommerce'),
    path('socialmedia/',views.socialmedia,name='socialmedia'),
    path('seo/',views.seo,name='seo'),
    path('adtech/',views.adtech,name='adtech'),
    path('market/',views.market,name='market'),
    path('travel/',views.travel,name='travel'),
    path('finance/',views.finance,name='finance'),
    path('healthcare/',views.healthcare,name='healthcare'),
    path('realestate/',views.realestate,name='realestate'),
    path('good/',views.good,name='good'),
    path('datasets/',views.datasets,name='datasets'),
    path('template/',views.template,name='template'),
    path('customizescraping/',views.customizescraping,name='customizescraping'),
    path('automation/',views.automation,name='automation'),

    # path('register/',views.register ,name='register'),
    # path('loginuser/',views.loginuser,name='loginuser'),
    # path('logoutuser/',views.logoutuser,name='logoutuser'),
    # path('success/',views.success,name='success'),
    # path('emailrecieved/',views.emailrecieved,name='emailrecieved'),
    # path('checkout/',views.checkout,name='checkout'),
    # path('profile/',views.profile,name='profile'),
    # path('cart/',views.cart.as_view(),name='cart'),
    # path('payout/',login_required(views.payout.as_view(),login_url='/loginuser/'),name='payout'),
    # path('myorders/',views.myorders.as_view(),name='myorders'),

    
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
