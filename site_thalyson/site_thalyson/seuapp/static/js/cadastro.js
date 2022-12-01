// Tela de cadastro

// Regex para verificar se o usuario nao possui apenas numeros

let usuario = document.getElementById("id_usuario");
usuario.setAttribute("onkeyup", "confereUser()");

const texto = /[a-zA-Z]/;

function confereUser() {
    let senha1 = document.getElementById("id_senha");
    let senha2 = document.getElementById("id_confirma_senha");
    let btn = document.getElementById("btn");
    
    let result = document.getElementById("result");
    
    if (!texto.test(usuario.value) || "") {
        result.innerText = "Usuario deve conter letras"
        btn.disabled = true
    } else {
        result.innerText = ""
        btn.disabled = false
    }
    
    if (senha1.value == "" || senha2.value == "") {
        btn.disabled = true
    }
}

/*
    Ajustando a formatação do numero de telefone
*/

function formatNumber(evento) {
    const padrao = /[0-9]/
    var tecla = evento.key
    if (!padrao.test(tecla)) {
        return evento.preventDefault()
    }
    let txt = document.getElementById('id_tel')
    if (txt.value.length == '') {
        txt.value += "("
    }

    if (txt.value.length == 1 && !txt.value.includes("(")) {
        txt.value = "(" + txt.value.substring(0)
    }

    if (txt.value.length == 3) {
        txt.value += ") "
    }
    if (txt.value.length == 10) {
        txt.value += "-"
    }
}

/* conferindo se as senhas estao coincidindo e bloqueando o botao de registro
caso elas estejam diferentes ou nulas
*/

let input1 = document.getElementById("id_confirma_senha");
input1.setAttribute("onkeyup", "confereSenha()");

let input2 = document.getElementById("id_senha");
input2.setAttribute("onkeyup", "confereSenha()");

function confereSenha() {
    let senha1 = document.getElementById("id_senha");
    let senha2 = document.getElementById("id_confirma_senha");
    let btn = document.getElementById("btn");

    let result = document.getElementById("result");

    if (senha1.value != senha2.value || senha2.value != senha1.value) {
        result.innerText = "As senhas não conferem"
        btn.disabled = true
    } else {
        result.innerText = ""
        btn.disabled = false
    }

    if (senha2.value == "") {
        result.innerText = ""
    }

    if (senha1.value == "" || senha2.value == "") {
        btn.disabled = true
    }

    if (!texto.test(usuario.value) || "") {
        result.innerText = "Usuario deve conter letras"
        btn.disabled = true
    }
};

// formatando inputs de senha para limitar o total de digitos

let id_senha = document.getElementById("id_senha");
let id_confirma_senha = document.getElementById("id_confirma_senha");

id_senha.setAttribute("maxlength", "16");
id_confirma_senha.setAttribute("maxlength", "16")

// Finalizando tela de cadastro