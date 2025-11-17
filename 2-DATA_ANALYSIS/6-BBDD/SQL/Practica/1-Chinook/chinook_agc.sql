-- 1. Obtén los clientes de brasil
SELECT firstname, lastname, country 
from customers 
WHERE country = 'Brazil';

-- 2. Obtén los empleados que son agentes de ventas
SELECT lastname, firstname, title 
FROM employees 
where title = 'Sales Support Agent';

-- 3. Obtén las canciones de ‘AC/DC’
SELECT t.Name, t.Composer, a.Title FROM tracks as t
JOIN albums as a
ON t.AlbumId = a.AlbumId
INNER JOIN artists AS ar
on a.ArtistId = ar.ArtistId
WHERE ar.Name = 'AC/DC';

SELECT * from tracks 
WHERE composer LIKE '%AC/DC%'

SELECT * FROM artists
WHERE artistid = 1;

-- 4. Obtén los campos de los clientes que no sean de USA: Nombre completo, ID, País
SELECT customerid, firstname, lastname, country 
FROM customers 
WHERE NOT Country = 'USA';

-- 5. Obtén los empleados que son agentes de ventas: Nombre completo, Dirección (Ciudad, Estado, País) y email
SELECT firstname || ' ' || lastname as Nombre_completo, 
address || ', ' || city || ', ' || state || ', ' || country as DIRECCION
from employees
WHERE title = 'Sales Support Agent';

-- 6. Obtén una lista con los países no repetidos a los que se han emitido facturas
SELECT DISTINCT billingcountry from invoices;

SELECT DISTINCT country from customers as c 
INNER JOIN invoices as i
on c.CustomerId = i.CustomerId;

-- 7. Obtén una lista con los estados de USA no repetidos de donde son los clientes y cuántos clientes en cada uno.
SELECT state, COUNT(*) AS total_clientes
FROM customers
WHERE country = 'USA'
GROUP BY state
ORDER BY total_clientes DESC;

-- 8. Cuántos artículos tiene la factura 37
SELECT COUNT (*) from invoices as i
INNER JOIN invoice_items as ii
On i.InvoiceId = ii.InvoiceId
where i.invoiceid = 37;

-- 9. Cuántas canciones tiene ‘AC/DC’
-- OPCIÓN 1
select ar.Name, COUNT(trackid) as Total_canciones FROM tracks as t
INNER JOIN albums as al
on t.AlbumId = al.AlbumId
INNER JOIN artists as ar
ON ar.ArtistId = al.ArtistId
where t.Composer = 'AC/DC';

-- OPCIÓN 2
SELECT composer, COUNT(trackid) FROM tracks
WHERE composer = 'AC/DC';

-- 10. Cuántos artículos tiene cada factura
SELECT InvoiceId, SUM(Quantity) AS Total_Articulos
FROM invoice_items
GROUP BY InvoiceId
ORDER BY InvoiceId ASC;

-- 11. Cuántas facturas hay de cada país
SELECT country, COUNT(invoiceid) as Facturas FROM customers AS c
INNER JOIN invoices AS i
ON c.customerid = i.CustomerId
GROUP by country
ORDER by Facturas DESC;

-- 12. Cuántas facturas ha habido en 2009 y 2011
SELECT COUNT(*) 
FROM invoices
WHERE (invoicedate BETWEEN '2009-01-01' AND '2009-12-31') 
   OR (invoicedate BETWEEN '2011-01-01' AND '2011-12-31');

-- 13. Cuántas facturas ha habido entre 2009 y 2011
SELECT COUNT(*) FROM invoices
WHERE invoicedate BETWEEN '2009-01-01' AND '2011-12-31';

-- 14. Cuántas clientes hay de España y de Brasil
SELECT country, COUNT(customerid) 
FROM customers
WHERE country = 'Spain' OR country = 'Brazil'
GROUP by country;

-- 15. Obtén las canciones que su título empieza por ‘You’
SELECT name FROM tracks
WHERE name LIKE 'You%';


-- PRUEBAS CLASE (NO SON CONSULTAS PARA EL EJERCICIO)
SELECT COUNT(*), genres.GenreId, tracks.Name from tracks as t
INNER JOIN genres as g
on t.GenreId = g.GenreId
group BY t.GenreId;


SELECT genres.Name, AVG(tracks.UnitPrice) as Precio_medio FROM tracks
INNER JOIN genres ON tracks.GenreId = genres.GenreId
GROUP by tracks.GenreId;

















15. Obtén las canciones que su título empieza por ‘You’
