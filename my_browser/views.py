import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        url = f"https://www.google.com/search?q={search_query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Zde implementujte konkrétní extrakci dat z HTML stránky
        results = []
        for result in soup.select('.search .g'):
            title = result.h3.text
            link = result.a['href']
            description = result.find('span', class_='snippet').text
            results.append({'title': title, 'link': link, 'description': description})

        return render(request, 'results.html', {'results': results})
    else:
        return render(request, 'index.html')