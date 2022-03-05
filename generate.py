from datetime import date

import grf

import lib

g = grf.NewGRF(
    b'CMBB',
    8,
    'Robs British Busses',
    'Robs British Busses',
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


MAN_11190_OpVecta_1_png = grf.ImageFile('sprites/UK_1991_MAN_11_190_Optare_Vecta_(Arriva)_32bpp.png')
MAN_11190_OpVecta_2_png = grf.ImageFile('sprites/UK_1991_MAN_11_190_Optare_Vecta_(Tees_And_District_Late)_32bpp.png')

RoadVehicle(
    id=4,
    name='MAN 11.190 Optare Vecta',
    liveries = [
        {
            'name': ' (Arriva)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(MAN_11190_OpVecta_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees and District)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(MAN_11190_OpVecta_2_png, *args, **kw, bpp=32)),
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
        'Manufacturer': 'MAN',
    }),
)


DenDrt_PP_1_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(Arriva)_32bpp.png')
DenDrt_PP_2_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(East_Yorkshire)_32bpp.png')
DenDrt_PP_3_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(First)_32bpp.png')
DenDrt_PP_4_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(Go_Ahead_London)_32bpp.png')
DenDrt_PP_5_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(Metroline)_32bpp.png')
DenDrt_PP_6_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(Stagecoach)_32bpp.png')

RoadVehicle(
    id=5,
    name='Dennis Dart Plaxton Pointer',
    liveries = [
        {
            'name': ' (Arriva)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(DenDrt_PP_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (East Yorkshire)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(DenDrt_PP_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (First)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(DenDrt_PP_3_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Go Ahead London)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(DenDrt_PP_4_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Metroline)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(DenDrt_PP_5_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Stagecoach)',
            'sprites': tmpl_rv(0, 0, lambda *args, **kw: grf.FileSprite(DenDrt_PP_6_png, *args, **kw, bpp=32)),
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

MB_VA_ALX100_1_png = grf.ImageFile('sprites/UK_1997_Mercedes-Benz_Vario_Alexander_ALX100_(Arriva)_32bpp.png')
MB_VA_ALX100_2_png = grf.ImageFile('sprites/UK_1997_Mercedes-Benz_Vario_Alexander_ALX100_(First)_32bpp.png')

RoadVehicle(
    id=6,
    name='Mercedes-Benz Vario Alexander ALX100',
    liveries = [
        {
            'name': ' (Arriva)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(MB_VA_ALX100_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (First)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(MB_VA_ALX100_2_png, *args, **kw, bpp=32)),
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
        'Manufacturer': 'Mercedes-Benz',
        'Operators': 'Arriva, First',
    }),
)

g.add(g.strings)
g.write('brilliant_british_busses.grf')
