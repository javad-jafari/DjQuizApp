from rest_framework import permissions
from quiz.models import Question, Quizzes
from pprint import pprint


class IsOwnerOrReadOnlyQueston(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else :
            if request.data:
                quiz = Quizzes.objects.get(id=request.data['quiz'])            
                if quiz.creator == request.user:
                    return True
            return False


    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.quiz.creator == request.user



class IsAdminOrOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user
