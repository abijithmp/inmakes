from django.shortcuts import render

from details.models import District
from wikipedia import wikipedia


# Create your views here.
def demo(request):
    districts = District.objects.all()
    for district in districts:
        wikipedia_page = wikipedia.page(district.name)

        district.wikipedia_url = wikipedia_page.url
    return render(request, 'index.html', {'districts': districts})
