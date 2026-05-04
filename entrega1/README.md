# Entrega 1 — Scanner y Parser de Patito

Analizador léxico y sintáctico para **Patito**, un mini-lenguaje pedagógico de tipado estático con sintaxis en español. Implementado con **ANTLR4** y **Python 3**.

Recibe un archivo `.pat` y reporta si es sintácticamente válido. Si hay errores, los muestra con línea y columna.

> Parte del repositorio `CompiladoresActividades` del curso TC3002B — Compiladores.

---

## Requisitos

- Python 3.10+
- pip

> Los archivos generados por ANTLR (`PatitoLexer.py`, `PatitoParser.py`, etc.) ya están incluidos. Solo necesitas instalar ANTLR si modificas la gramática.

---

## Instalación

```bash
git clone https://github.com/<tu-usuario>/CompiladoresActividades.git
cd CompiladoresActividades/entrega1

python3 -m venv venv
source venv/bin/activate           # Linux / macOS
# venv\Scripts\activate              # Windows

pip install -r requirements.txt
```

---

## Uso

```bash
# Validar un archivo .pat
python src/main.py <ruta-al-archivo.pat>

# Correr toda la suite de pruebas
python tests/test_runner.py
```

**Convención:** exit code `0` si el programa es válido, `1` si tiene errores. Los errores van a `stderr`, el veredicto a `stdout`.

Para agregar tus propios casos de prueba, coloca archivos `.pat` en `tests/programas/validos/` (deben parsear) o `tests/programas/invalidos/` (deben fallar). El runner los descubre automáticamente.

---

## El lenguaje en 30 segundos

```pat
programa demo;
vars
  a : entero;
inicio
{
  a = 1;
}
fin
```

- Tipos: `entero`, `flotante`.
- Control: `si`/`sino`, `mientras`/`haz`.
- Funciones tipadas con `regresa`.
- I/O: `escribe(...)`, `entrada(id)`.
- Comparaciones: `>`, `<`, `==`, `!=` (no encadenables sin paréntesis).

Ejemplos completos en `tests/programas/validos/`.

---

## Modificar la gramática

La fuente de verdad es `src/Patito.g4`. Para regenerar el lexer y parser:

```bash
brew install antlr                 # macOS, primera vez
cd src
antlr -Dlanguage=Python3 -visitor Patito.g4
```

> Tool ANTLR y runtime Python deben estar en la **misma versión** (4.13.2).

---

## Curso

Proyecto académico de **TC3002B — Compiladores** (ITC, Tec de Monterrey). Patito está basado en 18 diagramas de sintaxis (17 originales del enunciado + `REGRESA` como extensión propia).
