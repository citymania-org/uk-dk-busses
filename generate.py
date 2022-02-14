from datetime import date

import grf

import lib

g = grf.NewGRF(
    b'CMBB',
    8,
    'Brilliant British Busses',
    'Brilliant British Busses',
)
g.strings = lib.StringManager()
RoadVehicle = g.bind(lib.RoadVehicle)

def tmpl_rv(x, y, func):
    return [
        func(      x, y, 10, 28, xofs= -4, yofs=-15),
        func( x + 20, y, 26, 28, xofs=-18, yofs=-14),
        func( x + 50, y, 36, 28, xofs=-18, yofs=-17),
        func( x + 90, y, 26, 28, xofs=-10, yofs=-15),
        func(x + 120, y, 10, 28, xofs= -4, yofs=-15),
        func(x + 140, y, 26, 28, xofs=-16, yofs=-16),
        func(x + 170, y, 36, 28, xofs=-18, yofs=-20),
        func(x + 210, y, 26, 28, xofs= -6, yofs=-15),
    ]


optare_vectra_arriva_png = grf.ImageFile('sprites/UK 1991 Optare Vecta (Arriva).png', colourkey=(0, 0, 255))
optare_vectra_tnd_png = grf.ImageFile('sprites/UK 1991 Optare Vecta (Tees And District).png', colourkey=(0, 0, 255))

RoadVehicle(
    id=4,
    name='Optare Vecta',
    liveries = [
        {
            'name': ' (Arriva)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(optare_vectra_arriva_png, *args, **kw, bpp=24)),
        },
        {
            'name': ' (Tees and District)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(optare_vectra_tnd_png, *args, **kw, bpp=24)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1991, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    additional_text=lib.fake_info_text({
        'Manufacturer': 'Optare',
    }),
)


plaxton_pointer_arriva_png = grf.ImageFile('sprites/UK 1996 Dennis Dart Plaxton Pointer 2 (Arriva).png', colourkey=(0, 0, 255))

RoadVehicle(
    id=5,
    name='Dennis Dart Plaxton Pointer 2',
    liveries = [
        {
            'name': ' (Arriva)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(plaxton_pointer_arriva_png, *args, **kw, bpp=24)),
        },
        {
            'name': ' (Test)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(plaxton_pointer_arriva_png, *args, **kw, bpp=24)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1996, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    additional_text=lib.fake_info_text({
        'Manufacturer': 'Dennis Specialist Vehicles',
        'Operator': 'Arriva',
    }),
)

def tmpl_rv_vox(x, y, func):
    return [
        func(      x, y, 10, 22, xofs= -4, yofs=-10),
        func( x + 18, y, 26, 20, xofs=-18, yofs=-9),
        func( x + 52, y, 27, 13, xofs=-18, yofs=-6),
        func( x + 87, y, 26, 20, xofs=-10, yofs=-10),
        func(x + 121, y, 10, 22, xofs= -4, yofs=-10),
        func(x + 139, y, 26, 20, xofs=-16, yofs=-11),
        func(x + 173, y, 27, 13, xofs=-18, yofs=-6),
        func(x + 208, y, 26, 20, xofs= -6, yofs=-10),
    ]

alx1000_arriva_png = grf.ImageFile('sprites/UK_1997_Mercedes_Benz_Vario_Alexander_ALX100_(Arriva).png')

RoadVehicle(
    id=6,
    name='Alexander ALX1000',
    liveries = [
        {
            'name': ' (Arriva)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(alx1000_arriva_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Arriva)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(alx1000_arriva_png, *args, **kw, bpp=32)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1997, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    additional_text=lib.fake_info_text({
        'Manufacturer': 'Alexander',
        'Operator': 'Arriva',
    }),
)

g.add(g.strings)
g.write('brilliant_british_busses.grf')
