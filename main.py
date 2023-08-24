from flask import Flask,request
import json
app=Flask(__name__)
#cargo los datos del archivo Json
with open('lista.json','r') as json_file:
    animes_data=json.load(json_file)

# METODO GET
@app.route('/anime',methods=['GET'])
def get_nombres_animes():
    nombres_animes=[f"{anime['id']}.{anime['titulo']}" for anime in animes_data["animes"]]
    response = "\n".join(nombres_animes)
    return response, 200,{'Content-Type': 'text/plain; charset=utf-8'}

# METODO GET_PARTE2
@app.route('/anime/<int:id>',methods={'GET'})
def get_info_anime(id):
    anime=next((anime for anime in animes_data["animes"] if anime["id"]==id),None)
    response = "Anime no encontrado\nERROR 404"
    if anime != None:
        informacion=[f"Titulo:{anime['titulo']}"
                     f"\nID:{anime['id']} "
                     f"\nPuntaje:{anime['puntaje']}"
                     f"\nTipo:{anime['tipo']}"
                     f"\nSeason:{anime['season']}"
                     f"\nGeneros:{anime['generos']}"]
        response="".join(informacion)
        return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    return response, 200,{'Content-Type': 'text/plain; charset=utf-8'}

# METODO PATCH changes partial
@app.route('/anime/<int:id>', methods=['PATCH'])
def short_edition(id):
    anime = next((anime for anime in animes_data["animes"] if anime["id"] == id), None)
    response = "Anime no encontrado\nERROR 404"
    if anime != None:
        datosanime = request.json
        if datosanime and "id" in datosanime and datosanime["id"] != anime["id"]:
            return "Ids no coinciden\nSin cambios realizados"
        for i, dato in datosanime.items():
            if i in anime:
                anime[i] = dato
        informacion = [f"Titulo:{anime['titulo']}"
                       f"\nID:{anime['id']} "
                       f"\nPuntaje:{anime['puntaje']}"
                       f"\nTipo:{anime['tipo']}"
                       f"\nSeason:{anime['season']}"
                       f"\nGeneros:{anime['generos']}"]
        response = "".join(informacion)
        return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}

# METODO PUT changes all or replace it
@app.route('/anime/<int:id>', methods=['PUT'])
def complete_edition(id):
    anime = next((anime for anime in animes_data["animes"] if anime["id"] == id), None)
    response = "Anime no encontrado\nERROR 404"
    if anime != None:
        datosanime = request.json
        if len(datosanime)<6:
            return "Información incompleta\nsin cambios realizados"
        if datosanime["id"]!=id:
            return "Ids no coinciden\nSin cambios realizados"
        for i, dato in datosanime.items():
            if i in anime:
                anime[i] = dato
        informacion = [f"Titulo:{anime['titulo']}"
                       f"\nID:{anime['id']} "
                       f"\nPuntaje:{anime['puntaje']}"
                       f"\nTipo:{anime['tipo']}"
                       f"\nSeason:{anime['season']}"
                       f"\nGeneros:{anime['generos']}"]
        response = "".join(informacion)
        return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}

#METODO POST
@app.route('/anime/<int:id>',methods=['POST'])
def nuevo_anime(id):
    anime = next((anime for anime in animes_data["animes"] if anime["id"] == id), None)
    response = "Anime ya existe\nno hubieron cambios"
    if anime ==None:
        new=request.json
        if new["id"]!=id:
            return "Ids no coinciden\nSin cambios realizados"
        animes_data["animes"].append(new)
        informacion = [f"Titulo:{new['titulo']}"
                       f"\nID:{new['id']} "
                       f"\nPuntaje:{new['puntaje']}"
                       f"\nTipo:{new['tipo']}"
                       f"\nSeason:{new['season']}"
                       f"\nGeneros:{new['generos']}"]
        response = "".join(informacion)
        return response
    return response

# METODO DELETE-Elimina
@app.route('/anime/<int:id>',methods=['DELETE'])
def eliminar_anime(id):
    anime = next((anime for anime in animes_data["animes"] if anime["id"] == id), None)
    if anime != None:
        animes_data["animes"].remove(anime)
        return "Anime eliminado \ncorrectamente"
    return "Id No existe\nno hubieron cambios"

if __name__ == '__main__':
    app.run(debug=True)
