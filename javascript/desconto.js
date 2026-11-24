// Calculo de desconto de compra - versao traduzida para JavaScript.
// Regra: compras de R$ 100,00 ou mais ganham 10% de desconto.
// Uso: node desconto.js 100

/** Transforma o texto em numero. Devolve null se a entrada for invalida. */
function lerValor(texto) {
  if (texto.trim() === "") {
    return null;                    // Adaptacao 1: Number("") daria 0
  }
  const valor = Number(texto);      // Adaptacao 1: devolve NaN, nao da erro
  if (!Number.isFinite(valor) || valor < 0) {
    return null;                    // NaN, infinito ou negativo
  }
  return valor;
}

/** Funcao analisada no trabalho: aplica a regra de desconto. */
function calcularDesconto(valor) {
  if (valor >= 100) {
    valor = valor - valor * 0.10;
  }
  return Number(valor.toFixed(2));  // Adaptacao 2: JS nao tem round(x, 2)
}

/** Recebe a entrada como texto e devolve a resposta como texto. */
function processar(texto) {
  const valor = lerValor(texto);
  if (valor === null) {
    return "entrada invalida";
  }
  return calcularDesconto(valor).toFixed(2);
}

module.exports = { processar };

// So executa quando o arquivo e rodado direto (e nao quando os testes o importam).
if (require.main === module) {
  console.log(processar(process.argv[2]));
}
