programa anida;
vars
  i, n : entero;
inicio
{
  i = 0;
  n = 10;
  mientras (i < n) haz {
    si (i == 5) {
      [
        escribe("medio");
        i = i + 1;
      ]
    } sino {
      i = i + 1;
    };
  };
}
fin
