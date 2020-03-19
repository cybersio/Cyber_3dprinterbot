#import sys

import datetime
i = datetime.datetime.now()
print("PREVENTIVO DI STAMPA DEL %s/%s/%s" %(i.day, i.month, i.year))

#time_design = float(input("How many hours for design? (0 if not)"))
#part = int(input("How many print? "))
#material = input("MATERIALE USATO (PLA, PETG, ABS, TPU) ")
cost_k = float(input("COSTO MATERIALE AL KG "))
grams = float(input("GRAMMI USATI "))
electricity = float(input("COSTO ELETTR./ORA "))
hours = float(input("ORE DI STAMPA "))
profit = float(input("PERCENTUALE PROFITTO "))

#spool_grams = 1000
#cost_k = 0
#electricity = 0
#init = 3
#postproduction = 2
#profit = 1

#if(material == "PLA"):
#    electricity = 0.05
#elif (material == "PETG"):
#    electricity = 0.06
#elif (material == "TPU"):
#    electricity = 0.06
#elif(material == "ABS"):
#    electricity = 0.08
#else:
#    print ("insert a correct material (PLA, PETG, ABS, FLEX)")
#    sys.exit()

maintenance = (((electricity * hours) * 20) / 100);
final_cost = ((electricity * hours) + ((cost_k / 1000) * grams) + maintenance) * (profit /100);

#print('MATERIALE: ', material)
print('ORE: ', hours)
print('GRAMMI: ', grams)
print('COSTO ELETTRIC.: ', electricity * hours, '€')
print('USURA', maintenance, '€')
print('PERC. PROFITTO', profit, '%')
print('MATERIALE: ', (cost_k / 1000) * grams, '€')

#print('POSTPRODUCTION: ', postproduction * part, '€')
#print('PRINT FILE PREPARATION', init, '€')
print('FINAL COST: ', (final_cost), '€')

file = open("preventivo.txt", "w")
file.close()

file = open("preventivo.txt", "a")
file.write("\t\tPREVENTIVO DEL %s/%s/%s" %(i.day, i.month, i.year))

#if(time_design != 0):
#    file.write("\n\nCosto progettazione oggetti: ");
#    file.write(str(time_design * 10));
#    file.write("€")
    
#file.write("\n\nCosto preparazione file di stampa: ")
#file.write(str(part * init));
#file.write("€")

#file.write("\n\nNumero di oggetti stampati: ");
#file.write(str(part))


file.write("\n\nMateriale utilizzato: ")
file.write(material)

file.write("\n\nOre totali di stampa: ")
file.write(str(hours))

#file.write("\n\nCosto materiale: ")
#file.write(str(int(cost_k * grams * 2)))
#file.write("€")


#file.write("\n\nCosto post produzione totale: ")
#file.write(str(postproduction * part))
#file.write("€")

file.write("\n\nCOSTO FINALE (comprende costi di manutenzione e consumi): ")
file.write(str(int(final_cost)))
file.write("€")

file.write("\n\n\t\t\t\t\t\t 3d_printall")

file.close();
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 01:56:23 2020

@author: Carlo
"""

