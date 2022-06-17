from django.db import models

class NumValueReceta(models.Model):
    
    receta = models.CharField(max_length=50, default='')
    idSpoon = models.CharField(max_length=50, default='')
    servings = models.CharField(max_length=50, default='')
    carbohidratos = models.CharField(max_length=30)
    proteinas = models.CharField(max_length=30)
    grasas = models.CharField(max_length=30)
    kcal = models.CharField(max_length=30)
    saturedFat = models.CharField(max_length=30)
    colesterol = models.CharField(max_length=30)
    alcohol = models.CharField(max_length=30)
    cafeina = models.CharField(max_length=30)
    cobre = models.CharField(max_length=30)
    calcio = models.CharField(max_length=30)
    fluor = models.CharField(max_length=30)
    vitA = models.CharField(max_length=30)
    vitB1 = models.CharField(max_length=30)
    vitB2 = models.CharField(max_length=30)
    vitB3 = models.CharField(max_length=30)
    vitB5 = models.CharField(max_length=30)
    vitB6 = models.CharField(max_length=30)
    vitB12 = models.CharField(max_length=30)
    vitC = models.CharField(max_length=30)
    vitD = models.CharField(max_length=30)
    vitE = models.CharField(max_length=30)
    vitK = models.CharField(max_length=30)
    fibra = models.CharField(max_length=30)
    hierro = models.CharField(max_length=30)
    magnesio = models.CharField(max_length=30)
    manganeso = models.CharField(max_length=30)
    fosforo = models.CharField(max_length=30)
    potasio = models.CharField(max_length=30)
    selenio = models.CharField(max_length=30)
    sodio = models.CharField(max_length=30)
    azucar = models.CharField(max_length=30)
    zinc = models.CharField(max_length=30)


class NumValueIngrediente(models.Model):

        Nombre = models.CharField(max_length=30)
        IdSpoon = models.CharField(max_length=30)
        Carbohidratos = models.CharField(max_length=30)
        Proteinas = models.CharField(max_length=30)
        Grasas = models.CharField(max_length=30)
        Kcal = models.CharField(max_length=30)
        Alcohol = models.CharField(max_length=30)
        Cafeina = models.CharField(max_length=30)
        Cobre = models.CharField(max_length=30)
        Calcio = models.CharField(max_length=30)
        Colesterol = models.CharField(max_length=30)
        Fluor = models.CharField(max_length=30)
        SaturedFat = models.CharField(max_length=30)
        VitA = models.CharField(max_length=30)
        VitC = models.CharField(max_length=30)
        VitD = models.CharField(max_length=30)
        VitE = models.CharField(max_length=30)
        VitK = models.CharField(max_length=30)
        VitB1 = models.CharField(max_length=30)
        VitB2 = models.CharField(max_length=30)
        VitB3 = models.CharField(max_length=30)
        VitB5 = models.CharField(max_length=30)
        VitB6 = models.CharField(max_length=30)
        VitB12 = models.CharField(max_length=30)
        Fibra = models.CharField(max_length=30)
        Folato = models.CharField(max_length=30)
        AcFolico = models.CharField(max_length=30)
        Hierro = models.CharField(max_length=30)
        Magnesio = models.CharField(max_length=30)
        Manganeso = models.CharField(max_length=30)
        Fosforo = models.CharField(max_length=30)
        Potasio = models.CharField(max_length=30)
        Selenio = models.CharField(max_length=30)
        Sodio = models.CharField(max_length=30)
        Azucar = models.CharField(max_length=30)
        Zinc = models.CharField(max_length=30)