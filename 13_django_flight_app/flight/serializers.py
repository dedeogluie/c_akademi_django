from rest_framework import serializers

from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "estimated_time_of_departure"
        )

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many = True)
    flight = serializers.StringRelatedField()  # read_only
    flight_id = serializers.IntegerField()
    user = serializers.StringRelatedField()  # read_only
    # user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Reservation
        fields = (
            'id',
            'user',
            'user_id',
            'flight',
            'flight',
            'flight_id',
            'passenger',
        )

    def create(self, validated_data):
        passenger_data = validated_data.pop('passenger')
        validated_data['user_id'] = self.context['request'].user.id
        reservation = Reservation.objects.create(**validated_data)
        
        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas)

        reservation.save()
        return reservation
    

class StaffFlightSerializer(serializers.ModelSerializer):

    reservation = ReservationSerializer(many = True, read_only=True)

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "estimated_time_of_departure",
            "reservation",
        )