#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys


class ContentHandler(ContentHandler):

    def __init__(self):
        self.inItem = False
        self.inContent = False
        self.title = ""
        self.theContent = ""
        self.html = ""

    def startElement(self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title' or name == 'link':
                self.inContent = True

    def endElement(self, name):
        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                self.title = (self.theContent).encode('utf-8')
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
                self.html += '<p><a href="' + self.theContent.encode('utf-8') \
                    + '">' + self.title + '</a></p>'
                self.inContent = False
                self.title = ""
                self.theContent = ""

    def characters(self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


def getNews():
    theParser = make_parser()
    theHandler = ContentHandler()
    theParser.setContentHandler(theHandler)
    theParser.parse("http://barrapunto.com/index.rss")
    return theHandler.html
