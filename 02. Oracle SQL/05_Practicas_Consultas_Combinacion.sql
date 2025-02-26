-- 1. Seleccionar el apellido, oficio, slario, num dept y su nombre de todos los empleados
--     cuyo salrio sea mayor de 3000000
select emp.apellido, emp.oficio, emp.salario, emp.dept_no, dept.dnombre
from emp 
inner join dept
on emp.dept_no = dept.dept_no
where salario > 300000;

-- 2. Mostrar todos los nombres de Hospital con sus nombres de salas correspondientes
select sala.nombre nombresala, hospital.nombre nombrehospital
from hospital 
inner join sala 
on hospital.hospital_cod = sala.hospital_cod;

-- 3. Calcular cuántos trabajadores de la empresa hay en cada ciudad
select count(emp.emp_no) trabajadores, dept.loc ciudad
from emp 
right join dept
on emp.dept_no = dept.dept_no
group by dept.loc;

-- 4. Visualizar cuantas personas realizan cda oficio en cada departamento mostrando
--     el nombre del departamento
select dept.dnombre, count(emp.emp_no) personas, emp.oficio
from emp
right join dept
on emp.dept_no = dept.dept_no
group by dept.dnombre, emp.oficio;

-- 5. Contar cuantas salas hay en cada hospital, mostrando el nombre de las salas y 
--     el nombre del hospital.
select hospital.nombre nombrehospital, sala.nombre nombresala, count(sala.sala_cod) numerosalas
from hospital
left join sala
on hospital.hospital_cod = sala.hospital_cod
group by hospital.nombre, sala.nombre;

-- 6. Queremos saber cuántos trabajadores se diero de alta entre el año 1997 y
--     1998 y en qué departamento.
select dept.dnombre departamento, count(emp.emp_no) altas
from emp 
inner join dept 
on emp.dept_no = dept.dept_no
where fecha_alt between '01/01/1997' and '31/12/1998'
group by dept.dnombre;

-- 7. Buscar aquellas ciudades con cuatro o más personas trabajando
select dept.loc ciudad, count(emp.emp_no) personas
from dept
inner join emp
on dept.dept_no = emp.dept_no
group by dept.loc
having count(emp.emp_no) >= 4;

-- 8. Calcular la media salarial por ciudad. Mostrar solamente la media para Madrid y ¿?
select dept.loc ciudad, avg(emp.salario) media_salarial
from dept
left join emp
on dept.dept_no = emp.dept_no
group by dept.loc
having dept.loc in ('MADRID', 'SEVILLA');

-- 9. Mostrar los doctores junto con el nombre del hospital en el que ejercen, 
--     la dirección y el teléfono del mismo.
select doctor.apellido, hospital.nombre, hospital.direccion, hospital.telefono 
from doctor 
inner join hospital
on doctor.hospital_cod = hospital.hospital_cod;

-- 10. Mostrar los nombres de los hospitales junto con el mejor salario de los empleados
--      de la plantilla de cada hospital.
select hospital.nombre, max(plantilla.salario) salariomaximo
from hospital
inner join plantilla
on hospital.hospital_cod = plantilla.hospital_cod
group by hospital.nombre;

-- 11. Visualizar el apellido, función y turno de los empleados de la plantilla junto con el
--      nombre de la sala y el nombre del hospital con el teléfono
select plantilla.apellido, plantilla.funcion, plantilla.turno, sala.nombre nombresala,
hospital.nombre nombrehospital, hospital.telefono
from plantilla
inner join hospital
on plantilla.hospital_cod = hospital.hospital_cod
inner join sala
on sala.hospital_cod = plantilla.hospital_cod and sala.sala_cod = plantilla.sala_cod;

-- 12. Visualizar el máximo salario, mínimo salario de los directores dependiendo de la ciudad
--  en la que trabajen. Indicar el número total de directores por ciudad.
select count(emp.oficio) directores, dept.loc, max(emp.salario) salariomaximo, min(emp.salario) salariominimo
from dept
left join emp
on dept.dept_no = emp.dept_no
where emp.oficio = 'DIRECTOR'
group by dept.loc;

-- 13. Averiguar la combinación de qué salas podría haber por cada uno de los hospitales
select sala.nombre nombresala, hospital.nombre nombrehospital
from sala
cross join hospital
order by nombrehospital;