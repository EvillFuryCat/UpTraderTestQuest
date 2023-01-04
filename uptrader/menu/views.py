from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        return render(request=request, template_name='exchange_menu/tree.html')
