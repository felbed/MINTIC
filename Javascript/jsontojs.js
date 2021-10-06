function reviver(clave, valor) { 
    if (clave == "color") { 
        switch(valor) { 
            case "blanco": valor = "#fff"; 
            break; 
            case "rojo": valor = "#f00"; 
            break; 
            default: valor = "#000"; 
            break; 
        } 
    } 
} 

var jsonTexto = '{"color":"blanco","km":100000,"esNuevo":false,"rueda":{"marca":"desconocida","estado":"malo"}}'; 
var coche = JSON.parse(jsonTexto, reviver); 
console.log(coche);