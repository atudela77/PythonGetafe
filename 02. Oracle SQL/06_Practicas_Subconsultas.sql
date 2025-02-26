-- 1. Mostrar le número de empleado, el apellido y la fecha de alta del empleado
--     más antiguo de la empresa.
select emp.emp_no, emp.apellido, emp.fecha_alt
from emp
where emp.fecha_alt = (select min(emp.fecha_alt) from emp);

-- 2. Mostrar el número de empleado, el apellido y la fecha de alta del empleado
--     más reciente de la mepresa.
select emp.emp_no, emp.apellido, emp.fecha_alt
from emp
where emp.fecha_alt = (select max(emp.fecha_alt) from emp);

-- 3. Visualizar el apellido y el salario de los empleados con el mismo oficio
--     que Jiménez.
select emp.apellido, emp.salario
from emp
where emp.oficio = (select emp.oficio from emp where emp.apellido = 'jimenez');

-- 4. Queremos saber el apellido, oficio, salario y número de departamento de 
--     los empleados con salario mayor que el mejor salario del departamento 30.
select emp.apellido, emp.oficio, emp.salario, emp.dept_no
from emp
where emp.salario > (select max(emp.salario) from emp where dept_no = 30);

-- 5. Mostrar el apellido, la función u oficio, sala o departamento de todos los
--     empleados que trabajen en Empresa o plantilla.
select emp.apellido apellido, emp.oficio funcion, dept.dnombre oficina
from emp
inner join dept
on emp.dept_no = dept.dept_no
union
select plantilla.apellido, plantilla.funcion, sala.nombre
from plantilla
inner join sala
on plantilla.sala_cod = sala.sala_cod
order by 1;

-- 6. Mostrar apellidos y oficio de los empleados del departamento 20 cuyo
--     trabajo sea el mismo que el de cualquier empleado de ventas.
select emp.apellido, emp.oficio
from emp
where emp.dept_no = 20 and
emp.oficio in 
(
    select emp.oficio 
    from emp 
    where emp.dept_no = (select dept.dept_no from dept where dept.dnombre = 'VENTAS')
);
-- SOLUCIÓN 2
select emp.apellido, emp.oficio
from emp
where emp.dept_no = 20 and
emp.oficio in 
(
    select emp.oficio 
    from emp 
    inner join dept 
    on emp.dept_no = dept.dept_no and dept.dnombre = 'VENTAS'
);

-- 7. Mostrar los empleados que tienen mejor salario que la media de los directores, no 
--     incluyendo al presidente
select emp.emp_no, emp.apellido, emp.oficio, emp.dir, emp.fecha_alt, emp.salario
from emp
where emp.salario > (select avg(emp.salario) from emp where emp.oficio = 'DIRECTOR')
and oficio <> 'PRESIDENTE';

-- 8. Mostrar el apellido, función, salario y código de hospital de los empleados
--     de la plantilla que siendo enfermeros o enfermeras pertenecen al hospital
--     San Carlos.
select plantilla.apellido, plantilla.funcion, plantilla.salario, plantilla.hospital_cod,
hospital.nombre
from plantilla
inner join hospital
on plantilla.hospital_cod = hospital.hospital_cod
where plantilla.funcion like 'ENFERMER_' and hospital.nombre = 'san carlos';

-- 9. Averiguar el salario de todas las personas de la bbdd, de forma que se 
--     aprecien las diferencias salariales entre ellos.
select personal.apellido, personal.oficio, personal.salario 
from
(
select emp.apellido, emp.oficio, emp.salario from emp
union
select plantilla.apellido, plantilla.funcion, plantilla.salario from plantilla
union
select doctor.apellido, doctor.especialidad, doctor.salario from doctor
) personal
order by salario desc;

-- 10. Realizar la misma consulta anterior, pero solamente mostraremos las
--      personas cuyo oficio acabe en O.
select personal.apellido, personal.oficio, personal.salario 
from
(
select emp.apellido, emp.oficio, emp.salario from emp
union
select plantilla.apellido, plantilla.funcion, plantilla.salario from plantilla
union
select doctor.apellido, doctor.especialidad, doctor.salario from doctor
) personal
where personal.oficio like '%O'
order by salario desc;

-- 11.Visualizar los datos de los hospitales que tienen personal (doctores) de 
--     cardiología
select * 
from hospital
where hospital.hospital_cod in 
(select doctor.hospital_cod from doctor where doctor.especialidad = 'Cardiologia');

-- 12. Visualizar el apellido y el salario anual de los empleados de la plantilla del
--      Hospital provincial y general.
select plantilla.apellido, plantilla.salario * 12 salarioanual
from plantilla
where plantilla.hospital_cod in 
(
select hospital.hospital_cod from hospital where hospital.nombre in ('provincial','general')
);

-- 13. Mostrar el apellido de los enfermos que nacieron antes que el señor Miller
select enfermo.apellido
from enfermo
where enfermo.fecha_nac < 
(
    select enfermo.fecha_nac
    from enfermo
    where enfermo.apellido = 'Miller G.'
);

-- 14. Crear un informe para evaluar cómo van las cuentas generales de la empresa.
--      Para ello, necesitamos saber lo que cobra cada persona por cada oficio de 
--      manera detallada. Necesitamos el máximo salario y el mínimo más la media 
--      salarial, el total de sueldos y el número de trabajadores que hay en cada
--      puesto de toda la base de datos.
select personal.oficio, max(personal.salario) maximo, round(avg(personal.salario),2) media, 
sum(personal.salario) suma, min(personal.salario) minimo, count(personal.oficio) numero
from
(
select emp.oficio, emp.salario from emp
union
select plantilla.funcion, plantilla.salario from plantilla
union
select doctor.especialidad, doctor.salario from doctor
) personal
group by personal.oficio
order by maximo desc;