programa medio;
vars
  x, y : entero;
entero suma(a : entero, b : entero)
{
  vars
    r : entero;
  {
    r = a + b;
    regresa r;
  }
};
inicio
{
  entrada(x);
  y = suma(x, 2);
  si (y == 0) { escribe(y); };
  mientras (y > 0) haz { y = y - 1; };
}
fin
