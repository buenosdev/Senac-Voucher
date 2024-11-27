// -------------- Testes

// document.write(/[az]/i.test("AZ"));
// document.write(/love/i.test("LovE"));
// document.write(/\[bx]/.test("123x"));
// document.write(/\s/i.test(" w"));

// -------------- Validação de datas

// document.write(/^\d{2}\/\d{2}\/\d{4}$/.test('33/33/33'));

// var dia = /^(0[1-9]|1[0-9]|2[0-9]|3[0-1])$/;

// var mes = /^(0[1-9]|1[0-2])$/;

// var ano = /^\d{4}$/;

// var data =  /^(0[1-9]|1[0-9]|2[0-9]|3[0-1])\/(0[1-9]|1[0-2])\/\d{4}$/;


// document.write(dia.test("32"))

// document.write(mes.test("12"))

// document.write(data.test("22/04/2120"))

// -------------- Validação de CPF

// var cpf = /^([0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2})$/;

// document.write(cpf.test("957.877.555-55"))

// -------------- Validação de Email
// var email = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

// document.write(email.test("seila@gmail.com"))

// -------------- Validação de input-email

const inputs = document.querySelectorAll('.required');

const spans = document.querySelectorAll('.span-required');

const email = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

function emailValidate(){
    if (email.test(inputs[0].value)){
        removeError(0)
    
}
    else{
        setError(0);
    }
}

function setError(index){
    spans[index].style.display='block';
    spans[index].style.color = 'red';
}

function removeError(index){
    spans[index].style.display = 'none';
}