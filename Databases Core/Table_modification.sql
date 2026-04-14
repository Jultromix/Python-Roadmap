CREATE TABLE empleados_demo(
  empleado_id     INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  nombre          TEXT NOT NULL,
  cargo           TEXT
);

-- Modify a table by adding a new column:

ALTER TABLE empleados_demo
ADD COLUMN email TEXT;

ALTER TABLE empleados_demo
ADD COLUMN fecha_ingreso DATE NOT NULL DEFAULT current_date;

ALTER TABLE empleados_demo
ADD COLUMN activo BOOLEAN NOT NULL DEFAULT TRUE;

-- Can I modify the column data type? 
ALTER TABLE empleados_demo
ALTER COLUMN email TYPE VARCHAR(100);

-- Can I modify the restrictions?
ALTER TABLE empleados_demo
ALTER COLUMN email DROP NOT NULL;

-- Can I rename columns?
ALTER TABLE empleados_demo
RENAME COLUMN cargo TO puesto;

-- Can I add constraints?
ALTER TABLE empleados_demo
ADD CONSTRAINT email_unico UNIQUE (email);

-- Can I remove constraints? yes and it's an irreversible action
ALTER TABLE empleados_demo
DROP CONSTRAINT email_unico;

-- Can I delete a column? yes and it's an irreversible action
ALTER TABLE empleados_demo 
DROP activo;

-- Can I rename the table?
ALTER TABLE empleados_demo
RENAME TO empleados_v2;