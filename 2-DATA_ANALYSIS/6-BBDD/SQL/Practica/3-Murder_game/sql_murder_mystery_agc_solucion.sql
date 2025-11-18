SELECT * FROM crime_scene_report
WHERE date = 20180115 AND city = 'SQL City' AND type = 'murder';

SELECT * from person 
WHERE name LIKE '%Annabel%'AND address_street_name = 'Franklin Ave';

SELECT * from person 
WHERE address_street_name = 'Northwestern Dr'
order by address_number DESC LIMIT 1;

-- TESTIMONIO DE Annabel Miller
SELECT i.transcript 
from interview i 
INNER JOIN person p 
ON i.person_id = p.id
WHERE p.name = 'Annabel Miller';

-- GENTE QUE ESTABA EN EL GIMNASIO SEGÚN Annabel Miller CUANDO DICE QUE VIO EL ASESINATO EL DIA 9 DE ENERO DE 2018
SELECT * FROM get_fit_now_member gnm
INNER JOIN get_fit_now_check_in gci
ON gnm.id = gci.membership_id
where check_in_date = 20180109;

-- TESTIMONIO DE Morty Schapiro
SELECT i.transcript
from interview i 
INNER JOIN person p 
ON i.person_id = p.id
WHERE p.name = 'Morty Schapiro';

-- PERSONAS QUE CUADRAN CON EL EL TESTIMONIO DE Morty Schapiro
SELECT DISTINCT gci.membership_id, gnm.name, gnm.membership_status
from get_fit_now_check_in gci
INNER join get_fit_now_member gnm
ON gci.membership_id = gnm.id
WHERE membership_id LIKE '48Z%';

-- PERSONA DE LA QUE HABLA Morty Schapiro: Jeremy Bowers (AUTOR MATERIAL)
SELECT gnm.name, p.name from get_fit_now_member gnm
INNER JOIN person p 
ON gnm.person_id = p.id
INNER JOIN drivers_license dl
ON p.license_id = dl.id
WHERE plate_number LIKE '%H42W%';

-- TESTIMONIO DE Jeremy Bowers
SELECT i.transcript
from interview i 
INNER JOIN person p 
ON i.person_id = p.id
WHERE p.name = 'Jeremy Bowers'; 

-- MUJERES QUE CUADRAN CON EL TESTIMONIO DE Jeremy Bowers
SELECT p.name, dl.gender 
FROM person p 
INNER JOIN drivers_license dl
ON p.license_id = dl.id
where dl.hair_color = 'red' 
      AND height BETWEEN 65 AND 67
      AND car_make = 'Tesla' 
      AND car_model = 'Model S';

-- MUJER DE LA QUE HABLA EL TESTIMONIO DE Jeremy Bowers: Miranda Priestly (AUTORA INTELECTUAL)
SELECT p.name, fec.event_name, date FROM person p 
INNER JOIN facebook_event_checkin fec
on p.id = fec.person_id
WHERE p.name in ('Red Korb', 'Regina George', 'Miranda Priestly')
      and fec.event_name = 'SQL Symphony Concert'
      AND fec.date BETWEEN 20171201 AND 20171231;



