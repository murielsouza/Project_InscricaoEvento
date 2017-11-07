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

    def create(self, validated_data):
        user_data = validated_data.pop('usuario')
        u = User.objects.create(**user_data)
        p = Pessoa.objects.create(usuario = u, **validated_data)
        return p

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    data_inicio = serializers.DateTimeField(source='dataEHoraDeInicio', format='%d-%m-%Y %H:%M:%S')
    class Meta:
        model = Evento
        fields = '__all__'

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    #evento = EventoSerializer(many = False)
    class Meta:
        model = Ticket
        fields = ('nome', 'descricao','valor','evento')

    def create(self, validated_data):
        print(validated_data)
        #evento_data = validated_data.pop("evento")
        #evento = Evento.objects.get(nome=evento_data['nome'])
        return Ticket.objects.create(**validated_data)

    #def create(self, validated_data): #corrigir
    #    evento_data = validated_data.pop('evento')
    #    e = Evento.objects.create(**evento_data)
    #    t = Ticket.objects.create(evento = e, **validated_data)
    #    return t

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    #evento = EventoSerializer(many = False)
    #participante = PessoaSerializer(many = False)
    #tickets = TicketSerializer(many = True)
    class Meta:
        model = Inscricao
        fields = ('participante', 'evento','tickets','validacao')

    def create(self,validated_data): #alguns comentários dessa função estão errados, verificar!!
        #pessoa_data = validated_data.pop("participante")
        #evento_data = validated_data.pop("evento")
        #ticket_data = validated_data.pop("tickets")
        #pessoa = models.Pessoa.objects.create(**pessoa_data)
        #evento = model.Evento.objects.create(**evento_data)
        #ticket = models.Ticket.objects.create(**ticket_data)
        return Inscricao.objects.create(**validated_data)

    #fazer depois: uma forma de realizar uma inscrição ou ticket sem a necessidade de inserir dados de objetos relacionados
    #exemplo, fazer a incrição sem a necessidade de criar um evento novo, utilizar os já existentes;
