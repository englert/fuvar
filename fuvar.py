'''fuvar.csv
taxi_id,  indulas,             idotartam, tavolsag, viteldij, borravalo, fizetes_modja
  0         1                     2         3         4          5           6
5240;     2016-12-15 23:45:00;   900;       2,5;     10,75;     2,45;     bankkártya               
'''
with open('fuvar.csv', 'r', encoding = 'utf-8-sig') as f:
    fejléc = f.readline()
    lista   = [ sor.strip().replace(',','.').split(';') for sor in f ]

# 3. Hány utazás van?

print( f"3. feladat: {len(lista)} fuvar")

# 4. a 6185-ös azonosítójú taxisnak mennyi volt a bevétele, és ez hány fuvarból állt?

bevétel =[float(sor[4]) + float(sor[5])  for sor in lista if sor[0] == '6185']
print( f"4. feladat: {len(bevétel)} fuvar alatt: {str(sum(bevétel)).replace('.',';')} $")

# 5. határozza meg a fizetési módokat,  az egyes fizetési módokat hányszor választották az utak során?

fizetési_módok = { sor[6] for sor in lista }
fuvar = [sor[6] for sor in lista]
print('5. feladat:')
x = [print(f"{'':>8}{sor}: {fuvar.count(sor)} fuvar") for sor in fizetési_módok]

# 6. Összesen hány km-t tettek meg a taxisok 2 tizedes pontossággal (1 mérföld 1,6 km)

km = [ float(sor[3]) for sor in lista ]
print(f'6. feladat:{sum(km)*1.6:.2f} km')

# 7. az időben leghosszabb fuvar adatai:
i = max([ (int(sor[2]), i) for i, sor in enumerate(lista) ])[1]
időtartam = lista[i][2]
taxi_id   = lista[i][0]
távolsag  = 1.6 * float(lista[i][3])
viteldíj  = lista[i][4]

print("7. feladat: Leghosszabb")
print(f"        Fuvar hossza: {időtartam} másodperc")
print(f"        Taxi azonosító: {taxi_id} ")
print(f"        Megtett távolság: {távolsag:.2f} km ")
print(f"        Viteldíj: {viteldíj} $")

'''
8. Hozzon létre hibak.txt néven egy UTF-8 kódolású szöveges állományt.
Hibás sornak tekintjük azokat az eseteket, amelyekben az utazás időtartama és a viteldíj egy nullánál nagyobb érték,
de a hozzá tartozó megtett távolság értéke nulla.
A sorok indulási időpont szerint növekvő rendben legyenek az állományban!
'''
print( "8. feladat: hibak.txt" )
with open('fuvar.csv', 'r', encoding = 'utf-8-sig') as file:
    elsosor    = file.readline()
    fuvarlista = [ sor for sor in file ]
    
with open('hibak.txt', 'w', encoding = 'utf-8') as output:
     output.writelines(elsosor)
     hiba = [ (sor[1], i) for i, sor in enumerate(lista) if (sor[2] !='0' and sor[4] != '0.0') and sor[3] =='0.0' ]
     hiba.sort()
     [ print(fuvarlista[sor[1]], file=output, end='') for sor in hiba ]



