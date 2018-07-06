#Mors Alfabesi
# A = .-
# B = -...
# C = -.-.
# D = -..
# E = .
# F = ..-.
# G = ..-
# H = ....
# I = ..
# J = .---
# K = -.-
# L = .-..
# M = --
# N = -.
# O = ---
# P = .--.
# Q = --.-
# R = .-.
# S = ...
# T = -
# U = ..-
# V = ...-
# W = .--
# X = -..-
# Y = -.--
# Z = --..
# 0 = -----
# 1 = .----
# 2 = ..---
# 3 = ...--
# 4 = ....-
# 5 = .....
# 6 = -....
# 7 = --...
# 8 = ---..
# 9 = ----.
def MorsAlfabesiDonustur():
    yazi = input('Mors alfabesi ile yazdırmak istediğiniz mesaj nedir? \n')
    yazi = yazi.upper()
    for i in range(len(yazi)):
        if yazi[i] == 'A':
            print('.-', end = '')
        elif yazi[i] == 'B':
            print('-...', end = '')
        elif yazi[i] == 'C':
            print('-.-.', end = '')
        elif yazi[i] == 'D':
            print('-..', end = '')
        elif yazi[i] == 'E':
            print('.', end = '')
        elif yazi[i] == 'F':
            print('..-.', end = '')
        elif yazi[i] == 'G':
            print('..-', end = '')
        elif yazi[i] == 'H':
            print('....', end = '')
        elif yazi[i] == 'I':
            print('..', end = '')
        elif yazi[i] == 'J':
            print('.---', end = '')
        elif yazi[i] == 'K':
            print('-.-', end = '')
        elif yazi[i] == 'L':
            print('.-..', end = '')
        elif yazi[i] == 'M':
            print('--', end = '')
        elif yazi[i] == 'N':
            print('-.', end = '')
        elif yazi[i] == 'O':
            print('---', end = '')
        elif yazi[i] == 'P':
            print('.--.', end = '')
        elif yazi[i] == 'Q':
            print('--.-', end = '')
        elif yazi[i] == 'R':
            print('-.-.', end = '')
        elif yazi[i] == 'S':
            print('...', end = '')
        elif yazi[i] == 'T':
            print('-', end = '')
        elif yazi[i] == 'U':
            print('..-', end = '')
        elif yazi[i] == 'V':
            print('...-', end = '')
        elif yazi[i] == 'W':
            print('.--', end = '')
        elif yazi[i] == 'X':
            print('-..-', end = '')
        elif yazi[i] == 'Y':
            print('-.--', end = '')
        elif yazi[i] == 'Z':
            print('--..', end = '')
        elif yazi[i] == '0':
            print('-----', end = '')
        elif yazi[i] == '1':
            print('.----', end = '')
        elif yazi[i] == '2':
            print('..---', end = '')
        elif yazi[i] == '3':
            print('...--', end = '')
        elif yazi[i] == '4':
            print('....-', end = '')
        elif yazi[i] == '5':
            print('.....', end = '')
        elif yazi[i] == '6':
            print('-....', end = '')
        elif yazi[i] == '7':
            print('--...', end = '')
        elif yazi[i] == '8':
            print('---..', end = '')
        elif yazi[i] == '9':
            print('----.', end = '')
        else:
            print('',end = '')
        print(' ',end = '')
    print("")
    secim = input("Yeniden denemek ister misiniz(Evet = e , Hayır = h):")
    secim = secim.upper()
    if secim == "E":
        MorsAlfabesiDonustur()
    elif secim == "H":
        print("Bizi tercih ettiğiniz içi teşekkürler ")

MorsAlfabesiDonustur()
