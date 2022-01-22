from nml.grfstrings import NewGRFString, default_lang

import grf

# b'test\\UE08FTEST\\0D\\UE098hi: \\UE08Etest'
# b'test\xee\x82\x8fTEST\r\xee\x82\x98hi: \xee\x82\x8etest'

def grf_compile_string(s):
    nstr = NewGRFString(s, default_lang, '')
    value = nstr.parse_string('ascii', default_lang, 1, {}).encode('utf-8')
    res = b''
    print(value)

    i = 0
    while i < len(value):
        if value[i] == 92:  # /
            if value[i + 1] in (92, 34):  # / and "
                res += value[i + 1: i + 2]
                i += 2
            elif value[i + 1] == 85:  # U
                res += chr(int(value[i + 2 : i + 6], 16)).encode("utf8")
                i += 6
            else:
                res += bytes((int(value[i + 1 : i + 3], 16),))
                i += 3
        else:
            res += value[i: i + 1]
            i += 1
    return res


def fake_info_text(props):
    return '{}'.join('{BLACK}' + k + ': {GOLD}' + v for k, v in props.items())


class RoadVehicle(grf.SpriteGenerator):
    def __init__(self, *, id, name, sprites, additional_text=None, **props):
        if len(sprites) != 8:
            raise ValueError(f'RoadVehicle expects 8 sprites, found {len(sprites)}')
        self.id = id
        self.sprites = sprites
        self.name = name
        self.props = props
        self.additional_text = additional_text

    def get_sprites(self):
        res = [
            grf.Action4(
                feature=grf.RV,
                offset=self.id,
                is_generic_offset=False,
                strings=[self.name.encode('utf-8')]
            ),
            grf.Action0(
                feature=grf.RV,
                first_id=self.id,
                count=1,
                props={
                    'sprite_id': 0xff,
                    **self.props
                }
            ),
            grf.Action1(
                feature=grf.RV,
                set_count=1,
                sprite_count=8,
            ),
            *self.sprites,
            grf.GenericSpriteLayout(
                feature=grf.RV,
                ref_id=0,
                ent1=(0,),
                ent2=(0,),
            ),
        ]
        maps = []
        if self.additional_text:
            string_id = 0xd000 + self.id
            res.append(grf.Action4(
                feature=grf.RV,
                offset=string_id,
                is_generic_offset=True,
                strings=[grf_compile_string(self.additional_text)],
            ))
            res.append(grf.VarAction2(
                feature=grf.RV,
                ref_id=2,
                ranges={
                    0: grf.Ref(0),
                    0x23: grf.CB(string_id - 0xd000),
                },
                default=grf.Ref(0),
                code='current_callback',
            ))
            maps = [[255, 2]]

        res.append(grf.Action3(
            feature=grf.RV,
            ids=[self.id],
            maps=maps,
            default=grf.Ref(0),
        ))
        return res
