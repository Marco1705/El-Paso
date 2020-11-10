import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import statistics

front = pd.read_csv('fronteras.csv')
is_mex = front["Border"] == "US-Mexico Border"
is_tx = front["Port Name"] == "El Paso"
is_ped = front["Measure"] == "Pedestrians"
front["Date"] = pd.to_datetime(front["Date"], format="%m/%d/%Y")
is_year = front["Date"].dt.strftime("%Y").isin(["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"])
is_enero = front["Date"].dt.strftime("%m") == "01"
is_sum = sum(front["Value"])
frame1 = front[is_tx & is_mex & is_ped & is_year]

x1 = frame1["Date"]
y1 = frame1["Value"]
plt.plot(x1,y1)
plt.show()

anio = ["01","02","03","04","05","06","07","08","09","10","11","12"]
def pregunta0(mes, ano):
    is_ano = frame1['Date'].dt.strftime('%Y') == ano
    is_mes = frame1["Date"].dt.strftime("%m").isin(mes)
    frame2 = frame1[is_ano & is_mes]
    suma_value = frame2["Value"].sum()
    ##print(suma_value)
    ##print(cuadro_descrip)

pregunta0(anio,"2000")
pregunta0(anio,"2001")
pregunta0(anio,"2002")
pregunta0(anio,"2003")
pregunta0(anio,"2004")
pregunta0(anio,"2005")
pregunta0(anio,"2006")
pregunta0(anio,"2007")
pregunta0(anio,"2008")
pregunta0(anio,"2009")
pregunta0(anio,"2010")
pregunta0(anio,"2011")
pregunta0(anio,"2012")
pregunta0(anio,"2013")
pregunta0(anio,"2014")
pregunta0(anio,"2015")
pregunta0(anio,"2016")
pregunta0(anio,"2017")
pregunta0(anio,"2018")
pregunta0(anio,"2019")
##print(frame1)
##cuadro_descrip = frame1.describe()
##print(cuadro_descrip)


##EJERCICIO 2##

def pregunta1(mes, ano):
    is_ano = frame1['Date'].dt.strftime('%Y').isin(ano)
    is_mes = frame1["Date"].dt.strftime("%m") == mes
    frame2 = frame1[is_ano & is_mes]
    cuadro_descrip = frame2.Value.mean()
    ##print(mes)
    ##print(cuadro_descrip)

lista1 = ['2000' , '2001', '2002', '2003', '2004']
lista2 = ['2005', '2006', '2007', '2008', '2009']
lista3 = ['2010', '2011', '2012', '2013', '2014']
lista4 = ['2015', '2016', '2017', '2018']


#Primeros 5 años
##print('2000 - 2004')
pregunta1('01', lista1)
pregunta1('02', lista1)
pregunta1('03', lista1)
pregunta1('04', lista1)
pregunta1('05', lista1)
pregunta1('06', lista1)
pregunta1('07', lista1)
pregunta1('08', lista1)
pregunta1('09', lista1)
pregunta1('10', lista1)
pregunta1('11', lista1)
pregunta1('12', lista1)
#segundos 5 años
##print('2005 - 2009')
pregunta1('01', lista2)
pregunta1('02', lista2)
pregunta1('03', lista2)
pregunta1('04', lista2)
pregunta1('05', lista2)
pregunta1('06', lista2)
pregunta1('07', lista2)
pregunta1('08', lista2)
pregunta1('09', lista2)
pregunta1('10', lista2)
pregunta1('11', lista2)
pregunta1('12', lista2)
#terceros 5 años
##print('2010 - 2014')
pregunta1('01', lista3)
pregunta1('02', lista3)
pregunta1('03', lista3)
pregunta1('04', lista3)
pregunta1('05', lista3)
pregunta1('06', lista3)
pregunta1('07', lista3)
pregunta1('08', lista3)
pregunta1('09', lista3)
pregunta1('10', lista3)
pregunta1('11', lista3)
pregunta1('12', lista3)
#ultimos 4 años
##print('2015 - 2018')
pregunta1('01', lista4)
pregunta1('02', lista4)
pregunta1('03', lista4)
pregunta1('04', lista4)
pregunta1('05', lista4)
pregunta1('06', lista4)
pregunta1('07', lista4)
pregunta1('08', lista4)
pregunta1('09', lista4)
pregunta1('10', lista4)
pregunta1('11', lista4)
pregunta1('12', lista4)

##is_year_5 = front["Date"].dt.strftime("%Y").isin(["2000","2001","2002","2003","2004","2005"])
##is_enero_5 = front["Date"].dt.strftime("%m") == "01"
##frame_en5 = front[is_tx & is_mex & is_ped & is_year_5 & is_enero_5]
##promedio_enero = frame_en5["Value"].mean()

##plt.plot(x1,y1)
##plt.show()

##EJERICCIO 3##

ultimos_10 = front["Date"].dt.strftime("%Y").isin(["2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"])
frame_3 = front[is_tx & is_ped & ultimos_10]
mediana = statistics.median(frame_3["Value"])
##print(frame_3)
frame3_des = frame_3.describe()
##print(frame3_des)
##print("Mediana", mediana)
centro = (frame3_des["Value"].max()-382224)/2
##print("Centro de Rango", centro)
Media_recortada = (frame3_des["Value"].sum()-382224-422575-794407-730640)/132
##print("Media Recortada ", Media_recortada)