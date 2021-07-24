from flask import Flask 
from flask_restful import Api,Resource
import pandas as pd
import numpy as np

app = Flask(__name__)
api = Api(app)


def songSearch(userInput):
	data = pd.read_csv('tracks.csv')
	counter = -1
	dicts = {}
	for i in range(0,len(data['name'])):
		if userInput.lower() == str(data['name'][i]).lower():
			counter = counter + 1 
			artists = data.artists[i]
			loudness = data.loudness[i]
			popular = data.popularity[i]
			danceable = data.danceability[i]
			inst = data.instrumentalness[i]
			duration = float(data.duration_ms[i]/60000)
			dicts[counter] = {'song':data.name[i],'artists':artists,'duration':str(str(duration)+'s'),'loudness':str(loudness),'danceablity':str(danceable),'instrumentalness':str(inst),'popularity':str(popular)}
	return(dicts)



class spotifydata (Resource):
	def get(self,userInput):
		return songSearch(userInput)

api.add_resource(spotifydata,'/<string:userInput>')

if __name__ == '__main__':
	app.run(debug=True)