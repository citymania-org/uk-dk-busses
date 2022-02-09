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
    climates_available=grf.TEMPERATE | grf.ARCTIC | grf.TROPICAL,
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
    climates_available=grf.TEMPERATE | grf.ARCTIC | grf.TROPICAL,
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

g.add(g.strings)
g.write('brilliant_british_busses.grf')
