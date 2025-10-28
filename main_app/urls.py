from django.urls import path
from .views import Homepage, FocusLogsIndex
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('focusLogs/', FocusLogsIndex.as_view(), name='focusLogs_index')
]