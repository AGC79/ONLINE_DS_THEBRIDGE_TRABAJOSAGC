-- Eliminar las tablas existentes si existen para evitar conflictos al recrearlas.
-- Esto asegura que no haya errores por duplicación de tablas al ejecutar scripts de creación.

DROP TABLE IF EXISTS Proyectos_realizados;
DROP TABLE IF EXISTS Alumno;
DROP TABLE IF EXISTS Proyectos;
DROP TABLE IF EXISTS Profesor;
DROP TABLE IF EXISTS Bootcamp;
DROP TABLE IF EXISTS Promocion;
DROP TABLE IF EXISTS Campus;

-- CREACIÓN DE TABLAS
CREATE TABLE Campus (
    id_campus INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Promocion (
    id_promocion INT PRIMARY KEY,
    mes VARCHAR(50) NOT NULL
);

CREATE TABLE Bootcamp (
    id_bootcamp INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Proyectos (
    id_proyecto INT PRIMARY KEY,
	id_bootcamp INT UNIQUE,
    nombre VARCHAR(50) NOT NULL,

    FOREIGN KEY (id_bootcamp) REFERENCES Bootcamp(id_bootcamp)
);
a
CREATE TABLE Alumno (
    id_alumno INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    id_bootcamp INT NOT NULL,
    id_promocion INT NOT NULL,
    id_campus INT NOT NULL,
    fecha_inicio DATE NOT NULL,

    FOREIGN KEY (id_bootcamp) REFERENCES Proyectos(id_bootcamp),
    FOREIGN KEY (id_promocion) REFERENCES Promocion(id_promocion),
    FOREIGN KEY (id_campus) REFERENCES Campus(id_campus)
);

CREATE TABLE Proyectos_realizados (
    id_proyectos_realizados INT PRIMARY KEY,
    id_alumno INT NOT NULL,
    id_proyecto INT NOT NULL,
    calificacion VARCHAR(10) NOT NULL CHECK (calificacion IN ('Apto','No Apto')),
    FOREIGN KEY (id_alumno) REFERENCES Alumno(id_alumno),
    FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id_proyecto)
);

CREATE TABLE Profesor (
    id_profesor INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    rol VARCHAR(50) NOT NULL CHECK (rol IN ('LI', 'TA')),
	modalidad VARCHAR(50) NOT NULL CHECK (modalidad IN ('Presencial', 'Online')),
	id_bootcamp INT NOT NULL,
    id_promocion INT NOT NULL,
    id_campus INT NOT NULL,

    FOREIGN KEY (id_bootcamp) REFERENCES Bootcamp(id_bootcamp),
    FOREIGN KEY (id_promocion) REFERENCES Promocion(id_promocion),
    FOREIGN KEY (id_campus) REFERENCES Campus(id_campus)
);


-- INSERCIÓN MANUAL DE VALORES PARA LA MAYORÍA DE LAS TABLAS

INSERT INTO bootcamp (id_bootcamp, nombre)
VALUES 
    (0, 'DS'),
    (1, 'FS');

INSERT INTO Campus (id_campus, nombre)
VALUES 
    (0, 'Madrid'),
    (1, 'Valencia'),
	(2, 'Bilbao'),
	(3, 'Vitoria'),
	(4, 'Sevilla');

INSERT INTO Promocion (id_promocion, mes)
VALUES 
    (0, 'Febrero'),
    (1, 'Marzo'),
	(2, 'Abril'),
	(3, 'Junio'),
	(4, 'Septiembre'),
	(5, 'Octubre');

INSERT INTO Proyectos (id_proyecto, id_bootcamp, nombre)
VALUES 
    (0, 0, 'Proyecto_HLF'),
    (1, 0, 'Proyecto_EDA'),
	(2, 0, 'Proyecto_BBDD'),
	(3, 0, 'Proyecto_ML'),
	(4, 0, 'Proyecto_Deployment'),
	(5, 1, 'Proyecto_WebDev'),
	(6, 1, 'Proyecto_FrontEnd'),
	(7, 1, 'Proyecto_Backend'),
	(8, 1, 'Proyecto_React'),
	(9, 1, 'Proyecto_FullSatck');

INSERT INTO Profesor (id_profesor, nombre, rol, modalidad, id_bootcamp, id_promocion, id_campus) VALUES
(0, 'Noa Yáñez', 'TA', 'Presencial', 0, 4, 0),
(1, 'Saturnina Benitez', 'TA', 'Presencial', 0, 4, 0),
(2, 'Anna Feliu', 'TA', 'Presencial', 1, 4, 0),
(3, 'Rosalva Ayuso', 'TA', 'Presencial', 1, 4, 1),
(4, 'Ana Sofía Ferrer', 'TA', 'Presencial', 1, 0, 1),
(5, 'Angélica Corral', 'TA', 'Presencial', 1, 0, 0),
(6, 'Ariel Lledó', 'TA', 'Presencial', 0, 4, 0),
(7, 'Mario Prats', 'LI', 'Online', 1, 0, 1),
(8, 'Luis Ángel Suárez', 'LI', 'Online', 1, 4, 0),
(9, 'María Dolores Diaz', 'LI', 'Online', 0, 4, 0);

-- VALORES INSERTADOS EN TABLA alumno CON AUTOMATIZACIÓN (VER DOCUMENTO proyecto_bbdd_inserciones_automatizadas.ipynb)

-- VALORES INSERTADOS EN TABLA proyectos_realizados CON AUTOMATIZACIÓN (VER DOCUMENTO proyecto_bbdd_inserciones_automatizadas.ipynb)