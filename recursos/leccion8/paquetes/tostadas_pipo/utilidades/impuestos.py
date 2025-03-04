"""Módulo para calcular el impuesto"""


def impuesto_iva(monto=0, impuesto=12):
    """Calcula el impuesto del IVA"""
    total = (monto * impuesto) / 100
    return total
