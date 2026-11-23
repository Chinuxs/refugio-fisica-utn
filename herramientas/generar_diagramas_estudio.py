"""Regenera los SVG de TyE, MAS e Impulso con Python 3, sin dependencias.

Uso desde cualquier directorio: py herramientas/generar_diagramas_estudio.py
Las curvas de MAS se calculan a partir de seno/coseno, no se trazan a mano.
"""
from pathlib import Path
from html import escape
import math

ROOT = Path(__file__).resolve().parents[1] / "estudio" / "apuntes"
BG, PANEL, EDGE = "#141b25", "#202a38", "#45556b"
WHITE, MUTED = "#f4f7fc", "#b9c7da"
BLUE, GOLD, GREEN, RED = "#79b7ff", "#ffce75", "#79dfba", "#ff96ab"
COLORS = [MUTED, BLUE, GOLD, GREEN, RED, WHITE]


class SVG:
    def __init__(self, title, subtitle, desc, height=600):
        self.height = height
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="{height}" viewBox="0 0 1080 {height}" role="img" aria-labelledby="title desc">',
                      f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
                      '<defs>']
        for i, color in enumerate(COLORS):
            self.parts.append(f'<marker id="a{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="{color}"/></marker>')
        self.parts += ['<pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M0 10 L10 0" stroke="#79b7ff" stroke-width="1" opacity="0.3"/></pattern>',
                       '<style>text{font-family:Inter,"Segoe UI",Arial,sans-serif}.eq{font-family:"Cambria Math","STIX Two Math",Georgia,serif}</style></defs>']
        self.rect(12, 12, 1056, height-24, BG, radius=24, stroke=EDGE)
        self.text(42, 57, title, 29, WHITE, bold=True)
        self.text(42, 90, subtitle, 19, MUTED)

    def raw(self, s): self.parts.append(s)

    def rect(self, x, y, w, h, color=PANEL, radius=12, stroke=None, dash=None):
        self.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{color}"' +
                 (f' stroke="{stroke}"' if stroke else '') + (f' stroke-dasharray="{dash}"' if dash else '') + '/>')

    def text(self, x, y, label, size=21, color=WHITE, anchor="start", bold=False, eq=False):
        self.raw(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}"' +
                 (' font-weight="700"' if bold else '') + (' class="eq"' if eq else '') + f'>{escape(str(label))}</text>')

    def line(self, x1, y1, x2, y2, color=MUTED, width=2, arrow=False, dash=None):
        self.raw(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"' +
                 (f' marker-end="url(#a{COLORS.index(color)})"' if arrow else '') +
                 (f' stroke-dasharray="{dash}"' if dash else '') + '/>')

    def path(self, d, color=MUTED, width=2, fill="none", dash=None):
        self.raw(f'<path d="{d}" stroke="{color}" stroke-width="{width}" fill="{fill}"' + (f' stroke-dasharray="{dash}"' if dash else '') + '/>')

    def circle(self, x, y, r=12, color=BLUE, stroke=None):
        self.raw(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"' + (f' stroke="{stroke}" stroke-width="2"' if stroke else '') + '/>')

    def block(self, x, y, label="m", color=BLUE, w=60, h=44):
        self.rect(x, y, w, h, PANEL, 7, color)
        self.text(x+w/2, y+h/2+7, label, 22, color, "middle", bold=True)

    def spring(self, x1, y1, x2, y2, color=MUTED, coils=8):
        dx, dy = x2-x1, y2-y1
        length = math.hypot(dx, dy)
        ux, uy = dx/length, dy/length
        points = [(x1, y1), (x1+ux*10, y1+uy*10)]
        for j in range(2*coils):
            t = 10+(length-20)*(j+.5)/(2*coils)
            s = 9 if j % 2 else -9
            points.append((x1+ux*t-uy*s, y1+uy*t+ux*s))
        points += [(x2-ux*10, y2-uy*10), (x2,y2)]
        self.path('M'+' L'.join(f'{x:.2f} {y:.2f}' for x,y in points), color, 3)

    def panel(self, x, y, w, h, heading):
        self.rect(x, y, w, h, PANEL, 16)
        self.text(x+20, y+36, heading, 21, WHITE, bold=True)

    def footer(self, label):
        self.text(42, self.height-35, label, 19, MUTED)

    def save(self, topic, name):
        dest = ROOT / topic / 'assets' / (name+'.svg')
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text('\n'.join(self.parts+['</svg>'])+'\n', encoding='utf-8')
        print(dest.relative_to(ROOT))


def selector(topic, title, rows, footer, name='elegir-metodo'):
    s = SVG(title, 'Reconocer el dato o la situación → elegir el primer planteo.',
            'Diagrama de decisiones. '+'. '.join(a+': '+b+'; '+c for a,b,c in rows), 650)
    for i,(a,b,c) in enumerate(rows):
        y=128+i*88
        s.rect(42,y,430,70)
        s.text(62,y+30,a,23,BLUE,bold=True)
        s.text(62,y+55,c,18,MUTED)
        s.line(490,y+35,545,y+35,GOLD,3,True)
        s.rect(565,y,473,70)
        s.text(588,y+43,b,23,WHITE,eq=True)
    s.footer(footer)
    s.save(topic,name)


def energia():
    topic='trabajo-energia'
    s=SVG('De altura a resorte: seguir la energía', 'TP 6 · ejercicio 19 · reposo al inicio y en la máxima compresión.',
          'Un bloque de 10 kg baja desde 3 metros. Sólo el tramo BC es rugoso. Termina comprimiendo 0,30 m un resorte de 2250 N/m. Energía inicial 294 J, final 101,25 J y 192,75 J transformados en energía interna.',650)
    s.path('M125 220 C145 220 185 345 355 345 H910',MUTED,5)
    s.line(445,345,650,345,GOLD,7)
    for x in range(446,650,13):s.line(x,350,x-9,363,GOLD)
    s.block(114,171,'m')
    s.text(96,148,'A · v = 0',22,BLUE,bold=True)
    s.line(80,220,80,345,GREEN,2)
    s.line(72,220,88,220,GREEN);s.line(72,345,88,345,GREEN)
    s.text(45,288,'3 m',19,GREEN)
    s.text(190,243,'liso',20,MUTED)
    s.text(440,392,'B',21,GOLD);s.text(643,392,'C',21,GOLD)
    s.text(503,316,'roce',21,GOLD)
    s.line(590,289,505,289,RED,3,True)
    s.text(620,263,'movimiento',19,BLUE)
    s.line(620,281,729,281,BLUE,3,True)
    s.text(711,392,'h = 0',19,MUTED)
    s.block(841,301,'m')
    s.spring(901,322,1002,322,GREEN)
    s.line(1005,275,1005,347,MUTED,5)
    s.text(819,150,'FINAL · v = 0',22,GREEN,bold=True)
    s.text(819,183,'k = 2250 N/m',20,MUTED)
    s.text(819,214,'x = 0,30 m',20,MUTED)
    s.panel(42,423,480,166,'INICIO · Eᵢ = mgh = 294 J')
    s.rect(65,480,420,25,GOLD,4)
    s.text(65,546,'Toda la energía mecánica está en Uɡ.',20,MUTED)
    s.panel(540,423,498,166,'FINAL · E𝒇 = ½kx² = 101,25 J')
    s.rect(563,480,145,25,GREEN,4)
    s.rect(708,480,276,25,'url(#hatch)',4,BLUE)
    s.text(563,540,'Uₑ = 101,25 J',20,GREEN)
    s.text(563,572,'192,75 J → energía interna',20,BLUE)
    s.footer('Wroce = E𝒇 − Eᵢ = −192,75 J. La energía total se conserva; la mecánica disminuye.')
    s.save(topic,'balance-energia')

    s=SVG('Trabajo: proyección y área con signo', 'Dos lecturas del mismo concepto: fuerza durante un desplazamiento.',
          'A la izquierda una fuerza inclinada actúa sobre un bloque que se desplaza a la derecha. A la derecha un gráfico ilustrativo de fuerza en función de posición tiene áreas positivas y negativas.',570)
    s.panel(42,126,478,366,'FUERZA CONSTANTE')
    s.block(153,289)
    s.line(83,335,480,335,MUTED,3)
    s.line(183,311,389,195,BLUE,4,True)
    s.line(183,311,389,311,MUTED,2,False,'6 6')
    s.line(389,195,389,311,MUTED,2,False,'6 6')
    s.path('M248 311 A65 65 0 0 0 240 279',GOLD,3)
    s.text(253,292,'θ',23,GOLD)
    s.text(372,179,'F',24,BLUE,bold=True)
    s.text(298,301,'F cos θ',20,MUTED,eq=True)
    s.line(153,376,397,376,GREEN,3,True)
    s.text(266,409,'d',23,GREEN)
    s.text(280,462,'W = Fd cos θ',28,WHITE,'middle',eq=True)
    s.panel(540,126,498,366,'FUERZA VARIABLE · gráfico ilustrativo')
    # Positive and negative portions of a piecewise-linear F(x).
    s.path('M606 327 L766 187 L846 327 Z',BLUE,2,'#233e5e')
    s.path('M846 327 L926 397 L966 327 Z',RED,2,'#492e40')
    s.line(595,327,993,327,MUTED,2,True)
    s.line(606,418,606,167,MUTED,2,True)
    s.text(575,201,'Fₓ',22,MUTED);s.text(985,356,'x',21,MUTED)
    s.text(588,353,'0',18,MUTED)
    s.text(721,287,'+ área',22,BLUE)
    s.text(870,369,'− área',20,RED)
    s.text(788,462,'W = ∫ Fₓ dx',28,WHITE,'middle',eq=True)
    s.footer('La proyección decide el signo. En el gráfico se suman áreas algebraicas; el resultado es trabajo.')
    s.save(topic,'trabajo-proyeccion-area')

    selector(topic,'Trabajo y Energía · elegir el método',[
        ('F y desplazamiento','Wneto = ΔK','Constante o gráfico Fₓ(x)'),
        ('Alturas, resortes o roce','Eᵢ + Wnc = E𝒇','Fijar h = 0 y deformaciones'),
        ('Pista con varios sectores','Un balance por tramo','Separar superficies lisas y rugosas'),
        ('Loop y condición de contacto','Energía + ΣF radial = mv²/R','La rapidez sola no garantiza contacto'),
        ('Motor, tiempo o caudal','Potencia = W/Δt o F · v','Distinguir media e instantánea'),
    ],'Peso y resorte: si ya están en U, no volver a contarlos como trabajo.')

    s=SVG('Loop: llegar arriba manteniendo contacto', 'Cuerpo por dentro de una pista circular lisa; el resorte parte a la altura de la base.',
          'En la cima del loop la normal y el peso apuntan hacia el centro. El límite es normal cero y velocidad al cuadrado igual a gR. La energía inicial mínima es cinco medios de mgR.',580)
    s.panel(42,126,460,369,'1 · CONTACTO EN LA CIMA')
    s.circle(270,324,119,'none',MUTED)
    s.circle(270,324,5,WHITE)
    s.circle(270,205,14,BLUE)
    s.line(259,220,259,288,BLUE,3,True)
    s.line(283,220,283,302,GOLD,3,True)
    s.text(224,265,'N',22,BLUE);s.text(303,286,'mg',22,GOLD)
    s.line(285,201,380,201,GREEN,3,True);s.text(369,182,'v',22,GREEN)
    s.line(277,324,383,324,MUTED,2,False,'5 5');s.text(324,348,'R',20,MUTED)
    s.text(270,477,'N + mg = mv²/R',27,WHITE,'middle',eq=True)
    s.panel(522,126,516,369,'2 · ENERGÍA DESDE LA BASE')
    s.text(550,206,'En el límite de contacto:',23,MUTED)
    s.text(550,248,'N = 0  →  v²cima = gR',28,BLUE,eq=True)
    s.text(550,306,'½kx² = mg(2R) + ½m(gR)',28,WHITE,eq=True)
    s.text(550,344,'altura ganada      +      K en la cima',19,MUTED)
    s.rect(548,380,463,75,'#22394b',12)
    s.text(780,429,'xmín = √(5mgR/k)',32,GREEN,'middle',eq=True)
    s.footer('Poner v = 0 arriba no alcanza. Con pérdidas, hace falta más energía inicial.')
    s.save(topic,'loop-contacto-energia')


def mas():
    topic='movimiento-armonico-simple'
    s=SVG('MAS: qué pasa en cada posición', 'Recorrido de izquierda a derecha · resorte horizontal ideal · x medido desde el equilibrio.',
          'En menos A y más A la velocidad es cero y la aceleración máxima apunta al equilibrio. Al pasar por cero la rapidez es máxima y la aceleración nula. Se comparan barras de energía cinética y potencial.',640)
    for i,(heading,pos,kfrac,note) in enumerate([
        ('EXTREMO · x = −A',118,0,'v = 0; a apunta a +x'),
        ('CENTRO · x = 0',186,1,'v = +ωA; a = 0'),
        ('EXTREMO · x = +A',246,0,'v = 0; a apunta a −x'),
    ]):
        x=42+i*337
        s.panel(x,126,321,396,heading)
        s.line(x+25,208,x+25,282,MUTED,5)
        s.spring(x+27,247,x+pos-26,247)
        s.block(x+pos-26,225,'m',BLUE,52)
        s.line(x+25,270,x+293,270,MUTED,2)
        if i!=1:
            end=x+pos+(60 if i==0 else -70)
            s.line(x+pos,312,end,312,GOLD,3,True,'6 4')
            s.text((x+pos+end)/2,337,'a',21,GOLD,'middle')
        else:
            s.line(x+pos-25,312,x+pos+67,312,BLUE,3,True)
            s.text(x+pos+20,337,'v',21,BLUE,'middle')
        s.text(x+20,376,note,20,WHITE)
        for j,(lab,fraction,color) in enumerate([('K',kfrac,BLUE),('U',1-kfrac,GOLD)]):
            y=405+j*47
            s.text(x+20,y+20,lab,21,color,bold=True)
            s.rect(x+57,y,229,25,BG,4)
            if fraction:s.rect(x+57,y,229*fraction,25,color,4)
            else:s.text(x+67,y+19,'0',18,MUTED)
    s.text(540,560,'E = K + U = ½kA²  ·  constante durante toda la oscilación',25,GREEN,'middle',eq=True)
    s.footer('Flecha azul: velocidad. Flecha dorada discontinua: aceleración, no una fuerza adicional.')
    s.save(topic,'posicion-velocidad-energia')

    s=SVG('Posición, velocidad y aceleración en un período', 'x = A sen(ωt) · fase inicial cero · cada curva está dividida por su propia amplitud.',
          'Tres curvas normalizadas: posición seno, velocidad coseno y aceleración menos seno. En T/4 la posición es A, velocidad cero y aceleración mínima; en 3T/4 sucede lo opuesto.',700)
    x0,x1=192,992
    for idx,(label,fn,col) in enumerate([('x/A',math.sin,BLUE),('v/(ωA)',math.cos,GREEN),('a/(ω²A)',lambda p:-math.sin(p),GOLD)]):
        cy=208+idx*157
        s.text(48,cy+8,label,25,col,bold=True)
        for j in range(5):s.line(x0+j*200,cy-58,x0+j*200,cy+58,EDGE,1,False,'4 5')
        s.line(x0,cy,x1+20,cy,MUTED,1.5,True)
        s.text(x0-32,cy-44,'+1',17,MUTED);s.text(x0-28,cy+55,'−1',17,MUTED)
        pts=[(x0+(x1-x0)*j/200,cy-51*fn(2*math.pi*j/200)) for j in range(201)]
        s.path('M'+' L'.join(f'{x:.2f} {y:.2f}' for x,y in pts),col,3.5)
        for j in range(5):s.circle(x0+j*200,cy-51*fn(j*math.pi/2),4,col)
    for j,label in enumerate(['0','T/4','T/2','3T/4','T']):s.text(x0+j*200,619,label,21,MUTED,'middle')
    s.text(1012,619,'t',21,MUTED)
    s.footer('El signo indica el sentido. Las alturas de curvas distintas no comparan magnitudes con unidades diferentes.')
    s.save(topic,'curvas-mas')

    selector(topic,'MAS · elegir el método',[
        ('Dan x(t)','Leer A, ω y fase → derivar','Conservar el seno o coseno que dieron'),
        ('Dan x₀ y v₀','A² = x₀² + (v₀/ω)²','Fijar la fase con posición y velocidad'),
        ('Piden v en una posición','v² = ω²(A² − x²)','Elegir el signo según el sentido'),
        ('Piden el primer tiempo','Fase → sentido → t válido','Revisar las dos ramas del seno'),
        ('Resorte vertical','Equilibrio nuevo → x desde allí','El alargamiento estático no es A'),
    ],'Primero: equilibrio, eje positivo e instante inicial. Después: ecuaciones.')

    mas_comparaciones()


def mas_comparaciones():
    """Diagramas de elaboración propia y curvas calculadas."""
    dest = ROOT / 'movimiento-armonico-simple' / 'assets'
    dest.mkdir(parents=True, exist_ok=True)
    sistemas = '''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="640" viewBox="0 0 1080 640" role="img" aria-labelledby="title desc">
<title id="title">Tres osciladores: equilibrio y restauración</title><desc id="desc">Resortes horizontal y vertical, y péndulo. Posiciones de equilibrio y extremos; delta se mide desde longitud natural y x desde el equilibrio.</desc>
<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#ffce75"/></marker>
<style>text{font-family:Inter,"Segoe UI",Arial,sans-serif;fill:#f4f7fc;font-size:20px}.muted{fill:#b9c7da;font-size:17px}.blue{fill:#79b7ff}.gold{fill:#ffce75}.green{fill:#79dfba}.panel{fill:#202a38}.spring{fill:none;stroke:#79b7ff;stroke-width:3}.guide{stroke:#b9c7da;stroke-dasharray:6 5;fill:none}.rest{stroke:#ffce75;stroke-width:3;marker-end:url(#arr)}.mass{fill:#202a38;stroke:#79b7ff;stroke-width:3}.ghost{fill:none;stroke:#b9c7da;stroke-width:1.5;stroke-dasharray:5 4}</style></defs>
<rect x="12" y="12" width="1056" height="616" rx="24" fill="#141b25" stroke="#45556b"/>
<text x="42" y="57" style="font-size:29px;font-weight:700">Tres osciladores: equilibrio y restauración</text>
<text x="42" y="90" class="muted">Modelos ideales · flecha dorada = componente restauradora · posiciones esquemáticas</text>
<rect x="42" y="120" width="321" height="450" rx="15" class="panel"/><rect x="379" y="120" width="321" height="450" rx="15" class="panel"/><rect x="716" y="120" width="322" height="450" rx="15" class="panel"/>
<text x="60" y="156" font-weight="700">RESORTE HORIZONTAL</text><text x="397" y="156" font-weight="700">RESORTE VERTICAL</text><text x="734" y="156" font-weight="700">PÉNDULO SIMPLE</text>
<path d="M66 253V321M66 321H340" stroke="#b9c7da" stroke-width="3" fill="none"/>
<path class="spring" d="M66 300H83L94 288L105 312L116 288L127 312L138 288L149 312L160 288L171 312L182 288L193 312L204 288L215 312L226 288L237 312L248 300H271"/>
<rect x="151" y="279" width="38" height="42" rx="5" class="ghost"/><rect x="211" y="279" width="38" height="42" rx="5" class="ghost"/><rect x="271" y="279" width="38" height="42" rx="5" class="mass"/><text x="290" y="307" text-anchor="middle">m</text>
<path class="guide" d="M170 324V373M230 324V373M290 324V373"/><path d="M120 373H335" stroke="#b9c7da" stroke-width="2"/><path d="M335 373L325 368V378Z" fill="#b9c7da"/>
<text x="170" y="402" text-anchor="middle" class="muted">−A</text><text x="230" y="402" text-anchor="middle" class="blue">0</text><text x="290" y="402" text-anchor="middle" class="muted">+A</text><text x="334" y="402" class="muted">x</text>
<path class="rest" d="M286 258H240"/><text x="259" y="244" class="gold" text-anchor="middle">−kx</text>
<text x="60" y="447" class="blue">x = +A (extremo)</text><text x="60" y="478" class="muted">Equilibrio: x = 0</text><text x="60" y="525">T = 2π√(m/k)</text>
<path d="M410 190H669" stroke="#b9c7da" stroke-width="4"/><path class="spring" d="M520 192V207L510 218L530 229L510 240L530 251L510 262L530 273L510 284L530 295L510 306L530 317L510 328L530 339L520 350V369"/>
<path class="guide" d="M401 215H670M401 310H670M401 390H670"/><rect x="499" y="209" width="42" height="42" rx="5" class="ghost"/><text x="550" y="250" class="muted">−A</text><rect x="499" y="289" width="42" height="42" rx="5" class="ghost"/><rect x="499" y="369" width="42" height="42" rx="5" class="mass"/><text x="520" y="397" text-anchor="middle">m</text>
<path d="M432 215V310M425 215H439M425 310H439" stroke="#79b7ff" stroke-width="2" fill="none"/><text x="409" y="280" class="blue">δ</text>
<path d="M463 310V390M456 310H470M456 390H470" stroke="#79dfba" stroke-width="2" fill="none"/><text x="444" y="354" class="green">x</text>
<path class="rest" d="M565 390V333"/><text x="574" y="358" class="gold">−kx</text>
<text x="550" y="208" class="muted">natural</text><text x="550" y="300" class="blue">x = 0</text><text x="550" y="416" class="muted">+A</text><path d="M675 312V418" stroke="#b9c7da" stroke-width="2"/><path d="M675 418L670 408H680Z" fill="#b9c7da"/><text x="667" y="438" class="muted">+x</text>
<text x="397" y="460" class="muted">δ = mg/k; x = z − δ</text><text x="397" y="488" class="green">Aquí x = +A</text><text x="397" y="525">T = 2π√(m/k)</text>
<circle cx="852" cy="192" r="5" fill="#f4f7fc"/><path class="guide" d="M852 192V398"/><path d="M852 192L898 381" stroke="#79b7ff" stroke-width="3"/><path class="guide" d="M852 192L806 381M806 381A194.5 194.5 0 0 0 898 381"/><circle cx="852" cy="386.5" r="15" class="ghost"/><circle cx="806" cy="381" r="15" class="ghost"/><circle cx="898" cy="381" r="15" class="mass"/>
<path d="M852 266A74 74 0 0 0 869.5 264" fill="none" stroke="#79dfba" stroke-width="2"/><text x="874" y="271" class="green">θ</text><text x="897" y="309" class="blue">L</text><path class="rest" d="M886 386L835 398"/><text x="752" y="427" class="gold">−mg sen θ</text>
<text x="742" y="463" class="muted">Equilibrio: θ = 0</text><text x="742" y="490" class="green">Aquí θ = +θₘ; arco s = Lθ</text><text x="742" y="525">T ≈ 2π√(L/g)</text>
<text x="42" y="605" class="muted">A y x en m; θ y θₘ en rad. El alargamiento estático δ no determina por sí solo la amplitud.</text>
</svg>
'''
    (dest / 'equilibrio-resorte-pendulo.svg').write_text(sistemas, encoding='utf-8')
    plantilla = '''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="710" viewBox="0 0 1080 710" role="img" aria-labelledby="title desc">
<title id="title">Cambiar amplitud o período</title><desc id="desc">Curvas seno calculadas: A 1 y 0,5 metros, T 2 segundos; A 1 metro, T 2 y 1 segundos. Los mismos ejes y escalas.</desc>
<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#ffce75"/></marker>
<style>text{font-family:Inter,"Segoe UI",Arial,sans-serif;fill:#f4f7fc;font-size:20px}.muted{fill:#b9c7da;font-size:17px}.blue{fill:#79b7ff}.gold{fill:#ffce75}.green{fill:#79dfba}.panel{fill:#202a38}.spring{fill:none;stroke:#79b7ff;stroke-width:3}.guide{stroke:#b9c7da;stroke-dasharray:6 5;fill:none}.rest{stroke:#ffce75;stroke-width:3;marker-end:url(#arr)}.mass{fill:#202a38;stroke:#79b7ff;stroke-width:3}.ghost{fill:none;stroke:#b9c7da;stroke-width:1.5;stroke-dasharray:5 4}</style></defs>
<rect x="12" y="12" width="1056" height="686" rx="24" fill="#141b25" stroke="#45556b"/>
<text x="42" y="57" style="font-size:29px;font-weight:700">Cambiar amplitud o período</text>
<text x="42" y="90" class="muted">x(t) = A sen(2πt/T) · fase cero · mismos ejes y escalas</text>
<rect x="42" y="120" width="996" height="248" rx="15" class="panel"/><rect x="42" y="385" width="996" height="248" rx="15" class="panel"/>
<text x="60" y="153" font-weight="700">1. Igual período, distinta amplitud</text><text x="60" y="418" font-weight="700">2. Igual amplitud, distinto período</text>
<text x="65" y="182" class="muted">x (m)</text>
<path d="M135 307H992" stroke="#45556b" stroke-dasharray="4 5"/><text x="117" y="313" text-anchor="end" class="muted">-1</text>
<path d="M135 247H992" stroke="#45556b" stroke-dasharray="4 5"/><text x="117" y="253" text-anchor="end" class="muted">0</text>
<path d="M135 187H992" stroke="#45556b" stroke-dasharray="4 5"/><text x="117" y="193" text-anchor="end" class="muted">1</text>
<path d="M135 175V319" stroke="#45556b" stroke-dasharray="4 5"/><text x="135" y="341" text-anchor="middle" class="muted">0</text>
<path d="M345 175V319" stroke="#45556b" stroke-dasharray="4 5"/><text x="345" y="341" text-anchor="middle" class="muted">1</text>
<path d="M555 175V319" stroke="#45556b" stroke-dasharray="4 5"/><text x="555" y="341" text-anchor="middle" class="muted">2</text>
<path d="M765 175V319" stroke="#45556b" stroke-dasharray="4 5"/><text x="765" y="341" text-anchor="middle" class="muted">3</text>
<path d="M975 175V319" stroke="#45556b" stroke-dasharray="4 5"/><text x="975" y="341" text-anchor="middle" class="muted">4</text>
<path d="M135 319V172M135 247H1000" fill="none" stroke="#b9c7da" stroke-width="1.5"/><text x="1000" y="341" text-anchor="end" class="muted">t (s)</text>
<text x="65" y="447" class="muted">x (m)</text>
<path d="M135 572H992" stroke="#45556b" stroke-dasharray="4 5"/><text x="117" y="578" text-anchor="end" class="muted">-1</text>
<path d="M135 512H992" stroke="#45556b" stroke-dasharray="4 5"/><text x="117" y="518" text-anchor="end" class="muted">0</text>
<path d="M135 452H992" stroke="#45556b" stroke-dasharray="4 5"/><text x="117" y="458" text-anchor="end" class="muted">1</text>
<path d="M135 440V584" stroke="#45556b" stroke-dasharray="4 5"/><text x="135" y="606" text-anchor="middle" class="muted">0</text>
<path d="M345 440V584" stroke="#45556b" stroke-dasharray="4 5"/><text x="345" y="606" text-anchor="middle" class="muted">1</text>
<path d="M555 440V584" stroke="#45556b" stroke-dasharray="4 5"/><text x="555" y="606" text-anchor="middle" class="muted">2</text>
<path d="M765 440V584" stroke="#45556b" stroke-dasharray="4 5"/><text x="765" y="606" text-anchor="middle" class="muted">3</text>
<path d="M975 440V584" stroke="#45556b" stroke-dasharray="4 5"/><text x="975" y="606" text-anchor="middle" class="muted">4</text>
<path d="M135 584V437M135 512H1000" fill="none" stroke="#b9c7da" stroke-width="1.5"/><text x="1000" y="606" text-anchor="end" class="muted">t (s)</text>
<path d="@@p1@@" fill="none" stroke="#79b7ff" stroke-width="3"/>
<path d="@@p2@@" fill="none" stroke="#ffce75" stroke-width="3" stroke-dasharray="8 5"/>
<path d="@@p3@@" fill="none" stroke="#79b7ff" stroke-width="3"/>
<path d="@@p4@@" fill="none" stroke="#ffce75" stroke-width="3" stroke-dasharray="8 5"/>
<text x="560" y="153" class="blue">A = 1 m, T = 2 s</text><text x="796" y="153" class="gold">A = 0,5 m, T = 2 s (- -)</text>
<text x="560" y="418" class="blue">A = 1 m, T = 2 s</text><text x="796" y="418" class="gold">A = 1 m, T = 1 s (- -)</text>
<text x="42" y="675" class="muted">Cambiar A no cambia el ritmo en MAS ideal. Menor T significa más ciclos en el mismo tiempo.</text>
</svg>
'''

    def curva(cy, amplitud, periodo):
        puntos = []
        for j in range(201):
            x = 135 + 840*j/200
            y = cy - 60*amplitud*math.sin(2*math.pi*(4*j/200)/periodo)
            puntos.append(('L' if j else 'M') + f'{x:.2f} {y:.2f}')
        return ' '.join(puntos)

    for nombre, cy, amplitud, periodo in (
        ('p1', 247, 1, 2), ('p2', 247, .5, 2),
        ('p3', 512, 1, 2), ('p4', 512, 1, 1),
    ):
        plantilla = plantilla.replace('@@' + nombre + '@@', curva(cy, amplitud, periodo))
    (dest / 'comparar-parametros.svg').write_text(plantilla, encoding='utf-8')
    print('movimiento-armonico-simple/assets/equilibrio-resorte-pendulo.svg')
    print('movimiento-armonico-simple/assets/comparar-parametros.svg')


def impulso():
    topic='impulso-cantidad-movimiento'
    s=SVG('Mismo momento; distinta energía cinética', 'Ejemplo ilustrativo · dos masas de 1 kg · velocidades medidas respecto del suelo.',
          'Una masa a 2 m/s alcanza a otra en reposo. Con impulso externo cero se conserva P=2 kg m/s. Choque elástico: velocidades cero y dos, energía 2 J. Inelástico con e=0,5: velocidades 0,5 y 1,5, energía 1,25 J. Plástico: unidas a 1 m/s, energía 1 J.',720)
    s.text(64,145,'ANTES',21,MUTED,bold=True)
    s.block(182,123,'1');s.line(250,145,346,145,BLUE,3,True);s.text(264,123,'2 m/s',20,BLUE)
    s.block(437,123,'2',GOLD);s.text(515,151,'v₂ = 0',22,GOLD)
    s.text(734,147,'Pᵢ = 2 kg·m/s; Kᵢ = 2 J',22,WHITE,eq=True)
    for i,(title,v1,v2,k,e) in enumerate([
        ('ELÁSTICO',0,2,2,'e = 1'),('INELÁSTICO',.5,1.5,1.25,'e = 0,5'),('PLÁSTICO',1,1,1,'e = 0'),
    ]):
        x=42+i*337
        s.panel(x,207,321,377,title)
        s.text(x+20,277,e,21,MUTED)
        if i==2:
            s.block(x+58,323,'1',BLUE,59);s.block(x+117,323,'2',GOLD,59)
            s.line(x+185,345,x+271,345,GREEN,3,True)
            s.text(x+64,408,'juntas · V = 1 m/s',21,GREEN)
        else:
            for j,v in enumerate([v1,v2]):
                col=[BLUE,GOLD][j];xx=x+27+j*147
                s.block(xx,323,str(j+1),col,46)
                if v:s.line(xx+50,345,xx+50+v*36,345,col,3,True)
                s.text(xx,408,f'v{["₁","₂"][j]} = {str(v).replace(".",",")}',22,col)
            s.text(x+20,438,'velocidades en m/s',18,MUTED)
        s.text(x+20,483,'P𝒇 = 2 kg·m/s',23,WHITE,eq=True)
        s.rect(x+20,507,281,22,BG,4)
        s.rect(x+20,507,281*k/2,22,GREEN,4)
        s.text(x+20,562,f'K𝒇 = {str(k).replace(".",",")} J',23,GREEN)
    s.text(540,624,'P se conserva en los tres casos. K sólo se conserva en el elástico.',23,WHITE,'middle')
    s.footer('Hipótesis: impulso externo despreciable durante el choque. “Plástico” significa que quedan unidos.')
    s.save(topic,'comparar-choques')

    s=SVG('Impulso: el área bajo F(t)', 'TP 8 · ejercicio 6 · fuerza positiva entre 0 y 5 s.',
          'Gráfico de fuerza: crece linealmente de 0 a 4 N entre 0 y 2 s, se mantiene hasta 3 s y baja a cero a 5 s. Cada una de las tres áreas vale 4 N s, total 12 N s. La fuerza media es 2,4 N.',580)
    s.rect(42,126,666,362)
    base,scale,x0=432,58,105
    s.path('M105 432 L305 200 L305 432 Z',BLUE,2,'#203e5c')
    s.rect(305,200,100,232,'#314633',0,GREEN)
    s.path('M405 432 L405 200 L605 432 Z',GOLD,2,'#483d2c')
    s.line(95,432,662,432,MUTED,2,True)
    s.line(105,452,105,165,MUTED,2,True)
    for i in range(6):
        x=x0+i*100;s.line(x,432,x,440,MUTED);s.text(x,467,str(i),19,MUTED,'middle')
    for i in [0,2,4]:
        y=base-scale*i;s.text(86,y+6,str(i),18,MUTED,'end')
    s.text(59,157,'F (N)',22,MUTED);s.text(638,470,'t (s)',20,MUTED)
    ymed=base-scale*2.4
    s.line(105,ymed,605,ymed,WHITE,2,False,'7 5')
    s.text(395,180,'Fmedia = 2,4 N (línea discontinua)',18,MUTED,'middle')
    for x,label,col in [(230,'4 N·s',BLUE),(355,'4 N·s',GREEN),(480,'4 N·s',GOLD)]:s.text(x,404,label,21,col,'middle',bold=True)
    s.panel(728,126,310,362,'ÁREA TOTAL')
    s.text(751,209,'J = 4 + 4 + 4',26,WHITE,eq=True)
    s.text(751,250,'J = 12 N·s',29,BLUE,bold=True)
    s.text(751,315,'Fmedia = J / Δt',25,WHITE,eq=True)
    s.text(751,354,'= 12 / 5 = 2,4 N',23,WHITE)
    s.text(751,419,'Δv = J/m = 6 m/s',23,GREEN,eq=True)
    s.text(751,453,'para m = 2 kg',19,MUTED)
    s.footer('F(t) da impulso [N·s]. F(x) da trabajo [J]. Leer siempre qué representa el eje horizontal.')
    s.save(topic,'area-impulso')

    s=SVG('Choque y frenado: separar las etapas', 'Proyectil que queda empotrado en un bloque sobre piso rugoso.',
          'Antes: proyectil m con velocidad v y bloque M quieto. Durante el choque corto se desprecia el impulso del roce y mv=(m+M)V. Después, el roce frena al conjunto y V al cuadrado=2 mu g d. Resolver hacia atrás para hallar v.',590)
    for i,heading in enumerate(['ANTES DEL CHOQUE','JUSTO DESPUÉS','FINAL DEL FRENADO']):
        x=42+i*337;s.panel(x,126,321,359,heading)
        if i==0:
            s.circle(x+40,250,8,BLUE)
            s.line(x+57,250,x+167,250,BLUE,3,True)
            s.text(x+89,230,'v',24,BLUE)
            s.text(x+27,281,'m',21,BLUE)
            s.block(x+205,230,'M',GOLD,69,57)
            s.text(x+200,323,'quieto',20,MUTED)
            s.text(x+20,390,'Momento inicial:',21,MUTED)
            s.text(x+20,431,'pᵢ = mv',28,WHITE,eq=True)
        elif i==1:
            s.block(x+34,230,'m + M',GREEN,116,57)
            s.line(x+163,253,x+280,253,GREEN,3,True)
            s.text(x+218,231,'V',24,GREEN)
            s.text(x+20,323,'Impacto: Jext ≈ 0',21,MUTED)
            s.text(x+20,390,'Conservar momento:',21,MUTED)
            s.text(x+20,431,'mv = (m + M)V',28,WHITE,eq=True)
        else:
            s.block(x+185,230,'m + M',GREEN,116,57)
            s.text(x+210,323,'v𝒇 = 0',23,GREEN)
            for xx in range(int(x+30),int(x+300),15):s.line(xx,291,xx-8,301,GOLD)
            s.line(x+30,340,x+260,340,GOLD,2,True);s.text(x+133,367,'d',21,GOLD)
            s.text(x+20,400,'Roce → cambio de K:',21,MUTED)
            s.text(x+20,440,'½V² = μₖgd',28,WHITE,eq=True)
        s.line(x+20,287,x+300,287,MUTED,2)
    s.text(540,528,'Resolver hacia atrás: frenado → V; después, choque → v del proyectil.',23,WHITE,'middle')
    s.footer('El roce es despreciable sólo durante el impacto corto. En el frenado, su trabajo es esencial.')
    s.save(topic,'choque-por-etapas')

    s=SVG('Centro de masa: posición y referencia', 'Promedio ponderado por las masas; restar la velocidad del CM para cambiar de referencia.',
          'Ejemplo del TP 8 ejercicio 8: masas de 2 y 4 kg en x=3 y x=6 m dan centro de masa en x=5 m. Ejercicio 12: masas de 3 y 7 gramos con velocidades 3 y 0 m/s tienen CM a 0,9 m/s; velocidades relativas 2,1 y menos 0,9 m/s.',580)
    s.panel(42,126,478,351,'POSICIÓN · TP 8, EJ. 8')
    s.line(90,322,483,322,MUTED,2,True)
    for x,lab in [(140,'3 m'),(340,'5 m'),(440,'6 m')]:
        s.line(x,311,x,333,MUTED);s.text(x,364,lab,20,MUTED,'middle')
    s.circle(140,277,19,BLUE);s.circle(440,277,28,GOLD)
    s.text(140,238,'2 kg',22,BLUE,'middle');s.text(440,231,'4 kg',22,GOLD,'middle')
    s.path('M340 259 L353 277 L340 295 L327 277 Z',GREEN,2,'none')
    s.text(340,238,'CM',22,GREEN,'middle',bold=True)
    s.line(340,294,340,311,GREEN,2,False,'4 4')
    s.text(278,427,'xCM = (2·3 + 4·6)/6 = 5 m',25,WHITE,'middle',eq=True)
    s.panel(540,126,498,351,'VELOCIDAD · TP 8, EJ. 12')
    s.text(562,207,'Suelo: 3 g a 3 m/s; 7 g en reposo.',22,MUTED)
    s.text(562,253,'vCM = (3·3 + 7·0)/10 = 0,9 m/s',24,GREEN,eq=True)
    s.text(562,312,'Desde el CM:',21,MUTED)
    s.text(562,354,'v′₁ = 3 − 0,9 = +2,1 m/s',25,BLUE,eq=True)
    s.text(562,399,'v′₂ = 0 − 0,9 = −0,9 m/s',25,GOLD,eq=True)
    s.text(562,450,'En esta referencia: Σmᵢv′ᵢ = 0.',22,WHITE)
    s.footer('El CM está más cerca de la masa mayor. Momento total cero no significa que cada partícula esté quieta.')
    s.save(topic,'centro-masa')


if __name__ == '__main__':
    energia()
    mas()
    impulso()
