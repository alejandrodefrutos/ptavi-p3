#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista = []

    def startElement(self, name, attrs):

        if name == "root-layout":
            self.rootlayout = {}
            self.rootlayout["widht"] = str(attrs.get("width", ""))
            self.rootlayout["height"] = str(attrs.get("height", ""))
            self.rootlayout["background-color"] = str(attrs.get("background-color", ""))
            self.lista.append([name, self.rootlayout])

        elif name == "region":
            self.region = {}
            self.region["id"] = str(attrs.get("id", ""))
            self.region["top"] = str(attrs.get("top", ""))
            self.region["bottom"] = str(attrs.get("bottom", ""))
            self.region["left"] = str(attrs.get("left", ""))
            self.region["right"] = str(attrs.get("right", ""))
            self.lista.append([name, self.region])

        elif name == "img":

            self.img = {}
            self.img['src'] = str(attrs.get("src", ""))
            self.img['region'] = str(attrs.get("region", ""))
            self.img['begin'] = str(attrs.get("begin", ""))
            self.img['dur'] = str(attrs.get("dur", ""))
            self.lista.append([name, self.img])

        elif name == "audio":
            self.audio = {}
            self.audio['src'] = str(attrs.get("src", ""))
            self.audio['begin'] = str(attrs.get("begin", ""))
            self.audio['dur'] = str(attrs.get("dur", ""))
            self.lista.append([name, self.audio])

        elif name == "textstream":
            self.textstream = {}
            self.textstream['src'] = str(attrs.get("src", ""))
            self.textstream['region'] = str(attrs.get("region", ""))
            self.lista.append([name, self.textstream])

    def get_tags(self):
        return self.lista
