#!/usr/bin/env python
import machine
import upy

# Relé 1

# sinais do relé teste
global elevar
global abaixar
global reset_indicador

elevar = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
abaixar = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
reset_indicador = machine.Pin(4, machine.Pin.OUT)

global ln
global co
global ip
ln = machine.Pin(5, machine.Pin.OUT)
co = machine.Pin(6, machine.Pin.OUT)
ip = machine.Pin(7, machine.Pin.OUT)
