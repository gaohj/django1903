from django.core.cache import cache
from rest_framework.authentication import BasicAuthentication
from apps.models import User



class UserAuthentication(BasicAuthentication):
    def authenticate(self, request):
        try:
            #http://192.168.58.40:9000/apis/movies/?token=adfasfsdf
            token = request.query_params.get("token")
            user_id = cache.get(token)
            user = User.objects.get(pk=user_id)
            return user,token
        except Exception as e:
            return None
