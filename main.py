import pandas as pd
#from flask import Flask

#app=Flask(_name_)

base=pd.read_excel("Clasificacion de botes.xlsx")

#@app.route("/")
def Principal():
    return "Esta es una Api que te muestra los botes de la facultad"

#@app.route("/Por_Tipo/<Tipo>")
def PorTipo(Tipo):
  fila=base[base["Tipo"]==Tipo]
  respuesta=f"El tipo de bote es {fila.loc[:,'Tipo']}"
  return respuesta

print (PorTipo('Botellas de PET'))

#@app.route("/Por_Numero/<Numero>")
def PorNumero(Numero):
  Ubicacion=int(Numero)
  resultados=base[base["Longitud"]==Numero]
  resultados=str(resultados)
  return resultados

print (PorNumero(7))

#@app.route("/Por_Tamaño/<Tamaño>")
def PorTamaño(Tamaño):
  resultados=base[base["Tamaño"]==Tamaño]
  resultados=str(resultados)
  return resultados

print (PorTamaño('Grande'))
