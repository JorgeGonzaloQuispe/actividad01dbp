from flask import Flask
from flask import jsonify
import json
app=Flask(__name__)
#cargo los datos del archivo Json
with open('lista.json','r') as json_file:
    animes_data=json.load(json_file)

# METODO GET
# ruta para obtener la lista de animes
@app.route('/anime',methods=['GET'])
def get_nombres_animes():
    nombres_animes=[f"{anime['id']}.{anime['titulo']}" for anime in animes_data["animes"]]
    response = "\n".join(nombres_animes)
    return response, 200,{'Content-Type': 'text/plain; charset=utf-8'}

#METODO GET_PARTE2
@app.route('/anime/<int:id>',methods={'GET'})
def get_info_anime(id):
    anime=next((anime for anime in animes_data["animes"] if anime["id"]==id),None)
    response = "Anime no encontrado\nERROR 404"
    if anime:
        informacion=[f"Titulo:{anime['titulo']}"
                     f"\nID:{anime['id']} "
                     f"\nPuntaje:{anime['puntaje']}"
                     f"\nTipo:{anime['tipo']}"
                     f"\nSeason:{anime['season']}"
                     f"\nGeneros:{anime['generos']}"]
        response="".join(informacion)
        return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    return response, 200,{'Content-Type': 'text/plain; charset=utf-8'}


if __name__ == '__main__':
    app.run(debug=True)