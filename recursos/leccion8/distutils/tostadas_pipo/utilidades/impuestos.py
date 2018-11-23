# -*- coding: utf8 -*-

""" Módulo para cálculos de diversos impuestos """

def impuesto_iva12(monto=0):
    """ Calcula el impuesto del IVA de 12 % """
    total = ((monto * 12)/100)
    return total


def impuesto_iva14(monto=0):
    """ Calcula el impuesto del IVA de 14 % """
    total = ((monto * 14)/100)
    return total
