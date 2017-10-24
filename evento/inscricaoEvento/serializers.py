from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from inscricaoEvento.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many = False)
    class Meta:
        model = Pessoa
        fields = '__all__'

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    data_inicio = serializers.DateTimeField(source='dataEHoraDeInicio', format='%d-%m-%Y %H:%M:%S')
    class Meta:
        model = Evento
        fields = '__all__'

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    evento = EventoSerializer(many = False)
    class Meta:
        model = Ticket
        fields = ('nome', 'descricao','valor','evento')

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    evento = EventoSerializer(many = False)
    participante = PessoaSerializer(many = False)
    tickets = TicketSerializer(many = True)
    class Meta:
        model = Inscricao
        fields = ('participante', 'evento','tickets','validacao')
