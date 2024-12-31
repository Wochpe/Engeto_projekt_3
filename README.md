# Engeto_project_3
The third project in the Python Academy by Engeto.

## Project Description
This project is designed to extract the results of the parliamentary elections in 2017. You can find the link to view it <[here](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)>.

## Installation of Libraries
The libraries used in the code are stored in the requirements.txt file.
It is recommended to install a new virtual environment and run the following command with the installed manager pip3:
```
$ pip3 --version                      # check the version of the manager
$ pip3 install -r requirements.txt    # install the libraries
```

## Running the Project
Running the election_scraper.py file from the command line requires two mandatory arguments.
As a result, you will get a file named by you with the election results and a .csv extension.

## Project Example
Voting results for the Mladá Boleslav district::
1. Argument ```https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2107```
2. Argument ```vysledky_MB.csv```

## Running the program:
```
python election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2107" "vysledky_MB.csv"
```
## Download progress:
```
DOWNLOADING DATA FROM SELECTED URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2107
SAVING TO FILE: results_MB.csv
EXITING election_scraper
```
## Partial output::
```
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
535427,Bakov nad Jizerou,3 922,2 551,2 539,285,3,3,204,1,179,153,27,32,36,2,1,252,2,2,113,864,1,8,42,2,18,4,6,295,4
535443,Bělá pod Bezdězem,3 805,2 219,2 204,215,2,0,214,1,107,153,28,33,33,4,4,218,3,4,61,802,3,3,38,0,9,8,7,253,1
...
```
