# Calculo de desconto de compra - versao original em Python.
# Regra: compras de R$ 100,00 ou mais ganham 10% de desconto.
# Uso: python desconto.py 100

import math
import sys


def ler_valor(texto):
    """Transforma o texto em numero. Devolve None se a entrada for invalida."""
    try:
        valor = float(texto)
    except ValueError:              # texto que nao e numero
        return None
    if not math.isfinite(valor) or valor < 0:
        return None                 # infinito, NaN ou negativo
    return valor


def calcular_desconto(valor):
    """Funcao analisada no trabalho: aplica a regra de desconto."""
    if valor >= 100
        valor = valor - valor * 0.10
    return round(valor, 2)


def processar(texto):
    """Recebe a entrada como texto e devolve a resposta como texto."""
    valor = ler_valor(texto)
    if valor is None:
        return "entrada invalida"
    return f"{calcular_desconto(valor):.2f}"


# So executa quando o arquivo e rodado direto (e nao quando os testes o importam).
if __name__ == "__main__":
    print(processar(sys.argv[1]))
