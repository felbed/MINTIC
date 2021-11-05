var pl = {
  peliculas: [
    {
      nombre: 'Hombre en llamas',
      año: 2004,
      género: ['Acción', 'Drama'],
    },
    {
      nombre: 'Son como niños',
      año: 2010,
      género: 'Comedia',
    },
    {
      nombre: 'Jumanji',
      año: 1995,
      género: ['Acción', 'Aventura', 'Comedia'],
    },
  ],
};

console.log(pl);

console.log(JSON.parse('{}'));

const x = JSON.stringify(pl);
console.log(x);
console.log(JSON.parse(x));
