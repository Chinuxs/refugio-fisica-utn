"""Recalcula el Lab 2 y exporta un XLSX con fórmulas, sin dependencias.

El original sólo se lee. La unidad de las masas debe elegirse explícitamente.
La unidad elegida es un criterio de cálculo, no una lectura de balanza verificada.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import statistics
from xml.etree import ElementTree as ET
from zipfile import ZipFile, ZIP_DEFLATED

NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'


def numeric_cells(path):
    with ZipFile(path) as archive:
        root = ET.fromstring(archive.read('xl/worksheets/sheet1.xml'))
        return {c.attrib['r']: float(c.find(f'{{{NS}}}v').text)
                for c in root.findall(f'.//{{{NS}}}c')
                if c.attrib.get('t') not in {'s', 'inlineStr', 'str', 'e'}
                and c.find(f'{{{NS}}}v') is not None}


def sheet_xml(rows, widths):
    sheet = ET.Element('worksheet', xmlns=NS)
    cols = ET.SubElement(sheet, 'cols')
    for i, width in enumerate(widths, 1):
        ET.SubElement(cols, 'col', min=str(i), max=str(i), width=str(width), customWidth='1')
    data = ET.SubElement(sheet, 'sheetData')
    for index, values in enumerate(rows, 1):
        row = ET.SubElement(data, 'row', r=str(index))
        for column, value in enumerate(values):
            if value is None:
                continue
            cell = ET.SubElement(row, 'c', r=f'{chr(65 + column)}{index}')
            if isinstance(value, tuple):
                formula, cached = value
                cell.set('s', '1')
                ET.SubElement(cell, 'f').text = formula
                ET.SubElement(cell, 'v').text = repr(float(cached))
            elif isinstance(value, (int, float)):
                cell.set('s', '1')
                ET.SubElement(cell, 'v').text = repr(value)
            else:
                cell.set('t', 'inlineStr')
                ET.SubElement(ET.SubElement(cell, 'is'), 't').text = str(value)
    return ET.tostring(sheet, encoding='utf-8', xml_declaration=True)


def write_xlsx(destination, sheets):
    types = ['<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
             '<Default Extension="xml" ContentType="application/xml"/>',
             '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>',
             '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>']
    names, relations = [], []
    for i, (name, _, _) in enumerate(sheets, 1):
        names.append(f'<sheet name="{name}" sheetId="{i}" r:id="rId{i}"/>')
        relations.append(f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>')
        types.append(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')
    relations.append('<Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>')
    style = f'''<styleSheet xmlns="{NS}"><numFmts count="1"><numFmt numFmtId="164" formatCode="0.000000000000"/></numFmts>
<fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts><fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills>
<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders><cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/><xf numFmtId="164" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/></cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles></styleSheet>'''
    with ZipFile(destination, 'w', ZIP_DEFLATED) as archive:
        archive.writestr('[Content_Types].xml', '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">' + ''.join(types) + '</Types>')
        archive.writestr('_rels/.rels', '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        archive.writestr('xl/workbook.xml', f'<workbook xmlns="{NS}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>' + ''.join(names) + '</sheets><calcPr calcId="0" fullCalcOnLoad="1"/></workbook>')
        archive.writestr('xl/_rels/workbook.xml.rels', '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' + ''.join(relations) + '</Relationships>')
        archive.writestr('xl/styles.xml', style)
        for i, (_, rows, widths) in enumerate(sheets, 1):
            archive.writestr(f'xl/worksheets/sheet{i}.xml', sheet_xml(rows, widths))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('origen', type=Path)
    parser.add_argument('carpeta_salida', type=Path)
    parser.add_argument('--unidad-masas', choices=['g', 'kg'], required=True)
    args = parser.parse_args()
    args.carpeta_salida.mkdir(parents=True, exist_ok=True)
    target = args.carpeta_salida / f'laboratorio-2-propuesta-masas-{args.unidad_masas}.xlsx'
    if target.resolve() == args.origen.resolve():
        raise ValueError('La salida debe ser distinta del original')
    original_hash = hashlib.sha256(args.origen.read_bytes()).hexdigest()
    cells = numeric_cells(args.origen)
    raw = [cells[c] for c in ['E3', 'F3', 'G3']]
    factor = 0.001 if args.unidad_masas == 'g' else 1.0
    M, m1, m2 = [v * factor for v in raw]
    distance, height, g = cells['H3'], cells['I3'], 9.8
    if not math.isclose(distance, height):
        raise ValueError('Revisar el vínculo: se espera Δh = ΔX')
    mt = M + m1 + m2
    velocities = [(cells[f'B{i}'], cells[f'C{i}']) for i in range(4, 9)]
    values = []
    for number, (v1, v2) in enumerate(velocities, 1):
        k1, k2 = mt * v1**2 / 2, mt * v2**2 / 2
        u1, u2 = m1 * g * height, m2 * g * height
        values.append([number, k1, k2, k2-k1, u1, u2, u2-u1, k2-k1+u2-u1])
    mean = statistics.mean(r[7] for r in values)
    for row in values:
        error = mean - row[7]
        row.extend([error, error**2])
    sumsq = sum(r[9] for r in values)
    n = len(values)
    sem = math.sqrt(sumsq / (n * (n-1)))

    datos = [
        ['Laboratorio 2: resultados revisados; originales conservados'],
        [f'Unidad adoptada para las masas originales: {args.unidad_masas}. No es una lectura de balanza verificada.'],
        ['El archivo original no se modifica. Modelo de la consigna; g = 9,8 m/s².'],
        ['Magnitud', 'Valor', 'Unidad'],
        ['M original', raw[0], args.unidad_masas],
        ['m1 original', raw[1], args.unidad_masas],
        ['m2 original', raw[2], args.unidad_masas],
        ['Delta X', distance, 'm'],
        ['Delta h', height, 'm'],
        ['g', g, 'm/s²'],
        ['Factor a kg', factor, 'kg/unidad original'],
        ['M en SI', ('B5*B11', M), 'kg'],
        ['m1 en SI', ('B6*B11', m1), 'kg'],
        ['m2 en SI', ('B7*B11', m2), 'kg'],
        ['Masa total', ('SUM(B12:B14)', mt), 'kg'],
        [], ['n', 'v1 (m/s)', 'v2 (m/s)'],
    ] + [[i, v1, v2] for i, (v1, v2) in enumerate(velocities, 1)]
    result = [
        ['Resultados del modelo con la unidad adoptada declarada en Datos'],
        ['Tabla II: columnas B-G; Tabla III: columnas H-J. Unidades de e²: J².'],
        [], ['n', 'K1 (J)', 'K2 (J)', 'Delta K (J)', 'U1 (J)', 'U2 (J)', 'Delta U (J)', 'Wfr (J)', 'e = Wmedio-Wfr (J)', 'e² (J²)'],
    ]
    for i, row in enumerate(values, 5):
        d = i + 13
        formulas = [f'0.5*Datos!$B$15*Datos!B{d}^2', f'0.5*Datos!$B$15*Datos!C{d}^2',
                    f'C{i}-B{i}', 'Datos!$B$13*Datos!$B$10*Datos!$B$9',
                    'Datos!$B$14*Datos!$B$10*Datos!$B$9', f'F{i}-E{i}',
                    f'D{i}+G{i}', f'$B$12-H{i}', f'I{i}^2']
        result.append([row[0]] + list(zip(formulas, row[1:])))
    result += [[], [], ['Wfr medio (J)', ('AVERAGE(H5:H9)', mean)],
               ['Suma e² (J²)', ('SUM(J5:J9)', sumsq)],
               ['n', ('COUNT(H5:H9)', n)],
               ['Error del valor medio (J)', ('SQRT(B13/(B14*(B14-1)))', sem)],
               ['Fricción equivalente (N)', ('-B12/Datos!B8', -mean/distance)],
               ['Error estadístico de F (N)', ('B15/Datos!B8', sem/distance)]]
    notes = [
        ['Lectura para completar la consigna'],
        ['a)', 'K2 > K1; U2 < U1; E_m2 < E_m1; el trabajo de rozamiento es negativo.'],
        ['b)', 'Delta h = Delta X = 0,50 m (cuerdas inextensibles, sin deslizamiento).'],
        ['c)', 'Wfr = 0,5*(M+m1+m2)*(v2^2-v1^2)+(m2-m1)*g*Delta h.'],
        ['Error', 'Es error estadístico del promedio; faltan incertidumbres de instrumentos.'],
        ['Conclusión', 'La ganancia cinética es menor que la caída potencial; el déficit es compatible con rozamiento.'],
        ['Unidad adoptada', f'Masas originales interpretadas en {args.unidad_masas}; ver justificación y límites en laboratorio-2-resultados.md.'],
        ['Pendiente', 'Incertidumbres instrumentales no informadas; el error calculado sólo incluye dispersión estadística.'],
        ['Error para formulario (J)', sem],
        ['Trabajo promedio para formulario (J)', mean],
        ['Fuente', str(args.origen)], ['SHA256 original', original_hash],
    ]
    write_xlsx(target, [('Datos', datos, [40, 25, 25]),
                        ('Resultados', result, [32] + [24] * 9),
                        ('Lectura', notes, [30, 110])])
    with (args.carpeta_salida / 'laboratorio-2-tablas-propuesta.csv').open('w', encoding='utf-8-sig', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(['n', 'K1_J', 'K2_J', 'DeltaK_J', 'U1_J', 'U2_J', 'DeltaU_J', 'Wfr_J', 'e_J', 'e2_J2'])
        writer.writerows(values)
    assert hashlib.sha256(args.origen.read_bytes()).hexdigest() == original_hash
    print(json.dumps({'unidad_original_asumida': args.unidad_masas,
                      'Wmedio_J': mean, 'suma_e2_J2': sumsq, 'error_medio_J': sem,
                      'F_equivalente_N': -mean/distance, 'archivo': str(target)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
