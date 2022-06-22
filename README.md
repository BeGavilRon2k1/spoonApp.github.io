# spoonApp.github.io

## "Parrillada Cercana"
This is a project, created by 3.14, born to give people cheaper options to obtain food, working together with local commerce and agriculture to obtain products with a lower cost and the subsequent sale at a similar price.



**Table of Contents**

[TOC]

###Authors

***3.14 Financial Contents***

###Urls funcionales

*  " " : redirects to the main template.

* '**añadir/baserow/< str : addid >**' : in case you have to add a recipe from the spoonacular page.

* '**añadir/base**' : add the values of a base plate

* '**añadir/personalized**' : add the values of a custom

* '**home**' : goes to the main

* '**home/< str : busca >**' : look for plates (for now only in the base ones)

* '**all**' : shows the main page with all base plates

###Views

* **databaseBaserow** : takes care of adding recipes and ingredients to baserow

* **baserowToDjangoIngredSolid** : handles solid ingredients

* **baserowToDjangoIngredLiquid** : handles liquid ingredients

* **ingredientes** : takes care of adding the ingredients to baserow or django

* **databaseDjango** : takes care of adding recipes and ingredients to django

* **home y homeAll** : go to the main page

* **datosTemplate** : get the data

* **datosPlato** :  shows the data of the selected dish

* **getIngredientePlatoBaseLink** : obtains the ingredients of the basic dishes

* **getIngredientePlatoPersonalizadoLink** : obtains the ingredients of the personalized dishes

###Models

* **NumValueReceta** : is responsible for mounting the database with the table for the recipe values

* **numvalueingrediente** : is in charge of assembling the database with the table for the values of the ingredients that are going to form the recipes

####End
