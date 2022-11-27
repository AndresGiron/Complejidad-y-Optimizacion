% Use this editor as a MiniZinc scratch book
%Valores validos para las paginas de los articulos
var 'union'(0..0,5..9): I;
var 'union'(0..0,4..7): N; 
var 'union'(0..0,2..5): L; 
var 'union'(0..0,2..4): S;  
var 'union'(0..0,1..3): C; 
%El resultado de la funcion objetivo debe ser un entero
var int: P;
%Restricciones 
constraint I + N + L + S + C <= 10;
% Funcion a maximizar
constraint P = I*1500 + N*2000 + L*1000 + S*1500 + C*750;
solve maximize P; 