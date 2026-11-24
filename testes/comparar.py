"""Compara lado a lado os resultados das duas versoes (rodar depois dos testes).

Uso (a partir da pasta trabalho-n2): python3 testes/comparar.py
Mostra no terminal a comparacao dos resultados.
"""

import json
import os

PASTA = os.path.dirname(os.path.abspath(__file__))


def carregar(nome):
    with open(os.path.join(PASTA, nome), encoding="utf-8") as arquivo:
        return {r["caso"]: r for r in json.load(arquivo)}


def main():
    py = carregar("resultados_python.json")
    js = carregar("resultados_javascript.json")

    for caso, rp in py.items():
        rj = js[caso]
        ok = rp["situacao"] == "APROVADO" and rj["situacao"] == "APROVADO"
        situacao = "Ambas aprovadas" if ok else "DIVERGENCIA"
        print(f"{caso}: Python={rp['obtido']:>16}  JavaScript={rj['obtido']:>16}  {situacao}")


if __name__ == "__main__":
    main()
