const arreglo1 = ["b", "a", "k", "e", "r"];
const arreglo2 = [4,3,1,2,5];
const arreglo3 = ["B", "A", "K", "E", "R"];

const descendente = arreglo1.sort((a,b)=>a>b ?-1:1);
console.log(descendente);

const ascendente = arreglo2.sort((a,b)=>a>b ?1:-1);
console.log(ascendente);

const orden = arreglo3.sort((a,b)=>a>b ?1:-1);
console.log(orden);