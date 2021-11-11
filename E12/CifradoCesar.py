#!/usr/bin/env python3

import argparse
import detectEnglish


def EncriptarYDesencriptar(modo, mensaje, clav):
    message = mensaje
    espacios = 1
    while espacios > 0:
        clave = clav
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            if modo == "c":
                translatedIndex = symbolIndex + key
            elif modo == "d":
                translatedIndex = symbolIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print(translated)

def Hackear(mensaje):
    message = mensaje
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    for key in range(len(SYMBOLS)):
        translated = ''
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]

            else:
                translated = translated + symbol

        print('Key #%s: %s' % (key, translated))
        print(detectEnglish.isEnglish(translated))

parser = argparse.ArgumentParser(
    description='Script para cifrar, desencriptar y hackear cadenas de texto')
parser.add_argument(
    'modo', help='c para cifrar, d para descifrar y H para hacker', type=str)
parser.add_argument('mensaje', type=str)
parser.add_argument('-c', '--clave', type=str)
args = parser.parse_args()

#print(args.modo, args.mensaje, args.clave)
if args.modo == "c":
    EncriptarYDesencriptar(args.modo, args.mensaje, args.clave)
elif args.modo == "d":
    EncriptarYDesencriptar(args.modo, args.mensaje, args.clave)
elif args.modo == "H":
    Hackear(args.mensaje)
