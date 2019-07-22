from rest_framework.pagination import PageNumberPagination

class FavouritePagination(PageNumberPagination):
    page_size = 4