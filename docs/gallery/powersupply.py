import sys
sys.path.insert(0, '../../')
import SchemDraw as schem
import SchemDraw.elements as e

d = schem.Drawing(inches_per_unit=.5, unit=3)
D1 = d.add( e.DIODE, theta=-45 )
d.add( e.DOT )
D2 = d.add( e.DIODE, theta=225, reverse=True )
d.add( e.DOT )
D3 = d.add( e.DIODE, theta=135, reverse=True )
d.add( e.DOT )
D4 = d.add( e.DIODE, theta=45 )
d.add( e.DOT )

d.add( e.LINE, xy=D3.end, d='left', l=d.unit*1.5 )
d.add( e.DOT_OPEN )
d.add( e.GAP, d='up', toy=D1.start, label='AC IN')
d.add( e.LINE, xy=D4.end, d='left', l=d.unit*1.5 )
d.add( e.DOT_OPEN )

top = d.add( e.LINE, xy=D2.end, d='right', l=d.unit*3 )
Q2 = d.add( e.BJT_NPN_C, anchor='collector', d='up', label='Q2\n2n3055' )
d.add( e.LINE, xy=Q2.base, d='down', l=d.unit/2)
Q2b = d.add( e.DOT )
d.add( e.LINE, d='left', l=d.unit/3)
Q1 = d.add( e.BJT_NPN_C, anchor='emitter', d='up', label='Q1\n    2n3054' )
d.add( e.LINE, d='up', xy=Q1.collector, toy=top.center )
d.add( e.DOT )

d.add( e.LINE, d='down', xy=Q1.base, l=d.unit/2 )
d.add( e.DOT )
d.add( e.ZENER, d='down', reverse=True, botlabel='D2\n500mA' )
d.add( e.DOT )
G = d.add( e.GND )
d.add( e.LINE, d='left' )
d.add( e.DOT )
d.add( e.CAP_P, botlabel='C2\n100$\mu$F\n50V', d='up', reverse=True )
d.add( e.DOT )
d.push()
d.add( e.LINE, d='right' )
d.pop()
d.add( e.RES, d='up', toy=top.end, botlabel='R1\n2.2K\n50V' )
d.add( e.DOT )

d.here = [d.here[0]-d.unit, d.here[1]]
d.add( e.DOT )
d.add( e.CAP_P, d='down', toy=G.start, label='C1\n 1000$\mu$F\n50V', flip=True )
d.add( e.DOT )
d.add( e.LINE, xy=G.start, tox=D4.start, d='left' )
d.add( e.LINE, d='up', toy=D4.start )

d.add( e.RES, d='right', xy=Q2b.center, label='R2', botlabel='56$\Omega$ 1W' )
d.add( e.DOT )
d.push()
d.add( e.LINE, d='up', toy=top.start )
d.add( e.DOT )
d.add( e.LINE, d='left', tox=Q2.emitter )
d.pop()
d.add( e.CAP_P, d='down', toy=G.start, botlabel='C3\n470$\mu$F\n50V')
d.add( e.DOT )
d.add( e.LINE, d='left', tox=G.start, move_cur=False )
d.add( e.LINE, d='right' )
d.add( e.DOT )
d.add( e.RES, d='up', toy=top.center, botlabel='R3\n10K\n1W' )
d.add( e.DOT )
d.add( e.LINE, d='left', move_cur=False )
d.add( e.LINE, d='right' )
d.add( e.DOT_OPEN )
d.add( e.GAP, d='down', toy=G.start, label='$V_{out}$' )
d.add( e.DOT_OPEN )
d.add( e.LINE, d='left' )

d.draw(showplot=False)
d.save('powersupply.png')

