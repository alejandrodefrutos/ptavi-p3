#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import smallsmilhandler
import sys
import os
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fichero))
        self.lista = sHandler.get_tags()

    def __str__(self):
        for lista in self.lista:
            print lista[0],
            for atributo in lista[1]:
                if (lista[1])[atributo] != "":
                    print '\t', atributo, '=', (lista[1])[atributo],
            print

    def do_local(self):
        for lista in self.lista:
            for atributo in lista[1]:
                if atributo == "src":
                    os.system("wget -q " + (lista[1])[atributo])
                    source = (lista[1])[atributo]
                    numeroelementos = (len(source.split("/")))
                    (lista[1])[atributo] = source.split("/")[numeroelementos-1]


if __name__ == "__main__":
    try:
        archivo_smil = sys.argv[1]
    except IndexError:
        print 'Usage: python karaoke.py file.smil'
        sys.exit()
    smil = KaraokeLocal(archivo_smil)
    smil.__str__()
    smil.do_local()
    smil.__str__()
