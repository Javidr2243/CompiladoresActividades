programa cober;
vars
  a, b, c : entero;
  f : flotante;
nula imprimePar(n : entero)
{
  {
    si (n != 0) { escribe("par:", n); } sino { escribe("cero"); };
    regresa;
  }
};
flotante triple(x : flotante)
{
  vars
    t : flotante;
  {
    t = x * 3.0;
    regresa t;
  }
};
inicio
{
  a = 1;
  b = 2;
  c = 3;
  [
    a = a + 1;
    si (a < b) {
      mientras (a < c) haz {
        si (a == b) { escribe("igual"); };
        a = a + 1;
      };
    } sino {
      escribe("ya no", a);
    };
  ]
  imprimePar(a);
  f = triple(1.5);
}
fin
