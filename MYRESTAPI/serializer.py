from rest_framework import serializers

class mySerializer(serializers.Serializer):
    Length=serializers.CharField(max_length=30)
    Quantity=serializers.CharField(max_length=30)
    Weight=serializers.CharField(max_length=30)

    def __str__(self):
        return 'My Serializer Object....!'
        # return self.Length+' '+self.Quantity+' '+self.Weight