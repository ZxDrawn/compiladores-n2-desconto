/*
 * Executa os 6 casos de teste compartilhados na versao JavaScript.
 *
 * Uso (a partir da pasta trabalho-n2): node javascript/testar.js
 * Gera tambem o arquivo testes/resultados_javascript.json.
 */

const fs = require("fs");
const path = require("path");
const { processar } = require("./desconto");

const RAIZ = path.dirname(__dirname);
const CASOS = path.join(RAIZ, "testes", "casos.json");
const SAIDA = path.join(RAIZ, "testes", "resultados_javascript.json");

function main() {
  const casos = JSON.parse(fs.readFileSync(CASOS, "utf-8"));

  const resultados = [];
  let aprovados = 0;
  for (const caso of casos) {
    const obtido = processar(caso.entrada);
    const situacao = obtido === caso.esperado ? "APROVADO" : "REPROVADO";
    if (situacao === "APROVADO") aprovados++;
    resultados.push({ ...caso, obtido, situacao });
    console.log(
      `${caso.caso} | entrada=${caso.entrada.padStart(6)} | ` +
        `esperado=${caso.esperado.padStart(16)} | obtido=${obtido.padStart(16)} | ${situacao}`
    );
  }

  console.log(`\nJavaScript: ${aprovados}/${casos.length} testes aprovados`);

  fs.writeFileSync(SAIDA, JSON.stringify(resultados, null, 2) + "\n", "utf-8");

  process.exit(aprovados === casos.length ? 0 : 1);
}

main();
