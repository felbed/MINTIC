var suma = (numero1, numero2) =>{ 
    return numero1 + numero2; 
}

var suma = (numero1, numero2) => numero1 + numero2; 

var res = suma(3, 2);
console.log(res);

function calcular(operacion, numero1, numero2){ 
    return operacion(numero1, numero2); 
} 

var c = calcular((numero1, numero2) => numero1 + numero2, 6, 7); 
console.log(c);

/*Sintaxis con un solo parámetro*/
var nombres = (nombre) => console.log('hola ' + nombre) 
nombres("ivan");

/*Funciones flecha sin parametros*/
var mostrarfecha = () => new Date().getDay();
console.log(mostrarfecha());

/*Sintaxis de las funciones que devuelven objeto*/
var usuario = (nombre, apellido) => ({nombre: nombre, apellido: apellido})
console.log(usuario("ivan", "salas"));

var subtotal = (precio, cantidad) => {result = precio * cantidad; return result}; 

console.log(subtotal(3,2));

var total = (IVA) => {return subtotal(3, 2) * IVA};

console.log(total(1.1));

var impuesto = (valor, porcentaje) => {result = valor * (porcentaje/100); return result};

console.log(impuesto(total(1.1), 3));

