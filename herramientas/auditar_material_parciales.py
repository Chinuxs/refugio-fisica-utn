"""Inventario reproducible; no modifica ni elimina las fuentes externas."""
import argparse
import csv
import hashlib
from pathlib import Path


def sha256(path):
    # Prefijo extendido para los nombres largos presentes en Windows.
    full = str(path.resolve())
    if full[1:3] == ':\\':
        full = '\\\\?\\' + full
    digest = hashlib.sha256()
    with open(full, 'rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('base', type=Path)
    parser.add_argument('salida', type=Path)
    args = parser.parse_args()
    base = args.base.resolve()
    roots = ['8.2do Parcialito', '12. 3er Parcialito']
    reference_roots = ['6. Trabajo & Energia', '7. MAS', '8. Modelo sistema de partículas']
    references = {}
    for name in reference_roots:
        for path in sorted((base / name).rglob('*')):
            if path.is_file() and path.suffix.lower() not in {'.rar', '.mp4'}:
                references.setdefault(sha256(path), []).append(str(path.relative_to(base)))
    rows = []
    seen = {}
    for name in roots:
        for path in sorted((base / name).rglob('*')):
            if not path.is_file():
                continue
            digest = sha256(path)
            relative = str(path.relative_to(base))
            matches = references.get(digest, []) + seen.get(digest, [])
            rows.append({'archivo': relative, 'bytes': path.stat().st_size,
                         'sha256': digest, 'duplicado_exacto_de': ' | '.join(matches),
                         'tipo': path.suffix.lower().lstrip('.')})
            seen.setdefault(digest, []).append(relative)
    with args.salida.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f'{len(rows)} archivos; {sum(bool(r["duplicado_exacto_de"]) for r in rows)} '
          f'copias exactas respecto de archivos externos ya registrados.')


if __name__ == '__main__':
    main()
