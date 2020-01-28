from django.conf.urls import url
from cmsplugin_feedback.views import FeedbackView

urlpatterns = [
    url(r'^form/(?P<plugin>\d+)/?$', FeedbackView.as_view(), name='feedback-form'),
]
