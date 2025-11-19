#!/usr/bin/env python3
"""
process_text.py

Lê 'entrada.txt', aplica regras de processamento e grava o resultado em 'saida.txt',
garantindo que o arquivo original permaneça inalterado.

Regras aplicadas:
- Substituir todas as ocorrências de "problema" por "desafio", preservando plural e capitalização.
- Remover qualquer linha que contenha a substring "ignor" (caso-insensitivo) — isso cobre "ignorar", "ignorada", etc.
- Manter todas as demais linhas intactas.
"""
from pathlib import Path
import re
import sys

INPUT_FILE = Path("entrada.txt")
OUTPUT_FILE = Path("saida.txt")

# Regex para localizar 'problema' com possível plural 's', com bordas de palavra
_PROBLEMA_RE = re.compile(r"\b(problema)(s)?\b", flags=re.IGNORECASE)

# Regex para detectar linhas a remover (qualquer ocorrência de 'ignor' — cobre 'ignorar', 'ignorada', ...)
_IGNOR_RE = re.compile(r"ignor", flags=re.IGNORECASE)


def replace_problema_match(m: re.Match) -> str:
    """
    Callback para re.sub que preserva plural e capitalização.

    Exemplos:
    - "problema" -> "desafio"
    - "problemas" -> "desafios"
    - "Problema" -> "Desafio"
    - "PROBLEMAS" -> "DESAFIOS"
    """
    base = m.group(1)  # 'problema' (original case)
    plural = m.group(2) or ""  # 's' or ''
    # Build replacement in lowercase
    repl = "desafio" + plural.lower()

    # Preserve case:
    if base.isupper():
        repl = repl.upper()
    elif base[0].isupper():
        # Capitalize first letter only (Desafio / Desafios)
        repl = repl.capitalize()

    return repl


def process_lines(lines):
    """Processa uma lista de linhas e retorna uma nova lista com o resultado."""
    out_lines = []
    for line in lines:
        # Se a linha contém 'ignor' (case-insensitive), pule-a (não incluir no output)
        if _IGNOR_RE.search(line):
            continue
        # Substituir ocorrências de 'problema' (com callback para preservar plural/case)
        new_line = _PROBLEMA_RE.sub(replace_problema_match, line)
        out_lines.append(new_line)
    return out_lines


def main():
    if not INPUT_FILE.exists():
        print(f"Arquivo de entrada não encontrado: {INPUT_FILE.resolve()}", file=sys.stderr)
        print("Crie 'entrada.txt' no mesmo diretório com o conteúdo de exemplo e execute novamente.", file=sys.stderr)
        sys.exit(1)

    # Ler todo o conteúdo (preservando quebras de linha)
    text = INPUT_FILE.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)  # keepends para preservar quebras de linha originais

    processed = process_lines(lines)

    # Escrever o arquivo de saída. Isso não modifica o arquivo de entrada.
    OUTPUT_FILE.write_text("".join(processed), encoding="utf-8")
    print(f"Processamento concluído. Arquivo gravado em: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()