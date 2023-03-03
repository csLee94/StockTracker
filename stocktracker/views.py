"""
created at: 2023-03-04
"""

from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Index
    """
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
