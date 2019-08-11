from rest_framework.pagination import PageNumberPagination

class PostPagination(PageNumberPagination):
    page_size = 4