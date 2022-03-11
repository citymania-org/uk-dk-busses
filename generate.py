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

def tmpl_rv_vox(x, y, func):
    return [
        func(      x, y, 10, 29, xofs=-3, yofs=-16),
        func( x + 18, y, 26, 27, xofs=-15, yofs=-16),
        func( x + 52, y, 27, 21, xofs=-10, yofs=-16),
        func( x + 87, y, 26, 27, xofs=-10, yofs=-16),
        func(x + 121, y, 10, 29, xofs=-3, yofs=-16),
        func(x + 139, y, 26, 27, xofs=-15, yofs=-16),
        func(x + 173, y, 27, 21, xofs=-10, yofs=-16),
        func(x + 208, y, 26, 27, xofs=-10, yofs=-16),
    ]



a1_1_png = grf.ImageFile('sprites/UK_1972_Leyland_National_(white)_32bpp.png')
a1_2_png = grf.ImageFile('sprites/UK_1972_Leyland_National_(red)_32bpp.png')
a1_3_png = grf.ImageFile('sprites/UK_1972_Leyland_National_(dark_green)_32bpp.png')
a1_4_png = grf.ImageFile('sprites/UK_1972_Leyland_National_(Bournemouth_Transport)_32bpp.png')
a1_5_png = grf.ImageFile('sprites/UK_1972_Leyland_National_(Stagecoach)_32bpp.png')
a1_6_png = grf.ImageFile('sprites/UK_1972_Leyland_National_(Tees_And_District)_32bpp.png')
a1_7_png = grf.ImageFile('sprites/UK_1972_Leyland_National_(Tees_And_District_Late)_32bpp.png')

RoadVehicle(
    id=1,
    name='Leyland National',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a1_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a1_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a1_3_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Bournemouth Transport)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a1_4_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Stagecoach)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a1_5_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a1_6_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District Late)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a1_7_png, *args, **kw, bpp=32)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1972, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'Leyland',
    }),
)


a2_1_png = grf.ImageFile('sprites/UK_1979_Leyland_National_2_(white)_32bpp.png')
a2_2_png = grf.ImageFile('sprites/UK_1979_Leyland_National_2_(red)_32bpp.png')
a2_3_png = grf.ImageFile('sprites/UK_1979_Leyland_National_2_(dark_green)_32bpp.png')
a2_4_png = grf.ImageFile('sprites/UK_1979_Leyland_National_2_(Stagecoach)_32bpp.png')
a2_5_png = grf.ImageFile('sprites/UK_1979_Leyland_National_2_(Tees_And_District)_32bpp.png')
a2_6_png = grf.ImageFile('sprites/UK_1979_Leyland_National_2_(Tees_And_District_Late)_32bpp.png')

RoadVehicle(
    id=2,
    name='Leyland National 2',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a2_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a2_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a2_3_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Stagecoach)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a2_4_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a2_5_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District Late)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a2_6_png, *args, **kw, bpp=32)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1979, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'Leyland',
    }),
)


a3_1_png = grf.ImageFile('sprites/UK_1968_Bristol_VR_(white)_32bpp.png')
a3_2_png = grf.ImageFile('sprites/UK_1968_Bristol_VR_(red)_32bpp.png')
a3_3_png = grf.ImageFile('sprites/UK_1968_Bristol_VR_(dark_green)_32bpp.png')
a3_4_png = grf.ImageFile('sprites/UK_1968_Bristol_VR_(Tees_And_District)_32bpp.png')
a3_5_png = grf.ImageFile('sprites/UK_1968_Bristol_VR_(Tees_And_District_Late)_32bpp.png')

RoadVehicle(
    id=3,
    name='Bristol VR',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a3_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a3_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a3_3_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a3_4_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District Late)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a3_5_png, *args, **kw, bpp=32)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1968, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'Bristol',
    }),
)


a4_1_png = grf.ImageFile('sprites/UK_1991_MAN_11_190_Optare_Vecta_(white)_32bpp.png')
a4_2_png = grf.ImageFile('sprites/UK_1991_MAN_11_190_Optare_Vecta_(red)_32bpp.png')
a4_3_png = grf.ImageFile('sprites/UK_1991_MAN_11_190_Optare_Vecta_(dark_green)_32bpp.png')
a4_4_png = grf.ImageFile('sprites/UK_1991_MAN_11_190_Optare_Vecta_(Arriva)_32bpp.png')
a4_5_png = grf.ImageFile('sprites/UK_1991_MAN_11_190_Optare_Vecta_(Tees_And_District_Late)_32bpp.png')

RoadVehicle(
    id=4,
    name='MAN 11.190 Optare Vecta',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a4_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a4_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a4_3_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Arriva)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a4_4_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a4_5_png, *args, **kw, bpp=32)),
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
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'MAN',
    }),
)


a5_1_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(white)_32bpp.png')
a5_2_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(red)_32bpp.png')
a5_3_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(dark_green)_32bpp.png')
a5_4_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(Arriva)_32bpp.png')
a5_5_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(East_Yorkshire)_32bpp.png')
a5_6_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(First)_32bpp.png')
a5_7_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(Go_Ahead_London)_32bpp.png')
a5_8_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(Metroline)_32bpp.png')
a5_9_png = grf.ImageFile('sprites/UK_1991_Dennis_Dart_Plaxton_Pointer_(Stagecoach)_32bpp.png')

RoadVehicle(
    id=5,
    name='Dennis Dart Plaxton Pointer',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a5_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a5_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a5_3_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Arriva)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a5_4_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (East Yorkshire)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a5_5_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (First)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a5_6_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Go Ahead London)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a5_7_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Metroline)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a5_8_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Stagecoach)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a5_9_png, *args, **kw, bpp=32)),
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
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'Dennis Specialist Vehicles',
    }),
)


a6_1_png = grf.ImageFile('sprites/UK_1997_Mercedes-Benz_Vario_Alexander_ALX100_(white)_32bpp.png')
a6_2_png = grf.ImageFile('sprites/UK_1997_Mercedes-Benz_Vario_Alexander_ALX100_(red)_32bpp.png')
a6_3_png = grf.ImageFile('sprites/UK_1997_Mercedes-Benz_Vario_Alexander_ALX100_(dark_green)_32bpp.png')
a6_4_png = grf.ImageFile('sprites/UK_1997_Mercedes-Benz_Vario_Alexander_ALX100_(Arriva)_32bpp.png')
a6_5_png = grf.ImageFile('sprites/UK_1997_Mercedes-Benz_Vario_Alexander_ALX100_(First)_32bpp.png')

RoadVehicle(
    id=6,
    name='Mercedes-Benz Vario Alexander ALX100',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a6_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a6_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a6_3_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Arriva)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a6_4_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (First)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a6_5_png, *args, **kw, bpp=32)),
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
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'Mercedes-Benz',
    }),
)


a7_1_png = grf.ImageFile('sprites/UK_1967_Bristol_LH_(white)_32bpp.png')
a7_2_png = grf.ImageFile('sprites/UK_1967_Bristol_LH_(red)_32bpp.png')
a7_3_png = grf.ImageFile('sprites/UK_1967_Bristol_LH_(dark_green)_32bpp.png')
a7_4_png = grf.ImageFile('sprites/UK_1967_Bristol_LH_(Tees_And_District)_32bpp.png')
a7_5_png = grf.ImageFile('sprites/UK_1967_Bristol_LH_(Tees_And_District_Late)_32bpp.png')

RoadVehicle(
    id=7,
    name='Bristol LH',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a7_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a7_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a7_3_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a7_4_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District Late)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a7_5_png, *args, **kw, bpp=32)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1967, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'Bristol',
    }),
)


a8_1_png = grf.ImageFile('sprites/UK_1980_Leyland_Olympian_ECW_(white)_32bpp.png')
a8_2_png = grf.ImageFile('sprites/UK_1980_Leyland_Olympian_ECW_(red)_32bpp.png')
a8_3_png = grf.ImageFile('sprites/UK_1980_Leyland_Olympian_ECW_(dark_green)_32bpp.png')
a8_4_png = grf.ImageFile('sprites/UK_1980_Leyland_Olympian_ECW_(First)_32bpp.png')
a8_5_png = grf.ImageFile('sprites/UK_1980_Leyland_Olympian_ECW_(Tees_And_District)_32bpp.png')
a8_6_png = grf.ImageFile('sprites/UK_1980_Leyland_Olympian_ECW_(Tees_And_District_Late)_32bpp.png')
a8_7_png = grf.ImageFile('sprites/UK_1980_Leyland_Olympian_ECW_(Tees_And_District_Tyne_Link)_32bpp.png')

RoadVehicle(
    id=8,
    name='Leyland Olympian ECW',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a8_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a8_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a8_3_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (First)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a8_4_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a8_5_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District Late)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a8_6_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Tees And District Tyne Link)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a8_7_png, *args, **kw, bpp=32)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1980, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'Leyland',
    }),
)


a9_1_png = grf.ImageFile('sprites/UK_1999_Volvo_B7L_Wright_Eclipse_(white)_32bpp.png')
a9_2_png = grf.ImageFile('sprites/UK_1999_Volvo_B7L_Wright_Eclipse_(red)_32bpp.png')
a9_3_png = grf.ImageFile('sprites/UK_1999_Volvo_B7L_Wright_Eclipse_(dark_green)_32bpp.png')

RoadVehicle(
    id=9,
    name='Volvo B7L Wright Eclipse',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a9_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a9_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a9_3_png, *args, **kw, bpp=32)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1999, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'Volvo',
    }),
)


a10_1_png = grf.ImageFile('sprites/UK_2008_Volvo_B7RLE_Wright_Eclipse_2_(white)_32bpp.png')
a10_2_png = grf.ImageFile('sprites/UK_2008_Volvo_B7RLE_Wright_Eclipse_2_(red)_32bpp.png')
a10_3_png = grf.ImageFile('sprites/UK_2008_Volvo_B7RLE_Wright_Eclipse_2_(dark_green)_32bpp.png')

RoadVehicle(
    id=10,
    name='Volvo B7RLE Wright Eclipse 2',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a10_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a10_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a10_3_png, *args, **kw, bpp=32)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(2008, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'Volvo',
    }),
)


a11_1_png = grf.ImageFile('sprites/UK_2015_Volvo_B8RLE_Wright_Eclipse_3_(white)_32bpp.png')
a11_2_png = grf.ImageFile('sprites/UK_2015_Volvo_B8RLE_Wright_Eclipse_3_(red)_32bpp.png')
a11_3_png = grf.ImageFile('sprites/UK_2015_Volvo_B8RLE_Wright_Eclipse_3_(dark_green)_32bpp.png')

RoadVehicle(
    id=11,
    name='Volvo B8RLE Wright Eclipse 3',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a11_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a11_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a11_3_png, *args, **kw, bpp=32)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(2015, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'Volvo',
    }),
)


a12_1_png = grf.ImageFile('sprites/UK_2001_Volvo_B7TL_Wright_Eclipse_Gemini_(white)_32bpp.png')
a12_2_png = grf.ImageFile('sprites/UK_2001_Volvo_B7TL_Wright_Eclipse_Gemini_(red)_32bpp.png')
a12_3_png = grf.ImageFile('sprites/UK_2001_Volvo_B7TL_Wright_Eclipse_Gemini_(dark_green)_32bpp.png')

RoadVehicle(
    id=12,
    name='Volvo B7TL Wright Eclipse Gemini',
    liveries = [
        {
            'name': ' (White)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a12_1_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Red)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a12_2_png, *args, **kw, bpp=32)),
        },
        {
            'name': ' (Dark Green)',
            'sprites': tmpl_rv_vox(0, 0, lambda *args, **kw: grf.FileSprite(a12_3_png, *args, **kw, bpp=32)),
        },
    ],
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(2001, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    additional_text=lib.fake_info_text({
        'Info': 'Volvo',
    }),
)

g.add(g.strings)
g.write('robs_british_busses.grf')
