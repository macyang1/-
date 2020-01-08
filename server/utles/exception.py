from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status

from rest_framework.response import Response

def exception_handler(exc, context):
    # drf的exception_handler做基础处理
    response = drf_exception_handler(exc, context)
    # 为空，自定义二次处理
    if response is None:
        # print(exc)
        # print(context)
        print('%s - %s - %s' % (context['view'], context['request'].method, exc))
        return Response({
            'detail': '服务器错误'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)
    return response
