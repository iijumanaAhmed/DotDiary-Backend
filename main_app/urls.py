from django.urls import path
from .views import Homepage, FocusLogsIndex, FocusLogSession, TagsIndex, AssignDistraction, UnassignDistraction, ToDoListsIndex, ToDoListDetail, TasksIndex, TaskToDo, SignupUser, UserProfile
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('focusLogs/', FocusLogsIndex.as_view(), name='focusLogs_index'),
    path('focusLogs/<int:session_id>/', FocusLogSession.as_view(), name='focusLog_session'),
    path('tags/', TagsIndex.as_view(), name='tags_index'),
    path('focusLogs/<int:session_id>/assignDistraction/<int:distraction_id>/', AssignDistraction.as_view(), name='assign_distraction'), 
    path('focusLogs/<int:session_id>/unassignDistraction/<int:distraction_id>/', UnassignDistraction.as_view(), name='unassign_distraction'),
    path('toDoLists/', ToDoListsIndex.as_view(), name='toDoLists_index'),
    path('toDoLists/<int:todolist_id>/', ToDoListDetail.as_view(), name='toDoList_detail'),
    path('toDoLists/<int:todolist_id>/tasks/', TasksIndex.as_view(), name='tasks_index'),  
    path('toDoLists/<int:todolist_id>/tasks/<int:task_id>/', TaskToDo.as_view(), name='task_todo'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignupUser.as_view(), name='signup'),
    path('profile/<int:user_id>/', UserProfile.as_view(), name='signup')
]
