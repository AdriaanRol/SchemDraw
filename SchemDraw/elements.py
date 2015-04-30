'''
Electrical element symbols for schematic drawing.

Each element is a dictionary with key/values defining how it should be drawn.

Coordinates are all defined in element cooridnates, where the element begins
at [0,0] and is drawn from left to right. The drawing engine will then rotate
and translate the element to its final position. A standard resistor is
1 drawing unit long, and with default lead extension will become 3 units long.

Possible dictionary keys:
    name:  A name string for the element. Currently only used for testing.
    paths: A list of each path line in the element. For example, a capacitor
           has two paths, one for each capacitor "plate". On 2-terminal
           elements, the leads will be automatically extended away from the
           first and last points of the first path, and don't need to
           be included in the path.
    base:  Dictionary defining a base element. For example, the variable
           resistor has a base of resistor, then adds an additional path.
    shapes: A list of shape dictionaries.
            'shape' key can be [ 'circle', 'poly', 'arc', 'arrow' ]
            Other keys depend on the shape as follows.
            circle:
                'center': xy center coordinate
                'radius': radius of circle
                'fill'  : [True, False] fill the circle
                'fillcolor' : color for fill
            poly:
                'xy' : List of xy coordinates defining polygon
                'closed': [True, False] Close the polygon
                'fill'  : [True, False] fill the polygon
                'fillcolor' : color for fill
            arc:
                'center' : Center coordinate of arc
                'width', 'height': width and height of arc
                'theta1' : Starting angle (degrees)
                'theta2' : Ending angle (degrees)
                'angle'  : Rotation angle of entire arc
                'arrow'  : ['cw', 'ccw'] Add an arrowhead, clockwise or counterclockwise
            arrow:
                'start'  : start of arrow
                'end'    : end of arrow
                'headwidth', 'headlength': width and length of arrowhead
    theta: Default angle (in degrees) for the element. Overrides the current
           drawing angle.
    anchors: A dictionary defining named positions within the element. For
             example, the NFET element has a 'source', 'gate', and 'drain'
             anchor. Each anchor will become an attribute of the element class
             which can then be used for connecting other elements.

    extend: [True, False] Extend the leads to fill the full element length.
    move_cur: [True, False] Move the drawing cursor location after drawing.
    color: A matplotlib-compatible color for the element. Examples include
           'red', 'blue', '#34ac92'
    drop: Final location to leave drawing cursor.
    lblloc: ['top', 'bot', 'lft', 'rgt'] default location for text label.
            Defaults to 'top'.
    lblofst: Default distance between element and text label.
    labels: List of (label, pos, align) tuples defining text labels to always draw
            in the element. Align is (horiz, vert) tuple of
            (['center', 'left', right'], ['center', 'bottom', 'top'])
    labels: list of label dictionaries. Each label has keys:
            'label' : string label
            'pos'   : xy position
            'align' : (['center', 'left', right'], ['center', 'bottom', 'top']) alignment
            'size'  : font size


'''

import numpy as _np

_gap = [_np.nan, _np.nan]   # To leave a break in the plot

# Resistor is defined as 1 matplotlib plot unit long.
# When default leads are added, the total length will be three units.
_rh = 0.25      # Resistor height
_rw = 1.0 / 6   # Full (inner) length of resistor is 1.0 data unit

# Basic elements

RES = {
    'name'  : 'RES',
    'paths' : [ [[0,0],[0.5*_rw,_rh],[1.5*_rw,-_rh],[2.5*_rw,_rh],[3.5*_rw,-_rh],[4.5*_rw,_rh],[5.5*_rw,-_rh],[6*_rw,0]] ],
    }

RES_VAR = {
    'name'  : 'RES_VAR',
    'base'  : RES,
    'shapes' : [ { 'shape' : 'arrow',
                   'start' : [1.5*_rw,-_rh*2],
                   'end'   : [4.5*_rw,_rw*3.5],
                   'headwidth' : .12,
                   'headlength' : .2 } ],
    'paths' : [ [[1.5*_rw,-_rh*2],[4.5*_rw,_rw*3.5]] ]
     }

RBOX = {
    'name'  : 'RBOX',
    'paths' : [ [ [0,0],[0,_rh],[_rw*6,_rh],[_rw*6,-_rh],[0,-_rh],[0,0],_gap,[_rw*6,0] ] ]
    }

POT = {
    'name'  : 'POT',
    'base'   : RES,
    'shapes' : [ { 'shape' : 'arrow',
                   'start' : [_rw*3,_rw*5],
                   'end'   : [_rw*3,_rw*1.5],
                   'headwidth' : .15,
                   'headlength' : .25 } ],
    'lblloc' : 'bot',
    'anchors' : { 'tap' : [_rw*3,_rw*1.5] }
     }

_cap_gap = 0.18
CAP = {   # Straight capacitor
    'name'  : 'CAP',
    'paths'   : [ [[0,0],_gap,[0,_rh],[0,-_rh],_gap,[_cap_gap,_rh],[_cap_gap,-_rh],_gap,[_cap_gap,0]] ],
    }

CAP_P = {   # Polarized
    'name'  : 'CAP_P',
    'base'  : CAP,
    'labels' : [ {'label':'+', 'pos':[-_cap_gap*1.2,_cap_gap]} ]
    }

CAP2 = {  # Curved capacitor
    'name'  : 'CAP2',
    'paths'   : [ [[0,0],_gap,[0,_rh],[0,-_rh],_gap,[_cap_gap,0]] ],
    'shapes'  : [ { 'shape'  : 'arc',
                    'center' :[(_cap_gap*1.5),0],
                    'theta1' : 120,
                    'theta2' : -120,
                    'width'  : _cap_gap,
                    'height' : _rh*2.5 } ],
    }

CAP2_P = {   # Polarized
    'name'  : 'CAP2_P',
    'base'  : CAP2,
    'labels' : [ {'label':'+', 'pos':[-_cap_gap*1.2,_cap_gap]} ]
    }

_cap_gap = 0.2
XTAL = {   # Crystal
    'name'  : 'XTAL',
    'paths'   : [ [[0,0],_gap,[0,_rh],[0,-_rh],_gap,
                   [_cap_gap/2,_rh],[_cap_gap/2,-_rh],[_cap_gap*1.5,-_rh],[_cap_gap*1.5,_rh],[_cap_gap/2,_rh],_gap,
                   [_cap_gap*2,_rh],[_cap_gap*2,-_rh],_gap,[_cap_gap*2,0]],
                ],
    }

DIODE = {
    'name'  : 'DIODE',
    'paths'   : [ [[0,0],_gap,[_rh*1.4,_rh],[_rh*1.4,-_rh],_gap,[_rh*1.4,0] ] ],
    'anchors' : { 'center' : [_rh,0] },
    'shapes'  : [ { 'shape':'poly',
                    'xy'   : _np.array([[0,_rh],[_rh*1.4,0],[0,-_rh]]),
                    'fill' : False } ]
    }

DIODE_F = {
    'name'  : 'DIODE_F',
    'base': DIODE,
    'shapes' : [ { 'shape':'poly',
                    'xy'   : _np.array([[0,_rh],[_rh*1.4,0],[0,-_rh]]),
                    'fill' : True } ]
    }

_sd = .1
SCHOTTKY = {  # Schottky diode
    'name' : 'SCHOTTKY',
    'base' : DIODE,
    'paths' : [ [[_rh*1.4,_rh], [_rh*1.4-_sd,_rh],  [_rh*1.4-_sd,_rh-_sd]],
                [[_rh*1.4,-_rh], [_rh*1.4+_sd,-_rh], [_rh*1.4+_sd,-_rh+_sd]] ]
}

SCHOTTKY_F = {
    'name' : 'SCHOTTKY_F',
    'base' : DIODE_F,
    'paths' : [ [[_rh*1.4,_rh], [_rh*1.4-_sd,_rh],  [_rh*1.4-_sd,_rh-_sd]],
                [[_rh*1.4,-_rh], [_rh*1.4+_sd,-_rh], [_rh*1.4+_sd,-_rh+_sd]] ]
}

ZENER = {  # Zener diode
    'name' : 'ZENER',
    'base' : DIODE,
    'paths' : [ [[_rh*1.4,_rh],  [_rh*1.4+_sd,_rh+_sd]],
                [[_rh*1.4,-_rh], [_rh*1.4-_sd,-_rh-_sd]] ]
}

ZENER_F = {
    'name' : 'ZENER_F',
    'base' : DIODE_F,
    'paths' : [ [[_rh*1.4,_rh],  [_rh*1.4+_sd,_rh+_sd]],
                [[_rh*1.4,-_rh], [_rh*1.4-_sd,-_rh-_sd]] ]
}

LED = {
    'name':'LED',
    'base':DIODE,
    'paths' : [[[_rh,_rh*1.5],[_rh*2,_rh*3.25]]],  # Duplicate arrow with a path to work around matplotlib autoscale bug.
    'shapes':[ { 'shape':'arrow',
                 'start': [_rh,_rh*1.5],
                 'end'  : [_rh*2,_rh*3.25],
                   'headwidth' : .12,
                   'headlength' : .2 },
               { 'shape':'arrow',
                 'start': [_rh*.1,_rh*1.5],
                 'end'  : [_rh*1.1,_rh*3.25],
                   'headwidth' : .12,
                   'headlength' : .2 }, ]
    }

# LED with squiggle light
x = _np.linspace(-1,1)
y = -x*(x-.7)*(x+.7)/2 + _rh*2.5
x = _np.linspace(_rh*.75,_rh*1.25)
theta = 20
c = _np.cos( _np.radians(theta) )
s = _np.sin( _np.radians(theta) )
m = _np.array( [[c,s],[-s,c]] )
p = _np.transpose(_np.vstack((x,y)))
p = _np.dot( p, m )
p2 = _np.transpose(_np.vstack((x-.2,y)))
p2 = _np.dot( p2, m )
LED2 = {
    'name'   : 'LED2',
    'base'   : DIODE,
    'paths'  : [p,p2],
    'shapes' : [ {'shape':'arrow',
                  'start' : p[1],
                  'end'   : p[0],
                  'headwidth' : .07,
                  'headlength' : .08
                 },
                 {'shape':'arrow',
                  'start' : p2[1],
                  'end'   : p2[0],
                  'headwidth' : .07,
                  'headlength' : .08
                 } ]
    }


_mr = 0.2
MEMRISTOR = { 
    'name'  : 'MEMRISTOR',
    'paths' : [ [[0,_mr*1.25],[_mr*5,_mr*1.25],[_mr*5,_mr*-1.25],[0,_mr*-1.25],[0,_mr*1.25]],
                [[0,0],[_mr,0],[_mr,-_mr*.75],[_mr*2,-_mr*.75],[_mr*2,_mr*.75],[_mr*3,_mr*.75],[_mr*3,-_mr*.75],[_mr*4,-_mr*.75],[_mr*4,0],[_mr*5,0]],
              ],
    'shapes' : [ {'shape':'poly', 
                  'xy' : [[0,_mr*1.25],[0,-_mr*1.25],[_mr/2,-_mr*1.25],[_mr/2,_mr*1.25] ],
                  'fill' : True
                 }
               ]
    }

_mrv = .25
MEMRISTOR2 = { 
    'name'  : 'MEMRISTOR2',
    'paths' : [ [[0,0],[0,_mrv],[_mr,_mrv],[_mr,-_mrv],[_mr*2,-_mrv],[_mr*2,_mrv],
                 [_mr*3,_mrv],[_mr*3,-_mrv],[_mr*4,-_mrv],[_mr*4,_mrv],
                 [_mr*5,_mrv],[_mr*5,-_mrv],[_mr*6,-_mrv],[_mr*6,0],
                 [_mr*7,0]],

              ],
    }


# Connection dots, lines
_dotr = .075
DOT_OPEN = {
    'name'  : 'DOT_OPEN',
    'paths'    : [ [[0,0]] ],
    'shapes'  : [ { 'shape':'circle',
                    'center':[0,0],
                    'radius':_dotr,
                    'fill' : True,
                    'fillcolor' : 'white' } ],
    'theta'   : 0,
    'extend'  : False,
    }

DOT = {
    'name'  : 'DOT',
    'paths'  : [ [[0,0]] ],
    'shapes' : [ { 'shape':'circle',
                   'center':[0,0],
                   'radius':_dotr,
                   'fill' : True,
                   'fillcolor' : 'black' }  ],
    'theta'   : 0,
    'extend'  : False,
    }
    
ELLIPSIS = {
    'name' : 'ELLIPSIS',
    'shapes'  : [{ 'shape':'circle',
                  'center':[.5,0],
                  'radius':_dotr/2,
                  'fill':True,
                  'fillcolor':'black'},
                { 'shape':'circle',
                  'center':[1,0],
                  'radius':_dotr/2,
                  'fill':True,
                  'fillcolor':'black'},
                { 'shape':'circle',
                  'center':[1.5,0],
                  'radius':_dotr/2,
                  'fill':True,
                  'fillcolor':'black'} ],
    'extend' : False,
    'drop'   : [2,0]
    }


LINE = { 'name'  : 'LINE', 'paths' : [ _np.array([[0,0]]) ] }

# Label centered over a gap
GAP_LABEL = {
    'name'    : 'LABEL',
    'paths'   : [ [[0,0],_gap,[1,0]] ],
    'lblloc'  : 'center',
    'lblofst' : 0,
    'color'   : 'white'
    }

GAP = {
    'base' : GAP_LABEL
    }

# Label at the specific location
LABEL = {
    'name' : 'LABEL',
    'lblloc' : 'center',
    'lblofst' : 0,
    'move_cur' : False
    }


# Grounds
_gnd_gap = 0.12
_gnd_lead = 0.4
GND = {
    'name'  : 'GND',
    'paths'   : [ [[0,0],[0,-_gnd_lead],[-_rh,-_gnd_lead],[_rh,-_gnd_lead],_gap,[-_rh*.7,-_gnd_gap-_gnd_lead],[_rh*.7,-_gnd_gap-_gnd_lead],_gap,[-_rh*.2,-_gnd_gap*2-_gnd_lead],[_rh*.2,-_gnd_gap*2-_gnd_lead]]  ],
    'move_cur': False,
    'extend'  : False,
    'theta'   : 0
    }

GND_SIG = {
    'name'  : 'GND_SIG',
    'paths'    : [ [[0,0],[0,-_gnd_lead],[-_rh,-_gnd_lead],[0,-_gnd_lead*2],[_rh,-_gnd_lead],[0,-_gnd_lead]] ],
    'move_cur': False,
    'extend'  : False,
    'theta'   : 0
    }

_chgnd_dx = _rh*.75
_chgnd_dy = _rh
GND_CHASSIS = {
    'name'  : 'GND_CHASSIS',
    'paths'    : [ [[0,0],[0,-_gnd_lead],[-_chgnd_dx,-_gnd_lead-_chgnd_dy]],
                   [[0,-_gnd_lead],[-_chgnd_dx,-_gnd_lead],[-_chgnd_dx*2,-_gnd_lead-_chgnd_dy]],
                   [[0,-_gnd_lead],[_chgnd_dx,-_gnd_lead],[0,-_gnd_lead-_chgnd_dy]]  ],
    'move_cur': False,
    'extend'  : False,
    'theta'   : 0
    }


# Opamp
_oa_back = 2.5
_oa_xlen = _oa_back * _np.sqrt(3)/2
_oa_lblx = _oa_xlen/8
_oa_pluslen = .2
OPAMP_NOSIGN = {
    'name'  : 'OPAMP_NOSIGN',
    'paths'   : [ [[0,0],[0,_oa_back/2],[_oa_xlen,0],[0,-_oa_back/2],[0,0], _gap, [_oa_xlen,0]], # Triangle
                ],
    'anchors' : { 'center' : [_oa_xlen/2,0],
                  'in1'    : [0,_oa_back/4],
                  'in2'    : [0,-_oa_back/4],
                  'out'    : [_oa_xlen,0]  },
    'extend'  : False,
    }

OPAMP = {
    'name'  : 'OPAMP',
    'paths'   : [ [[0,0],[0,_oa_back/2],[_oa_xlen,0],[0,-_oa_back/2],[0,0], _gap, [_oa_xlen,0]], # Triangle
                  [[_oa_lblx-_oa_pluslen/2, _oa_back/4], [_oa_lblx+_oa_pluslen/2, _oa_back/4]],  # '-' sign
                  [[_oa_lblx-_oa_pluslen/2, -_oa_back/4],[_oa_lblx+_oa_pluslen/2, -_oa_back/4]], # '+' sign
                  [[_oa_lblx,-_oa_back/4-_oa_pluslen/2], [_oa_lblx, -_oa_back/4+_oa_pluslen/2]]  # '' sign
                ],
    'anchors' : { 'center' : [_oa_xlen/2,0],
                  'in1'    : [0,_oa_back/4],
                  'in2'    : [0,-_oa_back/4],
                  'out'    : [_oa_xlen,0]  },
    'extend'  : False,
    }


# FETs
_fetw = _rw*4
_feth = _rw*5
_fetl = _feth/2
_fet_gap = _rw*1.5
_fetr = _rw*.7  # Radius of "not" bubble
NFET = {
    'name'  : 'NFET',
    'paths'  : [ [ [0,0],[0,-_fetl],[_fetw,-_fetl],[_fetw,-_fetl-_fetw],[0,-_fetl-_fetw],[0,-2*_fetl-_fetw] ],
                 [ [_fetw+_fet_gap,-_fetl],[_fetw+_fet_gap,-_fetl-_fetw] ],
                 [ [_fetw+_fet_gap,-_fetl-_fetw/2], [_fetw+_fet_gap+_fetl+_fetr,-_fetl-_fetw/2] ] ],
    'extend'  : False,
    'drop'    : _np.array([0,-2*_fetl-_fetw]),
    'lblloc' : 'lft',
    'anchors' : { 'source' : [0, -2*_fetl-_fetw],
                  'drain'  : [0, 0],
                  'gate'   : [_fetw+_fet_gap+_fetl+_fetr,-_fetl-_fetw/2] }
     }

PFET = {
    'name'  : 'PFET',
    'paths'  : [ [ [0,0],[0,-_fetl],[_fetw,-_fetl],[_fetw,-_fetl-_fetw],[0,-_fetl-_fetw],[0,-2*_fetl-_fetw] ],
                 [ [_fetw+_fet_gap,-_fetl],[_fetw+_fet_gap,-_fetl-_fetw] ],
                 [ [_fetw+_fet_gap+_fetr*2,-_fetl-_fetw/2], [_fetw+_fet_gap+_fetl+_fetr,-_fetl-_fetw/2] ] ],
    'shapes' : [ { 'shape'   : 'circle',
                    'center' : [_fetw+_fet_gap+_fetr,-_fetl-_fetw/2],
                    'radius' : _fetr } ],
    'extend'  : False,
    'drop'    : _np.array([0,-2*_fetl-_fetw]),
    'lblloc' : 'lft',
    'anchors' : { 'source' : [0, 0],
                  'drain'  : [0, -2*_fetl-_fetw],
                  'gate'   : [_fetw+_fet_gap+_fetl+_fetr,-_fetl-_fetw/2] }
     }


# BJT transistors
_bjt_r = _rw*3.3   # Radius of BJT circle
_bjt_v = _bjt_r*2/3  # x coord of vertical line
_bjt_v_len = _bjt_r*4/3  # height of vertical line
_bjt_a = _bjt_v_len/4    # Intercept of emitter/collector lines
_bjt_emx = _bjt_v + _bjt_r*.7  # x-coord of emitter exiting circle
_bjt_emy = _bjt_v_len*.7    # y-coord of emitter exiting circle

BJT = {
    'name'  : 'BJT',
    'paths'  : [ [[0,0],[_bjt_v,0]],
                 [[_bjt_v,_bjt_v_len/2],[_bjt_v,-_bjt_v_len/2]],
                 [[_bjt_v,_bjt_a],[_bjt_emx,_bjt_emy],[_bjt_emx,_bjt_emy+_bjt_a]],
                 [[_bjt_v,-_bjt_a],[_bjt_emx,-_bjt_emy],[_bjt_emx,-_bjt_emy-_bjt_a]] ],
     'extend'  : False,
     'drop'    : _np.array([_bjt_emx,_bjt_emy+_bjt_a]),
     'lblloc'  : 'rgt',
     'anchors' : { 'base'      : [0, 0],
                   'collector' : [_bjt_emx,_bjt_emy+_bjt_a],
                   'emitter'   : [_bjt_emx,-_bjt_emy-_bjt_a] }
      }

BJT_NPN = {
    'name'  : 'BJT_NPN',
    'base' : BJT,
    'shapes' : [ { 'shape' : 'arrow',
                   'start' : [_bjt_v,-_bjt_a],
                   'end'   : [_bjt_emx,-_bjt_emy] }  ]
    }

BJT_PNP = {
    'name'  : 'BJT_PNP',
    'base' : BJT,
    'shapes' : [ { 'shape' : 'arrow',
                   'end'    : [_bjt_v,_bjt_a],
                   'start'   : [_bjt_emx,_bjt_emy] } ],
    'anchors' : { 'base'      : [0, 0],
                  'emitter' : [_bjt_emx,_bjt_emy+_bjt_a],
                  'collector'   : [_bjt_emx,-_bjt_emy-_bjt_a] }
     }

BJT_NPN_C = {
    'name'  : 'BJT_NPN_C',
    'base' : BJT_NPN,
    'shapes' : [ { 'shape' : 'circle',
                   'center' : [_bjt_r,0],
                   'radius' : _bjt_r  }]
    }

BJT_PNP_C = {
    'name'  : 'BJT_PNP_C',
    'base' : BJT_PNP,
    'shapes' : [ { 'shape' : 'circle',
                   'center' : [_bjt_r,0],
                   'radius' : _bjt_r  }]
    }

# Inductor without spiraling
_ind_w = .25
_ind_shape_list = []
for _i in range(4):
    _ind_shape_list.append( {'shape':'arc',
                             'center':[(_i*2+1)*_ind_w/2,0],
                             'theta1' : 0,
                             'theta2' : 180,
                             'width'  : _ind_w,
                             'height' : _ind_w } )
INDUCTOR = {
    'name'  : 'INDUCTOR',
    'paths' : [ [[0,0],_gap,[1,0] ] ],
    'shapes' : _ind_shape_list }

# Inductor with spiraling - "Prolate cycloid"
# Magic numbers that work to look like an inductor spiral
_a = .25
_b = .6
_t = _np.linspace(1.4,9.55*_np.pi,100)
_x = _a*_t - _b*_np.sin(_t)
_y = _a - _b * _np.cos(_t)
_x = (_x - _x[0])  # Scale to about the right size
_x = _x / _x[-1]
_y = (_y - _y[0]) * .4
_ind_path = _np.transpose(_np.vstack((_x,_y)))
INDUCTOR2 = {
    'name'  : 'INDUCTOR2',
    'paths' : [ _ind_path ]
    }

# Independent sources
SOURCE = {
    'name'  : 'SOURCE',
    'paths'  : [ [[0,0],[0,0],_gap,[1,0],[1,0] ] ],
    'theta'  : 90.,
    'shapes' : [ {'shape': 'circle',
                  'center': [0.5, 0],
                  'radius': 0.5 } ],
     }

_plus_len = .2
SOURCE_V = {
    'name'  : 'SOURCE_V',
    'base' : SOURCE,
    'paths' : [ [[.25,-_plus_len/2],[.25,_plus_len/2]   ], # '-' sign
                [[.75-_plus_len/2,0],[.75+_plus_len/2,0]], # '+' sign
                [[.75,-_plus_len/2 ],[.75,_plus_len/2 ]], # '+' sign
              ]
    }

SOURCE_I = {
    'name'  : 'SOURCE_I',
    'base' : SOURCE,
    'shapes' : [ { 'shape' : 'arrow',
                   'start' : [.75,0],
                   'end'   : [.25,0] } ]
    }


_sin_y = _np.linspace(.25,.75,num=25) - 0.5
_sin_x = .2 * _np.sin((_sin_y-.25)*_np.pi*2/.5) + 0.5
_sin_path = _np.transpose(_np.vstack((_sin_x,_sin_y)))
SOURCE_SIN = {
    'name'  : 'SOURCE_SIN',
    'base'  : SOURCE,
    'paths' : [ _sin_path ]
    }


#Controlled sources
SOURCE_CONT = {
    'name'  : 'SOURCE_CONT',
    'paths'   : [ [[0,0],[.5,.5],[1,0]],
                  [[0,0],[.5,-.5],[1,0]] ],
    'theta'   : 90.,
     }

SOURCE_CONT_V = {
    'name'  : 'SOURCE_CONT_V',
    'base'   : SOURCE_CONT,
    'paths' : [ [[.25,-_plus_len/2],[.25,_plus_len/2]   ], # '-' sign
                [[.75-_plus_len/2,0],[.75+_plus_len/2,0]], # '+' sign
                [[.75,-_plus_len/2 ],[.75,_plus_len/2 ]],  # '+' sign
              ]
    }

SOURCE_CONT_I = {
    'name'  : 'SOURCE_CONT_I',
    'base' : SOURCE_CONT,
    'shapes' : [ { 'shape' : 'arrow',
                   'start' : [.75,0],
                   'end'   : [.25,0] } ]
    }

# Batteries
_batw = _rh*.75
_bat1 = _rh*1.5
_bat2 = _rh*.75
BAT_CELL = {
    'name'  : 'BAT_CELL',
    'paths' : [ [[0,_bat1],[0,-_bat1] ],
                [[_batw,_bat2],[_batw,-_bat2]],
                [[0,0],_gap,[_batw,0]]
              ]
    }

BATTERY = {
    'name'  : 'BATTERY',
    'paths' : [ [[0,_bat1],[0,-_bat1] ],
                [[_batw,_bat2],[_batw,-_bat2]],
                [[_batw*2,_bat1],[_batw*2,-_bat1] ],
                [[_batw*3,_bat2],[_batw*3,-_bat2]],
                [[0,0],_gap,[_batw*3,0]]
              ]
    }



# Meters
METER_V = {
    'name'  : 'METER_V',
    'base' : SOURCE,
    'labels' : [ {'label':'V', 'pos':[.5,0]} ]
    }

METER_I = {
    'name'  : 'METER_I',
    'base' : SOURCE,
    'labels' : [ {'label':'I', 'pos':[.5,0]} ]
    }

METER_OHM = {
    'name'  : 'METER_OHM',
    'base' : SOURCE,
    'labels' : [ {'label':'$\Omega$', 'pos':[.5,0]} ]
    }


# Arrows for labeling current
ARROWLINE = {
    'name'  : 'ARROWLINE',
    'paths' : [ [[0,0],[1,0]]],
    'shapes' : [ { 'shape' : 'arrow',
                   'start' : [0,0],
                   'end'   : [0.55,0],
                   'headwidth' : .2,
                   'headlength' : .3 } ],
    'lblofst' : .2,
    }

ARROW_I = {
    'name'  : 'ARROW_I',
    'shapes' : [ { 'shape' : 'arrow',
                   'start' : [0,0],
                   'end'   : [2,0],
                   'headwidth' : .2,
                   'headlength' : .3 } ],
    'anchors' : { 'center' : [1,0]},
    'lblofst' : .2,
    'move_cur' : False
    }

# Switches
_sw_dot_r = .12
SWITCH_SPST = {
    'name'  : 'SWITCH_SPST',
    'paths'  : [ [ [0,0],_gap,[_sw_dot_r*2,.1],[.8,.45],_gap,[1,0] ] ],
    'shapes' : [ { 'shape'  : 'circle',
                   'center' : [_sw_dot_r,0],
                   'radius' : _sw_dot_r },
                 { 'shape'  : 'circle',
                   'center' : [1-_sw_dot_r,0],
                   'radius' : _sw_dot_r } ]
    }

SWITCH_SPST_OPEN = {
    'name'  : 'SWITCH_SPST_OPEN',
    'base' : SWITCH_SPST,
    'shapes' : [ { 'shape' : 'arc',
                   'center' : [.4,.1],
                   'width'  : .5,
                   'height' : .75,
                   'theta1' : -10,
                   'theta2' : 70,
                   'arrow'  : 'ccw' } ]
    }

SWITCH_SPST_CLOSE = {
    'name'  : 'SWITCH_SPST_CLOSE',
    'base' : SWITCH_SPST,
    'shapes' : [ { 'shape' : 'arc',
                   'center' : [.4,.25],
                   'width'  : .5,
                   'height' : .75,
                   'theta1' : -10,
                   'theta2' : 70,
                   'arrow'  : 'cw' } ]
    }

SWITCH_SPDT = {
    'name'  : 'SWITCH_SPDT',
    'base'  : SWITCH_SPST,
    'shapes' : [ { 'shape'  : 'circle',
                   'center' : [1-_sw_dot_r,.7],
                   'radius' : _sw_dot_r } ],
    'anchors' : { 'a' : [0,0],
                  'b' : [1,0],
                  'c' : [1,.7]
                },
    'extend' : False
    }

SWITCH_SPDT_OPEN  = {
    'name'  : 'SWITCH_SPDT_OPEN',
    'base'  : SWITCH_SPST_OPEN,
    'shapes' : [ { 'shape'  : 'circle',
                   'center' : [1-_sw_dot_r,.7],
                   'radius' : _sw_dot_r } ],
    'extend' : False
    }

SWITCH_SPDT_CLOSE  = {
    'name'  : 'SWITCH_SPDT_CLOSE',
    'base'  : SWITCH_SPST_CLOSE,
    'shapes' : [ { 'shape'  : 'circle',
                   'center' : [1-_sw_dot_r,.7],
                   'radius' : _sw_dot_r } ],
    'extend' : False
    }

SWITCH_SPDT2 = {
    'name'  : 'SWITCH_SPDT2',
    'paths'  : [ [ [0,0],_gap,[_sw_dot_r*2,.1],[.7,.25],_gap,[1,.4] ] ],
    'shapes' : [ { 'shape'  : 'circle',
                   'center' : [_sw_dot_r,0],
                   'radius' : _sw_dot_r },
                 { 'shape'  : 'circle',
                   'center' : [1-_sw_dot_r,-.4],
                   'radius' : _sw_dot_r },
                 { 'shape'  : 'circle',
                   'center' : [1-_sw_dot_r,.4],
                   'radius' : _sw_dot_r } ],
    'anchors' : { 'a' : [0,0],
                  'b' : [1,.4],
                  'c' : [1,-.4]
                },
    'extend' : False
    }

SWITCH_SPDT2_OPEN = {
    'name'  : 'SWITCH_SPDT2_OPEN',
    'base'  : SWITCH_SPDT2,
    'shapes' : [ { 'shape' : 'arc',
                   'center' : [.35,0],
                   'width'  : .5,
                   'height' : .75,
                   'theta1' : -10,
                   'theta2' : 70,
                   'arrow'  : 'ccw' } ]
    }

SWITCH_SPDT2_CLOSE = {
    'name'  : 'SWITCH_SPDT2_CLOSE',
    'base'  : SWITCH_SPDT2,
    'shapes' : [ { 'shape' : 'arc',
                   'center' : [.3,.1],
                   'width'  : .5,
                   'height' : .75,
                   'theta1' : -10,
                   'theta2' : 70,
                   'arrow'  : 'cw' } ]
    }

# Pushbuttons
BUTTON = {
    'name'  : 'BUTTON',
    'paths'  : [ [ [0,0],_gap,[_sw_dot_r,.3],[1-_sw_dot_r,.3],_gap,[.5,.3],[.5,.5],_gap,[1,0] ] ],
    'shapes' : [ { 'shape'  : 'circle',
                   'center' : [_sw_dot_r,0],
                   'radius' : _sw_dot_r },
                 { 'shape'  : 'circle',
                   'center' : [1-_sw_dot_r,0],
                   'radius' : _sw_dot_r } ]
    }

BUTTON_NC = {
    'name'  : 'BUTTON_NC',
    'paths'  : [ [ [0,0],_gap,[_sw_dot_r,-_sw_dot_r-.05],[1-_sw_dot_r,-_sw_dot_r-.05],_gap,[.5,-_sw_dot_r-.05],[.5,_sw_dot_r+.15],_gap,[1,0] ] ],
    'shapes' : [ { 'shape'  : 'circle',
                   'center' : [_sw_dot_r,0],
                   'radius' : _sw_dot_r },
                 { 'shape'  : 'circle',
                   'center' : [1-_sw_dot_r,0],
                   'radius' : _sw_dot_r } ]
    }


# Speakers, bulbs, etc.
_sph = .5
SPEAKER = {
    'name'  : 'SPEAKER',
    'paths'  : [ [ [0,0],[_rh,0] ],
                 [ [0,-_sph],[_rh,-_sph]]
            ],
    'drop'   : [0,-_sph],
    'extend' : False,
    'shapes' : [ { 'shape' : 'poly',
                   'xy'    : [ [_rh,_sph/2],[_rh,-_sph*1.5],[_rh*2,-_sph*1.5],[_rh*2,_sph/2] ] },
                 { 'shape' : 'poly',
                   'xy'    : [ [_rh*2,_sph/2], [_rh*3.5,_sph*1.25],[_rh*3.5,-_sph*2.25],[_rh*2,-_sph*1.5] ],
                   'closed' : False } ]
    }

_a = .25
_b = .7
_t = _np.linspace(1.4,3.6*_np.pi,100)
_x = _a*_t - _b*_np.sin(_t)
_y = _a - _b * _np.cos(_t)
_x = (_x - _x[0])  # Scale to about the right size
_x = _x / _x[-1]
_y = (_y - _y[0]) * .25
_lamp_path = _np.transpose(_np.vstack((_x,_y)))
LAMP = {
    'name'  : 'LAMP',
    'base' : SOURCE,
    'paths': [_lamp_path]
    }


def blackbox( w, h, linputs=None, rinputs=None, tinputs=None, binputs=None, mainlabel='', leadlen=0.5 ):
    ''' Generate a black-box element consisting of rectangle with inputs on each side.
    
        w, h : width and height of rectangle
        mainlabel : main box label
        leadlen   : length of lead extensions
        linputs, rinputs, tinputs, binputs: dictionary input definition for each side
        of the box. Default to no inputs. Dictionary keys:
            cnt : number of inputs for that side
            labels: list of string labels for each input. drawn inside the box. default is blank.
            plabels: list of pin label strings. drawn outside the box. Default is blank.
            loc: list of pin locations (0 to 1), along side. Defaults to evenly spaced pins.
            leads: True/False, draw leads coming out of box. Default=True.
            lblofst: float offset for labels. Default=.15
            plblofst: float offset for pin labels. Default=.1
            lblsize: font size for labels. Default=16
            plblsize: font size for pin labels. Default=12

        Anchors will be generated on each pin matching label names if provided. If no 
        labels, anchors are named 'inL1', 'inL2', ... 'inR1', 'inR2', 'inT1', 'inB1', etc.

    '''
    box = {
           'paths' : [ [[0,0],[w,0],[w,h],[0,h],[0,0]] ],
           'anchors':{},
           'labels':[],
           'extend':False, }

    if mainlabel is not None:
        box['labels'].append( {'label':mainlabel, 'pos':[w/2,h*2/3] })
    
    for side, sidelabel in [('left',linputs),('right',rinputs),('top',tinputs),('bottom',binputs)]:
        if sidelabel==None: continue
        cnt        = sidelabel.get('cnt',0)
        sidelabels = sidelabel.get('labels',[])
        plabels    = sidelabel.get('plabels',[])
        loc        = sidelabel.get('loc',None)
        leads      = sidelabel.get('leads',True)
        lblofst    = sidelabel.get('lblofst',.15)
        plblofst   = sidelabel.get('plblofst',.1)
        lblsize    = sidelabel.get('lblsize',16)
        plblsize   = sidelabel.get('plblsize',12)
        
        # Determine pin spacings
        if side=='left':
            x0 = 0
            dx = 0
            if cnt > 1:
                y0 = h/(cnt+2)
                dy = (h-2*y0)/(cnt-1)
            else:
                y0 = h/2
                dy = 0
            lblpos = _np.array([lblofst,0])
            lblalign = ('left','center')
            plblpos = _np.array([-plblofst,0])
            plblalign = ('right','bottom')
            leadext = _np.array([-leadlen,0])
        elif side=='right':
            x0 = w
            dx = 0
            if cnt > 1:
                y0 = h/(cnt+2)
                dy = (h-2*y0)/(cnt-1)
            else:
                y0 = h/2
                dy = 0
            lblpos = _np.array([-lblofst,0])
            lblalign = ('right','center')
            plblpos = _np.array([plblofst,0])
            plblalign = ('left','bottom')
            leadext = _np.array([leadlen,0])
        elif side=='top':
            y0 = h
            dy = 0
            if cnt > 1:
                x0 = w/(cnt+2)
                dx = (w-2*x0)/(cnt-1)
            else:
                x0 = w/2
                dx = 0
            lblpos = _np.array([0,-lblofst])
            lblalign = ('center','top')
            plblpos = _np.array([plblofst,0])
            plblalign = ('left','bottom')
            leadext = _np.array([0,leadlen])
        elif side=='bottom':
            y0 = 0
            dy = 0
            if cnt > 1:
                x0 = w/(cnt+2)
                dx = (w-2*x0)/(cnt-1)
            else:
                x0 = w/2
                dx = 0
            lblpos = _np.array([0,lblofst])
            lblalign = ('center','bottom')
            plblpos = _np.array([plblofst,-plblofst])
            plblalign = ('left','top')
            leadext = _np.array([0,-leadlen])
        
        # Add each input
        for i in range(cnt):
            if 'loc' in sidelabel:
                # Custom-spaced labels
                if dx>0:
                    x = sidelabel['loc'][i] * w
                    y = y0
                elif dy>0:
                    y = sidelabel['loc'][i] * h
                    x = x0
            else:
                # Evenly-spaced labels
                x = x0 + dx*i
                y = y0 + dy*i
            
            # Anchor name use label for pin, otherwise use 'inL1', etc.
            if len(sidelabels)==cnt:
                import re
                aname = re.sub(r'\W+', '', sidelabels[i])
            else:
                aname = 'in' + side[0].upper() + str(i+1)
            
            if aname in box['anchors']: aname = aname + '_%d'%i
            
            # Add lead lines
            if leads:
                box['paths'].append( [[x,y],_np.array([x,y])+leadext] )
                box['anchors'][aname] = _np.array([x,y])+leadext   
            else:
                box['anchors'][aname] = [x,y]            
    
            # Add labels
            if len(sidelabels)==cnt:
                box['labels'].append( {'label':sidelabels[i], 'pos':_np.array([x,y])+lblpos, 'align':lblalign, 'size':lblsize } )
            
            if len(plabels)==cnt:
                box['labels'].append( {'label':plabels[i], 'pos':_np.array([x,y])+plblpos, 'align':plblalign, 'size':plblsize }  )

    return box