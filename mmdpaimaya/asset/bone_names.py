# -*- coding: utf-8 -*-
'''
Mapping from MMD romaji bone names to English names.
Uses League of Legends skeleton naming convention (L_/R_ prefix).
Keys are the romaji strings produced by jaka.romaji().
Values are the desired English joint names.
Bones not found in this table keep their romaji name unchanged.
'''

# fmt: off
BONE_NAME_EN = {
    # ── Core / Root ──────────────────────────────────────────────
    'sentaa':              'Root',
    'subetenooya':         'Root',
    'guroobaru':           'Root',
    'undou':               'Root',

    # ── Spine ────────────────────────────────────────────────────
    'kahanshin':           'Pelvis',
    'jouhanshin':          'Spine1',
    'jouhanshin2':         'Spine2',
    'jouhanshin3':         'Spine3',
    'koshi':               'Pelvis',
    'mune':                'Chest',
    'hidarimune':          'L_Breast',
    'migimune':            'R_Breast',
    'migichichi':          'R_Breast',
    'hidarichichi':        'L_Breast',

    # ── Head / Neck ───────────────────────────────────────────────
    'kubi':                'Neck',
    'atama':               'Head',
    'atamachien':          'Head_Delay',

    # ── Eyes / Face ──────────────────────────────────────────────
    'ryoumegane':          'C_Eye',
    'hidarime':            'L_Eye',
    'migime':              'R_Eye',
    'hidarimenoomoukimesen': 'L_Eye_Dir',
    'migimenoomoukimesen': 'R_Eye_Dir',
    'mienai':              'Invisible',

    # ── Shoulders / Clavicle ─────────────────────────────────────
    'hidarikata':          'L_Clavicle',
    'migikata':            'R_Clavicle',
    'hidarikatachien':     'L_Clavicle_Delay',
    'migikatachien':       'R_Clavicle_Delay',
    'hidarikataP':         'L_Clavicle_P',
    'migikataP':           'R_Clavicle_P',

    # ── Arms ─────────────────────────────────────────────────────
    'hidariude':           'L_Shoulder',
    'migiude':             'R_Shoulder',
    'hidarihiji':          'L_Elbow',
    'migihiji':            'R_Elbow',
    'hidaritekubi':        'L_Hand',
    'migitekubi':          'R_Hand',
    'hidarite':            'L_Hand',
    'migite':              'R_Hand',

    # Arm twists
    'hidariudemojiri':     'L_Shoulder_Twist',
    'migiudemojiri':       'R_Shoulder_Twist',
    'hidariudemojiri1':    'L_Shoulder_Twist1',
    'hidariudemojiri2':    'L_Shoulder_Twist2',
    'hidariudemojiri3':    'L_Shoulder_Twist3',
    'migiudemojiri1':      'R_Shoulder_Twist1',
    'migiudemojiri2':      'R_Shoulder_Twist2',
    'migiudemojiri3':      'R_Shoulder_Twist3',
    'hidaritemojiri':      'L_Hand_Twist',
    'migitemojiri':        'R_Hand_Twist',
    'hidaritemojiri1':     'L_Hand_Twist1',
    'hidaritemojiri2':     'L_Hand_Twist2',
    'hidaritemojiri3':     'L_Hand_Twist3',
    'migitemojiri1':       'R_Hand_Twist1',
    'migitemojiri2':       'R_Hand_Twist2',
    'migitemojiri3':       'R_Hand_Twist3',

    # IK helpers
    'hidariudeIK':         'L_Shoulder_IK',
    'migiudeIK':           'R_Shoulder_IK',

    # ── Fingers – Left ───────────────────────────────────────────
    # Thumb
    'hidarioyayubi0':      'L_Thumb1',
    'hidarioyayubi0M':     'L_Thumb1',
    'hidarioyayubi1':      'L_Thumb2',
    'hidarioyayubi2':      'L_Thumb3',
    'hidarioyayubisaki':   'L_Thumb_Tip',

    # Index
    'hidarihitosashiyubi1':  'L_Index1',
    'hidarihitosashiyubi2':  'L_Index2',
    'hidarihitosashiyubi3':  'L_Index3',
    'hidarihitosashiyubisaki': 'L_Index_Tip',
    'hidarininyubi1':      'L_Index1',
    'hidarininyubi2':      'L_Index2',
    'hidarininyubi3':      'L_Index3',
    'hidarininyubisaki':   'L_Index_Tip',

    # Middle
    'hidarinakayubi1':     'L_Middle1',
    'hidarinakayubi2':     'L_Middle2',
    'hidarinakayubi3':     'L_Middle3',
    'hidarinakayubisaki':  'L_Middle_Tip',
    'sachuuyubi1':         'L_Middle1',
    'sachuuyubi2':         'L_Middle2',
    'sachuuyubi3':         'L_Middle3',
    'sachuuyubisaki':      'L_Middle_Tip',

    # Ring
    'hidarikusuriyubi1':   'L_Ring1',
    'hidarikusuriyubi2':   'L_Ring2',
    'hidarikusuriyubi3':   'L_Ring3',
    'hidarikusuriyubisaki': 'L_Ring_Tip',

    # Pinky
    'hidarikoyubi1':       'L_Pinky1',
    'hidarikoyubi2':       'L_Pinky2',
    'hidarikoyubi3':       'L_Pinky3',
    'hidarikoyubisaki':    'L_Pinky_Tip',

    # ── Fingers – Right ──────────────────────────────────────────
    # Thumb
    'miginakayubi2':       'Middle2R',
    'miginakayubi3':       'Middle3R',
    'miginakayubisaki':    'MiddleTipR',
    'uchuuyubi1':          'Middle1R',
    'uchuuyubi2':          'Middle2R',
    'uchuuyubi3':          'Middle3R',
    'uchuuyubisaki':       'MiddleTipR',

    # Ring
    'migikusuriyubi1':     'Ring1R',
    'migikusuriyubi2':     'Ring2R',
    'migikusuriyubi3':     'Ring3R',
    'migikusuriyubisaki':  'RingTipR',

    # Pinky
    'migikoyubi1':         'Pinky1R',
    'migikoyubi2':         'Pinky2R',
    'migikoyubi3':         'Pinky3R',
    'migikoyubisaki':      'PinkyTipR',

    # ── Legs ─────────────────────────────────────────────────────
    'hidariashi':          'LegL',
    'migiashi':            'LegR',
    'hidarihiza':          'KneeL',
    'migihiza':            'KneeR',
    'hidariashikubi':      'AnkleL',
    'migiashikubi':        'AnkleR',
    'hidariashisaki':      'ToeL',
    'migiashisaki':        'ToeR',
    'hidaritsumashaki':    'ToeL',
    'migitsumashaki':      'ToeR',

    # Leg IK
    'hidariashiIK':        'LegIKL',
    'migiashiIK':          'LegIKR',
    'hidariashiIKoya':     'LegIKRootL',
    'migiashiIKoya':       'LegIKRootR',
    'hidarihizaIK':        'KneeIKL',
    'migihizaIK':          'KneeIKR',
    'hidaritsumasaki':     'ToeTipL',
    'migitsumasaki':       'ToeTipR',
    'hidaritsumaasakiIK':  'ToeIKL',
    'migitsumaasakiIK':    'ToeIKR',

    # Leg Twists / Helpers
    'hidarimomouwa':       'ThighHelperL',
    'migimomouwa':         'ThighHelperR',
    'hidariashiblock':     'LegBlockL',
    'migiashiblock':       'LegBlockR',

    # ── Extra / Physics ──────────────────────────────────────────
    'koshi':               'Waist',
    'mune':                'Chest',
    'hidarimune':          'ChestL',
    'migimune':            'ChestR',
    'migichichi':          'BreastR',
    'hidarichichi':        'BreastL',

    # Skirt / accessories (generic patterns handled in code via regex)
    # Hair / tails use their romaji names as-is if not in this table.
}
# fmt: on


def to_english(romaji_name):
    '''
    Convert a romaji bone name to its English equivalent.
    Falls back to the original romaji_name if no mapping exists.
    The lookup strips trailing digits handled by exact key then prefix search.
    '''
    # Exact match first
    if romaji_name in BONE_NAME_EN:
        return BONE_NAME_EN[romaji_name]

    # Try stripping a trailing '_<suffix>' that romaji() sometimes appends
    # e.g. 'atama_1' → try 'atama' first
    base = romaji_name.rsplit('_', 1)[0]
    if base in BONE_NAME_EN:
        suffix = romaji_name[len(base):]
        return BONE_NAME_EN[base] + suffix

    # No match – keep as-is (custom bones, physics, accessories, etc.)
    return romaji_name
