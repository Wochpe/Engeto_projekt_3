# Engeto_projekt_3
Třetí projekt na Python Akademii od Engeta.

## Popis projektu
Tento projekt slouží k extrahování výsledků parlamentních voleb v roce 2017. Odkaz k prohlédnutí naleznete <[zde](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)>.

## Instalace knihoven
Knihovny, které jsou v kódu použity, jsou uložené v souboru requirements.txt. Pro instalaci je doporučeno nainstalovat
nové virtuální prostředí a s nainstalovaným managerem pip spustit následujícím způsobem:

## Spuštění projektu
Spuštění souboru election_scraper.py v rámci příkazového řádku vyžaduje dva povinné argumenty.

Jako výsledek získáte vámi pojmenovaný soubor s výsledky voleb a příponou .csv.

## Ukázka projektu
Výsledky hlasování pro okres Mladá Boleslav:
- 1. Argument "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2107"
- 2. Argument "vysledky_MB.csv"

Spuštění programu:
> python election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2107" "vysledky_MB.csv"

Průběh stahování:
>STAHUJI DATA Z VYBRANÉHO URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2107
>UKLÁDÁM DO SOUBORU: vysledky_MB.csv
>UKONCUJI election_scraper

Částečný výstup:
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
535427,Bakov nad Jizerou,3 922,2 551,2 539,285,3,3,204,1,179,153,27,32,36,2,1,252,2,2,113,864,1,8,42,2,18,4,6,295,4
535443,Bělá pod Bezdězem,3 805,2 219,2 204,215,2,0,214,1,107,153,28,33,33,4,4,218,3,4,61,802,3,3,38,0,9,8,7,253,1
...
