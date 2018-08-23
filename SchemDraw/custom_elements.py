"""
This file contains custom elements defined by Adriaan Rol
The intention is that these get merged into SchemDraw.elements after cleaning
up so as to merge them into the master of CDelker
"""
import numpy as np
import SchemDraw.elements as e


LOW_PASS = {
    'name': 'LOW_PASS',
    'base': e.RBOX,
    'paths': [[[0.15, 0.05],
               [0.6, 0.05],
               [0.8, -.15]]]
}

# Single port amplifier
AMP = {'name': 'AMP',
       'paths': [[[0, 0],
                  [np.nan, np.nan],
                  [0.7, 0]]],
       'anchors': {'center': [2, 0]},
       'shapes': [{'shape': 'poly', 'xy': np.array([[0.,  0.5],
                                                    [0.7,  0.],
                                                    [0., -0.5]]), 'fill': False}]}


dircoup_w = 2
dircoup_h = .5
h_offset = 0.01

dx = .07
dy = .07

# Directional coupler
DIR_COUP = {
    'name': 'DIR_COUP',
    'paths': [[[0, h_offset], [0, dircoup_h], [dircoup_w, dircoup_h], [dircoup_w, -dircoup_h],
               [0, -dircoup_h], [0, h_offset],  [dircoup_w, h_offset]
               ]],

    'shapes': [{'shape': 'arc',
                'center': [dircoup_w*.9, -dircoup_h],
                'theta1':90, 'theta2':180,
                'width':1, 'height':1,  # 'angle':0,
                },
               {'shape': 'arc',
                'center': [dircoup_w*.1, -dircoup_h],
                'theta1':0, 'theta2':90,
                'width':1, 'height':1,  # 'angle':0,
                },
               {'shape': 'poly',
                'xy': [[dircoup_w*.333-dx, -dircoup_h-dy],
                       [dircoup_w*.333+dx, -dircoup_h-dy],
                       [dircoup_w*.333+dx, -dircoup_h+dy],
                       [dircoup_w*.333-dx, -dircoup_h+dy]],
                'fill': True,
                'fillcolor':'black'
                },
               {'shape': 'poly',
                'xy': [[dircoup_w*.666-dx, -dircoup_h-dy],
                       [dircoup_w*.666+dx, -dircoup_h-dy],
                       [dircoup_w*.666+dx, -dircoup_h+dy],
                       [dircoup_w*.666-dx, -dircoup_h+dy]],
                'fill': True,
                'fillcolor':'black'
                },
               {'shape': 'poly',
                'xy': [[0-dx, h_offset-dy], [0+dx, h_offset-dy],
                       [0+dx, h_offset+dy], [0-dx, h_offset+dy]],
                'fill': True,
                'fillcolor':'black'
                },
               {'shape': 'poly',
                'xy': [[dircoup_w-dx, h_offset-dy],
                       [dircoup_w+dx, h_offset-dy],
                       [dircoup_w+dx, h_offset+dy],
                       [dircoup_w-dx, h_offset+dy]],
                'fill': True,
                'fillcolor':'black'
                },
               ]
}


IQMIXER = {
    'name': 'IQMIXER',
    'base': e.SOURCE,
    'paths': [[[-.35+dx, -.35], [.35+dx, .35],
               [np.nan, np.nan],
               [.35+dx, -.35], [-.35+dx, .35],
               [np.nan, np.nan],
               [0.5, -1], [0.5, -.50],
               [np.nan, np.nan],
               [0.5, .5], [0.5, 1],
               ]]
}

h=.65
CIRCULATOR = {
    'name'  : 'CIRCULATOR',
    'base'  : e.SOURCE,
    'shapes':[{'shape':'arc', 'center':[.5,0],
             'width':h, 'height':h, 'theta1':130, 'theta2':320, 'arrow':'ccw'}],# 'arrow':'cw'}
    }
