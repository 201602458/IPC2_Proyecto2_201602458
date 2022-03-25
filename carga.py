import os
import re
import matriz
#import xml.etree.ElementTree as ET
from xml.dom import minidom

class Carga_archivo:
    var=matriz.matriz()

    def archivoCarga(self, link):
        try:
            self.txt = minidom.parse(link)#aqui se pone el self.link

        except:
            print("Error en el archivo XML")
        
        
    def cargaCiudad(self, nombre):
        etqCiudad = self.txt.getElementsByTagName('nombre')
        #nameCiudad= etqCiudad[0].attributes['codigo'].value

        for j in range(len(etqCiudad)):
            nameCiudad= etqCiudad[j].childNodes[0].nodeValue
            if(nombre == nameCiudad):
                print(nameCiudad)

                filas = etqCiudad[j].attributes['filas'].value
                columnas = etqCiudad[j].attributes['columnas'].value
                self.var.crear(filas,columnas)
                
                print(filas)
                print(columnas)

            
        #print(nombre)
        #print(etqCiudad)
        #print(nameCiudad)

    def cargarPatrones(self, ciudad, robot):
        patron = self.txt.getElementsByTagName('patron')#patron

        #for j in patron:

      