# Trabalho N2 - Introdução a Compiladores

Tradução manual de um programa de **Python** (original) para **JavaScript**.

**Integrantes:**
- Kaiky Vinícius Oliveira Nascimento
- Abner Kaike Silva Almeida
- Eduardo Moreira Barreiro
- João Lucas de Oliveira Magalhães
- Jean Carlos Alves da Silva

Bacharelado em Ciência da Computação, 8º período – Centro Universitário Afya Ji-Paraná.

## O que o programa faz

Calcula o valor final de uma compra:

- Compra de **R$ 100,00 ou mais**: ganha **10% de desconto**.
- Compra abaixo de R$ 100,00: sem desconto.
- Resultado com **2 casas decimais** (ex.: `90.00`).
- Texto que não é número, número negativo ou infinito: responde `entrada invalida`.

A entrada é digitada na linha de comando, com ponto como separador decimal (ex.: `99.99`).

## Arquivos

```
Compiladores/
  python/
    desconto.py        programa original (função analisada: calcular_desconto)
    testar.py          roda os 6 testes na versão Python
  javascript/
    desconto.js        programa traduzido (função analisada: calcularDesconto)
    testar.js          roda os 6 testes na versão JavaScript
  testes/
    casos.json         os 6 testes (entrada e saída esperada), usados pelas duas versões
    resultados_*.json  resultado de cada versão
    comparar.py        mostra no terminal a comparação das duas versões
  evidencias/
    dis_python.txt            bytecode do Python (módulo dis)
    bytecode_javascript.txt   bytecode do JavaScript (Node.js / V8)
    erros/                    cópias com erro proposital e as mensagens
```

## O que precisa instalar

| Item | Versão usada | Onde baixar |
|---|---|---|
| Python | 3.12.10 (Windows) | https://www.python.org/downloads/ |
| Node.js | 24.20.0 (Windows) | https://nodejs.org/ (versão LTS) |

Nenhuma biblioteca extra. Para conferir: `python --version` e `node --version`
(no Linux/Mac, use `python3` no lugar de `python`).

## Como rodar

Todos os comandos são dados dentro da pasta `Compiladores`.

```bash
python python/desconto.py 100      # mostra 90.00
node javascript/desconto.js 100    # mostra 90.00
```

## Como testar

```bash
python python/testar.py            # Python: 6/6 testes aprovados
node javascript/testar.js          # JavaScript: 6/6 testes aprovados
python testes/comparar.py          # mostra a comparação no terminal
```

| Teste | O que verifica | Entrada | Esperado |
|---|---|---|---|
| T01 | compra comum, sem desconto | 50 | 50.00 |
| T02 | logo abaixo do limite | 99.99 | 99.99 |
| T03 | exatamente no limite (regra usa >=) | 100 | 90.00 |
| T04 | compra comum, com desconto | 250 | 225.00 |
| T05 | zero é válido | 0 | 0.00 |
| T06 | negativo é inválido | -10 | entrada invalida |

Resultado: **6/6 nas duas versões**.

## Como ver o bytecode (evidências)

```bash
# Python
python -c "import sys; sys.path.insert(0, 'python'); import dis, desconto; dis.dis(desconto.calcular_desconto)"

# JavaScript
node --print-bytecode --print-bytecode-filter=calcularDesconto javascript/desconto.js 100
```

O resultado esperado está em `evidencias/dis_python.txt` e `evidencias/bytecode_javascript.txt`
(gerados no Windows com Python 3.12.10 e Node.js 24.20.0). Em outras versões a listagem pode mudar um pouco,
e os endereços de memória do JavaScript mudam a cada execução.

## Erros propositais

```bash
python evidencias/erros/desconto_erro.py 50     # SyntaxError: expected ':'  (antes de rodar)
node evidencias/erros/desconto_erro.js 50       # 50.00 (a linha com erro não é usada)
node evidencias/erros/desconto_erro.js 100      # ReferenceError: desconto is not defined (rodando)
```

## Adaptações da tradução

1. **Entrada inválida:** em Python, `float("abc")` dá erro e usamos `try/except`. Em JavaScript, `Number("abc")` não dá erro, devolve `NaN`, e `Number("")` devolve `0`. Por isso o JavaScript testa o texto vazio e usa `Number.isFinite`. Teste: T06.
2. **Arredondamento:** Python tem `round(valor, 2)`. JavaScript não tem; usamos `toFixed(2)` (que devolve texto) e `Number(...)` para voltar a número. Teste: T03.

## Testes extras (fora dos 6)

| Entrada | Python | JavaScript | Por quê |
|---|---|---|---|
| `1_000` | `900.00` | `entrada invalida` | Python aceita `_` dentro de números; JavaScript não. |
| `0x10` | `entrada invalida` | `16.00` | JavaScript aceita número hexadecimal; Python não. |
| `0.125` | `0.12` | `0.13` | Em empate, `round` arredonda para o par e `toFixed` para cima. |

São entradas fora da especificação. Ficam registradas como limitação.

## Contribuições

- **Kaiky e Eduardo:** evidências de bytecode, tradução/adaptações e testes.
- **Abner, João Lucas e Jean Carlos Alves da Silva:** versão original em Python, experimento de erros e relatório.
