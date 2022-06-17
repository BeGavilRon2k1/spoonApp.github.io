from ctypes import util
from re import A
from xmlrpc.client import Server
from django.shortcuts import render, redirect
from django.http import HttpResponse
from pyparsing import empty
import requests
import numpy as np
from django.views.generic import ListView
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from polls.models import NumValueReceta
from polls.models import NumValueIngrediente

from django.forms import modelformset_factory
import django_tables2 as tables
from django_tables2 import RequestConfig

from django.template import Template
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.conf import settings
from polls import utils
import http.client
import pandas as pd 
import re
from decimal import Decimal

apiSpoon = settings.APIKEY_MANU_RAPIDAPI
myRapidKey = settings.APIKEY_MY_RAPIDAPI
conn = http.client.HTTPSConnection(settings.CONN_SPOON)

def databaseBaserow(request):

    idRecipe = '1733445'
    servings = 0 #0 son por defecto y 1 es 1 comensal
    typeDatabase = 0 # 0 es BaseRow y 1 es Django
    typeSaveData = 1 # 0 es porcentage y 1 es numero

    headers = {
    'x-rapidapi-key': apiSpoon,
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    conn.request("GET", "https://api.spoonacular.com/recipes/"+ str(idRecipe) +"/nutritionWidget.json", headers=headers)
 
    resN = conn.getresponse()
    dataN = resN.read()
    datosNutricion  = json.loads(dataN)

    conn.request("GET", "https://api.spoonacular.com/recipes/"+ str(idRecipe) +"/information", headers=headers)

    resI = conn.getresponse()
    dataI = resI.read()
    datosInformation  = json.loads(dataI)
    
    #obtencion de valores por %
    valueporcentage = utils.obteinPorcentageData({'Nut': datosNutricion, 'Inf': datosInformation})
    valueNumber = utils.obteinData({'Nut': datosNutricion, 'Inf':datosInformation}, servings)
    
    #obtención de los nombres de los ingredientes
    cantidadIngredientes = utils.obtenerCantidadIngredientes(datosInformation)
    
    if typeSaveData == 0:
        utils.añadirValoresReceta(valueporcentage, cantidadIngredientes, typeDatabase)
    elif typeSaveData == 1:
        utils.añadirValoresReceta(valueNumber, cantidadIngredientes, typeDatabase)
    
    utils.añadirValoresReceta(valueNumber, cantidadIngredientes, 1)

    #Obtencion de los datos ingredientes
    idIngredientes = utils.obtenerIdIngredientes(datosInformation)
    for key in idIngredientes:
        ingredientes(key, typeDatabase)

    
    return render(request, 'ccc.html', {'Nut': idIngredientes})

def baserowToDjangoIngredSolid(request):

    datos = requests.get(
    "https://api.baserow.io/api/database/rows/table/72880/?user_field_names=true",
    "http://api.baserow.io/api/database/rows/table/72880/?page=2&user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu"
    }
    ) 

    data = datos.json()
    date = len(data['results'])
    
    
    for key in data['results']:
        NumValueIngrediente.objects.create(
            
            Nombre=key['Nombre'], IdSpoon=key['IdSpoon'],
            Carbohidratos=key['Carbohidratos(g)'], Proteinas=key['Proteinas'], Grasas=key['Grasas'],
            Kcal=key['Kcal'], SaturedFat=key['GrasasSaturadas'], Colesterol=key['Colesterol'],
            Alcohol=key['Alcohol'], Cafeina=key['Cafeina'], Cobre=key['Cobre'],
            Calcio=key['Calcio'], Fluor=key['Fluor'], VitA=key['VitA'],
            VitB1=key['VitB1'], VitB2=key['VitB2'], VitB3=key['VitB3'],
            VitB5=key['VitB5'], VitB6=key['VitB6'], VitB12=key['VitB12'],
            VitC=key['VitC'], VitD=key['VitD'], VitE=key['VitE'],
            VitK=key['VitK'], Fibra=key['Fibra'], Hierro=key['Hierro'],
            Magnesio=key['Magnesio'], Manganeso=key['Manganeso'], Fosforo=key['Fosforo'],
            Potasio=key['Potasio'], Selenio=key['Selenio'], Sodio=key['Sodio'],
            Azucar=key['Azucar'], Zinc=key['Zinc'])

    return render(request, 'ccc.html', {'Nut': data})

def baserowToDjangoIngredLiquid(request):

    datos = requests.get(
    "https://api.baserow.io/api/database/rows/table/72882/?user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu"
    }
    ) 
    data = datos.json()
    
    for key in data['results']:
        NumValueIngrediente.objects.create(
            
            Nombre=key['Nombre'], IdSpoon=key['IdSpoon'],
            Carbohidratos=(float(key['Carbohidratos(g)'])/float(key['Change_ml'])),
            Proteinas=(float(key['Proteinas'])/float(key['Change_ml'])),
            Grasas=(float(key['Grasas'])/float(key['Change_ml'])),
            Kcal=(float(key['Kcal'])/float(key['Change_ml'])),
            SaturedFat=(float(key['GrasasSaturadas'])/float(key['Change_ml'])),
            Colesterol=(float(key['Colesterol'])/float(key['Change_ml'])),
            Alcohol=(float(key['Alcohol'])/float(key['Change_ml'])),
            Cafeina=(float(key['Cafeina'])/float(key['Change_ml'])),
            Cobre=(float(key['Cobre'])/float(key['Change_ml'])),
            Calcio=(float(key['Calcio'])/float(key['Change_ml'])),
            Fluor=(float(key['Fluor'])/float(key['Change_ml'])),
            VitA=(float(key['VitA'])/float(key['Change_ml'])),
            VitB1=(float(key['VitB1'])/float(key['Change_ml'])),
            VitB2=(float(key['VitB2'])/float(key['Change_ml'])),
            VitB3=(float(key['VitB3'])/float(key['Change_ml'])),
            VitB5=(float(key['VitB5'])/float(key['Change_ml'])),
            VitB6=(float(key['VitB6'])/float(key['Change_ml'])),
            VitB12=(float(key['VitB12'])/float(key['Change_ml'])),
            VitC=(float(key['VitC'])/float(key['Change_ml'])),
            VitD=(float(key['VitD'])/float(key['Change_ml'])),
            VitE=(float(key['VitE'])/float(key['Change_ml'])),
            VitK=(float(key['VitK'])/float(key['Change_ml'])),
            Fibra=(float(key['Fibra'])/float(key['Change_ml'])),
            Hierro=(float(key['Hierro'])/float(key['Change_ml'])),
            Magnesio=(float(key['Magnesio'])/float(key['Change_ml'])),
            Manganeso=(float(key['Manganeso'])/float(key['Change_ml'])),
            Fosforo=(float(key['Fosforo'])/float(key['Change_ml'])),
            Folato=(float(key['Folato'])/float(key['Change_ml'])),
            Potasio=(float(key['Potasio'])/float(key['Change_ml'])),
            Selenio=(float(key['Selenio'])/float(key['Change_ml'])),
            Sodio=(float(key['Sodio'])/float(key['Change_ml'])),
            Azucar=(float(key['Azucar'])/float(key['Change_ml'])),
            Zinc=(float(key['Zinc'])/float(key['Change_ml'])))

    return HttpResponse('Listo')


def probasParaIngredientes(request):
    #NumValueIngrediente.objects
    a = NumValueIngrediente.objects.filter(Nombre='tomatoes')
    
    
    return render(request, 'eee.html', {'Nut': a})

    
def ingredientes(id, type):
    id = '4053'
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/"+ str(id) +"/information"

    querystring = {"amount":"1000","unit":"gram"}

    headers = {
	    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	    "X-RapidAPI-Key": "42cf77895bmshad685bb51a7fe7bp1f94c6jsn6d8e94ebdc37"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #obtención de datos de los ingredientes
    datos  = response.json()
    
    #Se añaden a las base de datos
    valorIngrediente = utils.infoIngredients(datos)
    utils.añadirValoresIngredientes(valorIngrediente, type)

def databaseDjango(request):

    idRecipe = '663505'
    
    headers = {
    'x-rapidapi-key': apiSpoon,
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    conn.request("GET", "https://api.spoonacular.com/recipes/"+ str(idRecipe) +"/nutritionWidget.json", headers=headers)
 
    resN = conn.getresponse()
    dataN = resN.read()
    datosNutricion  = json.loads(dataN)

    conn.request("GET", "https://api.spoonacular.com/recipes/"+ str(idRecipe) +"/information", headers=headers)

    resI = conn.getresponse()
    dataI = resI.read()
    datosInformation  = json.loads(dataI)

    datos = utils.obteinData({'Nut': datosNutricion, 'Inf':datosInformation}, 1)
    #valueporcentage = utils.obteinPorcentageData({'Nut': datosNutricion, 'Inf': datosInformation})
    nombreIngredientes = utils.obtenerIngredientes(datosInformation)
    #valorIngrediente = utils.infoIngredients(datos)
    
    ingredientes('20420', 1)
    
    #utils.añadirValoresReceta(valueporcentage, nombreIngredientes, 1)
    #utils.añadirValoresIngredientes(valorIngrediente, 1)
    return render(request, 'ccc.html', {'Nut': datos}) 
    #return render(request, 'ccc.html', {'Nut': datos})
    #return render(request, 'ccc.html', {'Nut': datosNutricion, 'Inf':datosInformation})


def probaIngredientesCantidad(request):

    idRecipe = '660820'
    
    headers = {
    'x-rapidapi-key': apiSpoon,
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    conn.request("GET", "https://api.spoonacular.com/recipes/"+ str(idRecipe) +"/nutritionWidget.json", headers=headers)
 
    resN = conn.getresponse()
    dataN = resN.read()
    datosNutricion  = json.loads(dataN)

    conn.request("GET", "https://api.spoonacular.com/recipes/"+ str(idRecipe) +"/information", headers=headers)

    resI = conn.getresponse()
    dataI = resI.read()
    datosInformation  = json.loads(dataI)

    #datos = utils.obteinData({'Nut': datosNutricion, 'Inf':datosInformation}, 1)
    #valueporcentage = utils.obteinPorcentageData({'Nut': datosNutricion, 'Inf': datosInformation})
    #nombreIngredientes = utils.obtenerIngredientes(datosInformation)
    #valorIngrediente = utils.infoIngredients(datos)
    
    #ingredientes('20420', 1)
    
    #utils.añadirValoresReceta(valueporcentage, nombreIngredientes, 1)
    #utils.añadirValoresIngredientes(valorIngrediente, 1)
    #return render(request, 'ccc.html', {'Nut': datos}) 
    #return render(request, 'ccc.html', {'Nut': datos})


    cantidadIngredientes = utils.obtenerCantidadIngredientes(datosInformation)

    #return render(request, 'ccc.html', {'Nut': cantidadIngredientes})
    return render(request, 'ccc.html', {'Nut': datosNutricion, 'Inf':datosInformation})

def home(request):
    
    result = request.POST.get('busca')
    
    if result:
        
        
        return render(request, 'main.html', {'r':datosTemplate(result)})
    else:
        return render(request, 'main.html', {})

def homeAll(request):
    
    datos = requests.get(
    "https://api.baserow.io/api/database/rows/table/68626/?user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu",#Alb.
        #"Authorization": "Token AMn3mq1KLo66knTMYkBupUm87qMuf61W",#Fra.
    }
    ) 
    data = datos.json()
    arrayobj = {}

    for key in data['results']:
        arrayobj = np.append(arrayobj, key)
    arrayobj=np.delete(arrayobj,0)
    return render(request, 'main.html', {'r':arrayobj})


def datosTemplate(busca):
    datos = requests.get(
    "https://api.baserow.io/api/database/rows/table/68626/?user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu",#Alb.
        #"Authorization": "Token AMn3mq1KLo66knTMYkBupUm87qMuf61W",#Fra.
    }
    ) 
    data = datos.json()
    arrayobj = {}

    for key in data['results']:
        if key['Platos_base'].find(busca) != -1:
            arrayobj = np.append(arrayobj, key)

    
    arrayobj=np.delete(arrayobj,0)

    return arrayobj

def datosPlato(request, ident):

#obtiene el id del plato base
    datos = requests.get(
    "https://api.baserow.io/api/database/rows/table/68626/" + str(ident) + "/?user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu"
    }
)
    dataBase = datos.json()
    ingredientes = []
    valoresBase = utils.obtenerValoresBase(dataBase['id'])
    valoresRecomend = utils.obtenerValoresRecomend()
    percentage = utils.basePercentage(valoresBase, valoresRecomend)

    for key, value in dataBase.items():
        if key[:12] == 'Ingrediente_':
            if value:

                a = key.split('_')
                aux = int(a[1])
                
                ingredientes.append({'ingrediente': value[0]['value'], 'cantidad': dataBase['Cantidad_'+str(aux)]})
    
    

    return render(request, 'dish.html', {'r':dataBase, 'i': ingredientes, 'vb': valoresBase, 'p':percentage}) 

def probaingredientes100(request):
    
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/10011821/information"

    querystring = {"amount":"1000","unit":"gram"}

    headers = {
	    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	    "X-RapidAPI-Key": "42cf77895bmshad685bb51a7fe7bp1f94c6jsn6d8e94ebdc37"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #obtención de datos de los ingredientes
    datos  = response.json()
    
    #Se añaden a las base de datos por 1g
    valorIngrediente = utils.infoIngredients(datos)
    utils.añadirValoresIngredientes(valorIngrediente, 0)

    return render(request, 'ccc.html', {'Nut': valorIngrediente})

#para añadir los valores de los platos base
def getIngredientePlatoBaseLink(request): 

    id = 12

    calorias = 0; proteinas = 0; hidratos = 0; grasas = 0; sodio = 0

    datos = requests.get(
    "https://api.baserow.io/api/database/rows/table/68626/"+str(id)+"/?user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu"
    }
)
    aux = 2
    data = datos.json()
    
    arrato = []
    debug = []
    for key, value in data.items():

        if key[:12] == 'Ingrediente_':
        

            if value:

                a = key.split('_')
                aux = int(a[1])

                cantidad = Decimal(data['Cantidad_'+str(aux)])
                #debug.append({aux, cantidad})
                
                valores = obtenerValoresIngredientesPlatos(request, value[0]['id'])
                #return valores
                calorias += (float(valores['cal'])*int(cantidad))
                #arrato.append(calorias)
                
                proteinas += float(valores['prot'])*int(cantidad)
                hidratos += float(valores['carbs'])*int(cantidad)
                grasas += float(valores['fat'])*int(cantidad)
                sodio += float(valores['sodio'])*int(cantidad)
                
                
                


    arrayDatos = {'receta': data['Platos_base'],'id':id, 'cal': calorias, 'prot': proteinas, 'carbs': hidratos, 'fat': grasas, 'sod': sodio}
    utils.añadirPlatoBaseValoresPrincipales(arrayDatos)
    return render(request, 'ccc.html', {'receta': data['Platos_base'], 'Nut': {'cal': calorias, 'prot': proteinas, 'carbs': hidratos, 'fat': grasas, 'sod': sodio}})


def getIngredientePlatoPersonalizadoLink(request): 

    id = 17

    calorias = 0; proteinas = 0; hidratos = 0; grasas = 0; sodio = 0

    datos = requests.get(
    "https://api.baserow.io/api/database/rows/table/68627/"+str(id)+"/?user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu"
    }
)   
    data = datos.json()
    #return render(request, 'ccc.html', {'Nut': data})

    for key, value in data.items():
        #cantidad = 0
        #cantidad = data['Cantidad_'+str(aux)]
        #cantidadAdd = data['Cantidad_Add_'+str(auxAdd)]

        if key[:12] == 'Ingrediente_':
            if value:
                a = key.split('_')
                aux = int(a[1])
                cantidad = Decimal(data['Cantidad_'+str(aux)])

                valores = obtenerValoresIngredientesPlatos(request, value[0]['ids']['database_table_72930'])

                calorias += float(valores['cal'])*float(cantidad)

                proteinas += float(valores['prot'])*float(cantidad)
                hidratos += float(valores['carbs'])*float(cantidad)
                grasas += float(valores['fat'])*float(cantidad)
                sodio += float(valores['sodio'])*float(cantidad)
        
        if key[:4] == 'Add_':
            if value:
                a = key.split('_')
                aux = int(a[1])
                cantidadAdd = Decimal(data['Cantidad_Add_'+str(aux)])

                valores = obtenerValoresIngredientesPlatos(request, value[0]['id'])
                
                calorias += float(valores['cal'])*float(cantidadAdd)

                proteinas += float(valores['prot'])*float(cantidadAdd)
                hidratos += float(valores['carbs'])*float(cantidadAdd)
                grasas += float(valores['fat'])*float(cantidadAdd)
                sodio += float(valores['sodio'])*float(cantidadAdd)
                              

    arrayDatos = {'receta': data['Plato_personalizado'],'id':id, 'cal': calorias, 'prot': proteinas, 'carbs': hidratos, 'fat': grasas, 'sod': sodio}
    
    utils.añadirPlatoPersonalizadoValoresPrincipales(arrayDatos)
    return render(request, 'ccc.html', {'receta': data['Plato_personalizado'], 'Nut': {'cal': calorias, 'prot': proteinas, 'carbs': hidratos, 'fat': grasas, 'sod': sodio}})
    #return render(request, 'ccc.html', {'Nut': data})
    #return render(request, 'ccc.html', {'Nut': valores})

def obtenerValoresIngredientesPlatos(request, id):

    #valores = {}
    calorias = 0; proteinas = 0; hidratos = 0; grasas = 0; sodio = 0

    datos = requests.get(
    "https://api.baserow.io/api/database/rows/table/72930/" + str(id) + "/?user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu"
    }
)
    data = datos.json()
    
    if data['Unidad']=='ml':
        #gInMl = 1/float(data['converse_ml'])
        percentageLiquid = 0.03
        
        calorias = float(data['Cal'])*percentageLiquid
        proteinas = float(data['Proteinas'])*percentageLiquid
        hidratos = float(data['Carbohidratos'])*percentageLiquid
        grasas = float(data['Grasas'])*percentageLiquid
        sodio = float(data['Sodio'])*percentageLiquid

    if data['Unidad']=='gr':

        calorias = data['Cal']
        proteinas = data['Proteinas']
        hidratos = data['Carbohidratos']
        grasas = data['Grasas']
        sodio = data['Sodio']
    

    return {'cal': calorias, 'prot': proteinas, 'carbs': hidratos, 'fat': grasas, 'sodio': sodio}
    #return render(request, 'ccc.html', {'Nut': data})

    









#{{ mydict|get_item:item.NAME }}
#from django.template.defaulttags import register
#...
#@register.filter
#def get_item(dictionary, key):
#    return dictionary.get(key)