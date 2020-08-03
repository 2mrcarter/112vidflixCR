from django.db import models
from tastypie.resources import ModelResource, ALL, fields
from rental.models import Movies, Genre
from tastypie.authorization import Authorization

# Create your models here.
# resourcesß /api/???

class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genres'
        ordering = ['id', 'name']
        filtering = {
            'id': ALL,
            'name': ALL
        }
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorizations = Authorization() #authroize all request to have right db permissions




class MovieResource(ModelResource):
    genre = fields.ToOneField(GenerResource, 'genre', full=True)
    
    class Meta:
        queryset = Movies.objects.all()
        resource_name = 'movies'
        ordering = ['title','id','price','release_year']
        filtering = {
            'title': ALL,
            'price': ALL,
            'release_year': ALL
        }
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorizations = Authorization() #authroize all request to have right db permissions



"""
Ordering: 
/api/movies/?order_by=title


Filter:
/api/movies/?price=12  Exact eq
/api/movies?price__lt=20 Lower than
/api/movies?price__gt=20 Greater than

"""