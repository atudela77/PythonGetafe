-- Mostrar el apellido, oficio, nombre de departamento y localidad de los empleados
SELECT
    emp.apellido,
    emp.oficio,
    dept.dnombre,
    dept.loc
FROM
         emp
    INNER JOIN dept ON emp.dept_no = dept.dept_no;
-- Mostrar el apellido, oficio, nombre de departamento y localidad de los empleados de Sevilla
SELECT
    emp.apellido,
    emp.oficio,
    dept.dnombre,
    dept.loc
FROM
         emp
    INNER JOIN dept ON emp.dept_no = dept.dept_no
WHERE
    dept.loc = 'SEVILLA';
-- Mostrar el número de personas por cada departamento y localización
SELECT
    dept.dnombre,
    dept.loc,
    COUNT(*) num_empleados
FROM
         emp
    INNER JOIN dept ON emp.dept_no = dept.dept_no
GROUP BY
    dept.dnombre,
    dept.loc;
-- Mostrar el apellido, función y nombre de hospital de las personas de la plantilla
SELECT
    plantilla.apellido,
    plantilla.funcion,
    hospital.nombre nombre_hospital
FROM
         plantilla
    INNER JOIN hospital ON plantilla.hospital_cod = hospital.hospital_cod;

--
    



-- INNER
SELECT
    emp.apellido,
    emp.dept_no  dep_emp,
    dept.dept_no dep_dept,
    dept.loc
FROM
         emp
    INNER JOIN dept ON emp.dept_no = dept.dept_no;
-- LEFT
SELECT
    emp.apellido,
    emp.dept_no  dep_emp,
    dept.dept_no dep_dept,
    dept.loc
FROM
    emp
    LEFT JOIN dept ON emp.dept_no = dept.dept_no;
-- RIGHT
SELECT
    emp.apellido,
    emp.dept_no  dep_emp,
    dept.dept_no dep_dept,
    dept.loc
FROM
         emp right
    JOIN dept ON emp.dept_no = dept.dept_no;
-- FULL
SELECT
    emp.apellido,
    emp.dept_no  dep_emp,
    dept.dept_no dep_dept,
    dept.loc
FROM
         emp full
    JOIN dept ON emp.dept_no = dept.dept_no;
-- CROSS --> Producto cartesiano
SELECT
    emp.apellido,
    emp.dept_no  dep_emp,
    dept.dept_no dep_dept,
    dept.loc
FROM
         emp
    CROSS JOIN dept;




-- Mostrar apellido, salario y especialidad junto a la dirección del hospital donde trabaja
-- de todos los doctores de la paz
SELECT
    doctor.apellido,
    doctor.salario,
    doctor.especialidad,
    hospital.direccion
FROM
         doctor
    INNER JOIN hospital ON doctor.hospital_cod = hospital.hospital_cod
WHERE
    hospital.nombre = 'la paz';


-- Mostrar cuantas personas trabajan en cada departamento mostrando el nombre del departamento
select dept.dnombre, count(emp_no) num_empleados
from dept left join emp on dept.dept_no = emp.dept_no
group by dept.dnombre;

