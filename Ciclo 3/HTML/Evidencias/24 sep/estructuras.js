var salario = 3500000;
var comisiones = salario * 0.12;
var bonificaciones = salario * 0.08;
var ingresos = salario + comisiones + bonificaciones;
var auxilio_transporte = ingresos * 0.12;
var total_ingresos = ingresos + auxilio_transporte;

var alimentacion = ingresos * 0.12;
var transporte = salario * 0.05;
var recreacion = salario * 0.1;
var estudios = ingresos * 0.2;
var banco = ingresos * 0.13;

var total_egresos = alimentacion + transporte + recreacion + estudios + banco;

var disponible = total_ingresos - total_egresos;

console.log(disponible)

var prestamo = 5000000;
var tasa_anual = 0.12;
var tasa_mensual = tasa_anual / 12;
var tiempo_annos = 5;
var tiempo_meses = tiempo_annos * 12;
var valor_anual = prestamo / tiempo_annos;
var valor_mensual = prestamo / tiempo_meses;

var pago_mensual = (prestamo / tiempo_meses)*(1+tasa_mensual)
var pago_anual = (prestamo / tiempo_annos)*(1+tasa_anual)
console.log("El valor del pago mensual es: " + pago_mensual)
console.log("El total con pago mensual es: " + (pago_mensual * tiempo_meses))
console.log("El valor del pago anual es: " + pago_anual)
console.log("El total con pago mensual es: " + (pago_anual * tiempo_annos))

function validar(miCampoTexto) { if (miCampoTexto.length >=6 && miCampoTexto.length <=12) { return false; } }

function validarEmail(valor) { if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/.test(valor)){ alert("La dirección de email " + valor + " es correcta."); } else { alert("La dirección de email es incorrecta."); } }

function validarEmail(campoCorreo) { if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/.test(valor)){ alert("La dirección de email " + valor + " es correcta."); } else { alert("La dirección de email es incorrecta."); } }

/* /^\w+([\.-]?\w+)*@(?:|hotmail|outlook|yahoo|live|gmail)\.(?:|com|es)+$/.test(campo.value)*/

if (valor.charAt(0).toUpperCase()){

}
if (string.charAt(0) == string.charAt(0)){

}