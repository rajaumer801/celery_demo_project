from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from quotes.models import Quote
from quotes.serializers import QuoteSerializer
from quotes.tasks import get_random_quotes_task


class QuoteViewSet(viewsets.ViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def list(self, request):
        queryset = Quote.objects.all()
        serializer = QuoteSerializer(queryset, many=True)
        return Response(data=serializer.data)

    def create(self, request):
        get_random_quotes_task.delay()
        serializer = QuoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def retrieve(self, request, pk=None):
        area = get_object_or_404(Quote, pk=pk)
        serializer = QuoteSerializer(area)
        return Response(data=serializer.data)

    def update(self, request, pk=None):
        instance = get_object_or_404(Quote, pk=pk)
        serializer = QuoteSerializer(
            instance=instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(Quote, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
