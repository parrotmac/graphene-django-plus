from django.conf.urls import url
from graphene_django.views import GraphQLView

from .schema import schema


urlpatterns = [
    url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
]
