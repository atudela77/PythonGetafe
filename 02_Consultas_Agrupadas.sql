-- Contar el número de registros de la tabla emp.
select count(*) num_registros from emp;
-- Mostrar el número de registros y el máximo salario de la tabla emp
select count(*) num_registros, max(salario) max_salario from emp;
-- Mostrar el número de personas por cada oficio.
select oficio, dept_no, count(*) num_personas from emp group by oficio, dept_no order by 1, 2;
-- Mostrar el número de personas por cada oficio pero solamente del departament (10 y 20)
select oficio, count(*) personas from emp where dept_no in (10, 20) group by oficio;
-- Mostrar el número de personas por cada oficio pero solamente los oficios donde haya más de una persona trabajando.
select oficio, count(*) personas from emp group by oficio having count(*) > 1 order by oficio;

-- Ejercicios de agrupaciones
-- Encontrar el sueldo medio de los analistas, mostrando el número de empleados con oficio de analista.
select oficio, avg(salario) sueldo_medio, count(*) num_empleados from emp where oficio = 'ANALISTA' group by oficio;
-- Visualizar el núnero de enfermeros, enfermeras e interinos que hay en la plantilla, ordenados por la función
select funcion, count(*) num_personas from plantilla group by funcion order by funcion;
-- Calcular el valor medio de las camas para cada nombre de sala. Indicar el nombre de cada sala y el número de cada una de ellas.
select nombre, round(avg(num_cama),2) numero_camas, count(*) num_salas from sala group by nombre;
-- Calcular el salario medio de la plantilla de la sala 6, según la función que realizan. Indicar al función y el número de empleados.
select funcion, count(*) num_empleados, cast(avg(salario) as decimal(10,2)) salario_medio from plantilla where sala_cod = 6 group by funcion;
-- Mostrar el número de hombres y el núymero de muheres qye hay entre los enfermos
select sexo, count(*) num_personas from enfermo group by sexo;
-- Mostrar la suma total del salario que cobran los empleados de la plantilla para cada función y turno.
select funcion, turno, sum(salario) salario_total from plantilla group by funcion, turno;



/* *********************** COSAS MIAS **************************** */
select dept_no, count(*) registros from emp group by dept_no order by 1;
select count(*) deptos, sum(dept_no) suma, cast(avg(dept_no) as decimal(10,2)) media, round(stddev(dept_no),2) desv_std, round(variance(dept_no),2) varianza from emp;
with e as (select dept_no, 21.58 media, power(dept_no - 21.58,2) resta from emp)
select round(sqrt(sum(resta)/(count(*)-1)),2) desv_std, round(sum(resta)/(count(*)-1),2) var from e;
select oficio, count(*) from emp;