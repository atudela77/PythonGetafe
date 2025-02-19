-- Consultas entre más de dos tablas.
select plantilla.apellido, plantilla.funcion, hospital.nombre, sala.nombre
from plantilla 
inner join sala on plantilla.sala_cod = sala.sala_cod and plantilla.hospital_cod = sala.hospital_cod
inner join hospital on hospital.hospital_cod = sala.hospital_cod;

/* Subconsultas */
-- Mostrar los datos del empleado que gana el salario más alto.
-- Consulta para saber el salario máximo de los empleados.
select max(salario) salario_maximo from emp;
-- Consulta con el salario máximo obtenido en la consulta anterior
select  apellido, oficio, salario from emp where salario = 650000;
-- Subconsulta equivalente
select apellido, oficio, salario from emp where salario = (select max(salario) from emp);


-- Mostrar todos los empleados que compartan departamento con el empleado que gana mayor salario.
select apellido, oficio, salario, dept_no from emp where dept_no = (select dept_no from emp where salario = (select max(salario) from emp));

-- Mostrar todos los empleados que compartan oficio con el empleado que se apellida 'sala'
select apellido, oficio, dept_no, salario from emp where oficio = (select oficio from emp where apellido = 'sala');

-- Mostrar todos los empleados que compartan oficio con el empleado que se apellida 'sala' y cuyo salario sea mayo que el del empleado apellidado 'ford'
select apellido, oficio, dept_no, salario from emp where oficio = (select oficio from emp where apellido = 'sala') and salario > (select salario from emp where apellido = 'ford');

-- Subconsulta que devuelve más de un valor
select emp_no, apellido, oficio, dept_no, salario from emp where oficio IN (select oficio from emp where apellido = 'sala' or apellido = 'jimenez');

-- Empleados que cobran el máximo de su departamento
select emp_no, initcap(apellido) apellido, oficio, dept_no, salario from emp a where salario = (select max(salario) from emp where dept_no = a.dept_no) order by dept_no;

-- UNION - Quita registros duplicados
select lpad(emp_no, 6, '0') identificador, initcap(apellido) apellido, initcap(lower(oficio)) ocupacion, to_char(salario, '999,999')||'€' sueldo, 'Empleado' tabla from emp
union
select lpad(empleado_no, 6, '0'), initcap(apellido), initcap(lower(funcion)), to_char(salario, '999,999')||'€' , 'Plantilla' tabla from plantilla 
union
select lpad(doctor_no, 6, '0'), initcap(apellido), initcap(lower(especialidad)), to_char(salario, '999,999')||'€' , 'Doctor' tabla from doctor
order by 1;

-- UNION ALL - No quita registros duplicados, muestra el contenido completo de todas las consultas indicadas.
select apellido, oficio, salario from emp
UNION ALL
select apellido, oficio, salario from emp
ORDER BY 1;

-- SELECT TO SELECT -- Vamos, cambiar al tabla del FROM por una SELECT.
select * 
from 
(
    select lpad(emp_no, 6, '0') identificador, initcap(apellido) apellido, initcap(oficio) ocupacion, to_char(salario, '999,999')||'€' sueldo, 'Empleado' tabla from emp
    union
    select lpad(empleado_no, 6, '0'), initcap(apellido), initcap(funcion), to_char(salario, '999,999')||'€' , 'Plantilla' tabla from plantilla 
    union
    select lpad(doctor_no, 6, '0'), initcap(apellido), initcap(especialidad), to_char(salario, '999,999')||'€' , 'Doctor' tabla from doctor
) 
tabla_union;


-- SELECT TO SELECT -- 2
select * from
(select apellido, oficio ocupacion, salario sueldo from emp
union
select apellido, funcion, salario from plantilla
union
select apellido, especialidad,salario from doctor) consulta
where sueldo >= 350000
order by ocupacion;


-- Consulta a nivel de fila >> CASE WHEN
select 
    initcap(apellido) apellido, 
    funcion, 
    case turno 
        when 'T' then 'Tarde' 
        when 'M' then 'Mañana' 
        when 'N' then 'Noche' 
        else Null 
        end turno 
from plantilla;
