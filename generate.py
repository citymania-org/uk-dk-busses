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


def tmpl_rv_vox(filename):
    png = grf.ImageFile('sprites/' + filename)
    func = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32 if filename.endswith('_32bpp.png') else 8)
    return [
        func(  0, 0, 10, 29, xofs=-3, yofs=-16),
        func( 18, 0, 26, 27, xofs=-15, yofs=-16),
        func( 52, 0, 27, 21, xofs=-10, yofs=-16),
        func( 87, 0, 26, 27, xofs=-10, yofs=-16),
        func(121, 0, 10, 29, xofs=-3, yofs=-16),
        func(139, 0, 26, 27, xofs=-15, yofs=-16),
        func(173, 0, 27, 21, xofs=-10, yofs=-16),
        func(208, 0, 26, 27, xofs=-10, yofs=-16),
    ]


def make_vox_liveries(liveries):
    return [{
        'name': ' ' + name,
        'sprites': tmpl_rv_vox(filename),
    } for name, filename in liveries.items()]


RoadVehicle(
    id=501,
    name='Leyland National',
    liveries = make_vox_liveries({
        '(White)': 'UK_1972_Leyland_National_(white)_32bpp.png',
        '(Bournemouth Transport)': 'UK_1972_Leyland_National_(Bournemouth_Transport)_32bpp.png',
        '(Greater Manchester Transport)': 'UK_1972_Leyland_National_(Greater_Manchester_Transport)_32bpp.png',
        '(Stagecoach)': 'UK_1972_Leyland_National_(Stagecoach)_32bpp.png',
        '(Tees And District)': 'UK_1972_Leyland_National_(Tees_And_District)_32bpp.png',
        '(Tees And District Late)': 'UK_1972_Leyland_National_(Tees_And_District_Late)_32bpp.png',
        '(Teesside Motor Services)': 'UK_1972_Leyland_National_(Teesside_Motor_Services)_32bpp.png',
        '(Teesside Motor Services Late)': 'UK_1972_Leyland_National_(Teesside_Motor_Services_Late)_32bpp.png',
        '(United)': 'UK_1972_Leyland_National_(United)_32bpp.png',
    }),
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
    sort_purchase_list=0,
    additional_text=lib.fake_info_text({
        'Info': 'Leyland',
    }),
)

RoadVehicle(
    id=502,
    name='Leyland National 2',
    liveries = make_vox_liveries({
        '(White)': 'UK_1979_Leyland_National_2_(white)_32bpp.png',
        '(Stagecoach)': 'UK_1979_Leyland_National_2_(Stagecoach)_32bpp.png',
        '(Tees And District)': 'UK_1979_Leyland_National_2_(Tees_And_District)_32bpp.png',
        '(Tees And District Late)': 'UK_1979_Leyland_National_2_(Tees_And_District_Late)_32bpp.png',
        '(United)': 'UK_1979_Leyland_National_2_(United)_32bpp.png',
    }),
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
    sort_purchase_list=0,
    additional_text=lib.fake_info_text({
        'Info': 'Leyland',
    }),
)

RoadVehicle(
    id=1001,
    name='Bristol VR',
    liveries = make_vox_liveries({
        '(White)': 'UK_1968_Bristol_VR_(white)_32bpp.png',
        '(Tees And District)': 'UK_1968_Bristol_VR_(Tees_And_District)_32bpp.png',
        '(Tees And District Late)': 'UK_1968_Bristol_VR_(Tees_And_District_Late)_32bpp.png',
        '(United)': 'UK_1968_Bristol_VR_(United)_32bpp.png',
    }),
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
    sort_purchase_list=0,
    additional_text=lib.fake_info_text({
        'Info': 'Bristol',
    }),
)

RoadVehicle(
    id=503,
    name='MAN 11.190 Optare Vecta',
    liveries = make_vox_liveries({
        '(White)': 'UK_1991_MAN_11_190_Optare_Vecta_(white)_32bpp.png',
        '(Arriva)': 'UK_1991_MAN_11_190_Optare_Vecta_(Arriva)_32bpp.png',
        '(Tees And District)': 'UK_1991_MAN_11_190_Optare_Vecta_(Tees_And_District_Late)_32bpp.png',
    }),
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
    sort_purchase_list=0,
    additional_text=lib.fake_info_text({
        'Info': 'MAN',
    }),
)

RoadVehicle(
    id=504,
    name='Dennis Dart Plaxton Pointer',
    liveries = make_vox_liveries({
        '(CC)': 'zdartcc_8bpp.png',
        '(White)': 'UK_1991_Dennis_Dart_Plaxton_Pointer_(white)_32bpp.png',
        '(Arriva)': 'UK_1991_Dennis_Dart_Plaxton_Pointer_(Arriva)_32bpp.png',
        '(East Yorkshire)': 'UK_1991_Dennis_Dart_Plaxton_Pointer_(East_Yorkshire)_32bpp.png',
        '(First)': 'UK_1991_Dennis_Dart_Plaxton_Pointer_(First)_32bpp.png',
        '(Go Ahead London)': 'UK_1991_Dennis_Dart_Plaxton_Pointer_(Go_Ahead_London)_32bpp.png',
        '(Metroline)': 'UK_1991_Dennis_Dart_Plaxton_Pointer_(Metroline)_32bpp.png',
        '(Stagecoach)': 'UK_1991_Dennis_Dart_Plaxton_Pointer_(Stagecoach)_32bpp.png',
        '(Stagecoach Late)': 'UK_1991_Dennis_Dart_Plaxton_Pointer_(Stagecoach_Late)_32bpp.png',
    }),
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
    sort_purchase_list=503,
    additional_text=lib.fake_info_text({
        'Info': 'Dennis Specialist Vehicles',
    }),
)

RoadVehicle(
    id=505,
    name='Mercedes-Benz Vario Alexander ALX100',
    liveries = make_vox_liveries({
        '(White)': 'UK_1997_Mercedes-Benz_Vario_Alexander_ALX100_(white)_32bpp.png',
        '(Arriva)': 'UK_1997_Mercedes-Benz_Vario_Alexander_ALX100_(Arriva)_32bpp.png',
        '(First)': 'UK_1997_Mercedes-Benz_Vario_Alexander_ALX100_(First)_32bpp.png',
    }),
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
    sound_effect=0x17,
    sort_purchase_list=0,
    additional_text=lib.fake_info_text({
        'Info': 'Mercedes-Benz',
    }),
)

RoadVehicle(
    id=506,
    name='Bristol LH',
    liveries = make_vox_liveries({
        '(White)': 'UK_1967_Bristol_LH_(white)_32bpp.png',
        '(Tees And District)': 'UK_1967_Bristol_LH_(Tees_And_District)_32bpp.png',
        '(Tees And District Late)': 'UK_1967_Bristol_LH_(Tees_And_District_Late)_32bpp.png',
        '(Teesside Motor Services)': 'UK_1967_Bristol_LH_(Teesside_Motor_Services)_32bpp.png',
        '(United)': 'UK_1967_Bristol_LH_(United)_32bpp.png',
    }),
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
    sort_purchase_list=501,
    additional_text=lib.fake_info_text({
        'Info': 'Bristol',
    }),
)

RoadVehicle(
    id=1002,
    name='Leyland Olympian ECW',
    liveries = make_vox_liveries({
        '(White)': 'UK_1980_Leyland_Olympian_ECW_(white)_32bpp.png',
        '(First)': 'UK_1980_Leyland_Olympian_ECW_(First)_32bpp.png',
        '(Tees And District)': 'UK_1980_Leyland_Olympian_ECW_(Tees_And_District)_32bpp.png',
        '(Tees And District Late)': 'UK_1980_Leyland_Olympian_ECW_(Tees_And_District_Late)_32bpp.png',
        '(Tees And District Tyne Link)': 'UK_1980_Leyland_Olympian_ECW_(Tees_And_District_Tyne_Link)_32bpp.png',
        '(United)': 'UK_1980_Leyland_Olympian_ECW_(United)_32bpp.png',
        '(United Late)': 'UK_1980_Leyland_Olympian_ECW_(United_Late)_32bpp.png',
    }),
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
    sort_purchase_list=0,
    additional_text=lib.fake_info_text({
        'Info': 'Leyland',
    }),
)

RoadVehicle(
    id=507,
    name='Volvo B7L Wright Eclipse',
    liveries = make_vox_liveries({
        '(White)': 'UK_1999_Volvo_B7L_Wright_Eclipse_(white)_32bpp.png',
        '(Arriva)': 'UK_1999_Volvo_B7L_Wright_Eclipse_(Arriva)_32bpp.png',
        '(Arriva Late)': 'UK_1999_Volvo_B7L_Wright_Eclipse_(Arriva_Late)_32bpp.png',
    }),
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
    sort_purchase_list=0,
    additional_text=lib.fake_info_text({
        'Info': 'Volvo',
    }),
)

RoadVehicle(
    id=508,
    name='Volvo B7RLE Wright Eclipse 2',
    liveries = make_vox_liveries({
        '(White)': 'UK_2008_Volvo_B7RLE_Wright_Eclipse_2_(white)_32bpp.png',
        '(Arriva Late)': 'UK_2008_Volvo_B7RLE_Wright_Eclipse_2_(Arriva_Late)_32bpp.png',
    }),
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
    sort_purchase_list=0,
    additional_text=lib.fake_info_text({
        'Info': 'Volvo',
    }),
)

RoadVehicle(
    id=509,
    name='Volvo B8RLE Wright Eclipse 3',
    liveries = make_vox_liveries({
        '(White)': 'UK_2015_Volvo_B8RLE_Wright_Eclipse_3_(white)_32bpp.png',
        '(East Coast Buses)': 'UK_2015_Volvo_B8RLE_Wright_Eclipse_3_(East_Coast_Buses)_32bpp.png',
    }),
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
    sort_purchase_list=0,
    additional_text=lib.fake_info_text({
        'Info': 'Volvo',
    }),
)

RoadVehicle(
    id=1003,
    name='Volvo B7TL Wright Eclipse Gemini',
    liveries = make_vox_liveries({
        '(White)': 'UK_2001_Volvo_B7TL_Wright_Eclipse_Gemini_(white)_32bpp.png',
    }),
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
    sort_purchase_list=0,
    additional_text=lib.fake_info_text({
        'Info': 'Volvo',
    }),
)

RoadVehicle(
    id=510,
    name='Bristol RE',
    liveries = make_vox_liveries({
        '(White)': 'UK_1962_Bristol_RE_(white)_32bpp.png',
        '(Delta)': 'UK_1962_Bristol_RE_(Delta)_32bpp.png',
        '(Potteries Motor Traction)': 'UK_1962_Bristol_RE_(Potteries_Motor_Traction)_32bpp.png',
    }),
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1962, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    sort_purchase_list=506,
    additional_text=lib.fake_info_text({
        'Info': 'Bristol',
    }),
)

RoadVehicle(
    id=511,
    name='Leyland Lynx',
    liveries = make_vox_liveries({
        '(CC)': 'zlynxcc_8bpp.png',
        '(White)': 'UK_1986_Leyland_Lynx_(white)_32bpp.png',
        '(Cleveland Transit)': 'UK_1986_Leyland_Lynx_(Cleveland_Transit)_32bpp.png',
    }),
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1986, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    sort_purchase_list=504,
    additional_text=lib.fake_info_text({
        'Info': 'Leyland',
    }),
)

RoadVehicle(
    id=512,
    name='Leyland Lynx 2',
    liveries = make_vox_liveries({
        '(White)': 'UK_1990_Leyland_Lynx_2_(white)_32bpp.png',
        '(Cleveland Transit)': 'UK_1990_Leyland_Lynx_2_(Cleveland_Transit)_32bpp.png',
        '(Tees And District Late)': 'UK_1990_Leyland_Lynx_2_(Tees_And_District_Late)_32bpp.png',
    }),
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1990, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    sound_effect=0x17,
    sort_purchase_list=504,
    additional_text=lib.fake_info_text({
        'Info': 'Leyland',
    }),
)

g.add(g.strings)
g.write('robs_british_busses.grf')
