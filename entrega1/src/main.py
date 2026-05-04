"""
main.py — punto de entrada del scanner+parser de Patito.

Uso: python main.py <archivo.pat>
"""

import sys
from dataclasses import dataclass

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from PatitoLexer import PatitoLexer
from PatitoParser import PatitoParser


@dataclass
class ErrorSintaxis:
    linea: int
    columna: int
    mensaje: str
    fuente: str  # "lexer" o "parser"
    token: str | None = None  # texto del símbolo que ofendió, si aplica


class PatitoErrorListener(ErrorListener):
    """
    Acumula errores en una lista en lugar de imprimirlos.
    Una instancia por fuente (lexer o parser) para saber de dónde vino cada error.
    """

    def __init__(self, fuente: str):
        super().__init__()
        self.fuente = fuente
        self.errores: list[ErrorSintaxis] = []

    def syntaxError(self, _recognizer, offendingSymbol, line, column, msg, _e):
        # Firma impuesta por ANTLR (heredada de ErrorListener).
        # offendingSymbol es un Token cuando viene del parser, o None desde el lexer.
        token_texto = offendingSymbol.text if offendingSymbol is not None else None
        self.errores.append(
            ErrorSintaxis(line, column, msg, self.fuente, token_texto)
        )


def main() -> int:
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo.pat>", file=sys.stderr)
        return 1

    ruta = sys.argv[1]

    # 1) Cargar el archivo como stream ANTLR.
    input_stream = FileStream(ruta, encoding="utf-8")

    # 2) Lexer + su listener custom.
    lexer = PatitoLexer(input_stream)
    lexer_listener = PatitoErrorListener(fuente="lexer")
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_listener)

    # 3) Buffer de tokens.
    token_stream = CommonTokenStream(lexer)

    # 4) Parser + su listener custom.
    parser = PatitoParser(token_stream)
    parser_listener = PatitoErrorListener(fuente="parser")
    parser.removeErrorListeners()
    parser.addErrorListener(parser_listener)

    # 5) Parsear desde la regla raíz.
    parser.programa()

    # 6) Reporte final basado en lista, no en el contador interno.
    errores = lexer_listener.errores + parser_listener.errores

    if not errores:
        print(f"Programa válido: {ruta}")
        return 0

    print(f"Programa inválido: {ruta}", file=sys.stderr)
    for err in errores:
        print(
            f"  [{err.fuente}] línea {err.linea}:{err.columna} — {err.mensaje}",
            file=sys.stderr,
        )
    print(f"Total: {len(errores)} error(es)", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
