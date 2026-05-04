"""
test_runner.py ejecuta main.py contra todos los .pat en validos/ e invalidos/
y reporta el resultado de cada caso.

Uso (desde la raíz del proyecto):
    python entrega1/tests/test_runner.py

Se utilizo Claude para realizar el test_runner
"""

import subprocess
import sys
from pathlib import Path


# Rutas relativas a este archivo, no al cwd. Así el runner funciona desde cualquier directorio.
TESTS_DIR = Path(__file__).resolve().parent
PROGRAMAS_DIR = TESTS_DIR / "programas"
MAIN_PY = TESTS_DIR.parent / "src" / "main.py"


def correr_main(archivo: Path) -> int:
    """Invoca main.py con el archivo dado y devuelve su exit code."""
    resultado = subprocess.run(
        [sys.executable, str(MAIN_PY), str(archivo)],
        capture_output=True,  # silencia stdout/stderr del hijo
        text=True,
    )
    return resultado.returncode


def descubrir_casos() -> list[tuple[Path, str]]:
    """Devuelve [(archivo, esperado)] donde esperado ∈ {'valido', 'invalido'}."""
    casos: list[tuple[Path, str]] = []
    for archivo in sorted((PROGRAMAS_DIR / "validos").glob("*.pat")):
        casos.append((archivo, "valido"))
    for archivo in sorted((PROGRAMAS_DIR / "invalidos").glob("*.pat")):
        casos.append((archivo, "invalido"))
    return casos


def main() -> int:
    if not MAIN_PY.exists():
        print(f"ERROR: no encuentro {MAIN_PY}", file=sys.stderr)
        return 2

    casos = descubrir_casos()
    if not casos:
        print(
            f"ERROR: no hay archivos .pat en {PROGRAMAS_DIR}", file=sys.stderr)
        return 2

    print("=== Test Results ===")

    pasados = 0
    fallidos: list[Path] = []

    for archivo, esperado in casos:
        exit_code = correr_main(archivo)
        actual = "valido" if exit_code == 0 else "invalido"
        ok = (esperado == actual)
        marca = "PASS" if ok else "FAIL"
        rel = archivo.relative_to(PROGRAMAS_DIR)
        print(f"{marca}  {rel}  (esperado: {esperado}, resultado: {actual})")
        if ok:
            pasados += 1
        else:
            fallidos.append(rel)

    total = len(casos)
    print("---")
    print(f"{pasados}/{total} passed, {total - pasados} failed")

    return 0 if pasados == total else 1


if __name__ == "__main__":
    sys.exit(main())
