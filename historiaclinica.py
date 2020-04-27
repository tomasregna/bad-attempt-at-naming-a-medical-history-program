#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
var = input("Please enter something: ")
print("You entered: " + var)

#%%
#print 'hi'

#orden = raw_input('Saludame:')
#print orden

test1={'a': 'a', 'A': 'a', 'a.': 'a', 'A.': 'a',
       'b': 'b', 'B': 'b', 'b.': 'b', 'B.': 'b',
       'c': 'c', 'C': 'c', 'c.': 'c', 'C.': 'c',
       'd': 'd', 'D': 'd', 'd.': 'd', 'D.': 'd',
       'e': 'e', 'E': 'e', 'e.': 'e', 'E.': 'e',
       'f': 'f', 'F': 'f', 'f.': 'f', 'F.': 'f',
       'g': 'g', 'G': 'g', 'g.': 'g', 'G.': 'g',
       'h': 'h', 'H': 'h', 'h.': 'h', 'H.': 'h'}
#       '': '', '': '', '.': '', '.': '',}

test2={'a':'hola',
       'b':'que',
       'c':'tal',
       'd':'tu',
       'e':'como',
       'f':'estas',
       'g':'dime',
       'h':'si'}

#letra=test1.get('A.')
#test2.get(letra)

#print len(test2)

#var='123'
#print '0'+var
#print var+'0'

#listita= {'1':'maria jeje', '2': 'carol j', '3': 'poopity scoop'}
#ene=len(listita)
#listita[str(ene+1)]='el retutu'
#print listita
#%%
import json

with open('registro.lst', 'w') as fp:
    data={"Nombre y Apellido": ["Oswaldo Mobray"],
          "DNI": ["31330334"],
          "Nacimiento": ["15/15/2015"],
          "Obra Social": ["Sans"],
          "Nro. Afiliado":["p3n3-1234"],
          "Teléfono":["4444 1234"],
          "Mail": ["comicsansXD@equisde.com.gov.tetas"],
          "Registro":[1]}
    json.dump(data, fp, sort_keys=False)
#%%
import json

with open('registro.lst', 'r') as fp:
    data = json.load(fp)

#%%
import json

with open('registro.lst','r') as fp:
    datinis=json.load(fp)
    datinis["Nombre y Apellido"].append("Miguel Thegame")

with open('registro.lst','w') as fpp:
    json.dump(datinis, fpp)
    
    '''
    FUNCIONAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    '''

#%%
import os

def indent():
    print ''

def limpiar():
    os.system('clear')
    

def AgregarPaciente():
    var=[]
    var.append(raw_input('Nombre y apellido:'))
    var.append(raw_input('DNI:'))
    var.append(raw_input('Fecha de nacimiento:'))
    var.append(raw_input('Obra social:'))
    var.append(raw_input('N. afiliado:'))
    var.append(raw_input('Telefono:'))
    var.append(raw_input('Mail:'))
    
    import json
    
    print var
    
    if not os.path.exists('registro.lst') :
        open('registro.lst', 'a').close()        
        with open('registro.lst', 'w') as fp:
            data=[[],[],[],[],[],[],[]]
            json.dump(data, fp, sort_keys=False)
            fp.close()


    with open('registro.lst','r') as fp:
        data1=json.load(fp)
        fp.close()

    print data1

    with open('registro.lst','w') as fp:
        for x in var:
            print var.index(x)
            #data1[var.index(x)].append(var[x])
            #print data1[var.index(x)]
        #json.dump(data, fp)
        fp.close()
    #print 'probemos algo...'
    #ccc=raw_input('deci hola:')
    #print ccc


menuletras={'a': 'a', 'A': 'a', 'a.': 'a', 'A.': 'a',
            'b': 'b', 'B': 'b', 'b.': 'b', 'B.': 'b',
            'c': 'c', 'C': 'c', 'c.': 'c', 'C.': 'c',
            'd': 'd', 'D': 'd', 'd.': 'd', 'D.': 'd',
            'e': 'e', 'E': 'e', 'e.': 'e', 'E.': 'e',
            'f': 'f', 'F': 'f', 'f.': 'f', 'F.': 'f',
            'g': 'g', 'G': 'g', 'g.': 'g', 'G.': 'g',
            'h': 'h', 'H': 'h', 'h.': 'h', 'H.': 'h',
            'i': 'i', 'I': 'i', 'i.': 'i', 'I.': 'i',
            'j': 'j', 'J': 'j', 'j.': 'j', 'J.': 'j'}

menu={'a': AgregarPaciente,
      'b': 'aaa',
      'c': 'aaaaaa',
      'd': 'aaaaaaaaaaaa',
      'e': 'aaaaaaaaaaaaaaaaaa',
      'f': 'aaaaaaaaaaaaaaaa',
      'g': 'aaaaaaaaaaaaaa',
      'h': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
      'i': 'aaaaaaaaaaaaaaaa',
      'j': 'aaa'}


#%%
def Main():
    limpiar()
    print '------------------------------------------------'
    indent()
    print 'Bienvenida a Historia Clínica v1.0.0'
    indent()
    print 'Seleccione alguna de las siguientes opciones:'
    indent()
    print 'A. Cargar datos paciente'
    print 'B. Consulta del día'
    print 'C. Ver historia clínica'
    print 'D. Ver listado'
    print 'E. Ver antecedentes'
    print 'F. Modificar datos paciente'
    print 'G. Modificar antecedentes'
    print 'H. Descargar historia clínica'
    print 'I. Backup'
    print 'J. Salir'
    indent()
    orden = raw_input('Seleccion:')

    letra=menuletras.get(orden)

#print menu.get(letra)

    menu[letra]()

#%%
import os

os.chdir('/home/intel/Desktop/Historia_Clinica')
while True:
    Main()



#%%
