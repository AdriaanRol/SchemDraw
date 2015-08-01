import SchemDraw as schem
import SchemDraw.elements as e

d = schem.Drawing(fontsize=12, unit=2.5)
Q1 = d.add( e.BJT_NPN, label='Q1', lftlabel='+IN' )
Q3 = d.add( e.BJT_PNP, xy=Q1.emitter, anchor='emitter', lftlabel='Q3', flip=True, d='left' )
d.add( e.LINE, d='down', xy=Q3.collector )
d.add( e.DOT )
d.push()
d.add( e.LINE, d='right', l=d.unit/4)
Q7 = d.add( e.BJT_NPN, anchor='base', label='Q7')
d.pop()
d.add( e.LINE, d='down', l=d.unit*1.25 )
Q5 = d.add( e.BJT_NPN, anchor='collector', d='left', flip=True, lftlabel='Q5')
d.add( e.LINE, d='left', xy=Q5.emitter, l=d.unit/2, lftlabel='OFST\nNULL', move_cur=False)
d.add( e.RES, d='down', xy=Q5.emitter, label='R1\n1K')
d.add( e.LINE, d='right', l=d.unit*.75 )
d.add( e.DOT )
R3 = d.add( e.RES, d='up', label='R3\n50K')
d.add( e.LINE, toy=Q5.base )
d.add( e.DOT )
d.push()
d.add( e.LINE, d='left', to=Q5.base )
d.add( e.LINE, xy=Q7.emitter, d='down', toy=Q5.base )
d.add( e.DOT )
d.pop()
d.add( e.LINE, d='right', l=d.unit/4 )
Q6 = d.add( e.BJT_NPN, anchor='base', label='Q6')
d.add( e.LINE, xy=Q6.emitter, l=d.unit/3, rgtlabel='\nOFST\nNULL', move_cur=False)
d.add( e.RES, xy=Q6.emitter, d='down', label='R2\n1K' )
d.add( e.DOT )

d.add( e.LINE, xy=Q6.collector, d='up', toy=Q3.collector )
Q4 = d.add( e.BJT_PNP, anchor='collector', d='right', label='Q4')
d.add( e.LINE, xy=Q4.base, d='left', tox=Q3.base )
d.add( e.LINE, xy=Q4.emitter, d='up', toy=Q1.emitter )
Q2 = d.add( e.BJT_NPN, anchor='emitter', d='left', flip=True, lftlabel='Q2', rgtlabel='$-$IN')
d.add( e.LINE, xy=Q2.collector, d='up', l=d.unit/3 )
d.add( e.DOT )
Q8 = d.add( e.BJT_PNP, lftlabel='Q8', anchor='base', d='left', flip=True )
d.add( e.LINE, xy=Q8.collector, d='down', toy=Q2.collector )
d.add( e.DOT )
d.add( e.LINE, d='left', xy=Q2.collector, tox=Q1.collector )
d.add( e.LINE, d='up', xy=Q8.emitter, l=d.unit/4 )
top = d.add( e.LINE, d='left', tox=Q7.collector )
d.add( e.LINE, d='down', toy=Q7.collector )

d.add( e.LINE, d='right', xy=top.start, l=d.unit*2 )
d.add( e.LINE, d='down', l=d.unit/4 )
Q9 = d.add( e.BJT_PNP, anchor='emitter', d='right', label='Q9', lblofst=-.1 )
d.add( e.LINE, d='left', xy=Q9.base, tox=Q8.base )
d.add( e.DOT, xy=Q4.base )
d.add( e.LINE, xy=Q4.base, d='down', l=d.unit/2 )
d.add( e.LINE, d='right', tox=Q9.collector )
d.add( e.DOT )
d.add( e.LINE, xy=Q9.collector, d='down', toy=Q6.collector )
Q10 = d.add( e.BJT_NPN, anchor='collector', d='left', flip=True, lftlabel='Q10' )
d.add( e.RES, d='down', xy=Q10.emitter, toy=R3.start, label='R4\n5K')
d.add( e.DOT )

Q11 = d.add( e.BJT_NPN, xy=Q10.base, anchor='base', label='Q11' )
d.add( e.DOT, xy=Q11.base )
d.add( e.LINE, d='up', l=d.unit/2 )
d.add( e.LINE, d='right', tox=Q11.collector )
d.add( e.DOT )
d.add( e.LINE, d='down', xy=Q11.emitter, toy=R3.start )
d.add( e.DOT )
d.add( e.LINE, d='up', xy=Q11.collector, l=d.unit*2)
d.add( e.RES, toy=Q9.collector, botlabel='R5\n39K')
Q12 = d.add( e.BJT_PNP, anchor='collector', d='left', flip=True, lftlabel='Q12', lblofst=-.1)
d.add( e.LINE, d='up', xy=Q12.emitter, l=d.unit/4 )
d.add( e.DOT )
d.add( e.LINE, d='left', tox=Q9.emitter )
d.add( e.DOT )
d.add( e.LINE, d='right', xy=Q12.base, l=d.unit/4 )
d.add( e.DOT )
d.push()
d.add( e.LINE, d='down', toy=Q12.collector )
d.add( e.LINE, d='left', tox=Q12.collector )
d.add( e.DOT )
d.pop()
d.add( e.LINE, d='right', l=d.unit*1.5 )
Q13 = d.add( e.BJT_PNP, anchor='base', label='Q13' )
d.add( e.LINE, d='up', l=d.unit/4 )
d.add( e.DOT )
d.add( e.LINE, d='left', tox=Q12.emitter )
K = d.add( e.LINE, d='down', xy=Q13.collector, l=d.unit/5 )
d.add( e.DOT )
d.add( e.LINE, d='down' )
Q16 = d.add( e.BJT_NPN, anchor='collector', d='right', label='Q16', lblofst=-.1 )
d.add( e.LINE, xy=Q16.base, d='left', l=d.unit/3 )
d.add( e.DOT )
R7 = d.add( e.RES, d='up', toy=K.end, label='R7\n4.5K' )
d.add( e.DOT )
d.add( e.LINE, d='right', tox=Q13.collector, move_cur=False )
R8 = d.add( e.RES, d='down', xy=R7.start, label='R8\n7.5K')
d.add( e.DOT )
d.add( e.LINE, d='right', tox=Q16.emitter )
J = d.add( e.DOT )
d.add( e.LINE, d='up', toy=Q16.emitter )
Q15 = d.add( e.BJT_NPN, anchor='collector', xy=R8.end, label='Q15', d='right' )
d.add( e.LINE, xy=Q15.base, d='left', l=d.unit/2 )
d.add( e.DOT )
C1 = d.add( e.CAP, d='up', toy=R7.end, label='C1\n30pF' )
d.add( e.LINE, d='right', tox=Q13.collector )
d.add( e.LINE, d='left', xy=C1.start, tox=Q6.collector )
d.add( e.DOT )
d.add( e.LINE, d='down', xy=J.center, l=d.unit/2 )
Q19 = d.add( e.BJT_NPN, anchor='collector', d='right', label='Q19' )
d.add( e.LINE, xy=Q19.base, d='left', tox=Q15.emitter )
d.add( e.DOT )
d.add( e.LINE, d='up', toy=Q15.emitter, move_cur=False )
d.add( e.LINE, xy=Q19.emitter, d='down', l=d.unit/4 )
d.add( e.DOT )
d.add( e.LINE, d='left' )
Q22 = d.add( e.BJT_NPN, anchor='base', d='left', flip=True, lftlabel='Q22' )
d.add( e.LINE, d='up', xy=Q22.collector, toy=Q15.base )
d.add( e.DOT )
d.add( e.LINE, d='down', xy=Q22.emitter, toy=R3.start )
d.add( e.DOT )
d.add( e.LINE, d='left', tox=R3.start, move_cur=False )
d.add( e.LINE, d='right', tox=Q15.emitter )
d.add( e.DOT )
d.push()
d.add( e.RES, d='up', label='R12\n50K' )
d.add( e.LINE, toy=Q19.base )
d.pop()
d.add( e.LINE, tox=Q19.emitter )
d.add( e.DOT )
R11 = d.add( e.RES, d='up', label='R11\n50' )
d.add( e.LINE, toy=Q19.emitter )

d.add( e.LINE, xy=Q13.emitter, d='up', l=d.unit/4 )
d.add( e.LINE, d='right', l=d.unit*1.5)
d.add( e.DOT )
d.add( e.LINE, l=d.unit/4, rgtlabel='V+', move_cur=False )
d.add( e.LINE, d='down', l=d.unit*.75 )
Q14 = d.add( e.BJT_NPN, anchor='collector', d='right', label='Q14' )
d.add( e.LINE, d='left', xy=Q14.base, l=d.unit/2 )
d.push()
d.add( e.DOT )
d.add( e.LINE, d='down', l=d.unit/2 )
Q17 = d.add( e.BJT_NPN, anchor='collector', d='left', flip=True, lftlabel='Q17', lblofst=-.1 )
d.add( e.LINE, xy=Q17.base, d='right', tox=Q14.emitter )
d.add( e.DOT )
J = d.add( e.LINE, d='up', toy=Q14.emitter )
d.pop()
d.add( e.LINE, tox=Q13.collector )
d.add( e.DOT )
d.add( e.RES, xy=J.start, d='down', label='R9\n25' )
d.add( e.DOT )
d.push()
d.add( e.LINE, d='left', tox=Q17.emitter )
d.add( e.LINE, d='up', toy=Q17.emitter )
d.pop()
d.add( e.LINE, d='down', l=d.unit/4 )
d.add( e.DOT )
d.add( e.LINE, d='right', l=d.unit/4, rgtlabel='OUT', move_cur=False )
d.add( e.RES, d='down', label='R10\n50' )
Q20 = d.add( e.BJT_PNP, d='right', anchor='emitter', label='Q20' )
d.add( e.LINE, xy=Q20.base, d='left', l=d.unit/2 )
d.add( e.LINE, d='up', toy=Q15.collector )
d.add( e.LINE, d='left', tox=Q15.collector )
d.add( e.DOT )
d.add( e.LINE, xy=Q20.collector, d='down', toy=R3.start )
d.add( e.DOT )
d.add( e.LINE, d='right', l=d.unit/4, rgtlabel='V-', move_cur=False )
d.add( e.LINE, d='left', tox=R11.start )

d.draw(showplot=False)
d.save('741.png')