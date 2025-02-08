let botao = document.querySelector("#botao");
botao.style.background="blue"; 
let estaQuebrado=false;
let contaCliques=0;

botao.addEventListener("mouseouver", e =>{
    if(!estaQuebrado){
        botao.style.background="green";
        botao.style.color="white";
    }
});

botao.addEventListener("mouseout", e =>{
    if(!estaQuebrado){
        botao.style.background="blue";
    }
});

botao.addEventListener("click", e =>{
    
    contaCliques++;
    
    if(contaCliques>=10){
        botao.style.background="red";
        botao.innerHTML="Quebrei";
        estaQuebrado=true;
    } ;
});
