from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class CustomPageNumberPaginatio(PageNumberPagination):
    page_size = 50
    page_query_param = 'sayfa'


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 45
    limit_query_param = 'adet'
    offset_query_param = 'baslangic'


class CustomCursorPagination(CursorPagination):
    cursor_query_param = 'imlec'
    ordering = 'id'
    page_size = 10