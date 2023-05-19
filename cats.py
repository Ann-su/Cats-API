from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

@app.route('/')
def home():
    generate = request.args.get('generate')

    if generate:
        # Pobranie losowego zdjęcia kota z TheCatAPI
        cat_image_response  = requests.get('https://api.thecatapi.com/v1/images/search')
        cat_image_data  = cat_image_response .json()
        cat_image_url = cat_image_data [0]['url']

        # Pobranie losowego cytatu o kocie z innego API
        fact_response = requests.get('https://cat-fact.herokuapp.com/facts/random')  # Przykładowe API z cytatami o kotach
        fact_data = fact_response.json()
        cat_fact = fact_data['text']
    else:
        cat_image_url = request.args.get('cat_image_url')
        cat_fact = request.args.get('cat_fact')
    return render_template('cats.html', cat_image_url=cat_image_url, cat_fact=cat_fact) #Przetworzenie danych i przekazanie ich do szablonu

if __name__ == '__main__':
    app.run()
