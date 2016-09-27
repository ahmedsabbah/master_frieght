from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.main, name='main'),

    url(r'^sales/$', views.sales, name='sales'),
    url(r'^rate_request/aif/new/$', views.getAIFRateRequest, name='getAIFRateRequest'),
    url(r'^rate_request/fcl/new/$', views.getFCLRateRequest, name='getFCLRateRequest'),
    url(r'^rate_request/lcl/new/$', views.getLCLRateRequest, name='getLCLRateRequest'),
    url(r'^rate_request/new/$', views.postRateRequest, name='postRateRequest'),

    url(r'^operations/$', views.operations, name='operations'),
    url(r'^quotation/aif/new/$', views.getAIFQuotation, name='getAIFQuotation'),
    url(r'^quotation/fcl/new/$', views.getFCLQuotation, name='getFCLQuotation'),
    url(r'^quotation/lcl/new/$', views.getLCLQuotation, name='getLCLQuotation'),
    url(r'^quotation/new/$', views.postQuotation, name='postQuotation'),

    url(r'^404/$', views.notFound, name='notFound'),
]