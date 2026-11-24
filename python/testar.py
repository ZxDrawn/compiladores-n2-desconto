"""Executa os 6 casos de teste compartilhados na versao Python.

Uso (a partir da pasta trabalho-n2): python3 python/testar.py
Gera tambem o arquivo testes/resultados_python.json.
"""

import json
import os
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PASTA)

from desconto import processar  # noqa: E402

RAIZ = os.path.dirname(PASTA)
CASOS = os.path.join(RAIZ, "testes", "casos.json")
SAIDA = os.path.join(RAIZ, "testes", "resultados_python.json")


def main():
    with open(CASOS, encoding="utf-8") as arquivo:
        casos = json.load(arquivo)

    resultados = []
    aprovados = 0
    for caso in casos:
        obtido = processar(caso["entrada"])
        situacao = "APROVADO" if obtido == caso["esperado"] else "REPROVADO"
        aprovados += situacao == "APROVADO"
        resultados.append({**caso, "obtido": obtido, "situacao": situacao})
        print(f"{caso['caso']} | entrada={caso['entrada']:>6} | "
              f"esperado={caso['esperado']:>16} | obtido={obtido:>16} | {situacao}")

    print(f"\nPython: {aprovados}/{len(casos)} testes aprovados")

    with open(SAIDA, "w", encoding="utf-8") as arquivo:
        json.dump(resultados, arquivo, ensure_ascii=False, indent=2)

    sys.exit(0 if aprovados == len(casos) else 1)


if __name__ == "__main__":
    main()
