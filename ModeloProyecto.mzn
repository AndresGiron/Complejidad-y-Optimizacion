%lectura de datos
int: cat;
array[1..cat] of int: rdrs;
array[1..cat] of int: pagMax;
array[1..cat] of int: pagMin;
int: maxp;

%variables 
array[1..cat] of var int: typeNews;


%restricciones
constraint sum(j in 1..cat) (typeNews[j]) <= maxp;
constraint forall(j in 1..cat) ((typeNews[j] <= pagMax[j] /\ typeNews[j] >= pagMin[j]) xor typeNews[j] = 0);


%objetivo
var int: utility; 
constraint utility = sum(j in 1..cat)(typeNews[j]*rdrs[j]);
solve maximize utility;
