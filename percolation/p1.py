import itertools
def numAllPercs(table, numStreams):
    f = lambda tab: filter(lambda i: tab[0][i] == " ", range(len(tab[0]))) # vzemi indekse stolpcev, ki se ne zacnejo z X
    g = lambda tab,nS: itertools.combinations(f(tab),nS) # seznam kombinacij stolpcev
    # krn sprejme seznam tabel od starta, ki so zmergani skupaj, zato jih grupira po len(tabel) skupaj, da dobimo seznam pravih tabel
    krn = lambda t,k: map(lambda x,t=t,k=k: t[x:x+k],range(0,len(t),k))
    get_next = lambda tab,id: [lambda tab=tab,id=id: krn(start(tab,id,0),len(tab)),lambda:[]][(tab[0][id] != " ")]()
    dirs = lambda x,gl,tab: [x != 0 and tab[gl][x-1] == " ", len(tab) > gl+1 and tab[gl+1][x] == " " or len(tab) == gl+1, x != len(tab[0])-1 and tab[gl][x+1] == " "]
    fun = lambda c,i,tabs: [lambda c=c,i=i,tabs=tabs: fun(c,i+1,reduce(lambda x,y: x+y,map(lambda x,c=c,i=i,tabs=tabs: get_next(x,c[i]),tabs))), lambda tabs=tabs: len(tabs)][(i == len(c) or not tabs)]()
    # start: vzame tabelo, stolpec in vrstico: v tocki pregleda mozne smeri z dirs, oznaci trenutno tocko z X in se rekurzivno premakne v mozne smeri
    # ce smer ni mozna, vrni [], ce prides do n+1 vrstice, pomeni, da si prisel do dna in vrni trenutno tabelo
    # dobljene tabele iz vseh moznih smeri sestej skupaj
    start = lambda tab,fk,gl: [lambda tab=tab,fk=fk,gl=gl: [lambda: [], lambda tab=tab,fk=fk,gl=gl: start(tab[:gl]+[tab[gl][:fk]+"X"+tab[gl][fk+1:]]+tab[gl+1:],fk-1,gl)][(dirs(fk,gl,tab)[0])]()\
                                                         + [lambda: [],lambda tab=tab,fk=fk,gl=gl: start(tab[:gl]+[tab[gl][:fk]+"X"+tab[gl][fk+1:]]+tab[gl+1:],fk,gl+1)][(dirs(fk,gl,tab)[1])]()\
                                                         + [lambda: [],lambda tab=tab,fk=fk,gl=gl: start(tab[:gl]+[tab[gl][:fk]+"X"+tab[gl][fk+1:]]+tab[gl+1:],fk+1,gl)][(dirs(fk,gl,tab)[2])](),
                                                            lambda: tab][(gl == len(tab))]()
    # vrni 0, ce numstreams 0, sicer za vsako kombinacijo klici fun, ki vrne stevilo pretokov in na koncu rezultate sestej
    # fun sprejme kombinacijo zacetnih stolpcev, stevilo zaporednega stolpca v kombinaciji, in seznam tabel z oznacenimi pretoki, ki se zacnejo s stolpcem s predhodno zap stevilko
    # za vsako posodobljeno tabelo v seznamu najde seznam tabel s pretoki, ki se zacnejo v dolocenem stolpcu in se ta ne zacne z X (start predpostavi, da ni X v prvi vrsti)
    # seznam seznamov tabel z reduce oblikuje v seznam tabel, s katerim se fun rekurzivno klice (poleg kombinacije in i-tega stolpca kombinacije)
    # ko se klice z n+1 stolpcem kombinacije, je fun pregledal stevilo moznih pronicanj n tokov in vrne dolzino seznama tabel (ki je parameter)
    # prav tako vrne dolzino (= 0), ce se med rekurzivnim filtriranjem tabel seznam ze prej izprazni
    return [lambda: 
		0, lambda table=table,numStreams=numStreams: 
			sum(map(
				lambda comb,table=table: 
					fun(comb,1,krn(start(table,comb[0],0),len(table))),g(table,numStreams))
			)
		][(numStreams > 0)]()


test1 = ["  X  X XX",
         " X  XX  X",
         " X XX   X",
         "    X X  ",
         "  X X    "]
test0 = ["X   X ", "XX  X "]
test2 = ["  X  X XX  X XX X",
         " X  XX  X XX  X X",
         " X XX   X    X   ",
         "    X X  X XX  X ",
         "  X X    X X  XX "]

test3 = [" X  X X  X XXX X X XX X X  XXXX X X X X ",
         "X X  X X  X XXX X  XXX X X XXXXX X X X  ",
         "XXX X X X XXX X X X X XXXX X X X XXX X  ",
         "XXX X XXX X X XXX X XX XXX X XX  XXX X  ",
         "XX  XX X X X X X X  XXXXX     XXX X XXX "]

import time

s = time.clock()
print numAllPercs(test3,3), #"hhhhhhhhhhhhhhwwwwwwwww"
s = time.clock()-s
print s