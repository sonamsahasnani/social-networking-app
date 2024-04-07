from django.db import models
from user.models import CustomUser

# Create your models here.

class FriendRequest(models.Model):
    from_id=models.ForeignKey(CustomUser,related_name='friend_request_sent_by',on_delete=models.CASCADE)
    to_id=models.ForeignKey(CustomUser,related_name='friend_request_sent_to',on_delete=models.CASCADE)
    accepted=models.BooleanField(default=False)

    def __str__(self):
        return ""

#class Friend(models.Model):
 #   user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
  #  friend_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

   # def __str__(self):
    #    return "{0} and {1}".format(self.user_id,self.friend_id)


