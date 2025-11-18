
/* SELECT firstname, lastname, country 
from customers 
WHERE country = 'Brazil';


SELECT lastname, firstname, title 
FROM employees 
where title = 'Sales Support Agent';



SELECT * from tracks 
WHERE composer LIKE '%AC/DC%'

SELECT * FROM artists
WHERE artistid = 1;


SELECT t.Name, t.Composer, a.Title FROM tracks as t
JOIN albums as a
ON t.AlbumId = a.AlbumId
INNER JOIN artists AS ar
on a.ArtistId = ar.ArtistId
WHERE ar.Name = 'AC/DC';



SELECT customerid, firstname, lastname, country 
FROM customers 
WHERE NOT Country = 'USA';



SELECT firstname || ' ' || lastname as Nombre_completo, 
address || ', ' || city || ', ' || state || ', ' || country as DIRECCION
from employees
WHERE title = 'Sales Support Agent';



SELECT DISTINCT country from customers as c 
INNER JOIN invoices as i
on c.CustomerId = i.CustomerId;

SELECT DISTINCT billingcountry from invoices;



SELECT COUNT(*), genres.GenreId, tracks.Name from tracks as t
INNER JOIN genres as g
on t.GenreId = g.GenreId
group BY t.GenreId;


SELECT genres.Name, AVG(tracks.UnitPrice) as Precio_medio FROM tracks
INNER JOIN genres ON tracks.GenreId = genres.GenreId
GROUP by tracks.GenreId;
*/

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
select ar.Name, COUNT(trackid) as Total_canciones FROM tracks as t
INNER JOIN albums as al
on t.AlbumId = al.AlbumId
INNER JOIN artists as ar
ON ar.ArtistId = al.ArtistId
where ar.Name = 'AC/DC';

SELECT * from tracks;


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
SELECT invoicedate, COUNT(*) FROM invoices
WHERE invoicedate = '2009-01-01' OR invoicedate = '2011-12-31';

-- 13. Cuántas facturas ha habido en 2009 y 2011
SELECT COUNT(*) FROM invoices
WHERE invoicedate BETWEEN '2009-01-01' AND '2011-12-31';

SELECT COUNT(*) FROM invoices
WHERE invoicedate LIKE '%2009%' OR LIKE '%2011%';

SELECT SUM(N.FA)

strftime('%Y', InvoiceDate) AS Year,
       COUNT(*) AS TotalFacturas
FROM invoices
WHERE InvoiceDate BETWEEN 
GROUP BY Year
ORDER BY Year;

SELECT country, COUNT(customerid) 
FROM customers
WHERE country IN ('Spain', 'Brazil')
GROUP by 1;

SELECT strftime('%Y', InvoiceDate) AS Year,
       COUNT(*) AS TotalFacturas
FROM invoices
WHERE strftime('%Y', InvoiceDate) IN ('2009','2011')
GROUP BY 1
ORDER BY 1;

-- 14. Cuántas clientes hay de España y de Brasil
SELECT country, COUNT(customerid) 
FROM customers
WHERE country = 'Spain' OR country = 'Brazil'
GROUP by country;

-- 15. Obtén las canciones que su título empieza por ‘You’
SELECT name FROM tracks
WHERE name LIKE 'You%';

-- 12. Cuántas facturas ha habido en 2009 y 2011
SELECT COUNT(*) 
FROM invoices
WHERE (invoicedate BETWEEN '2009-01-01' AND '2009-12-31') 
   OR (invoicedate BETWEEN '2011-01-01' AND '2011-12-31')
GROUP BY invoicedate;

-- 13. Cuántas facturas ha habido entre 2009 y 2011
SELECT COUNT(*) FROM invoices
WHERE invoicedate BETWEEN '2009-01-01' AND '2011-12-31';

SELECT strftime('%Y', InvoiceDate) AS Year,
       COUNT(*) AS TotalFacturas
FROM invoices
WHERE strftime('%Y', InvoiceDate) IN ('2009','2011')
GROUP BY Year
ORDER BY Year;

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


SELECT i.InvoiceId as id, c.FirstName || ' ' || lastname as nombre, i.InvoiceDate, i.BillingCountry
FROM invoices i
INNER JOIN customers c
ON i.CustomerId = c.CustomerId
where c.Country = 'Brazil';


SELECT i.InvoiceId, 
e.FirstName || ' ' || e.LastName as nombre_vendedor,
i.invoicedate as Fecha
FROM employees e
INNER JOIN customers c
on e.EmployeeId = c.SupportRepId
inner JOIN invoices i 
on c.CustomerId = i.CustomerId;

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



SELECT ii.InvoiceLineId, t.TrackId, t.Name
FROM invoice_items ii
INNER JOIN tracks t
on ii.TrackId = t.TrackId;






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
ON t.MediaTypeId = m.MediaTypeId;



SELECT 
p.Name,
COUNT(p.Name)
from playlist_track pt
INNER JOIN playlists p
on pt.PlaylistId = p.PlaylistId
group by 1;


SELECT
e.FirstName || ' ' || e.LastName,
SUM(i.Total) as Total_ventas
FROM invoices i 
INNER JOIN customers c 
on i.customerid = c.CustomerId
INNER JOIN employees e 
on c.SupportRepId = e.EmployeeId
GROUP by 1;


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


