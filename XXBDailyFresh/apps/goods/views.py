from django.shortcuts import render
from XXBDailyFresh import settings
import os


# Create your views here.

# http://127.0.0.1:8000
def index(request):
    """
     首页
    :param request:
    :return:
    """
    print("X" * 50)
    print(os.path.join(settings.BASE_DIR, 'templates'))
    return render(request, 'index.html')
