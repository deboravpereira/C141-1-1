import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


movies_data = pd.read_csv('final.csv')
all_movies = movies_data[['original_title','poster_link' , 'release_date', 'runtime','weighted_rating']]

#Segregar dados


#Criar apis


app.run(debug=True)
