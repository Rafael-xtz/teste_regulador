#!/usr/bin/env python


import config

# sinais do relé teste
global elevar
global abaixar
global reset_indicador
global ln
global co
global ip

class Regulador():
    def __init__(self):
        global elevar
        global abaixar
        global reset_indicador
        global ln
        global co
        global ip

        self.elevar = elevar
        self.abaixar = abaixar
        self.reset_indicador = reset_indicador
        self.ln = ln
        self.co = co
        self.ip = ip

