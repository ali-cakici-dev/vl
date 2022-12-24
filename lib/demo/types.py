import intellireader.commands_pb2 as commands_pb2

import intellireader.contactless.token_type_pb2 as token_type_pb2
import intellireader.mifare.generic.get_version_pb2 as get_version_pb2

import lib.proto

MIFARE_DESFIRE = 100
MIFARE_DESFIRE_LITE = 101
MIFARE_NTAG = 102
MIFARE_PLUS_EV1 = 103
MIFARE_PLUS_S_4K_SL1 = 104
MIFARE_PLUS_X_4K_SL1 = 105
MIFARE_PLUS_S_2K_SL1 = 106
MIFARE_PLUS_X_2K_SL1 = 107
MIFARE_PLUS_SE_1K = 108
MIFARE_PLUS_S_2_4K_SL3 = 109
MIFARE_PLUS_X_2_4K_SL3 = 110
MIFARE_ULTRALIGHT_EV1 = 111

MIFARE_HW_TYPES = {
    0x01: MIFARE_DESFIRE,
    0x81: MIFARE_DESFIRE,
    0x02: MIFARE_PLUS_EV1,
    0x82: MIFARE_PLUS_EV1,
    0x03: MIFARE_ULTRALIGHT_EV1,
    0x04: MIFARE_NTAG,
    0x08: MIFARE_DESFIRE_LITE,
}

MIFARE_PLUS_TYPES = {
    ('18', 'c1052f2f0035c7', MIFARE_PLUS_S_4K_SL1),
    ('18', 'c1052f2f01bcd6', MIFARE_PLUS_X_4K_SL1),

    ('08', 'c1052f2f0035c7', MIFARE_PLUS_S_2K_SL1),
    ('08', 'c1052f2f01bcd6', MIFARE_PLUS_X_2K_SL1),
    ('08', 'c105213000f6d1', MIFARE_PLUS_SE_1K),
    ('08', 'c105213010f6d1', MIFARE_PLUS_SE_1K),

    ('20', 'c1052f2f0035c7', MIFARE_PLUS_S_2_4K_SL3),
    ('20', 'c1052f2f01bcd6', MIFARE_PLUS_X_2_4K_SL3),
    ('20', 'c105213000f6d1', MIFARE_PLUS_SE_1K),
    ('20', 'c105213010f6d1', MIFARE_PLUS_SE_1K),
}

TOKEN_TYPES = {
    token_type_pb2.ISO_14443_4A: 'ISO 14443\nLayer 4A',
    token_type_pb2.ISO_14443_4B: 'ISO 14443\nLayer 4B',
    token_type_pb2.MIFARE_CLASSIC_1K: 'Mifare\nClassic 1K',
    token_type_pb2.MIFARE_CLASSIC_2K: 'Mifare\nClassic 2K',
    token_type_pb2.MIFARE_CLASSIC_4K: 'Mifare\nClassic 4K',
    token_type_pb2.MIFARE_CLASSIC_MINI: 'Mifare\nMini',
    token_type_pb2.MIFARE_PLUS_X_SL2_2K: 'Mifare Plus X\n2K in SL2',
    token_type_pb2.MIFARE_PLUS_X_SL2_4K: 'Mifare Plus X\n4K in SL2',
    token_type_pb2.MIFARE_UL_OR_ULC: 'Mifare\nUltralight',
    token_type_pb2.SMART_MX_WITH_MIFARE_1K: 'Smart MX\nClassic 1K',
    token_type_pb2.SMART_MX_WITH_MIFARE_4K: 'Smart MX\nClassic 4K',
    token_type_pb2.TAG_N_PLAY: 'Tag & Play',
    token_type_pb2.STM_SRI512: 'STM\nSRI512 tag',
    token_type_pb2.GENERIC_ISO15693: 'Generic\nISO15693',
    token_type_pb2.ICODE_SLI: 'ICODE\nSLI',
    token_type_pb2.ICODE_SLIX: 'ICODE\nSLIX',
    token_type_pb2.ICODE_SLIX2: 'ICODE\nSLIX2',
    token_type_pb2.ASK_CTS512B: 'ASK C.ticket\nCTS512B',
    MIFARE_DESFIRE: 'Mifare\nDESFire',
    MIFARE_DESFIRE_LITE: 'Mifare\nDESFire Lite',
    MIFARE_NTAG: 'Mifare\nNTag',
    MIFARE_PLUS_EV1: 'Mifare\nPlus EV1',
    MIFARE_PLUS_S_4K_SL1: 'Mifare Plus S\n4K in SL1',
    MIFARE_PLUS_X_4K_SL1: 'Mifare Plus X\n4K in SL1',
    MIFARE_PLUS_S_2K_SL1: 'Mifare Plus S\n2K in SL1',
    MIFARE_PLUS_X_2K_SL1: 'Mifare Plus X\n2K in SL1',
    MIFARE_PLUS_SE_1K: 'Mifare Plus\nSE 1K',
    MIFARE_PLUS_S_2_4K_SL3: 'Mifare Plus S\n2/4K in SL3',
    MIFARE_PLUS_X_2_4K_SL3: 'Mifare Plus X\n2/4K in SL3',
    MIFARE_ULTRALIGHT_EV1: 'Mifare\nUltralight\nEV1',
}

def token_type_text(proto, result):
    card_type = token_type(proto, result)
    return TOKEN_TYPES.get(card_type, 'Unknown\ncard')

def token_type(proto, result):
    version = get_version(proto)

    if len(result.token.answer_to_select) != 0:
        if len(version) > 1:
            hw_type = version[1]
            return MIFARE_HW_TYPES.get(hw_type, result.token.type)
    else:
        if len(version) > 2:
            hw_type = version[2]
            return MIFARE_HW_TYPES.get(hw_type, result.token.type)
        else:
            return result.token.type

    # Mifare Plus subtype
    token_hbytes = historical_bytes(result)
    token_hbytes = token_hbytes.hex()

    token_sak = result.token.sak.hex()

    for (sak, hbytes, subtype) in MIFARE_PLUS_TYPES:
        if sak == token_sak and token_hbytes == hbytes:
            return subtype

    return result.token.type

def get_version(proto):
    request = commands_pb2.MifareExtended()
    cmd = request.mfr_get_version
    cmd.SetInParent()

    response = get_version_pb2.ProductVersionInfo()

    proto.exchange(request, response)
    return response.info

def historical_bytes(result):
    tl = result.token.answer_to_select[0]
    t0 = result.token.answer_to_select[1]

    skip = 2
    if t0 & 0b01000000 != 0:
        skip += 1
    if t0 & 0b00100000 != 0:
        skip += 1
    if t0 & 0b00010000 != 0:
        skip += 1

    return result.token.answer_to_select[skip:]

