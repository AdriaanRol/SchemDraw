''' Logic gate circuit elements
    
    See elements.py for information on how elements are defined.
'''

import numpy as _np

_gap = [_np.nan, _np.nan]
_leadlen = .35
_gateh = 1.
_gatel = .65
_notbubble = .12

def andgate(inputs=2, nand=False, inputnots=[], name='AND' ):
    ''' Build n-input AND gate element definitions.
    
        inputs : number of inputs to gate.
        nand   : invert bubble on output
        inputnots : input numbers (starting at 1) with invert bubble
        name   : Define a name for gate. Only used in documentation currently.
    '''
    
    AND = {
        'name'  : name,
        'paths' : [ [ [_leadlen,0],[_leadlen,-_gateh/2],[_gatel+_leadlen,-_gateh/2] ],
                    [ [_leadlen,0],[_leadlen,_gateh/2], [_gatel+_leadlen,_gateh/2] ]
                  ],
        'shapes' :  [ { 'shape' : 'arc',
                       'center' : [_gatel+_leadlen,0],
                       'theta1' : -90,
                       'theta2' : 90,
                       'width'  : _gateh,
                       'height' : _gateh }
                    ],
        'extend' : False,
        'anchors' : {'out' : [_gatel+_gateh/2+_leadlen*2,0],
                    }
         }

    if nand:
        AND['shapes'].append( 
            { 'shape'  : 'circle',
              'center' : [_leadlen+_gatel+_gateh/2+_notbubble,0],
              'radius' : _notbubble } )
    
    # Set distance between inputs. A little larger for 2 input gates.
    if inputs == 2:
        dy = _gateh*.5
    elif inputs == 3:
        dy = _gateh*.33
    else: # inputs > 3:
        dy = _gateh*.4
        backlen = dy * (inputs-1)

    # Add the inputs and define anchor names
    for i in range(inputs):
        y = (i+1 - (inputs/2+.5)) * dy
        AND['anchors']['in%d'%(inputs-i) ] = [0,y]

        if (inputs-i) in inputnots:
            AND['shapes'].append(
                { 'shape'  : 'circle',
                  'center' : [_leadlen-_notbubble,y],
                  'radius' : _notbubble } )

            AND['paths'].append( [[0,y],[_leadlen-_notbubble*2,y]] )
        else:
            AND['paths'].append( [[0,y],[_leadlen,y]] )

    # Extended back for large number of inputs
    if inputs > 3:
        AND['paths'].append( [[_leadlen,backlen/2+dy/2],[_leadlen,-backlen/2-dy/2]] )

    # Output lead
    if nand:
        AND['paths'].append( [[0,0],_gap,[_gatel+_gateh/2+_leadlen+_notbubble*2,0],[_gatel+_gateh/2+_leadlen*2,0]] )
    else:
        AND['paths'].append( [[0,0],_gap,[_gatel+_gateh/2+_leadlen,0],[_gatel+_gateh/2+_leadlen*2,0]] )

    return AND


def orgate( inputs=2, nor=False, xor=False, inputnots=[], name='OR' ):
    ''' Build n-input OR gate element.
    
        inputs : number of inputs to gate.
        nor    : invert bubble on output
        xor    : exclusive-or
        inputnots : input numbers (starting at 1) with invert bubble
        name   : Define a name for gate. Only used in documentation currently.
    '''
    # Define OR path as a numpy array
    orflat = .5
    xorgap = .15
    x = _np.linspace(0,_gatel+.05)
    y = x**2
    y = y - max(y)
    y = _np.concatenate( ([min(y)], y))   # Combine the flat + parabolic parts
    x = _np.concatenate( ([0], x+orflat))

    # Back/input side
    y2 = _np.linspace( min(y), -min(y) )
    x2 = -y2**2
    back = min(x2)
    x2 = x2 - back

    # Offset for inputs
    x  = x  + _leadlen
    x2 = x2 + _leadlen

    if xor:
        x = x + xorgap
    
    tip = max(x)
    orheight = abs(min(y))
    
    OR = {
        'name'  : name,
        'paths' : [ _np.transpose(_np.vstack((x,y))),
                    _np.transpose(_np.vstack((x,-y))),
                    _np.transpose(_np.vstack((x2,y2))) ],
        'shapes' : [],
        'extend' : False,
        'anchors' : {'out' : [tip+_leadlen,0],
                    }
         }

    if xor:
        OR['paths'].append( _np.transpose(_np.vstack((x2+xorgap,y2)))) 
        
    if nor:
        OR['shapes'].append( 
            { 'shape'  : 'circle',
              'center' : [tip+_notbubble,0],
              'radius' : _notbubble } )

    # Set distance between inputs. A little larger for 2 input gates.
    if inputs == 2:
        dy = _gateh*.5
    elif inputs == 3:
        dy = _gateh*.33
    else: # inputs > 3:
        dy = _gateh*.4
        backlen = dy * (inputs-1)

    # Add the inputs and define anchor names
    for i in range(inputs):
        y = (i+1 - (inputs/2+.5)) * dy

        xback = _leadlen - y**2 - back
        if inputs > 3 and ((y > orheight) or (y < -orheight)):
            xback = _leadlen
        
        OR['anchors']['in%d'%(inputs-i) ] = [0,y]

        
        if (inputs-i) in inputnots:
            OR['shapes'].append(
                { 'shape'  : 'circle',
                  'center' : [xback-_notbubble, y],
                  'radius' : _notbubble } )

            OR['paths'].append( [[0,y],[xback-_notbubble*2,y]] )
        else:
            OR['paths'].append( [[0,y],[xback ,y]] )
                      
    # Extended back for large number of inputs
    if inputs > 3:
        OR['paths'].append( [[_leadlen,backlen/2+dy/2],[_leadlen,orheight]] )
        OR['paths'].append( [[_leadlen,-backlen/2-dy/2],[_leadlen,-orheight]] )
        
    # Output lead
    if nor:
        OR['paths'].append( [[0,0],_gap,[tip+_notbubble*2,0],[tip+_leadlen,0]] )
    else:
        OR['paths'].append( [[0,0],_gap,[tip,0],[tip+_leadlen,0]] )
    
    return OR


# Define common AND/NANDs
AND2 = andgate(2, name='AND2' )
AND3 = andgate(3, name='AND3' )
AND4 = andgate(4, name='AND4' )
NAND2 = andgate(2, nand=True, name='NAND2' )
NAND3 = andgate(3, nand=True, name='NAND3' )
NAND4 = andgate(4, nand=True, name='NAND4' )

# Define common OR gates
OR2 = orgate(2, name='OR2' )
OR3 = orgate(3, name='OR3' )
OR4 = orgate(4, name='OR4' )
NOR2 = orgate(2, nor=True, name='NOR2' )
NOR3 = orgate(3, nor=True, name='NOR3' )
NOR4 = orgate(4, nor=True, name='NOR4' )
XOR2 = orgate(2, xor=True, name='XOR2' )
XOR3 = orgate(3, xor=True, name='XOR3' )
XOR4 = orgate(4, xor=True, name='XOR4' )
XNOR2 = orgate(2, xor=True, nor=True, name='XNOR2' )
XNOR3 = orgate(3, xor=True, nor=True, name='XNOR3' )
XNOR4 = orgate(4, xor=True, nor=True, name='XNOR4' )

# Inverters/Buffers
BUF = {
    'name'  : 'BUF',
    'paths' : [ [ [0,0],[_leadlen,0],[_leadlen,-_gateh/2],[_gatel+_leadlen,0],[_leadlen,_gateh/2],[_leadlen,0] ],
                [ [_gatel+_leadlen,0],[_gatel+_leadlen*2,0] ] ],
    'extend' : False,
    'anchors' : {'out' : [_gatel+_gateh/2+_leadlen*2,0] }
     }

NOT = {
    'name'  : 'NOT',
    'paths' : [ [ [0,0],[_leadlen,0],[_leadlen,-_gateh/2],[_gatel+_leadlen,0],[_leadlen,_gateh/2],[_leadlen,0] ],
                [ [_gatel+_leadlen+_notbubble*2,0],[_gatel+_leadlen*2,0] ] ],
    'shapes' : [ {'shape':'circle',
                  'center':[_gatel+_leadlen+_notbubble,0],
                  'radius':_notbubble} ],
    'extend' : False,
    'anchors' : {'out' : [_gatel+_gateh/2+_leadlen*2,0] }
     }

NOTNOT = {
    'name'  : 'NOTNOT',
    'paths' : [ [ [0,0],[_leadlen-_notbubble*2,0],_gap,[_leadlen,0],[_leadlen,-_gateh/2],[_gatel+_leadlen,0],[_leadlen,_gateh/2],[_leadlen,0] ],
                [ [_gatel+_leadlen+_notbubble*2,0],[_gatel+_leadlen*2,0] ] ],
    'shapes' : [ {'shape':'circle',
                  'center':[_gatel+_leadlen+_notbubble,0],
                  'radius':_notbubble},
                  {'shape':'circle',
                  'center':[_leadlen-_notbubble,0],
                  'radius':_notbubble} ],
    'extend' : False,
    'anchors' : {'out' : [_gatel+_gateh/2+_leadlen*2,0] }
     }

