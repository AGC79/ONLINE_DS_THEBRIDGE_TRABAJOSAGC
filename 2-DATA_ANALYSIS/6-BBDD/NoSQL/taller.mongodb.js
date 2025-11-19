
// En cada consulta que se haga se tiene que usar el use

use('taller');

/*
db.clientes.insertOne({
    nombre: 'Pepi', 
    email: 'pepi@email.es', 
    telefono:'67543398', 
    edad: 20
})
*/

// db.clientes.find()

// Modelado embebido
/*
db.clientes.insertOne(
    {
    nombre: "Laura Pérez",
    email: "laura.perez@example.com",
    telefono: ["+34 600123456", "+34 699987654"],
    direcciones: [
        {
        tipo: "casa",
        calle: "Calle Mayor 123",
        ciudad: "Madrid",
        pais: "España"
        },
        {
        tipo: "trabajo",
        calle: "Av. de América 45",
        ciudad: "Madrid",
        pais: "España"
        }
    ],
    compras: [
        { producto: "Laptop", precio: 1200, fecha: "2024-03-15" },
        { producto: "Ratón", precio: 25, fecha: "2024-04-22" }
    ]
    }
)
    */

/*
db.clientes.insertOne([
    {
        nombre: 'Manoli'
    },

    {
        nombre: 'Josefina'
    }
])
*/

// db.clientes.find({nombre: 'Pepi'})

// db.clientes.find({_id: ObjectId("691d8b2fdf94e026ecb8818c")})

/*
db.clientes.insertMany([
    {
      nombre: "Laura Gómez",
      email: "laura.gomez@example.com",
      telefono: ["+34 600123456", "+34 699987654"],
      direcciones: [
        {
          tipo: "casa",
          calle: "Calle Mayor 123",
          ciudad: "Madrid",
          pais: "España"
        },
        {
          tipo: "trabajo",
          calle: "Av. de América 45",
          ciudad: "Madrid",
          pais: "España"
        }
      ],
      compras: [
        { producto: "Laptop", precio: 1200, fecha: "2024-03-15" },
        { producto: "Ratón", precio: 25, fecha: "2024-04-22" }
      ]
    },
    {
      nombre: "Carlos Ruiz",
      email: "carlos.ruiz@example.com",
      telefono: ["+34 611234567"],
      direcciones: [
        {
          tipo: "casa",
          calle: "Calle de Alcalá 58",
          ciudad: "Madrid",
          pais: "España"
        }
      ],
      compras: []
    },
    {
      nombre: "María López",
      email: "maria.lopez@example.com",
      telefono: ["+34 612345678"],
      direcciones: [
        {
          tipo: "casa",
          calle: "Calle Princesa 10",
          ciudad: "Barcelona",
          pais: "España"
        }
      ],
      compras: [
        { producto: "Tablet", precio: 350, fecha: "2023-11-10" }
      ]
    },
    {
    nombre: "José Martínez",
      email: "jose.martinez@example.com",
      telefono: ["+34 613456789"],
      direcciones: [],
      compras: [
        { producto: "Monitor", precio: 200, fecha: "2024-05-01" },
        { producto: "Teclado", precio: 50, fecha: "2024-05-02" }
      ]
    },
    {
      nombre: "Ana Torres",
      email: "ana.torres@example.com",
      telefono: [],
      direcciones: [
        {
          tipo: "casa",
          calle: "Rambla Catalunya 33",
          ciudad: "Barcelona",
          pais: "España"
        }
      ],
      compras: []
    },
    {
      nombre: "David Fernández",
      email: "david.fernandez@example.com",
      telefono: ["+34 614567890"],
      direcciones: [
        {
          tipo: "trabajo",
          calle: "Paseo de Gracia 22",
          ciudad: "Barcelona",
          pais: "España"
        }
      ],
      compras: [
        { producto: "Auriculares", precio: 80, fecha: "2024-02-14" }
      ]
    },
    {
    nombre: "Lucía Navarro",
      email: "lucia.navarro@example.com",
      telefono: ["+34 615678901"],
      direcciones: [],
      compras: [
        { producto: "Smartphone", precio: 900, fecha: "2023-12-20" },
        { producto: "Cargador", precio: 30, fecha: "2024-01-05" }
      ]
    },
    {
      nombre: "Miguel Álvarez",
      email: "miguel.alvarez@example.com",
      telefono: [],
      direcciones: [],
      compras: []
    },
    {
      nombre: "Isabel Romero",
      email: "isabel.romero@example.com",
      telefono: ["+34 616789012"],
      direcciones: [
        {
          tipo: "casa",
          calle: "Gran Vía 80",
          ciudad: "Valencia",
          pais: "España"
        }
      ],
      compras: [
        { producto: "Impresora", precio: 150, fecha: "2024-06-01" }
      ]
    },
    {

      nombre: "Raúl Díaz",
      email: "raul.diaz@example.com",
      telefono: ["+34 617890123"],
      direcciones: [
        {
          tipo: "trabajo",
          calle: "Av. Constitución 100",
          ciudad: "Sevilla",
          pais: "España"
        }
      ],
      compras: []
    }
  ])
*/

// db.clientes.find({ nombre: "Laura Gómez" })
// db.clientes.find({ "direcciones.ciudad": "Barcelona" })

// db.clientes.find({"compras.precio": {$gte:350}})

// db.clientes.find({"compras.producto": "Laptop"})

// en este caso el filtro pide todo, por eso esta vacío
// db.clientes.find({}, { nombre: 1, email: 1, _id: 0 })

// db.clientes.find({nombre: 'Laura Gómez'}, { nombre: 1, email: 1, _id: 0 })

// db.clientes.find({nombre: 'Laura Gómez'}, { nombre: 0, email: 0, _id: 0 })

// db.clientes.find({'direcciones.ciudad': 'Barcelona'}, {compras: 1, "direcciones.ciudad": 1, _id: 0 })

// db.clientes.find({"direcciones.pais":"España"}, {"nombre":0,"direcciones.ciudad":0,_id:0})

// db.clientes.find({compras:{$exists:true}})

// db.clientes.find({compras:{$exists:true}}, {compras: 1, email: 1, _id: 0})

// db.clientes.find({compras:{$exists:false}}, {compras: 1, email: 1, _id: 0})

// Aquí "compras.producto" va obligatoriamente con comillas
// db.clientes.find( { "compras.producto": { $in: ["Laptop" ]} } )

// en un json de javascript compras puede ir on comillas simples/dobles o sin comillas
// Aquí filtramos por los clientes que tienen compras
// db.clientes.find( { compras: { $eq: []} } )

// trae los elemeentos de Barcelona que tengan compras
// db.clientes.find({'direcciones.ciudad': 'Barcelona', compras:{$exists:true}})

// db.clientes.find({$or: [{ 'direcciones.ciudad': 'Barcelona' }, { nombre: 'Maria' }]})

/*
db.clientes.updateOne(
  { nombre: "Laura Gómez" },
  { $set: { email: "laura.nueva@example.com" } }
)
*/

/*
db.clientes.updateMany(
  { "direcciones.ciudad": "Barcelona" },
  { $set: { email: "barcelona@barcelona.com" } }
)
  */

// db.clientes.find({nombre: 'Laura Gómez'}, {articulos:1})

/*
db.clientes.updateMany(
  { _id: ObjectId("691d90427c77cb7cad80bf02") },
  {
    $push: {
      articulos: {
        $each: [
          { rating: 2, comentario: "este es el comentario" },
          { rating: 5, comentario: "este es el comentario de 5" }
        ]
      }
    }
  }
)
  */