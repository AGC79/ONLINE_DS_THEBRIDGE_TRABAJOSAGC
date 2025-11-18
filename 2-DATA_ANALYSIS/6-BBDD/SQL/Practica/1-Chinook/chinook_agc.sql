---------------------- PRIMERA PARTE ----------------------

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
where ar.Name = 'AC/DC';

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
WHERE (invoicedate BETWEEN '2009-01-01' AND '2009-12-31') OR 
(invoicedate BETWEEN '2011-01-01' AND '2011-12-31');

-- OPCIÓN 2 - MIRADA EN CHAT GPT strftime es una función de SQLite (y otros motores de SQL similares) que sirve para extraer o 
-- formatear partes de una fecha o hora.
SELECT strftime('%Y', InvoiceDate) AS Year,
       COUNT(*) AS TotalFacturas
FROM invoices
WHERE strftime('%Y', InvoiceDate) IN ('2009','2011')
GROUP BY Year
ORDER BY Year;

SELECT strftime('%Y', InvoiceDate) AS Year,
       COUNT(*) AS TotalFacturas
FROM invoices
WHERE strftime('%Y', InvoiceDate) IN ('2009','2011')
GROUP BY 1
ORDER BY 1;

-- 13. Cuántas facturas ha habido entre 2009 y 2011
SELECT COUNT(*) FROM invoices
WHERE invoicedate BETWEEN '2009-01-01' AND '2011-12-31';

SELECT COUNT(*)
FROM invoices
WHERE invoicedate LIKE '%2009%'
   OR invoicedate LIKE '%2011%';


SELECT sum()

strftime('%Y', InvoiceDate) AS Year,
       COUNT(*) AS TotalFacturas
FROM invoices
WHERE InvoiceDate BETWEEN 
GROUP BY Year
ORDER BY Year;

-- 14. Cuántas clientes hay de España y de Brasil
SELECT country, COUNT(customerid) 
FROM customers
WHERE country = 'Spain' OR country = 'Brazil'
GROUP by country;

SELECT country, COUNT(customerid) 
FROM customers
WHERE country IN ('Spain', 'Brazil')
GROUP by country;

-- 15. Obtén las canciones que su título empieza por ‘You’
SELECT name FROM tracks
WHERE name LIKE 'You%';



---------------------- SEGUNDA PARTE ----------------------

/*
1. Facturas de Clientes de Brasil, Nombre del cliente, Id de factura, fecha de la
factura y el país de la factura */
SELECT i.InvoiceId as id, c.FirstName || ' ' || lastname as nombre, i.InvoiceDate, i.BillingCountry
FROM invoices i
INNER JOIN customers c
ON i.CustomerId = c.CustomerId
where c.Country = 'Brazil';

-- 2. Obtén cada factura asociada a cada agente de ventas con su nombre completo
SELECT i.InvoiceId, 
e.FirstName || ' ' || e.LastName as nombre_vendedor,
i.invoicedate as Fecha
FROM employees e
INNER JOIN customers c
on e.EmployeeId = c.SupportRepId
inner JOIN invoices i 
on c.CustomerId = i.CustomerId;

-- 3. Obtén el nombre del cliente, el país, el nombre del agente y el total
SELECT 
e.FirstName || ' ' || e.LastName Nombre_empleado,
c.FirstName || ' ' || c.LastName as Nombre_cliente,
c.Country as Pais,
SUM(i.Total)
from employees e
join customers c
on e.EmployeeId = c.SupportRepId
join invoices i 
ON c.CustomerId = i.CustomerId
GROUP by 1, 2;

-- 4. Obtén cada artículo de la factura con el nombre de la canción
SELECT ii.InvoiceLineId, t.TrackId, t.Name
FROM invoice_items ii
INNER JOIN tracks t
on ii.TrackId = t.TrackId

-- 5. Muestra todas las canciones con su nombre, formato, álbum y género
SELECT
t.Name as Cancions,
m.Name as Formato,
a.Title as Titulo,
g.Name as Genero
from tracks t
INNER JOIN albums a 
on t.AlbumId = a.AlbumId
INNER JOIN genres g 
ON t.GenreId = g.GenreId
INNER JOIN media_types m 
ON t.MediaTypeId = m.MediaTypeId

-- 6. Cuántas canciones hay en cada playlist
SELECT 
p.Name,
COUNT(p.Name)
from playlist_track pt
INNER JOIN playlists p
on pt.PlaylistId = p.PlaylistId
group by 1;

-- 7. Cuánto ha vendido cada empleado
SELECT
e.FirstName || ' ' || e.LastName,
SUM(i.Total) as Total_ventas
FROM invoices i 
INNER JOIN customers c 
on i.customerid = c.CustomerId
INNER JOIN employees e 
on c.SupportRepId = e.EmployeeId
GROUP by 1;

-- 8. ¿Quién ha sido el agente de ventas que más ha vendido en 2009?
SELECT
e.FirstName || ' ' || e.LastName,
SUM(i.Total) as Total_ventas
FROM invoices i 
INNER JOIN customers c 
on i.customerid = c.CustomerId
INNER JOIN employees e 
on c.SupportRepId = e.EmployeeId
WHERE invoicedate LIKE '2009%'
GROUP by 1
ORDER BY 2 DESC LIMIT 1;

-- 9. ¿Cuáles son los 3 grupos que más han vendido?
SELECT ar.Name, ii.TrackId, ii.UnitPrice, ii.Quantity, SUM(ii.UnitPrice * ii.Quantity) as Vemtas_Totales
FROM invoice_items ii
INNER JOIN tracks t 
on ii.trackid=t.TrackId
INNER JOIn albums a 
ON t.AlbumId = a.AlbumId
INNER JOIN artists ar 
on a.ArtistId = ar.ArtistId
group by 1
ORDER by Vemtas_Totales DESC;

