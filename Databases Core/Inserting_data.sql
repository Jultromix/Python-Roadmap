-- Making a "basic insert", alwys speicfy the columns (works nice with few data)
INSERT INTO paises (nombre,codigo) VALUES ('Chile', 'CHL');
INSERT INTO paises (nombre,codigo) VALUES ('Argentina', 'arg');

-- For more data
INSERT INTO paises (nombre,codigo) VALUES
  ('México','MEX'),
  ('Colombia','COL'),
  ('Perú','PER'),
  ('Brasil','BRA');

SELECT * FROM paises;

-- Adding records but this time, it'll return what what's just added
INSERT INTO categorias (nombre) VALUES ('electronica')
RETURNING categoria_id, nombre;


-- Now return the whole column
INSERT INTO tipo_clientes (nombre) VALUES ('Premium')
RETURNING*;

INSERT INTO tipo_clientes (nombre) VALUES
  ('Estándar'),
  ('Corporativo'),
  ('Mayorista')
RETURNING tipo_cliente_id, nombre;

-- Adding with foreing key
INSERT INTO clientes (nombre, email, tipo_cliente_id) 
VALUES ('Maria Martinez','marymar@example.com',1)
RETURNING cliente_id, nombre, email;