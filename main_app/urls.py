from django.urls import path
from .views import Homepage, FocusLogsIndex, FocusLogSession, TagsIndex, AssignDistraction, UnassignDistraction
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('focusLogs/', FocusLogsIndex.as_view(), name='focusLogs_index'),
    path('focusLogs/<int:session_id>/', FocusLogSession.as_view(), name='focusLog_session'),
    path('tags/', TagsIndex.as_view(), name='tags_index'),
    path('focusLogs/<int:session_id>/assignDistraction/<int:distraction_id>/', AssignDistraction.as_view(), name='assign_distraction'), 
    path('focusLogs/<int:session_id>/unassignDistraction/<int:distraction_id>/', UnassignDistraction.as_view(), name='unassign_distraction')
]