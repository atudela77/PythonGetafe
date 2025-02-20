-- Insert sin listar las columnas.
select * from dept;
insert into dept values (50, 'PYTHON','GETAFE');

-- Insert listando las columnas.
insert into dept (dept_no, dnombre) values (60, 'I+D');

-- Insert con subconsulta
select * from plantilla;
-- Sacamos el número de empleado más grande.
select max(empleado_no) from plantilla;
-- Obteniendo el número de empleado más alto antes de insertar --> 9901
insert into plantilla (empleado_no, apellido, funcion, hospital_cod) values (9902, 'López', 'ENFERMERA', 22);
-- Obteniedo el número de empleado más alto con una subconsulta en el insert.
insert into plantilla (empleado_no, apellido, funcion, hospital_cod) values ((select max(empleado_no) + 1 from plantilla), 'Super López', 'ENFERMERA', 22);

-- Delete
-- delete from plantilla; --> Borra la tabla completa
delete from plantilla where apellido = 'Super López';
-- Otra
delete from plantilla where apellido like '%López';
-- delete con subconsulta 
delete from plantilla where hospital_cod = (select hospital_cod from hospital where nombre = 'El Carmen');

-- Update
select * from plantilla;
-- Se puede hacer referencia al contenido del campo, p. ej., salario = salario + 1
update plantilla set salario = salario + 1, funcion = 'INTERINA' where funcion = 'INTERINO';
-- Actualizar el salario de la plantilla de la sala cuadro al salario que tiene karplus
update plantilla set salario = (select salario from plantilla where apellido = 'karplus w.') where sala_cod = 4;
-- Modificar el turno a Mañana a todos los empleados de plantilla de la sala 
update plantilla set turno = 'M' where sala_cod in (select sala_cod from sala where nombre = 'psiquiatria');

--
insert into plantilla (empleado_no, hospital_cod, apellido, funcion, turno, sala_cod)
values
((select max(empleado_no) + 1 from plantilla), (select hospital_cod from hospital where nombre = 'El Carmen'), 'Cabrales', 'ENFERMERA', 'M', 4);
-- Borra los registros de plantilla que no tienen código de hospital
delete from plantilla where hospital_cod is null;
-- La siguiente no borra lo que se quiere, que sería lo mismo que lo anterior
delete from plantilla where hospital_cod not in (select hospital_cod from hospital);


