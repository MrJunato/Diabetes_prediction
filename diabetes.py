#Bloco de importação
##########################
import random            #
from sklearn import tree #
##########################

#Criação da matriz de pacientes e da matriz com os tipos de diabetes que é nossa variável resposta
pacientes = []
tipos = []

for i in range(1501):
    sexo = random.choice(["Homem", "Mulher"])
    #print("sexo: ", sexo)

    #Transformar homem no número 1 e mulher no número 0
    if sexo == "Homem":
        sexo = 1
    else:
        sexo = 0

    idade = random.randint(5,90)
    #print("idade: ", idade)

    hdl = random.randint(15,150)
    #print("hdl: ", hdl)

    hipertensao = bool(random.getrandbits(1)) #Se existe alguém com hipertensao na familia
    #print("hipertensao: ", hipertensao)

    ldl = random.randint(30,220)
    #print("ldl: ", ldl)

    glicose = random.randint(25,350)
    #print("glicose: ", glicose)

    familia_diabetes = bool(random.getrandbits(1)) #se existe alguém do diabetes na família
    #print("diabetes na familia: ", familia_diabetes)

    trigliceride = random.randint(50,700)
    #print("trigliceride: ", trigliceride)

    glicada = round(random.uniform(3,15),3)
    #print("glicada: ", glicada)

    #Definir altura
    if idade < 10:
        altura = random.randint(100,130)
    elif idade < 15:
        altura = random.randint(130, 170)
    elif idade >= 15:
        altura = random.randint(150,200)
    #print("altura: ", altura)

    #definir peso
    if altura < 130:
        peso = random.randint(20,48)
    elif altura < 140:
        peso = random.randint(27, 60)
    elif altura < 160:
        peso = random.randint(35, 80)
    elif altura >= 160:
        peso = random.randint(45,180)
    #print("peso: ", peso)

    #definir IMC
    imc = round((peso/(altura**2))*10000,3)
    #print("imc: ", imc)

    #DEFINIR TIPO DE DIABETES
    if glicose >= 126 and glicada >= 6.5 and idade <= 20:
        tipo_diabetes = "Diabetes tipo 1"
    elif glicose >= 126 and glicada >= 6.5 and idade >= 20:
        tipo_diabetes = "Diabetes tipo 2"
    else:
        tipo_diabetes = "Sem diabetes"
    #print("tipo de diabete: ", tipo_diabetes)

    paciente = [sexo,familia_diabetes,idade,altura,peso,imc,hdl,ldl,glicose,glicada,trigliceride,hipertensao]

    #Incluir o tipo de diabete do paciente gerado na matriz de tipo de diabates
    tipos.append(tipo_diabetes)

    #Incluir o paciente gerado na matriz de pacientes
    pacientes.append(paciente)

    print(i)
    print(paciente)

#print(pacientes)
#print(tipos)

#Utilizando o modelo de árvore de decisão para pacientes e tipos de diabetes
modelo = tree.DecisionTreeClassifier()
modelo.fit(pacientes, tipos)

#criando um novo paciente
novo = ["Homem",True,15,197,169,43.547,55,137,172,7.328,304,True]

# Transformar homem no número 1 e mulher no número 0
if novo[0] == "Homem":
    novo[0] = 1
else:
    novo[0] = 0

novo = tuple(novo) #Transforma a lista [] em tupla ()
novo = [novo] #Coloca a nova tupla dentro de uma lista para formar uma matriz [()]

#Prevendo se o paciente têm diabetes ou não
previsao = modelo.predict(novo)
print("\n\n------------------------------------------------------------------------------------------------------")
print("\nNovo paciente:", novo)
print("\nResultado da previsão: %s" % previsao)