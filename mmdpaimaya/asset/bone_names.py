# -*- coding: utf-8 -*-
'''
Mapping from MMD Japanese bone names to English names (League of Legends style).
Used by pmxpaimaya.py when creating joints in Maya.

Strategy (applied in order):
  1. Exact lookup in BONE_NAME_JP_EN  (Japanese → English)
  2. Strip trailing digits, try base lookup
  3. Component decomposition using Japanese morpheme table
  4. Fallback: romaji conversion (original behaviour)

Naming convention follows League of Legends skeleton style:
  - Left  bones: L_BoneName
  - Right bones: R_BoneName
  - Centered:    BoneName  (no prefix)
'''

import re

# ---------------------------------------------------------------------------
# 1.  STANDARD BONE TABLE  (exact match, Japanese key → English value)
# ---------------------------------------------------------------------------
# fmt: off
BONE_NAME_JP_EN = {
    # ── Core / Root ──────────────────────────────────────────────
    'センター':          'Root',
    '全ての親':          'Root',
    'グルーブ':          'Groove',
    '操作中心':          'Root',

    # ── Spine ────────────────────────────────────────────────────
    '下半身':            'Pelvis',
    '上半身':            'Spine1',
    '上半身2':           'Spine2',
    '上半身3':           'Spine3',
    '腰':                'Pelvis',

    # ── Chest ────────────────────────────────────────────────────
    '胸':                'Chest',
    '左胸':              'L_Breast',
    '右胸':              'R_Breast',
    '左乳':              'L_Breast',
    '右乳':              'R_Breast',

    # ── Head / Neck ───────────────────────────────────────────────
    '首':                'Neck',
    '頭':                'Head',

    # ── Eyes / Face ──────────────────────────────────────────────
    '両目':              'C_Eye',
    '左目':              'L_Eye',
    '右目':              'R_Eye',
    '左目光':            'L_EyeHighlight',
    '右目光':            'R_EyeHighlight',
    '顎':                'Jaw',
    '鼻':                'Nose',
    '鼻子':              'NoseTip',
    '鼻先':              'NoseTip',
    '牙':                'Fang',
    '牙上':              'FangUp',
    '牙下':              'FangDown',
    '左牙':              'L_Fang',
    '右牙':              'R_Fang',
    '舌':                'Tongue',
    '舌1':               'Tongue1',
    '舌2':               'Tongue2',
    '舌3':               'Tongue3',
    '左眉':              'L_Brow',
    '右眉':              'R_Brow',
    '左頬':              'L_Cheek',
    '右頬':              'R_Cheek',

    # ── Shoulders (clavicles) ────────────────────────────────────
    '左肩':              'L_Clavicle',
    '右肩':              'R_Clavicle',
    '左肩P':             'L_ClavicleP',
    '右肩P':             'R_ClavicleP',
    '左肩C':             'L_ClavicleC',
    '右肩C':             'R_ClavicleC',

    # ── Arms ─────────────────────────────────────────────────────
    '左腕':              'L_Shoulder',
    '右腕':              'R_Shoulder',
    '左肘':              'L_Elbow',
    '右肘':              'R_Elbow',
    '左ひじ':            'L_Elbow',
    '右ひじ':            'R_Elbow',
    '左手首':            'L_Hand',
    '右手首':            'R_Hand',
    '左てくび':          'L_Hand',
    '右てくび':          'R_Hand',

    # Arm twists
    '左腕捩':            'L_ArmTwist',
    '右腕捩':            'R_ArmTwist',
    '左腕捩1':           'L_ArmTwist1',
    '左腕捩2':           'L_ArmTwist2',
    '左腕捩3':           'L_ArmTwist3',
    '右腕捩1':           'R_ArmTwist1',
    '右腕捩2':           'R_ArmTwist2',
    '右腕捩3':           'R_ArmTwist3',
    '左手捩':            'L_WristTwist',
    '右手捩':            'R_WristTwist',
    '左手捩1':           'L_WristTwist1',
    '左手捩2':           'L_WristTwist2',
    '左手捩3':           'L_WristTwist3',
    '右手捩1':           'R_WristTwist1',
    '右手捩2':           'R_WristTwist2',
    '右手捩3':           'R_WristTwist3',

    # ── IK helpers ────────────────────────────────────────────────
    '左腕ＩＫ':          'L_Buffbone_Glb_Hand_Loc',
    '右腕ＩＫ':          'R_Buffbone_Glb_Hand_Loc',
    '左足ＩＫ':          'L_Buffbone_Glb_Foot_Loc',
    '右足ＩＫ':          'R_Buffbone_Glb_Foot_Loc',
    '左足IK':            'L_Buffbone_Glb_Foot_Loc',
    '右足IK':            'R_Buffbone_Glb_Foot_Loc',
    '左つま先ＩＫ':      'L_ToeIK',
    '右つま先ＩＫ':      'R_ToeIK',
    '左つま先IK':        'L_ToeIK',
    '右つま先IK':        'R_ToeIK',
    '左足IK親':          'L_Buffbone_Glb_Foot_Root',
    '右足IK親':          'R_Buffbone_Glb_Foot_Root',

    # ── Dummy / Misc ───────────────────────────────────────────
    'ダミー':            'Dummy',
    '左ダミー':          'L_Dummy',
    '右ダミー':          'R_Dummy',
    '操作中心':          'Root',
    'センター先':        'RootTip',
    '腰':                'Waist',
    '尾':                'Tail',
    '胸':                'Chest',
    '乳':                'Breast',
    '左乳':              'L_Breast',
    '右乳':              'R_Breast',


    # ── Fingers – Left ───────────────────────────────────────────
    '左親指０':          'L_Thumb1',
    '左親指１':          'L_Thumb2',
    '左親指２':          'L_Thumb3',
    '左親指先':          'L_ThumbTip',
    '左人指１':          'L_Index1',
    '左人指２':          'L_Index2',
    '左人指３':          'L_Index3',
    '左人指先':          'L_IndexTip',
    '左人差指１':        'L_Index1',
    '左人差指２':        'L_Index2',
    '左人差指３':        'L_Index3',
    '左人差指先':        'L_IndexTip',
    '左中指１':          'L_Middle1',
    '左中指２':          'L_Middle2',
    '左中指３':          'L_Middle3',
    '左中指先':          'L_MiddleTip',
    '左薬指１':          'L_Ring1',
    '左薬指２':          'L_Ring2',
    '左薬指３':          'L_Ring3',
    '左薬指先':          'L_RingTip',
    '左小指１':          'L_Pinky1',
    '左小指２':          'L_Pinky2',
    '左小指３':          'L_Pinky3',
    '左小指先':          'L_PinkyTip',

    # ── Fingers – Right ──────────────────────────────────────────
    '右親指０':          'R_Thumb1',
    '右親指１':          'R_Thumb2',
    '右親指２':          'R_Thumb3',
    '右親指先':          'R_ThumbTip',
    '右人指１':          'R_Index1',
    '右人指２':          'R_Index2',
    '右人指３':          'R_Index3',
    '右人指先':          'R_IndexTip',
    '右人差指１':        'R_Index1',
    '右人差指２':        'R_Index2',
    '右人差指３':        'R_Index3',
    '右人差指先':        'R_IndexTip',
    '右中指１':          'R_Middle1',
    '右中指２':          'R_Middle2',
    '右中指３':          'R_Middle3',
    '右中指先':          'R_MiddleTip',
    '右薬指１':          'R_Ring1',
    '右薬指２':          'R_Ring2',
    '右薬指３':          'R_Ring3',
    '右薬指先':          'R_RingTip',
    '右小指１':          'R_Pinky1',
    '右小指２':          'R_Pinky2',
    '右小指３':          'R_Pinky3',
    '右小指先':          'R_PinkyTip',

    # ── Legs ─────────────────────────────────────────────────────
    '左足':              'L_Hip',
    '右足':              'R_Hip',
    '左ひざ':            'L_KneeUpper',
    '右ひざ':            'R_KneeUpper',
    '左膝':              'L_KneeUpper',
    '右膝':              'R_KneeUpper',
    '左足首':            'L_Foot',
    '右足首':            'R_Foot',
    '左つま先':          'L_Toe',
    '右つま先':          'R_Toe',
    '左足先EX':          'L_Toe',
    '右足先EX':          'R_Toe',

    # ── Leg helpers ──────────────────────────────────────────────
    '左足D':             'L_HipD',
    '右足D':             'R_HipD',
    '左ひざD':           'L_KneeUpperD',
    '右ひざD':           'R_KneeUpperD',
    '左足首D':           'L_FootD',
    '右足首D':           'R_FootD',
}
# fmt: on


# ---------------------------------------------------------------------------
# 2.  COMPONENT TABLE  (Japanese morphemes for decomposing custom bones)
#     Sorted longest-first so greedy matching works correctly.
# ---------------------------------------------------------------------------
# fmt: off
# Pre-sorted longest-first for greedy matching (no runtime sort needed)
_COMPONENT_JP = [
    # 6+ chars
    ('ポニーテール', 'Ponytail'),
    ('ツインテール', 'Twintail'),
    # 4 chars
    ('スカート', 'Skirt'),
    ('マフラー', 'Scarf'),
    ('ネクタイ', 'Necktie'),
    ('エプロン', 'Apron'),
    ('ツインテ', 'Twintail'),
    # 3 chars
    ('後ろ髪', 'BackHair'),
    ('アホ毛', 'Ahoge'),
    ('おさげ', 'Braid'),
    ('ポニテ', 'Ponytail'),
    ('マント', 'Mantle'),
    ('リボン', 'Ribbon'),
    ('ベルト', 'Belt'),
    ('ボタン', 'Button'),
    ('フリル', 'Frill'),
    ('ケープ', 'Cape'),
    ('コート', 'Coat'),
    ('しっぽ', 'Tail'),
    ('眉毛',  'Brow'),
    # 2 chars
    ('後髪', 'BackHair'),
    ('横髪', 'SideHair'),
    ('前髪', 'FrontHair'),
    ('振袖', 'Sleeve'),
    ('尻尾', 'Tail'),
    ('後ろ', 'Back'),
    # 1 char
    ('左', 'L_'),
    ('右', 'R_'),
    ('前', 'Front'),
    ('後', 'Back'),
    ('上', 'Up'),
    ('下', 'Down'),
    ('中', 'Mid'),
    ('横', 'Side'),
    ('先', 'Tip'),
    ('元', 'Base'),
    ('親', 'Root'),
    ('髪', 'Hair'),
    ('毛', 'Hair'),
    ('羽', 'Wing'),
    ('耳', 'Ear'),
    ('角', 'Horn'),
    ('牙', 'Fang'),
    ('眉', 'Brow'),
    ('頬', 'Cheek'),
    ('口', 'Mouth'),
    ('顎', 'Jaw'),
    ('鼻', 'Nose'),
    ('舌', 'Tongue'),
    ('刀', 'Sword'),
    ('剣', 'Sword'),
    ('槍', 'Spear'),
    ('杖', 'Staff'),
    ('弓', 'Bow'),
    ('盾', 'Shield'),
    ('鞘', 'Sheath'),
    ('紐', 'Cord'),
    ('鎖', 'Chain'),
    ('袖', 'Sleeve'),
    ('襟', 'Collar'),
    ('裾', 'Hem'),
    ('子', 'Tip'),
    # ── Hiragana words (common in MMD bones) ──────────────────
    ('しっぽ', 'Tail'),
    ('ひざ', 'Knee'),
    ('ひじ', 'Elbow'),
    ('つま先', 'Toe'),
    ('おさげ', 'Braid'),
    ('かみ', 'Hair'),
    ('まえ', 'Front'),
    ('うしろ', 'Back'),
    ('よこ', 'Side'),
    ('ひだり', 'L_'),
    ('みぎ', 'R_'),
]
# fmt: on


# ---------------------------------------------------------------------------
# 3.  SINGLE-KANJI DICTIONARY  (character-level fallback)
#     When multi-char component matching fails, try translating one kanji
#     at a time.  Covers ~200 common kanji found in MMD bone names.
# ---------------------------------------------------------------------------
_KANJI_EN = {
    # Body
    '頭': 'Head', '首': 'Neck', '肩': 'Shoulder', '腕': 'Arm', '肘': 'Elbow',
    '手': 'Hand', '指': 'Finger', '爪': 'Claw', '拳': 'Fist', '掌': 'Palm',
    '胸': 'Chest', '乳': 'Breast', '腹': 'Belly', '腰': 'Waist', '尻': 'Hip',
    '股': 'Thigh', '脚': 'Leg', '膝': 'Knee', '足': 'Foot', '踵': 'Heel',
    '趾': 'Toe', '背': 'Back', '骨': 'Bone', '体': 'Body', '身': 'Body',
    '筋': 'Muscle', '肌': 'Skin', '皮': 'Skin',
    # Face
    '目': 'Eye', '眉': 'Brow', '瞳': 'Pupil', '瞼': 'Eyelid', '睫': 'Lash',
    '鼻': 'Nose', '口': 'Mouth', '唇': 'Lip', '歯': 'Teeth', '舌': 'Tongue',
    '顎': 'Jaw', '頬': 'Cheek', '耳': 'Ear', '顔': 'Face', '額': 'Forehead',
    '涙': 'Tear',
    # Hair
    '髪': 'Hair', '毛': 'Hair', '鬢': 'Sideburn', '髭': 'Beard',
    # Animal
    '羽': 'Wing', '翼': 'Wing', '尾': 'Tail', '角': 'Horn', '牙': 'Fang',
    '爪': 'Claw', '蹄': 'Hoof', '鱗': 'Scale', '鰭': 'Fin',
    # Direction
    '左': 'L', '右': 'R', '上': 'Up', '下': 'Down', '中': 'Mid',
    '前': 'Front', '後': 'Back', '横': 'Side', '内': 'Inner', '外': 'Outer',
    '先': 'Tip', '元': 'Base', '奥': 'Deep', '端': 'Edge',
    # Position
    '心': 'Center', '央': 'Center', '間': 'Between', '根': 'Root',
    '親': 'Parent', '子': 'Child', '小': 'Small', '大': 'Big',
    # Clothing
    '袖': 'Sleeve', '襟': 'Collar', '裾': 'Hem', '帯': 'Belt', '紐': 'Cord',
    '鎖': 'Chain', '飾': 'Ornament', '冠': 'Crown', '帽': 'Hat',
    '靴': 'Boot', '服': 'Cloth',
    # Weapons
    '刀': 'Sword', '剣': 'Sword', '槍': 'Spear', '杖': 'Staff', '弓': 'Bow',
    '矢': 'Arrow', '盾': 'Shield', '鞘': 'Sheath', '斧': 'Axe', '鎌': 'Scythe',
    '銃': 'Gun', '砲': 'Cannon',
    # Nature / Objects
    '花': 'Flower', '葉': 'Leaf', '草': 'Grass', '木': 'Tree', '枝': 'Branch',
    '石': 'Stone', '玉': 'Gem', '星': 'Star', '月': 'Moon', '日': 'Sun',
    '火': 'Fire', '水': 'Water', '風': 'Wind', '雷': 'Thunder', '雪': 'Snow',
    '氷': 'Ice', '光': 'Light', '影': 'Shadow', '闇': 'Dark',
    # Colors
    '赤': 'Red', '青': 'Blue', '白': 'White', '黒': 'Black', '金': 'Gold',
    '銀': 'Silver', '紫': 'Purple', '緑': 'Green', '黄': 'Yellow',
    # Misc
    '輪': 'Ring', '珠': 'Bead', '球': 'Ball', '紋': 'Crest', '印': 'Mark',
    '線': 'Line', '帯': 'Band', '巻': 'Scroll', '板': 'Board', '糸': 'Thread',
    '縄': 'Rope', '蝶': 'Butterfly', '鈴': 'Bell', '鍵': 'Key', '扉': 'Door',
    '柱': 'Pillar', '翅': 'Wing', '紙': 'Paper',
    # Physics / Motion
    '揺': 'Sway', '捩': 'Twist', '回': 'Rotate', '動': 'Move', '操': 'Control',
    '補': 'Aux', '調': 'Adjust', '遅': 'Delay',
}

# ---------------------------------------------------------------------------
# 4.  KATAKANA → ROMAJI  (for transliterating unknown katakana words)
# ---------------------------------------------------------------------------
_KATA_ROMAJI = {
    'ア': 'A',  'イ': 'I',  'ウ': 'U',  'エ': 'E',  'オ': 'O',
    'カ': 'Ka', 'キ': 'Ki', 'ク': 'Ku', 'ケ': 'Ke', 'コ': 'Ko',
    'サ': 'Sa', 'シ': 'Shi','ス': 'Su', 'セ': 'Se', 'ソ': 'So',
    'タ': 'Ta', 'チ': 'Chi','ツ': 'Tsu','テ': 'Te', 'ト': 'To',
    'ナ': 'Na', 'ニ': 'Ni', 'ヌ': 'Nu', 'ネ': 'Ne', 'ノ': 'No',
    'ハ': 'Ha', 'ヒ': 'Hi', 'フ': 'Fu', 'ヘ': 'He', 'ホ': 'Ho',
    'マ': 'Ma', 'ミ': 'Mi', 'ム': 'Mu', 'メ': 'Me', 'モ': 'Mo',
    'ヤ': 'Ya',             'ユ': 'Yu',             'ヨ': 'Yo',
    'ラ': 'Ra', 'リ': 'Ri', 'ル': 'Ru', 'レ': 'Re', 'ロ': 'Ro',
    'ワ': 'Wa', 'ヲ': 'Wo', 'ン': 'N',
    'ガ': 'Ga', 'ギ': 'Gi', 'グ': 'Gu', 'ゲ': 'Ge', 'ゴ': 'Go',
    'ザ': 'Za', 'ジ': 'Ji', 'ズ': 'Zu', 'ゼ': 'Ze', 'ゾ': 'Zo',
    'ダ': 'Da', 'ヂ': 'Di', 'ヅ': 'Du', 'デ': 'De', 'ド': 'Do',
    'バ': 'Ba', 'ビ': 'Bi', 'ブ': 'Bu', 'ベ': 'Be', 'ボ': 'Bo',
    'パ': 'Pa', 'ピ': 'Pi', 'プ': 'Pu', 'ペ': 'Pe', 'ポ': 'Po',
    'ヴ': 'Vu',
    # Combo (small kana for ya/yu/yo combos)
    'ャ': 'ya', 'ュ': 'yu', 'ョ': 'yo',
    'ァ': 'a',  'ィ': 'i',  'ゥ': 'u',  'ェ': 'e',  'ォ': 'o',
    'ッ': '',   # double consonant marker (handled in _kata_to_romaji)
    'ー': '',   # long vowel marker
}

# Hiragana particles to silently skip (only の = possessive/connecting particle)
_HIRA_SKIP = set('の')


def _kata_to_romaji(text):
    '''Convert a katakana string to romaji. Unknown chars passed through.'''
    result = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == 'ッ' and i + 1 < len(text):
            # Double the next consonant
            nxt = _KATA_ROMAJI.get(text[i + 1], '')
            if nxt and len(nxt) > 0:
                result.append(nxt[0])  # double first letter
            i += 1
            continue
        if ch == 'ー':
            # Elongate previous vowel (just skip for bone names)
            i += 1
            continue
        rom = _KATA_ROMAJI.get(ch)
        if rom is not None:
            result.append(rom)
        else:
            result.append(ch)
        i += 1
    return ''.join(result)


def _is_katakana(ch):
    return '\u30A0' <= ch <= '\u30FF'


def _is_hiragana(ch):
    return '\u3040' <= ch <= '\u309F'


def _is_kanji(ch):
    cp = ord(ch)
    return (0x4E00 <= cp <= 0x9FFF) or (0x3400 <= cp <= 0x4DBF)


def _decompose_jp(jp_name):
    '''
    Decompose a Japanese bone name into English components.
    Uses 3-level fallback:
      1. Multi-char component table  (前髪 → FrontHair)
      2. Single-char kanji dict      (牙 → Fang)
      3. Katakana → romaji           (ドレス → Doresu)
    Hiragana particles (の, は, etc.) are silently skipped.
    Returns translated string, or None only if input is pure ASCII.
    '''
    original = jp_name

    # ── Strip trailing digits ────────────────────────────────────
    num_suffix = ''
    i = len(jp_name)
    while i > 0 and (jp_name[i-1].isdigit() or jp_name[i-1] in '０１２３４５６７８９'):
        i -= 1
    if i < len(jp_name) and i > 0:
        num_raw    = jp_name[i:]
        jp_name    = jp_name[:i]
        num_suffix = num_raw.translate(str.maketrans('０１２３４５６７８９', '0123456789'))

    # ── Check if there's any Japanese text at all ────────────────
    has_jp = any(_is_kanji(c) or _is_katakana(c) or _is_hiragana(c) for c in jp_name)
    if not has_jp:
        return None  # pure ASCII → let caller handle via romaji fallback

    # ── Split on underscores and process ─────────────────────────
    segments      = jp_name.split('_')
    side_found    = ''
    english_parts = []

    for seg in segments:
        if not seg:
            english_parts.append('')
            continue

        remaining = seg
        seg_parts = []

        while remaining:
            # 1) Try multi-char component table first
            matched = False
            for comp, eng in _COMPONENT_JP:
                if remaining.startswith(comp):
                    if eng in ('L_', 'R_'):
                        side_found = eng
                    else:
                        seg_parts.append(eng)
                    remaining = remaining[len(comp):]
                    matched = True
                    break

            if matched:
                continue

            # 2) Single character fallback
            ch = remaining[0]

            # Skip hiragana particles
            if ch in _HIRA_SKIP:
                remaining = remaining[1:]
                continue

            # Kanji → English
            if _is_kanji(ch):
                eng = _KANJI_EN.get(ch)
                if eng:
                    if eng == 'L':
                        side_found = 'L_'
                    elif eng == 'R':
                        side_found = 'R_'
                    else:
                        seg_parts.append(eng)
                    remaining = remaining[1:]
                    continue
                # Unknown kanji: keep as-is
                seg_parts.append(ch)
                remaining = remaining[1:]
                continue

            # Katakana run → romaji
            if _is_katakana(ch):
                kata_run = []
                while remaining and _is_katakana(remaining[0]):
                    kata_run.append(remaining[0])
                    remaining = remaining[1:]
                rom = _kata_to_romaji(''.join(kata_run))
                seg_parts.append(rom.capitalize() if rom else '')
                continue

            # Hiragana: skip (grammar particles, adjective endings, etc.)
            if _is_hiragana(ch):
                remaining = remaining[1:]
                continue

            # ASCII or other: keep as-is and stop
            seg_parts.append(remaining)
            break

        english_parts.append(''.join(seg_parts))

    body = '_'.join(p for p in english_parts if p)
    if not body:
        return None

    return side_found + body + num_suffix


# ---------------------------------------------------------------------------
# 6.  ROMAJI COMPONENT TABLE  (for models that store names in romaji)
#     Pre-sorted longest-first.
# ---------------------------------------------------------------------------
_COMPONENT_ROMAJI = [
    # Long words first
    ('hitosashiyubi', 'Index'), ('nakayubi', 'Middle'), ('kusuriyubi', 'Ring'),
    ('koyubi', 'Pinky'), ('oyayubi', 'Thumb'),
    ('jouhanshin', 'Spine'), ('kahanshin', 'Pelvis'),
    ('ashikubi', 'Foot'), ('tekubi', 'Hand'),
    ('tsumasaki', 'Toe'), ('tsumashaki', 'Toe'), ('tsumaasaki', 'Toe'),
    # Clothing / accessories
    ('sukaato', 'Skirt'), ('sukato', 'Skirt'),
    ('ribon', 'Ribbon'), ('ribbon', 'Ribbon'),
    ('beruto', 'Belt'),
    ('manto', 'Mantle'), ('mantle', 'Mantle'),
    ('nekutai', 'Necktie'),
    ('furisode', 'Sleeve'),
    ('epuron', 'Apron'),
    # Hair
    ('maegami', 'FrontHair'), ('zenpatsu', 'FrontHair'),
    ('kouhaipatsu', 'BackHair'), ('sokuhaipatsu', 'SideHair'),
    ('ahoge', 'Ahoge'), ('osage', 'Braid'),
    ('tsuinteeru', 'Twintail'), ('twintail', 'Twintail'),
    ('poniteeru', 'Ponytail'), ('ponytail', 'Ponytail'),
    # Body
    ('atama', 'Head'), ('kubi', 'Neck'), ('koshi', 'Waist'),
    ('mune', 'Chest'), ('chichi', 'Breast'),
    ('kata', 'Shoulder'), ('ude', 'Arm'), ('hiji', 'Elbow'),
    ('ashi', 'Leg'), ('hiza', 'Knee'),
    ('yubi', 'Finger'), ('te', 'Hand'),
    ('shippo', 'Tail'), ('sippo', 'Tail'),
    ('mimi', 'Ear'), ('hane', 'Wing'),
    ('tsuno', 'Horn'), ('kiba', 'Fang'),
    ('me', 'Eye'), ('mayuge', 'Brow'),
    ('hana', 'Nose'), ('kuchi', 'Mouth'),
    ('ago', 'Jaw'), ('hoho', 'Cheek'),
    ('shita', 'Tongue'),
    ('kami', 'Hair'), ('ke', 'Hair'),
    # Weapons
    ('katana', 'Sword'), ('tsurugi', 'Sword'), ('ken', 'Sword'),
    ('yari', 'Spear'), ('tsuba', 'Guard'),
    # Directions
    ('hidari', 'L_'), ('migi', 'R_'),
    ('mae', 'Front'), ('ushiro', 'Back'),
    ('ue', 'Up'), ('shita', 'Down'),
    ('yoko', 'Side'), ('naka', 'Mid'),
    ('saki', 'Tip'), ('moto', 'Base'),
    ('oya', 'Root'),
    # Misc
    ('himo', 'Cord'), ('sode', 'Sleeve'), ('eri', 'Collar'),
    ('sentaa', 'Root'), ('sentah', 'Root'),
    ('guruubu', 'Groove'), ('guroobaru', 'Global'),
    ('mojiri', 'Twist'),
    ('IK', 'IK'),
]


def _decompose_romaji(name):
    '''
    Decompose a romaji bone name into English using component matching.
    Returns translated string, or None if nothing matched.
    '''
    # Strip trailing digits
    num_suffix = ''
    i = len(name)
    while i > 0 and name[i-1].isdigit():
        i -= 1
    if i < len(name) and i > 0:
        num_suffix = name[i:]
        name = name[:i]

    segments    = name.split('_')
    side_found  = ''
    eng_parts   = []
    any_match   = False

    for seg in segments:
        if not seg:
            eng_parts.append('')
            continue
        remaining = seg.lower()
        seg_parts = []

        while remaining:
            matched = False
            for comp, eng in _COMPONENT_ROMAJI:
                if remaining.startswith(comp):
                    if eng == 'L_' or eng == 'R_':
                        side_found = eng
                    else:
                        seg_parts.append(eng)
                    remaining = remaining[len(comp):]
                    matched = True
                    any_match = True
                    break
            if not matched:
                # Keep unmatched tail (capitalize first letter)
                seg_parts.append(remaining[0].upper() + remaining[1:] if remaining else '')
                break

        eng_parts.append(''.join(seg_parts))

    if not any_match:
        return None

    body = '_'.join(p for p in eng_parts if p)
    return side_found + body + num_suffix


# ---------------------------------------------------------------------------
# 7.  PUBLIC API
# ---------------------------------------------------------------------------
def to_english(jp_name, romaji_fallback=None):
    '''
    Convert a Japanese bone name to English (LoL naming style).

    Args:
        jp_name:          Original Japanese bone name from the PMX file.
        romaji_fallback:  Pre-converted romaji string to use if no translation
                          found. If None, jp_name is returned as-is.

    Priority:
      1. Exact match in BONE_NAME_JP_EN
      2. Strip trailing digits, try base match  (e.g. "上半身2" → "Spine2")
      3. Component decomposition from Japanese  (_decompose_jp)
      4. Romaji decomposition  (_decompose_romaji)
      5. Fallback to romaji_fallback (or jp_name)
    '''
    # 1. Exact match
    if jp_name in BONE_NAME_JP_EN:
        return BONE_NAME_JP_EN[jp_name]

    # 2. Strip trailing digits (both half & full-width)
    i = len(jp_name)
    while i > 0 and (jp_name[i-1].isdigit() or jp_name[i-1] in '０１２３４５６７８９'):
        i -= 1
    if i < len(jp_name) and i > 0:
        base = jp_name[:i]
        num  = jp_name[i:].translate(str.maketrans('０１２３４５６７８９', '0123456789'))
        if base in BONE_NAME_JP_EN:
            return BONE_NAME_JP_EN[base] + num

    # 3. Component decomposition (Japanese)
    decomposed = _decompose_jp(jp_name)
    if decomposed is not None:
        if decomposed.isascii():
            return decomposed
        # Decompose produced non-ASCII remnants; try romaji path

    # 4. Romaji decomposition (for models storing names in romaji)
    romaji_input = romaji_fallback if romaji_fallback else jp_name
    decomposed_r = _decompose_romaji(romaji_input)
    if decomposed_r is not None:
        return decomposed_r

    # 5. Fallback (always prefer romaji to avoid multibyte chars in Maya)
    result = romaji_fallback if romaji_fallback is not None else jp_name
    # Final safety: strip any remaining non-ASCII characters
    result = re.sub(r'[^\x00-\x7F]+', '_', result)
    result = re.sub(r'_+', '_', result).strip('_') or 'bone'
    return result


if __name__ == '__main__':
    # Standalone test (run: python bone_names.py)
    tests = [
        # Standard bones
        ('センター', 'fb', 'Root'),
        ('全ての親', 'fb', 'Root'),
        ('下半身', 'fb', 'Pelvis'),
        ('上半身', 'fb', 'Spine1'),
        ('上半身2', 'fb', 'Spine2'),
        ('首', 'fb', 'Neck'),
        ('頭', 'fb', 'Head'),
        ('左肩', 'fb', 'L_Clavicle'),
        ('右肩', 'fb', 'R_Clavicle'),
        ('左腕', 'fb', 'L_Shoulder'),
        ('右腕', 'fb', 'R_Shoulder'),
        ('左肘', 'fb', 'L_Elbow'),
        ('左手首', 'fb', 'L_Hand'),
        ('左足', 'fb', 'L_Hip'),
        ('左ひざ', 'fb', 'L_KneeUpper'),
        ('左足首', 'fb', 'L_Foot'),
        ('左つま先', 'fb', 'L_Toe'),
        ('左親指０', 'fb', 'L_Thumb1'),
        ('左親指１', 'fb', 'L_Thumb2'),
        ('左人差指１', 'fb', 'L_Index1'),
        ('左中指１', 'fb', 'L_Middle1'),
        ('左薬指１', 'fb', 'L_Ring1'),
        ('左小指１', 'fb', 'L_Pinky1'),
        ('左足ＩＫ', 'fb', 'L_Buffbone_Glb_Foot_Loc'),
        # Custom bones (component decompose)
        ('髪左１', 'fb', 'L_Hair1'),
        ('髪右２', 'fb', 'R_Hair2'),
        ('前髪１', 'fb', 'FrontHair1'),
        ('前髪左', 'fb', 'L_FrontHair'),
        ('スカート前１', 'fb', 'SkirtFront1'),
        ('スカート左１', 'fb', 'L_Skirt1'),
        ('しっぽ１', 'fb', 'Tail1'),
        ('左耳', 'fb', 'L_Ear'),
        ('右羽１', 'fb', 'R_Wing1'),
        ('刀先', 'fb', 'SwordTip'),
        ('アホ毛', 'fb', 'Ahoge'),
        ('リボン３', 'fb', 'Ribbon3'),
        # User-reported problematic bones
        ('グルーブ', 'fb', 'Groove'),
        ('センター2', 'fb', 'Root2'),
        ('牙下', 'fb', 'FangDown'),
        ('鼻子', 'fb', 'NoseTip'),
        # AUTO-TRANSLATION: kanji single-char fallback
        ('左瞼', 'fb', 'L_Eyelid'),          # 瞼 from kanji dict
        ('花飾１', 'fb', 'FlowerOrnament1'),  # 花+飾 both from kanji
        ('右翼', 'fb', 'R_Wing'),             # 翼 from kanji dict
        ('氷の剣', 'fb', 'IceSword'),         # の skipped (hiragana)
        ('左腹', 'fb', 'L_Belly'),
        ('金の冠', 'fb', 'GoldCrown'),        # の skipped
        ('赤い光', 'fb', 'RedLight'),         # い skipped
        # AUTO-TRANSLATION: katakana → romaji
        ('ドレス', 'fb', 'Doresu'),           # katakana loan word
        ('ドレス前１', 'fb', 'DoresuFront1'), # katakana + kanji + num
        ('マッスル', 'fb', 'Massuru'),        # ッ double consonant
        # AUTO-TRANSLATION: mixed
        ('左ガントレット', 'fb', 'L_Gantoretto'),
        # ROMAJI DECOMPOSITION (models storing romaji in b.name)
        ('sukaatomae1', 'sukaatomae1', 'SkirtFront1'),      # sukaato=Skirt + mae=Front
        ('sukaatohidari1', 'sukaatohidari1', 'L_Skirt1'),   # hidari=L_
        ('hidarikoyubi1', 'hidarikoyubi1', 'L_Pinky1'),     # finger via romaji
        ('migiude', 'migiude', 'R_Arm'),
        ('sentaa', 'sentaa', 'Root'),
        ('guruubu', 'guruubu', 'Groove'),
        ('kamimigi1', 'kamimigi1', 'R_Hair1'),
        ('ribon3', 'ribon3', 'Ribbon3'),
        # Fallback
        ('unknown', 'fallback_romaji', 'fallback_romaji'),
        ('カスタム', None, 'Kasutamu'),        # pure katakana → romaji (no fallback)
    ]
    ok = 0
    fail = 0
    for jp, fb, expected in tests:
        result = to_english(jp, fb)
        status = 'OK' if result == expected else 'FAIL'
        if status == 'FAIL':
            fail += 1
            print(f'  FAIL: {jp} -> {result} (expected {expected})')
        else:
            ok += 1
            print(f'  OK:   {jp} -> {result}')
    print(f'\n{ok} passed, {fail} failed out of {ok+fail} tests')
