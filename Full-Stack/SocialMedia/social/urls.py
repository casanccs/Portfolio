from django.urls import path
from social.views import *
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logoutView, name='logout'),
    path('login/', loginView, name='login'),
    path('createaccount/', createAccountView, name='createAccount'),
    path('createPost/', createPostView, name='createPost'),
    path('editPost/<int:entry_id>', editPostView, name='editPost'),
    path('editProfile/<int:profile_id>', editProfileView, name='editProfile'),
    path('deletePost/<int:entry_id>', deletePostView, name='deletePost'),
    path('searchProfile/', searchProfileView, name='searchProfile'),
    path('addFollow/<int:profile_id>', addFollowView, name='addFollow'),
    path('removeFollow/<int:profile_id>', removeFollowView, name='removeFollow'),
    path('accountDetail/<int:profile_id>', accountView, name='accountDetail'),
    path('messaging/<int:profile_id>', messagingView, name='messaging'),
    path('chat/<int:other_id>', chatView, name='chat'),
    path('entryDetail/<int:entry_id>', entryDetail, name='entryDetail'),
    path('following/', followingView, name='following'),
    path('followers/', followersView, name='followers'),
    path('deleteComment/<int:comment_id>', deleteCommentView, name='deleteComment'),
]
