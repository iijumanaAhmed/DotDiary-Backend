from django.urls import path
from .views import Homepage, FocusLogsIndex, FocusLogSession, TagsIndex
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('focusLogs/', FocusLogsIndex.as_view(), name='focusLogs_index'),
    path('focusLogs/<int:session_id>/', FocusLogSession.as_view(), name='focusLog_session'),
    path('tags/', TagsIndex.as_view(), name='tags_index'),
]