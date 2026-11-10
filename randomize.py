#!/usr/bin/env python3
from random import randint
from pathlib import Path

fcss = Path('.vscode/style.org.css')
fcss_final = Path('.vscode/style.css')
fmain = Path('main.org.md')
fmain_final = Path('main.md')


def random():
    return randint(-100, 100) / 100


def random_bias(base, bias):
    return randint(
            round(base * (1 - bias)),
            round(base * (1 + bias))
    )


def random_dim():
    return random_bias(128, 0.1)


def random_light():
    return random_bias(232, 0.1)
           


def make_g():
    css = []
    for _ in range(25):
        offset_x_2 = random()
        offset_y_2 = random()
        offset_2 = f'{offset_x_2}rem {offset_y_2}rem 2rem'
        
        offset_x_3 = random() + 1
        offset_y_3 = random() + 1
        offset_3 = f'{offset_x_3}rem {offset_y_3}rem 5rem'
        
        color_2 = f'rgb({random_dim()}, 0, 0)'
        color_3 = f'rgb({random_light()}, 0, 0)'
        
        _css = f'''.g{_} {{
    color: #f00;
    font-weight:1000;
    text-shadow:
    '''
        for __ in range(15):
            _css += '''0 0 0.2rem #000,
        '''
        
        for __ in range(10):
            _css += f'''{offset_2} {color_2},
        '''
        
        for __ in range(14):
            _css += f'''{offset_3} {color_3},
        '''
        
        _css += f'''{offset_3} {color_3};
}}'''

        css.append(_css)
    
    css = '\n\n'.join(css)
    return css


def make_bx():
    css = []
    for _ in range(25):
        offset_x = random()
        offset_y = random()
        offset_2 = f'{offset_x}rem {offset_y}rem 5rem'
        
        color_2 = f'rgb({random_bias(232, 0.1)}, {random_bias(82, 0.1)}, 0)'
        
        _css = f'''.xb{_} {{
    color: #000;
    font-weight:800;
    text-shadow:
        '''
        for __ in range(8):
            _css += '''0 0 1rem #f00,
        '''
        
        for __ in range(7):
            _css += f'''{offset_2} {color_2},
        '''
        
        _css += f'''{offset_2} {color_2};
}}'''

        css.append(_css)
    
    css = '\n\n'.join(css)
    return css


css = fcss.read_text(encoding='utf8')

css += make_g()
css += make_bx()

fcss_final.write_text(css, encoding='utf8')

raw_main = fmain.read_text(encoding='utf8')
raw_main = raw_main.split('class="g"')
main = [raw_main.pop(0)]

for _ in raw_main:
    main.append(f'class=g{randint(0, 25)}')
    main.append(_)
    
main = ''.join(main)
fmain_final.write_text(main, encoding='utf8')