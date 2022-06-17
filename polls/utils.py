import numpy as np
from polls.models import NumValueReceta, NumValueIngrediente
import requests
from decimal import Decimal
import re

def obteinData(data, servCond):
    Nut = data['Nut']
    Inf = data['Inf']

    totalValores = 0
    totalCCPF = 0
    servings = int(Inf['servings'])

    SaturedFat = '0'; alcohol = '0'; cafeine = '0'; colesterol = '0'; fluor = '0';
    azucar = '0'; sodio = '0'; copper = '0'; calcium = '0'; fosforo = '0';
    manganeso = '0'; magnesio = '0'; folate = '0'; hierro = '0'; fibra = '0';
    selenio = '0'; zinc = '0'; potasio = '0'; vitA = '0'; vitC = '0'; vitD = '0';
    vitE = '0'; vitK = '0'; vitB1 = '0'; vitB2 = '0'; vitB3 = '0'; vitB5 = '0';
    vitB6 = '0'; vitB12 = '0'

#principales valores
#carbohidratos
    if Nut['carbs']:
        carbohidratos = re.sub(r"[^0-9]","", Nut['carbs'])
        carbohidratos = int(carbohidratos)
        totalCCPF +=carbohidratos

#calorias
    if Nut['calories']:
        calories = re.sub(r"[^0-9]","", Nut['calories'])
        calories = int(calories) #para estar en gramos
        totalCCPF += calories
    else:
        calories = 'False'

#proteinas
    if Nut['protein']:
        proteinas = re.sub(r"[^0-9]","", Nut['protein'])
        proteinas = int(proteinas)
        totalCCPF += proteinas
    else:
        proteinas = 'False'

#grasas
    if Nut['fat']:
        fat = re.sub(r"[^0-9]","", Nut['fat'])
        fat = int(fat)
        totalCCPF += fat
    else:
        fat = 'False'

#Valores marcados como 'Bad'
    for key in Nut['bad']:

        #satured Fat
        if key['title']=='Saturated Fat':
            SaturedFat =  int(re.sub(r"[^0-9]","",key['amount']))
            totalValores += SaturedFat
            
        ###Cambiar la cafeina
            
        #alcohol
        if key['title']=='Alcohol':
            alcohol =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += alcohol
        
        #cafeina
        if key['title']=='Caffeine':
            cafeine =  re.sub(r"[^0-9]","", key['amount'])###
            totalValores += cafeine
        
        #colesterol
        if key['title']=='Cholesterol':
            colesterol =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += colesterol
        
        #fluor
        if key['title']=='Fluorine':
            fluor =  int(re.sub(r"[^0-9]","", key['amount']))/1000000
            totalValores += fluor
        
        #sugar
        if key['title']=='Sugar':
            azucar =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += azucar
        
        #sodium
        if key['title']=='Sodium':
            sodio =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += sodio
        
    bad = {'saturedFat': SaturedFat, 'alcohol':alcohol, 'cafeina':cafeine, 'colesterol':colesterol, 'fluor':fluor, 'azucar':azucar, 'sodio':sodio}

#Valores marcados como 'Good'
    for key in Nut['good']:
   
        #cobre
        if key['title']=='Copper':
            copper =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += copper
        
        #calcio
        if key['title']=='Calcium':
            calcium =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += calcium
        
        #fosforo
        if key['title']=='Phosphorus':
            fosforo =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += fosforo
        
        #manganese
        if key['title']=='Manganese':
            manganeso =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += manganeso
        
        #magnesium
        if key['title']=='Magnesium':
            magnesio =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += magnesio
        
        #folate
        if key['title']=='Folate':
            folate =  int(re.sub(r"[^0-9]","", key['amount']))/1000000
            totalValores += folate
        
        #iron
        if key['title']=='Iron':
            hierro =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += hierro
        
        #fiber
        if key['title']=='Fiber':
            fibra =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += fibra 
        
        #selenium
        if key['title']=='Selenium':
            selenio =  int(re.sub(r"[^0-9]","", key['amount']))/1000000
            totalValores += selenio 
        
        #zinc
        if key['title']=='Zinc':
            zinc =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += zinc 
        
        #potasium
        if key['title']=='Potassium':
            potasio =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += potasio
        
        #VitaminA
        if key['title']=='Vitamin A':
            vitA =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += vitA
            
        #VitaminC
        if key['title']=='Vitamin C':
            vitC =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += vitC
        
        #VitaminD
        if key['title']=='Vitamin D':
            vitD =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += vitD
        
        #VitaminE
        if key['title']=='Vitamin E':
            vitE =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += vitE
        
        #VitaminK
        if key['title']=='Vitamin K':
            vitK =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += vitK
    
        #VitaminB1
        if key['title']=='Vitamin B1':
            vitB1 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += vitB1
        
        #VitaminB2
        if key['title']=='Vitamin B2':
            vitB2 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += vitB2
        
        #VitaminB3
        if key['title']=='Vitamin B3':
            vitB3 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += vitB3
        
        #VitaminB5
        if key['title']=='Vitamin B5':
            vitB5 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += vitB5
        
        #VitaminB6
        if key['title']=='Vitamin B6':
            vitB6 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += vitB6
        
        #VitaminB12
        if key['title']=='Vitamin B12':
            vitB12 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += vitB12

    if servCond == 0:
        vitaminas = {'vA':vitA, 'vC':vitC, 'vD':vitD, 'vE':vitE, 'vK':vitK, 'vB1':vitB1, 'vB2':vitB2, 'vB3':vitB3, 'vB5':vitB5, 'vB6':vitB6, 'vB12':vitB12}
        good = {'cobre':copper, 'calcio': calcium, 'fosforo':fosforo, 'manganeso':manganeso, 'magnesio':magnesio, 'folate':folate, 'hierro':hierro, 'fibra':fibra, 'selenium':selenio, 'zinc':zinc, 'potasio':potasio, 'vitaminas':vitaminas}

        arrayDatos = {'receta':Inf['title'],'idSpoon':Inf['id'],'servings':servings,'calorias':calories,'gCal': calories, 'carbs':carbohidratos,'gCarbs':carbohidratos, 'proteinas':proteinas,'gProt':proteinas, 'grasas':fat,'gFat':fat, 'bad':bad, 'good':good}
    elif servCond == 1:
        vitaminas = {'vA':int(vitA)/servings, 'vC':int(vitC)/servings, 'vD':int(vitD)/servings, 'vE':int(vitE)/servings, 'vK':int(vitK)/servings, 'vB1':int(vitB1)/servings, 'vB2':int(vitB2)/servings, 'vB3':int(vitB3)/servings, 'vB5':int(vitB5)/servings, 'vB6':int(vitB6)/servings, 'vB12':int(vitB12)/servings}
        good = {'cobre':int(copper)/servings, 'calcio': int(calcium)/servings, 'fosforo':int(fosforo)/servings, 'manganeso':int(manganeso)/servings, 'magnesio':int(magnesio)/servings, 'folate':int(folate)/servings, 'hierro':int(hierro)/servings, 'fibra':int(fibra)/servings, 'selenium':int(selenio)/servings, 'zinc':int(zinc)/servings, 'potasio':int(potasio)/servings, 'vitaminas':vitaminas}

        arrayDatos = {'receta':Inf['title'],'idSpoon':Inf['id'],'servings':'1','calorias':calories/servings, 'carbs':carbohidratos/servings, 'proteinas':proteinas/servings, 'grasas':fat/servings, 'bad':bad, 'good':good}
    return arrayDatos

def obteinBool(data):
    Nut = data['Nut']
    Inf = data['Inf']

    SaturedFat = 'False'; alcohol = 'False'; cafeine = 'False'; colesterol = 'False'; fluor = 'False';
    azucar = 'False'; sodio = 'False'; copper = 'False'; calcium = 'False'; fosforo = 'False';
    manganeso = 'False'; magnesio = 'False'; folate = 'False'; hierro = 'False'; fibra = 'False';
    selenio = 'False'; zinc = 'False'; potasio = 'False'; vitA = 'False'; vitC = 'False'; vitD = 'False';
    vitE = 'False'; vitK = 'False'; vitB1 = 'False'; vitB2 = 'False'; vitB3 = 'False'; vitB5 = 'False';
    vitB6 = 'False'; vitB12 = 'False'

#principales valores
#carbohidratos
    if Nut['carbs']:
        carbohidratos = 'True'
    else:
        carbohidratos = 'False'

#calorias
    if Nut['calories']:
        calories =  'True' 
    else:
        calories = 'False'

#proteinas
    if Nut['protein']:
        proteinas =  'True'
    else:
        proteinas = 'False'

#grasas
    if Nut['fat']:
        fat =  'True'
    else:
        fat = 'False'

#Valores marcados como 'Bad'
    for key in Nut['bad']:

        #satured Fat
        if key['title']=='Saturated Fat':
            SaturedFat =  'True'
        
        #alcohol
        if key['title']=='Alcohol':
            alcohol =  'True'
        
        #cafeina
        if key['title']=='Caffeine':
            cafeine =  'True'
        
        #colesterol
        if key['title']=='Cholesterol':
            colesterol =  'True'
        
        #fluor
        if key['title']=='Fluorine':
            fluor =  'True'
        
        #sugar
        if key['title']=='Sugar':
            azucar =  'True'
        
        #sodium
        if key['title']=='Sodium':
            sodio =  'True'
        
    bad = {'saturedFat': SaturedFat, 'alcohol':alcohol, 'cafeina':cafeine, 'colesterol':colesterol, 'fluor':fluor, 'azucar':azucar, 'sodio':sodio}

#Valores marcados como 'Good'
    for key in Nut['good']:
   
        #cobre
        if key['title']=='Copper':
            aux =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            copper = aux*(50/100)
            copper =  'True'
        
        #calcio
        if key['title']=='Calcium':
            calcium =  'True'
        
        #fosforo
        if key['title']=='Phosphorus':
            fosforo =  'True'
        
        #manganese
        if key['title']=='Manganese':
            manganeso =  'True'
        
        #magnesium
        if key['title']=='Magnesium':
            magnesio =  'True'
        
        #folate
        if key['title']=='Folate':
            folate =  'True'
        
        #iron
        if key['title']=='Iron':
            hierro =  'True'
        
        #fiber
        if key['title']=='Fiber':
            fibra =  'True'
        
        #selenium
        if key['title']=='Selenium':
            selenio =  'True'
        
        #zinc
        if key['title']=='Zinc':
            zinc =  'True'
        
        #potasium
        if key['title']=='Potassium':
            potasio =  'True'
        
        #VitaminA
        if key['title']=='Vitamin A':
            vitA =  'True'
            
        #VitaminC
        if key['title']=='Vitamin C':
            vitC =  'True'
        
        #VitaminD
        if key['title']=='Vitamin D':
            vitD =  'True'
        
        #VitaminE
        if key['title']=='Vitamin E':
            vitE =  'True'
        
        #VitaminK
        if key['title']=='Vitamin K':
            vitK =  'True'
        
        #VitaminB1
        if key['title']=='Vitamin B1':
            vitB1 =  'True'
        
        #VitaminB2
        if key['title']=='Vitamin B2':
            vitB2 =  'True'
        
        #VitaminB3
        if key['title']=='Vitamin B3':
            vitB3 =  'True'
        
        #VitaminB5
        if key['title']=='Vitamin B5':
            vitB5 =  'True'
        
        #VitaminB6
        if key['title']=='Vitamin B6':
            vitB6 =  'True'
        
        #VitaminB12
        if key['title']=='Vitamin B12':
            vitB12 =  'True'

    vitaminas = {'vA':vitA, 'vC':vitC, 'vD':vitD, 'vE':vitE, 'vK':vitK, 'vB1':vitB1, 'vB2':vitB2, 'vB3':vitB3, 'vB5':vitB5, 'vB6':vitB6, 'vB12':vitB12}
    good = {'cobre':copper, 'calcio': calcium, 'fosforo':fosforo, 'manganeso':manganeso, 'magnesio':magnesio, 'folate':folate, 'hierro':hierro, 'fibra':fibra, 'selenium':selenio, 'zinc':zinc, 'potasio':potasio, 'vitaminas':vitaminas}

    arrayDatos = {'calorias':calories,'gCal': Nut['calories'], 'carbs':carbohidratos,'gCarbs':Nut['carbs'], 'proteinas':proteinas,'gProt':Nut['protein'], 'grasas':fat,'gFat':Nut['fat'], 'bad':bad, 'good':good}

    return arrayDatos

def obteinPorcentageData(data):
    Nut = data['Nut']
    Inf = data['Inf']

    totalValores = 0
    totalCCPF = 0
    totalVit = 0
    servings = int(Inf['servings'])

    SaturedFat = 'False'; alcohol = 'False'; cafeine = 'False'; colesterol = 'False'; fluor = 'False';
    azucar = 'False'; sodio = 'False'; copper = 'False'; calcium = 'False'; fosforo = 'False';
    manganeso = 'False'; magnesio = 'False'; folate = 'False'; hierro = 'False'; fibra = 'False';
    selenio = 'False'; zinc = 'False'; potasio = 'False'; vitA = 'False'; vitC = 'False'; vitD = 'False';
    vitE = 'False'; vitK = 'False'; vitB1 = 'False'; vitB2 = 'False'; vitB3 = 'False'; vitB5 = 'False';
    vitB6 = 'False'; vitB12 = 'False'

#principales valores
#carbohidratos
    if Nut['carbs']:
        carbohidratos = re.sub(r"[^0-9]","", Nut['carbs'])
        carbohidratos = int(carbohidratos)
        totalCCPF +=carbohidratos
        
    else:
        carbohidratos = 'False'

#calorias
    if Nut['calories']:
        calories = re.sub(r"[^0-9]","", Nut['calories'])
        calories = int(calories) #para estar en gramos
        totalCCPF += calories
    else:
        calories = 'False'

#proteinas
    if Nut['protein']:
        proteinas = re.sub(r"[^0-9]","", Nut['protein'])
        proteinas = int(proteinas)
        totalCCPF += proteinas
    else:
        proteinas = 'False'

#grasas
    if Nut['fat']:
        fat = re.sub(r"[^0-9]","", Nut['fat'])
        fat = int(fat)
        totalCCPF += fat
    else:
        fat = 'False'

#Valores marcados como 'Bad'
    for key in Nut['bad']:

        #satured Fat
        if key['title']=='Saturated Fat':
            SaturedFat =  int(re.sub(r"[^0-9]","",key['amount']))
            totalValores += SaturedFat
            
        #alcohol
        if key['title']=='Alcohol':
            alcohol =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += alcohol
        
        #cafeina
        if key['title']=='Caffeine':
            cafeine =  re.sub(r"[^0-9]","", key['amount'])
            totalValores += cafeine
        
        #colesterol
        if key['title']=='Cholesterol':
            colesterol =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += colesterol
        
        #fluor
        if key['title']=='Fluorine':
            fluor =  int(re.sub(r"[^0-9]","", key['amount']))/1000000
            totalValores += fluor
        
        #sugar
        if key['title']=='Sugar':
            azucar =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += azucar
        
        #sodium
        if key['title']=='Sodium':
            sodio =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += sodio
        
#Valores marcados como 'Good'
    for key in Nut['good']:
   
        #cobre
        if key['title']=='Copper':
            copper =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += copper
        
        #calcio
        if key['title']=='Calcium':
            calcium =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += calcium
        
        #fosforo
        if key['title']=='Phosphorus':
            fosforo =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += fosforo
        
        #manganese
        if key['title']=='Manganese':
            manganeso =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += manganeso
        
        #magnesium
        if key['title']=='Magnesium':
            magnesio =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += magnesio
        
        #folate
        if key['title']=='Folate':
            folate =  int(re.sub(r"[^0-9]","", key['amount']))/1000000
            totalValores += folate
        
        #iron
        if key['title']=='Iron':
            hierro =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += hierro
        
        #fiber
        if key['title']=='Fiber':
            fibra =  int(re.sub(r"[^0-9]","", key['amount']))
            totalValores += fibra 
        
        #selenium
        if key['title']=='Selenium':
            selenio =  int(re.sub(r"[^0-9]","", key['amount']))/1000000
            totalValores += selenio 
        
        #zinc
        if key['title']=='Zinc':
            zinc =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += zinc 
        
        #potasium
        if key['title']=='Potassium':
            potasio =  int(re.sub(r"[^0-9]","", key['amount']))/1000
            totalValores += potasio
        
        #VitaminA
        if key['title']=='Vitamin A':
            vitA =  int(re.sub(r"[^0-9]","", key['amount']))
            totalVit += vitA
            
        #VitaminC
        if key['title']=='Vitamin C':
            vitC =  int(re.sub(r"[^0-9]","", key['amount']))
            totalVit += vitC
        
        #VitaminD
        if key['title']=='Vitamin D':
            vitD =  int(re.sub(r"[^0-9]","", key['amount']))
            totalVit += vitD
        
        #VitaminE
        if key['title']=='Vitamin E':
            vitE =  int(re.sub(r"[^0-9]","", key['amount']))
            totalVit += vitE
        
        #VitaminK
        if key['title']=='Vitamin K':
            vitK =  int(re.sub(r"[^0-9]","", key['amount']))
            totalVit += vitK
        
        #VitaminB1
        if key['title']=='Vitamin B1':
            vitB1 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalVit += vitB1
        
        #VitaminB2
        if key['title']=='Vitamin B2':
            vitB2 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalVit += vitB2
        
        #VitaminB3
        if key['title']=='Vitamin B3':
            vitB3 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalVit += vitB3
        
        #VitaminB5
        if key['title']=='Vitamin B5':
            vitB5 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalVit += vitB5
        
        #VitaminB6
        if key['title']=='Vitamin B6':
            vitB6 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalVit += vitB6
        
        #VitaminB12
        if key['title']=='Vitamin B12':
            vitB12 =  int(re.sub(r"[^0-9]","", key['amount']))
            totalVit += vitB12

    vitaminas = {'vA':porcentaje(totalVit, vitA), 'vC':porcentaje(totalVit, vitC), 'vD':porcentaje(totalVit, vitD), 'vE':porcentaje(totalVit, vitE), 'vK':porcentaje(totalVit, vitK), 'vB1':porcentaje(totalVit, vitB1), 'vB2':porcentaje(totalVit, vitB2), 'vB3':porcentaje(totalVit, vitB3), 'vB5':porcentaje(totalVit, vitB5), 'vB6':porcentaje(totalVit, vitB6), 'vB12':porcentaje(totalVit, vitB12)}
    bad = {'saturedFat': porcentaje(totalValores, SaturedFat), 'alcohol':porcentaje(totalValores, alcohol), 'cafeina':porcentaje(totalValores, cafeine), 'colesterol':porcentaje(totalValores, colesterol), 'fluor':porcentaje(totalValores, fluor), 'azucar':porcentaje(totalValores, azucar), 'sodio':porcentaje(totalValores, sodio)}
    good = {'cobre':porcentaje(totalValores, copper), 'calcio': porcentaje(totalValores, calcium), 'fosforo':porcentaje(totalValores, fosforo), 'manganeso':porcentaje(totalValores, manganeso), 'magnesio':porcentaje(totalValores, magnesio), 'folate':porcentaje(totalValores, folate), 'hierro':porcentaje(totalValores, hierro), 'fibra':porcentaje(totalValores, fibra), 'selenium':porcentaje(totalValores, selenio), 'zinc':porcentaje(totalValores, zinc), 'potasio':porcentaje(totalValores, potasio), 'vitaminas':vitaminas}

    arrayDatos = {'receta':Inf['title'],'idSpoon':Inf['id'],'servings':servings,'calorias':porcentaje(totalCCPF, calories),'gCal': calories, 'carbs':porcentaje(totalCCPF, carbohidratos),'gCarbs':carbohidratos, 'proteinas':porcentaje(totalCCPF, proteinas),'gProt':proteinas, 'grasas':porcentaje(totalCCPF, fat),'gFat':fat, 'bad':bad, 'good':good}

    return arrayDatos

def porcentaje(total, valor):
    
    if valor == 'False':
        return 'False'
    else:
        porcentaje = int((valor*100)/total)
        dato = ''

        if porcentaje >= 50 and porcentaje <= 75:
            dato = 'Medio'
        elif porcentaje > 75:
            dato = 'Alto'
        else:
            dato = 'True'

        return dato

def añadirValoresReceta(data, ingredientes, type):

    #obtenemos todos los ingredientes ya añadidos
    recetaAñadida = obtenerRecetasAñadidas()
    condAñadir = True

    for key in recetaAñadida:
        if key == data['receta']:
            condAñadir = False ###

    if condAñadir == True and type==0:
        requests.post(
    "https://api.baserow.io/api/database/rows/table/70036/?user_field_names=true",
    headers={
        "Authorization": "Token AMn3mq1KLo66knTMYkBupUm87qMuf61W",
        "Content-Type": "application/json"
    },
    json={
        "Receta": data['receta'],

        'IdSpoon':data['idSpoon'],

        'Servings':data['servings'],

        "Ingredientes": ingredientes,

        "Carbohidratos(g)": data['carbs'],

        "Proteinas": data['proteinas'],
        
        "Grasas": data['grasas'],
        
        "Kcal": data['calorias'],
        
        "Alcohol": data['bad']['alcohol'],
        
        "Cafeina": data['bad']['cafeina'],
        
        "Cobre": data['good']['cobre'],
        
        "Calcio": data['good']['calcio'],
        
        "Colesterol": data['bad']['colesterol'],
        
        "Fluor": data['bad']['fluor'],
        
        "GrasasSaturadas": data['bad']['saturedFat'],
        
        "VitA": data['good']['vitaminas']['vA'],
        
        "VitC": data['good']['vitaminas']['vC'],
        
        "VitD": data['good']['vitaminas']['vD'],
        
        "VitE": data['good']['vitaminas']['vE'],
        
        "VitK": data['good']['vitaminas']['vK'],
        
        "VitB1": data['good']['vitaminas']['vB1'],
        
        "VitB2": data['good']['vitaminas']['vB2'],
        
        "VitB3": data['good']['vitaminas']['vB3'],
        
        "VitB5": data['good']['vitaminas']['vB5'],
        
        "VitB6": data['good']['vitaminas']['vB6'],
        
        "VitB12": data['good']['vitaminas']['vB12'],
        
        "Fibra": data['good']['fibra'],
        
        "Folato": data['good']['folate'],
        
        "AcFolico": "0",
        
        "Hierro": data['good']['hierro'],
        
        "Magnesio": data['good']['magnesio'],
        
        "Manganeso": data['good']['manganeso'],
        
        "Fosforo": data['good']['fosforo'],
        
        "Potasio": data['good']['potasio'],
        
        "Selenio": data['good']['selenium'],
        
        "Sodio": data['bad']['sodio'],
        
        "Azucar": data['bad']['azucar'],
        
        "Zinc": data['good']['zinc'],
        
        "gCarbohidratos": data['carbs'],
        
        "gProteinas": data['proteinas'],
        
        "gGrasas": data['grasas'],
        
        "Kcal 100g": data['calorias']
        }
    )
    elif condAñadir == True and type==1:

        NumValueReceta.objects.create(
            receta=data['receta'], idSpoon=data['idSpoon'], servings=data['servings'],
            carbohidratos=data['carbs'], proteinas=data['proteinas'], grasas=data['grasas'],
            kcal=data['calorias'], saturedFat=data['bad']['saturedFat'], colesterol=data['bad']['colesterol'],
            alcohol=data['bad']['alcohol'], cafeina=data['bad']['cafeina'], cobre=data['good']['cobre'],
            calcio=data['good']['calcio'], fluor=data['bad']['fluor'], vitA=data['good']['vitaminas']['vA'],
            vitB1=data['good']['vitaminas']['vB1'], vitB2=data['good']['vitaminas']['vB2'], vitB3=data['good']['vitaminas']['vB3'],
            vitB5=data['good']['vitaminas']['vB5'], vitB6=data['good']['vitaminas']['vB6'], vitB12=data['good']['vitaminas']['vB12'],
            vitC=data['good']['vitaminas']['vC'], vitD=data['good']['vitaminas']['vD'], vitE=data['good']['vitaminas']['vE'],
            vitK=data['good']['vitaminas']['vK'], fibra=data['good']['fibra'], hierro=data['good']['hierro'],
            magnesio=data['good']['magnesio'], manganeso=data['good']['manganeso'], fosforo=data['good']['fosforo'],
            potasio=data['good']['potasio'], selenio=data['good']['selenium'], sodio=data['bad']['sodio'],
            azucar=data['bad']['azucar'], zinc=data['good']['zinc'])

def añadirValoresIngredientes(data, type):
    #obtenemos todos los ingredientes ya añadidos
    ingredienteAñadido = obtenerIngredientesAñadidos()
    condAñadir = True

    for key in ingredienteAñadido:
        if key == data['ingrediente']:
            condAñadir = True ###

    if condAñadir == True and type==0:
        requests.post(
    "https://api.baserow.io/api/database/rows/table/70037/?user_field_names=true",
    headers={
        #"Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu",#Alb.
        "Authorization": "Token AMn3mq1KLo66knTMYkBupUm87qMuf61W",#Fra.
        "Content-Type": "application/json"
    },
    json={
        "Nombre": data['ingrediente'],

        "IdSpoon": data['idSpoon'],

        "Carbohidratos(g)": data['carbs'],

        "Proteinas": data['proteinas'],
        
        "Grasas": data['grasas'],
        
        "Kcal": data['calorias'],
        
        "Alcohol": data['bad']['alcohol'],
        
        "Cafeina": data['bad']['cafeina'],
        
        "Cobre": data['good']['cobre'],
        
        "Calcio": data['good']['calcio'],
        
        "Colesterol": data['bad']['colesterol'],
        
        "Fluor": data['bad']['fluor'],
        
        "GrasasSaturadas": data['bad']['saturedFat'],
        
        "VitA": data['good']['vitaminas']['vA'],
        
        "VitC": data['good']['vitaminas']['vC'],
        
        "VitD": data['good']['vitaminas']['vD'],
        
        "VitE": data['good']['vitaminas']['vE'],
        
        "VitK": data['good']['vitaminas']['vK'],
        
        "VitB1": data['good']['vitaminas']['vB1'],
        
        "VitB2": data['good']['vitaminas']['vB2'],
        
        "VitB3": data['good']['vitaminas']['vB3'],
        
        "VitB5": data['good']['vitaminas']['vB5'],
        
        "VitB6": data['good']['vitaminas']['vB6'],
        
        "VitB12": data['good']['vitaminas']['vB12'],
        
        "Fibra": data['good']['fibra'],
        
        "Folato": data['good']['folate'],
        
        "AcFolico": "0.0",
        
        "Hierro": data['good']['hierro'],
        
        "Magnesio": data['good']['magnesio'],
        
        "Manganeso": data['good']['manganeso'],
        
        "Fosforo": data['good']['fosforo'],
        
        "Potasio": data['good']['potasio'],
        
        "Selenio": data['good']['selenium'],
        
        "Sodio": data['bad']['sodio'],
        
        "Azucar": data['bad']['azucar'],
        
        "Zinc": data['good']['zinc'],
        
        "gCarbohidratos": data['gCarbs'],
        
        "gProteinas": data['gProt'],
        
        "gGrasas": data['gFat'],
        
        "Kcal 100g": data['gCal']
        }
    )
    elif condAñadir == True and type==1:

        NumValueIngrediente.objects.create(
            
            Nombre=data['ingrediente'], IdSpoon=data['idSpoon'],
            Carbohidratos=data['carbs'], Proteinas=data['proteinas'], Grasas=data['grasas'],
            Kcal=data['calorias'], SaturedFat=data['bad']['saturedFat'], Colesterol=data['bad']['colesterol'],
            Alcohol=data['bad']['alcohol'], Cafeina=data['bad']['cafeina'], Cobre=data['good']['cobre'],
            Calcio=data['good']['calcio'], Fluor=data['bad']['fluor'], VitA=data['good']['vitaminas']['vA'],
            VitB1=data['good']['vitaminas']['vB1'], VitB2=data['good']['vitaminas']['vB2'], VitB3=data['good']['vitaminas']['vB3'],
            VitB5=data['good']['vitaminas']['vB5'], VitB6=data['good']['vitaminas']['vB6'], VitB12=data['good']['vitaminas']['vB12'],
            VitC=data['good']['vitaminas']['vC'], VitD=data['good']['vitaminas']['vD'], VitE=data['good']['vitaminas']['vE'],
            VitK=data['good']['vitaminas']['vK'], Fibra=data['good']['fibra'], Hierro=data['good']['hierro'],
            Magnesio=data['good']['magnesio'], Manganeso=data['good']['manganeso'], Fosforo=data['good']['fosforo'],
            Potasio=data['good']['potasio'], Selenio=data['good']['selenium'], Sodio=data['bad']['sodio'],
            Azucar=data['bad']['azucar'], Zinc=data['good']['zinc'])

def obtenerIngredientes(Inf):
    
    datos = Inf['extendedIngredients']
    datosArray = {}
    stringArray = ''

    for key in datos:
        
        datosArray = np.append(datosArray, key['name'])

    #datosArray.pop(0)
    datosArray=np.delete(datosArray,0)
    
    for key in datosArray:
        stringArray += key+', '
    return stringArray

def obtenerIdIngredientes(Inf):
    
    datos = Inf['extendedIngredients']
    datosArray = {}
    stringArray = ''

    for key in datos:
        
        datosArray = np.append(datosArray, key['id'])

    #datosArray.pop(0)
    datosArray=np.delete(datosArray,0)
    
    return datosArray

def obtenerCantidadIngredientes(Inf):
    
    datos = Inf['extendedIngredients']
    servings = Inf['servings']
    nombre = {}
    cantidad = {}
    metric = {}
    stringArray = ''

    for key in datos:
        keyunidad = key['measures']['metric']['unitShort']
        keyamount = key['measures']['metric']['amount']

        if keyunidad == 'tsp' or keyunidad == 'tsps':
            if key['consistency']=='SOLID':
                keyamount = (keyamount*5.69)/int(servings)
                keyunidad = 'g'
            elif key['consistency']=='LIQUID':
                keyamount = (keyamount*4.929)/int(servings)
                keyunidad = 'ml'

        elif keyunidad == 'Tbsp' or keyunidad == 'Tbsps': 
            if key['consistency']=='SOLID':
                keyamount = (keyamount*17.07)/int(servings)
                keyunidad = 'g'
            elif key['consistency']=='LIQUID':
                keyamount = (keyamount*14.787)/int(servings)
                keyunidad = 'ml'

        elif keyunidad == 'cup': #cambiar##
            if key['consistency']=='SOLID':
                keyamount = (keyamount*5.69)/int(servings)
                keyunidad = 'g'
            elif key['consistency']=='LIQUID':
                keyamount = (keyamount*4.929)/int(servings)
                keyunidad = 'ml'
        elif keyunidad == '' or keyunidad == 'servings':
            keyunidad = 'u'
        
        nombre = np.append(nombre, key['name'])
        cantidad = np.append(cantidad, keyamount)
        metric = np.append(metric, keyunidad)

    #datosArray.pop(0)
    nombre=np.delete(nombre,0)
    cantidad=np.delete(cantidad,0)
    metric=np.delete(metric,0)
    
    long = nombre.size

    for i in range(0, long):
        #stringArray += str(nombre[0])+','
        stringArray += nombre[i]+',' + str(cantidad[i])+',' + metric[i]+'|'
        #stringArray += nombre['key']+',' + cantidad['key']+',' + metric['key']+'|'
    

    #Pruebas para despues obtener los ingredientes en un diccionario
    #proba = stringArray.split('|')
    #proba=np.delete(proba,long)
    #arrayProba = {}

    #for key in proba:
    #   proba2 = key.split(',')
    #    arrayProba = np.append(arrayProba, {'ingredient': proba2[0], 'amount': proba2[1], 'metric': proba2[2]}) 
    #    #b = {proba2[0]:proba2[1]}
    
    #arrayProba=np.delete(arrayProba,0)

    
    return stringArray 
    #return arrayProba 

#Obtencion de ingredientes ya añadidos a la base de datos
def obtenerIngredientesAñadidos():
    datosArray = {}

    datos = requests.get(
        "https://api.baserow.io/api/database/rows/table/70037/?user_field_names=true",
        headers={
            "Authorization": "Token AMn3mq1KLo66knTMYkBupUm87qMuf61W"
    }
)
    data = datos.json()

    for key in data['results']:
        datosArray = np.append(datosArray, key['Nombre'])

    datosArray=np.delete(datosArray,0)
    
    return datosArray

#Obtencion de recetas ya añadidas a la base de datos
def obtenerRecetasAñadidas():
    datosArray = {}

    datos = requests.get(
    "https://api.baserow.io/api/database/rows/table/70036/?user_field_names=true",
    headers={
        "Authorization": "Token AMn3mq1KLo66knTMYkBupUm87qMuf61W"
    }
)

    data = datos.json()

    for key in data['results']:
        datosArray = np.append(datosArray, key['Receta'])

    datosArray=np.delete(datosArray,0)
    
    return datosArray


def infoIngredients(data):
    Nut = data['nutrition']['nutrients']

    totalValores = 0
    totalCCPF = 0

    carbohidratos = '0.0'; calories = '0.0'; proteinas = '0.0'; fat = '0.0'
    SaturedFat = '0.0'; alcohol = '0.0'; cafeine = '0.0'; colesterol = '0.0'; fluor = '0.0';
    azucar = '0.0'; sodio = '0.0'; copper = '0.0'; calcium = '0.0'; fosforo = '0.0';
    manganeso = '0.0'; magnesio = '0.0'; folate = '0.0'; hierro = '0.0'; fibra = '0.0';
    selenio = '0.0'; zinc = '0.0'; potasio = '0.0'; vitA = '0.0'; vitC = '0.0'; vitD = '0.0';
    vitE = '0.0'; vitK = '0.0'; vitB1 = '0.0'; vitB2 = '0.0'; vitB3 = '0.0'; vitB5 = '0.0';
    vitB6 = '0.0'; vitB12 = '0.0'

    #principales valores
    for key in Nut:
     
        #carbohidratos
        if key['name']=='Carbohydrates':
            carbohidratos = key['amount']
            carbohidratos = int(carbohidratos)
            totalCCPF +=carbohidratos

        #calorias
        if key['name']=='Calories':
            calories = key['amount']
            calories = int(calories)
            totalCCPF += calories

        #proteinas
        if key['name']=='Protein':
            proteinas = key['amount']
            proteinas = int(proteinas)
            totalCCPF += proteinas

        #grasas
        if key['name']=='Fat':
            fat = key['amount']
            fat = int(fat)
            totalCCPF += fat

    #Valores marcados como 'Bad'
    

       #satured Fat
        if key['name']=='Saturated Fat':
            SaturedFat =  key['amount']
            totalValores += SaturedFat
            
        ###Cambiar la cafeina
            
        #alcohol
        if key['name']=='Alcohol':
            alcohol =  key['amount']
            totalValores += alcohol
        
        #cafeina
        if key['name']=='Caffeine':
            cafeine =  key['amount']
            totalValores += cafeine
        
        #colesterol
        if key['name']=='Cholesterol':
            colesterol =  int(key['amount'])/1000
            totalValores += colesterol
        
        #fluor
        if key['name']=='Fluorine':
            fluor =  int(key['amount'])/1000000
            totalValores += fluor
        
        #sugar
        if key['name']=='Sugar':
            azucar =  key['amount']
            totalValores += azucar
        
        #sodium
        if key['name']=='Sodium':
            sodio =  int(key['amount'])/1000
            totalValores += sodio
        
    #Valores marcados como 'Good'
    
   
        #cobre
        if key['name']=='Copper':
            copper =  int(key['amount'])/1000
            totalValores += copper
        
        #calcio
        if key['name']=='Calcium':
            calcium =  int(key['amount'])/1000
            totalValores += calcium
        
        #fosforo
        if key['name']=='Phosphorus':
            fosforo =  int(key['amount'])/1000
            totalValores += fosforo
        
        #manganese
        if key['name']=='Manganese':
            manganeso =  int(key['amount'])/1000
            totalValores += manganeso
        
        #magnesium
        if key['name']=='Magnesium':
            magnesio =  int(key['amount'])/1000
            totalValores += magnesio
        
        #folate
        if key['name']=='Folate':
            folate =  int(key['amount'])/1000000
            totalValores += folate
        
        #iron
        if key['name']=='Iron':
            hierro =  int(key['amount'])/1000
            totalValores += hierro
        
        #fiber
        if key['name']=='Fiber':
            fibra =  key['amount']
            totalValores += fibra 
        
        #selenium
        if key['name']=='Selenium':
            selenio =  int(key['amount'])/1000000
            totalValores += selenio 
        
        #zinc
        if key['name']=='Zinc':
            zinc =  int(key['amount'])/1000
            totalValores += zinc 
        
        #potasium
        if key['name']=='Potassium':
            potasio =  int(key['amount'])/1000
            totalValores += potasio
        
        #VitaminA
        if key['name']=='Vitamin A':
            vitA =  key['amount']
            totalValores += vitA
            
        #VitaminC
        if key['name']=='Vitamin C':
            vitC =  key['amount']
            totalValores += vitC
        
        #VitaminD
        if key['name']=='Vitamin D':
            vitD =  key['amount']
            totalValores += vitD
        
        #VitaminE
        if key['name']=='Vitamin E':
            vitE =  key['amount']
            totalValores += vitE
        
        #VitaminK
        if key['name']=='Vitamin K':
            vitK =  key['amount']
            totalValores += vitK
    
        #VitaminB1
        if key['name']=='Vitamin B1':
            vitB1 =  key['amount']
            totalValores += vitB1
        
        #VitaminB2
        if key['name']=='Vitamin B2':
            vitB2 =  key['amount']
            totalValores += vitB2
        
        #VitaminB3
        if key['name']=='Vitamin B3':
            vitB3 = key['amount']
            totalValores += vitB3
        
        #VitaminB5
        if key['name']=='Vitamin B5':
            vitB5 = key['amount']
            totalValores += vitB5
        
        #VitaminB6
        if key['name']=='Vitamin B6':
            vitB6 =  key['amount']
            totalValores += vitB6
        
        #VitaminB12
        if key['name']=='Vitamin B12':
            vitB12 =  key['amount']
            totalValores += vitB12

    vitaminas = {'vA':vitA, 'vC':vitC, 'vD':vitD, 'vE':vitE, 'vK':vitK, 'vB1':vitB1, 'vB2':vitB2, 'vB3':vitB3, 'vB5':vitB5, 'vB6':vitB6, 'vB12':vitB12}
    bad = {'saturedFat': float(SaturedFat)/1000, 'alcohol':float(alcohol)/1000, 'cafeina':float(cafeine)/1000, 'colesterol':float(colesterol)/1000, 'fluor':float(fluor)/1000, 'azucar':float(azucar)/1000, 'sodio':float(sodio)/1000}
    good = {'cobre':float(copper)/1000, 'calcio': float(calcium)/1000, 'fosforo':float(fosforo)/1000, 'manganeso':float(manganeso)/1000, 'magnesio':float(magnesio)/1000, 'folate':float(folate)/1000, 'hierro':float(hierro)/1000, 'fibra':float(fibra)/1000, 'selenium':float(selenio)/1000, 'zinc':float(zinc)/1000, 'potasio':float(potasio)/1000, 'vitaminas':vitaminas}

    arrayDatos = {'ingrediente':data['originalName'],'idSpoon':data['id'],'calorias':float(calories)/1000,'gCal': float(calories)/1000, 'carbs':float(carbohidratos)/1000,'gCarbs':float(carbohidratos)/1000, 'proteinas':float(proteinas)/1000,'gProt':float(proteinas)/1000, 'grasas':float(fat)/1000,'gFat':float(fat)/1000, 'bad':bad, 'good':good}

    return arrayDatos

def añadirPlatoBaseValoresPrincipales(arrayDatos):

    requests.post(
    "https://api.baserow.io/api/database/rows/table/73447/?user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu",
        "Content-Type": "application/json"
    },
    json={
        "Nombre_plato": arrayDatos['receta'],
        "Link_plato_base": [
            arrayDatos['id']
        ],
        "Calorias": arrayDatos['cal'],
        "Carbohidratos": arrayDatos['carbs'],
        "Proteinas": arrayDatos['prot'],
        "Grasas": arrayDatos['fat'],
        "Sodio": arrayDatos['sod']
    }
)

def añadirPlatoPersonalizadoValoresPrincipales(arrayDatos):

    requests.post(
    "https://api.baserow.io/api/database/rows/table/73447/?user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu",
        "Content-Type": "application/json"
    },
    json={
        "Nombre_plato": arrayDatos['receta'],
        "Link_plato_pers": [
            arrayDatos['id']
        ],
        "Calorias": arrayDatos['cal'],
        "Carbohidratos": arrayDatos['carbs'],
        "Proteinas": arrayDatos['prot'],
        "Grasas": arrayDatos['fat'],
        "Sodio": arrayDatos['sod']
    }
)

def obtenerValoresBase(id):
    calorias = 0; proteinas =  0; hidratos = 0; grasas = 0; sodio = 0


    datos = requests.get(
    "https://api.baserow.io/api/database/rows/table/73447/?user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu"
    }
)
    data = datos.json()
    
    for key in data['results']:
        fgh = key['Link_plato_base']
        if key['Link_plato_base'] and key['Link_plato_base'][0]['id'] == id:
            calorias = round(float(key['Calorias']),4)
            proteinas = round(float(key['Proteinas']),4)
            hidratos = round(float(key['Carbohidratos']),4)
            grasas = round(float(key['Grasas']),4)
            sodio = round(float(key['Sodio']),4)

    return {'cal': calorias, 'prot': proteinas, 'carbs': hidratos, 'fat': grasas, 'sodio': sodio}

def obtenerValoresRecomend():
    calorias = 0; proteinas =  0; hidratos = 0; grasas = 0; sodio = 0
    
    datos = requests.get(
     "https://api.baserow.io/api/database/rows/table/73525/?user_field_names=true",
    headers={
        "Authorization": "Token LqWaspuxChsgEY5vuY4efR5z2FX5PMYu"
    }
)

    data = datos.json()
    arrayDatos = []
    val = []

    for key in data['results']:
        
        genero = key['Genero']
        calorias = key['Calorias']
        proteinas = key['Proteinas']
        hidratos = key['Carbohidratos']
        grasas = key['Grasas']
        sodio = key['Sodio']

        val = {'cal':calorias, 'prot':proteinas, 'carbs':hidratos, 'fat':grasas, 'sod':sodio }

        arrayDatos.append({'genero':genero, 'val': val})


    return arrayDatos

def basePercentage(valoresBase, valoresRecomend):
    calorias = 0; proteinas =  0; hidratos = 0; grasas = 0; sodio = 0

    perR = 50    
    
    h = {
     'cal':int((float(valoresBase['cal'])*float(perR))/float(valoresRecomend[0]['val']['cal'])),
     'prot':int((float(valoresBase['prot'])*float(perR))/float(valoresRecomend[0]['val']['prot'])), 
     'carbs':int((float(valoresBase['carbs'])*float(perR))/float(valoresRecomend[0]['val']['carbs'])), 
     'fat':int((float(valoresBase['fat'])*float(perR))/float(valoresRecomend[0]['val']['fat'])), 
     'sod':int((float(valoresBase['sodio'])*float(perR))/float(valoresRecomend[0]['val']['sod'])) 
     }

    m = {
     'cal':int((float(valoresBase['cal'])*float(perR))/float(valoresRecomend[1]['val']['cal'])),
     'prot':int((float(valoresBase['prot'])*float(perR))/float(valoresRecomend[1]['val']['prot'])), 
     'carbs':int((float(valoresBase['carbs'])*float(perR))/float(valoresRecomend[1]['val']['carbs'])), 
     'fat':int((float(valoresBase['fat'])*float(perR))/float(valoresRecomend[1]['val']['fat'])), 
     'sod':int((float(valoresBase['sodio'])*float(perR))/float(valoresRecomend[1]['val']['sod']))
     }

    return {'h':h, 'm':m}
    
#607449100


        