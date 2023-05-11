from rest_framework import serializers

class UserPublicSerializers(serializers.Serializer):
    username = serializers.CharField(read_only= True)
    id = serializers.IntegerField(read_only = True)