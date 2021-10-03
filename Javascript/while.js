var cont=0; 
var par=0; 
while (cont<10) { 
    par=par+2; 
    console.log (par); 
    cont++; 
    /* controlar el ciclo, de la par que se va repetir 10*/ 
}

cont=0; 
while (cont<10) { 
    console.log ( cont); 
    cont++; 
}

var cont=0; 
var par=0;  
while (cont<6) {
    console.log ("2 * " + cont + " = " + par);
    par=par+2; 
     
    cont++; 
    /* controlar el ciclo, de la par que se va repetir 10*/ 
}

/* Serie Fibonacci*/
var limite = 13;
var serie = [0,1];
var i = 2;
while (i < limite) {
    serie.push(serie[i-1] + serie[i-2]);
    i++;
}

console.log(serie);

var x1 = 0;
var x2;
while (x1 < 5) {
    x2 = 0;
    while (x2 <= x1) {
        console.log(x1 + "," + x2)
        x2++;
    }
    x1++;
}

var x1;
var x2 = 0;
while (x2 < 5) {
    x1 = x2;
    while (x1 < 5) {
        console.log(x1 + "," + x2)
        x1++;       
    }
    x2++;
}

var contador = 0;
do{ 
    console.log(contador); 
    contador++; 
} while(contador < 3); 

console.log("Fin ciclo do while");

for(let contador = 0; contador < 3 ; contador++ ) { 
    console.log(contador); 
} 

console.log("Fin ciclo for");