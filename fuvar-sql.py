#taxi_id;    indulas;        idotartam;    tavolsag;    viteldij;    borravalo;    fizetes_modja
#   0          1                  2             3            4            5               6
#5240;   2016-12-15 23:45:00;   900;          2,5;        10,75;        2,45;        bankkártya

import sqlite3

def sql(sql_parancs, *args):
    c.execute(sql_parancs, *args)
    return c.fetchall()

conn = sqlite3.connect('fuvar.db')
c = conn.cursor()

sql(" DROP TABLE IF EXISTS fuvar ")
sql("""
    CREATE TABLE IF NOT EXISTS fuvar
    (taxi_id      INTEGER,
    indulas       TEXT,
    idotartam     INTEGER,
    tavolsag      REAL,
    viteldij      REAL,
    borravalo     REAL,
    fizetes_modja TEXT)
""")
conn.commit()

with open('fuvar.csv', encoding='utf-8-sig') as f:
    fejléc = f.readline().strip()
    for sor in f:
        sql( "INSERT INTO fuvar VALUES (?,?,?,?,?,?,?)",  ( sor.strip().replace(',','.').split(';'))   )

conn.commit()

#3. Hány utazás volt?
fuvarok_száma = sql(" SELECT count() FROM  fuvar ")[0][0]     
print( f'3. feladat: {fuvarok_száma} fuvar' )

#4. A 6185-ös taxinak mennyi a bevétele és ez hány fuvarból állt?
bevétel = sql(" SELECT SUM(viteldij+borravalo) FROM  fuvar WHERE taxi_id = 6185 ")[0][0]
print( f'4. feladat: 4 fuvar alatt: { bevétel }$' )

#5. Milyen fizetési módok vannak és ezeket hányszor használták?
res = sql(" SELECT fizetes_modja,  COUNT(*)  FROM fuvar  GROUP BY fizetes_modja ")   
print(   f'5.feladat:' )
[ print( f'       { i[0] }: { i[1] } fuvar') for i in res ]

#6. Összesen hány kilómétert tettek meg a taxisok? (1 mérföld: 1.6 kn) 2 tizedesre kerekítve.
összes_út = sql(" SELECT SUM(tavolsag)  FROM fuvar ")[0][0]  
print( f'6. feladat: { összes_út*1.6:.2f}km' )

#7. A leghosszabb fuvar adatai?
res = sql(" SELECT MAX(idotartam), taxi_id, tavolsag, viteldij  FROM fuvar ")[0]  
maxi, taxi_id, tavolsag, viteldij = res
print( f'7. feladat: Leghosszabb fuvar:')
print( f'        Fuvar hossza: {maxi} másodperc')
print( f'        Taxi azonosító: {taxi_id}')
print( f'        Megtett távolság: {tavolsag} km')
print( f'        Viteldíj: {viteldij}$')

#8. Hiba: idtartam nagyobb mint nulla és viteldij nagyobb mint nulla és a tavolsag egyenlő nulla.
#   ezeket az utazásokat írja ki egy hibak.txt fájlba az eredeti formátumban.
print(   f'8. feladat: hiba.txt')
hibás = sql("SELECT *  FROM fuvar WHERE idotartam >0 AND viteldij>0 AND tavolsag ==0 ORDER BY indulas ")   

with open( 'hibak.txt', 'w', encoding='utf-8') as f:
    print(fejléc, file = f)
    [ print( f'{ h[0] };{ h[1] };{ h[2] };{ h[3] };{ h[4] };{ h[5] };{ h[6] }', file=f ) for h in hibás ]



