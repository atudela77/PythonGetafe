/* ************************************* */
/* Clase del lunes 17 de febrero de 2025 */
/* ************************************* */

-- Los comentarios de una línea se indican con doble guión
/*
    Los comentarios de varias lineas se escriben utilizando
     barra asterisco para abrir y asterisco y barra para
     cerrar.
*/
select * from emp;
select * from dept;
select dept_no, dnombre, loc from dept;
select * from enfermo;
select * from emp order by oficio, apellido;
select * from emp where oficio = 'ANALISTA';
select * from emp where salario < 650000;
select * from emp where dept_no = 10 and salario < 600000;
select * from emp where oficio = 'DIRECTOR'; --En Oracle las cadenas de texto son key sensitive
select * from emp where dept_no in (10, 20) order by dept_no;
select * from emp where dept_no = 10 or dept_no = 20;
select * from emp where emp_no >= 7800 and emp_no <=7900;
select * from emp where not oficio = 'VENDEDOR'; -- No utilizar el NOT porque 
select * from emp where oficio <> 'VENDEDOR';
select * from emp where salario between 318500 and 390000;
select * from emp where dept_no in (10, 20) order by dept_no, emp_no;
select * from emp where dept_no not in (10, 20);
select * from emp where apellido like 's%';
select distinct oficio from emp order by 1;
select apellido, (salario + comision) TOTAL from emp 
where (salario + comision) is not null and rownum < 10
order by total desc;


-- Prácticas
-- Mostrar todos los datos de los empleados de nuestra tabla emp
select * from emp;
-- Mostrar el apellido, el oficio, salario anual con las dos extras para 
--  aquellos empleados con comisión mayor de 100000.
select apellido, oficio, salario * 14 salario_anual from emp where comision > 100000;
-- Igual que el entarior pero para aquellos empleados que su salario anual con extras supere las 750000 pesetas
select apellido, oficio, salario * 14 salario_anual from emp where salario * 14 > 750000;
-- Igual que el anterior pero para aquellos empleados que sumen entre salario anual con extras y comision el 1000000.
select apellido, oficio, salario * 14 salario_anual from emp where (salario * 14 + comision) > 1000000;
-- Mostrar todos los datos de empleados ordenados por departamento y dentro de este por oficio para tener una cisión jerárquica.
select * from emp order by dept_no, oficio;
-- Mostrar todos los enfermos nacidos antes del 1/1/70
select * from enfermo where fecha_nac < '01/01/70';
-- Igual que el anterior, para los nacidos antes del 1/1/70 ordenados por número de inscripción
select * from enfermo where fecha_nac < '01/01/70' order by inscripcion;
-- Listar todos los datos de la plantilla del hospital del turno de mañana
select * from plantilla where turno = 'M';
-- Igual que la anterior pero para el turno de noche
select * from plantilla where turno = 'T';
-- Listar los doctores cuyo salario supere los tres millones de pesetas
select * from doctor where salario * 14 > 3000000;
-- Visualiar los empleados de la plantilla del turno de mañana que tengan un salario entre 2000000 y 2250000
select plantilla.* from plantilla where turno = 'M' and (salario * 14) between 2000000 and 2250000; 
-- Visualizar los empleados de la tabla emp que no se dieron de alta entre 1/1/80 y 12/12/82
select * from emp where fecha_alt < '01/01/80' or fecha_alt > '12/12/82';
-- Mostrar los nombres de los departamentos situados en Madrid o en Barcelona
select * from dept where loc in ('MADRID', 'BARCELONA');


select initcap(apellido), instr(oficio, 'D'), lpad(apellido, 30, 'XXX'), rpad(apellido, 30, 'XXX') from emp;

























