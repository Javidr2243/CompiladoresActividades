grammar Patito;

// ============================================================ PARSER RULES (minúsculas)
// ============================================================ Orden: bottom-up (hojas → raíz). Las
// reglas más simples van primero; 'programa' (regla raíz) cierra el bloque al final.

// Relglas EBNF para ANTLR

// ---- 1. tipo ----
tipo: 'entero' | 'flotante';

// ---- 2. cte ----
cte: CTE_ENT | CTE_FLOT;

// ---- 3. factor ----
factor: '(' expresion ')' | ('+' | '-')? ( ID | cte) | llamada;

// ---- 4. termino ----
termino: factor ( ('*' | '/') factor)*;

// ---- 5. exp ----
exp: termino ( ('+' | '-') termino)*;

// ---- 6. expresion ----
expresion: exp ( ('>' | '<' | '!=' | '==') exp)?;

// ---- 7. asigna ----
asigna: ID '=' expresion ';';

// ---- 8. llamada ----
llamada: ID '(' expresion (',' expresion)* ')';

// ---- 9. imprime ----
imprime:
	'escribe' '(' (expresion | LETRERO) (
		',' (expresion | LETRERO)
	)* ')' ';';

// ---- 10. entrada ----
entrada: 'entrada' '(' ID ')' ';';

// ---- 11. regresa ---- Regla agregada para poder tener un return.
regresa: 'regresa' expresion? ';';

// ---- 12. condicion ----
condicion: 'si' '(' expresion ')' cuerpo ('sino' cuerpo)? ';';

// ---- 13. ciclo ----
ciclo: 'mientras' '(' expresion ')' 'haz' cuerpo ';';

// ---- 14. estatuto ----
estatuto:
	asigna
	| condicion
	| ciclo
	| llamada ';'
	| imprime
	| entrada
	| regresa
	| '[' estatuto+ ']';

// ---- 15. cuerpo ----
cuerpo: '{' estatuto+ '}';

// ---- 16. vars ----
vars: 'vars' (ID (',' ID)* ':' tipo ';')+;

// ---- 17. funcs ----
funcs:
	('nula' | tipo) ID '(' (ID ':' tipo (',' ID ':' tipo)*)? ')' '{' vars? cuerpo '}' ';';

// ---- 18. programa ----
programa:
	'programa' ID ';' vars? funcs* 'inicio' cuerpo 'fin' EOF;

// ============================================================ LEXER RULES (MAYÚSCULAS)
// ============================================================

// ---- CTE_FLOT ---- Antes que CTE_ENT para poder matchear primero FLOT
CTE_FLOT: [0-9]+ '.' [0-9]+;

// ---- CTE_ENT ----
CTE_ENT: [0-9]+;

// ---- ID ---- Tiene ID menor prioridad que las keywords declaradas antes lo que evita conflictos
ID: [a-zA-Z] [a-zA-Z0-9]*;

// ---- LETRERO ---- cualquier caracter excepto comillas dobles.
LETRERO: '"' ~["]* '"';

// ---- WS ---- Descarta espacios, tabs, CR, LF antes de que lleguen al parser.
WS: [ \t\r\n]+ -> skip;