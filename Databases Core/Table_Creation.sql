-- Parent tables
CREATE TABLE paises(
	pais_id       INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	nombre           TEXT NOT NULL UNIQUE,
	codigo            VARCHAR(3) NOT NULL UNIQUE
);

CREATE TABLE categorias(
	categoria_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	nombre        TEXT NOT NULL UNIQUE,
	descripcion   TEXT
);

CREATE TABLE tipo_clientes(
	tipo_cliente_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	nombre           TEXT NOT NULL UNIQUE
);


-- Child Tables
CREATE TABLE sucursales(
	sucursal_id   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	nombre          TEXT NOT NULL,
	ciudad          TEXT NOT NULL,
	pais_id         INTEGER NOT NULL REFERENCES paises(pais_id)
);

CREATE TABLE productos(
	producto_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	nombre       TEXT NOT NULL,
	codigo       INTEGER NOT NULL UNIQUE,
	descripcion  TEXT,
	precio       NUMERIC(10,2) NOT NULL,
	stock        INTEGER NOT NULL DEFAULT 0,
	categoria_id INTEGER NOT NULL REFERENCES categorias(categoria_id),
	activo       BOOLEAN NOT NULL DEFAULT TRUE
);


CREATE TABLE clientes(
	cliente_id       INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	nombre           TEXT NOT NULL,
	email            VARCHAR(100) NOT NULL UNIQUE,
	telefono         VARCHAR(20),
	fecha_registro   DATE NOT NULL DEFAULT CURRENT_DATE,
	activo           BOOLEAN NOT NULL DEFAULT TRUE,
	tipo_cliente_id  INTEGER NOT NULL REFERENCES tipo_clientes(tipo_cliente_id)
);

CREATE TABLE empleados(
	empleado_id    INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	nombre         TEXT NOT NULL,
	cargo          NUMERIC(10,2) NOT NULL,
	sucursal_id    INTEGER NOT NULL REFERENCES sucursales(sucursal_id)
);

CREATE TABLE pedidos(
	pedido_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	fecha          DATE NOT NULL DEFAULT CURRENT_DATE,
	cliente_id     INTEGER NOT NULL REFERENCES clientes(cliente_id),
	sucursal_id    INTEGER NOT NULL REFERENCES sucursales(sucursal_id),
	empleado_id    INTEGER NOT NULL REFERENCES empleados(empleado_id)
);

CREATE TABLE detalle_pedidos(
	detalle_id    INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	pedido_id     INTEGER NOT NULL REFERENCES pedidos(pedido_id),
	producto_id   INTEGER NOT NULL REFERENCES productos(producto_id),
	cantidad      INTEGER NOT NULL DEFAULT 1,
	precio_unit   NUMERIC(10,2) NOT NULL
);