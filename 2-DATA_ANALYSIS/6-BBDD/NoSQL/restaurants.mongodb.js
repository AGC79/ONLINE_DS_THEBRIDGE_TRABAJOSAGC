use('taller');

// 1. Mostrar todos los documentos de la colección restaurantes

// db.restaurants.find()

// 2. Mostrar los campos restaurant_id, nombre, distrito y cocina, pero excluya el campo _id para todos los 
// documentos de la colección restaurantes

// db.restaurants.find({}, {restaurant_id: 1, name: 1, borough: 1, cuisine: 1, _id: 0})


// 3. Mostrar los primeros 5 restaurantes que se encuentran en el distrito Bronx

// db.restaurants.find({borough: "Bronx"}).limit(5)


// 4. Devolver los restaurantes que lograron una puntuación superior a 80 pero inferior a 100

// db.restaurants.find({"grades": {$elemMatch: {"score": { $gt: 80, $lt: 100 }}}});


// 5. Devolver los restaurantes que se ubican en un valor de latitud inferior a -95.754168

// db.restaurants.find({"address.coord.0": {$lt: -95.754168}})

// 6. Devolver los restaurantes que no preparan cocina americana y lograron una puntuación superior a 70 y 
// se ubicaron en una longitud inferior a -65.754168. Nota: Realice esta consulta sin usar el operador $and

// db.restaurants.find({}, {cuisine: 1, _id: 0})

// Comando no correcto
// db.restaurants.find({$nor: [{cuisine: "American "}]})

// Comando correcto
// db.restaurants.find({ cuisine: { $ne: "American " }, "address.coord.0": {$lt: -95.754168} } )

//db.restaurants.find($nor: {}{"address.coord.0": {$lt: -65.754168}})

// 7. Devolver los restaurantes que no preparan cocina americana y lograron un punto de calificación 'A' que 
// no pertenece al distrito de Brooklyn. El documento debe mostrarse según la cocina en orden descendente.

db.restaurants.find({ cuisine: { $ne: "American " }, 
    "grades.grade": "A", 
    borough: {$ne: "Brooklyn"}} ).sort({ cuisine: -1 })


// 8. Devolver los restaurantes que pertenecen al distrito Bronx y preparan platos americanos o chinos
// 9. Devolver ID del restaurante, nombre, distrito y la cocina para aquellos restaurantes que pertenecen 
// al distrito de Staten Island o Queens o Bronx o Brooklyn


// 10. Devolver ID del restaurante, nombre, distrito y la cocina de aquellos restaurantes que lograron una 
// puntuación que no supere los 10


// 11. Devolver ID del restaurante, el nombre y las calificaciones del restaurante para aquellos restaurantes 
// que obtuvieron una calificación de "A" y obtuvieron un puntaje de 11 en una fecha ISO "2014-08-11T00: 00: 00Z" 
// entre muchas fechas de encuesta


// 12. Devolver ID del restaurante, nombre, dirección y ubicación geográfica del restaurante de aquellos donde el 
// segundo elemento de la matriz coord contiene un valor que es más de 42 y hasta 52


// 13. Crea un par de restaurantes que te gusten. Tendrás que buscar en Google Maps los datos de las coordenadas


// 14. Actualiza los restaurantes. Cambia el tipo de cocina 'Ice Cream, Gelato, Yogurt, Ices' por 'sweets'


// 15. Actualiza nombre del restaurante 'Wild Asia' por 'Wild Wild West'


// 16. Borra los restaurantes con latitud menor que -95.754168


// 17.  Borra los restaurantes cuyo nombre empiece por 'C'
