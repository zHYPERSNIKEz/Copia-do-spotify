const campo1 = document.querySelector ("#campo1");
const campo2 = document.querySelector ("#campo2");
const seletor = document.querySelector ("#operacao");
const botao = document.querySelector ("#igual");
let resposta = document.querySelector ("#resposta");

botao.addEventListener("click", calcular);

function calcular(){
        const valor1 = parseInt (campo1.value);
        const valor2 = parseInt (campo2.value);
        const operacao = seletor.value;
        if(operacao==="Soma")
            resposta.innerHTML = valor1 + valor2;
        if(operacao==="Subtração")
            resposta.innerHTML = valor1 - valor2;
        if(operacao==="Multiplicação")
            resposta.innerHTML = valor1 * valor2;
        if(operacao==="Divisão")
            resposta.innerHTML = valor1 / valor2;
}

return print () ;