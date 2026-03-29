# -*- coding: utf-8 -*-
'''
Human IKに使うジョイントの名前の正規表現の辞書。
'''
import maya.cmds as mc
import math

dic_hik = {
    0: ['Center','.*sentaa'],
    1: ['LowerBody','kahanshin'],
    2: ['LegL','hidariashi'],
    3: ['KneeL','hidarihiza'],
    4: ['AnkleL','hidariashikubi'],
    5: ['LegR','migiashi'],
    6: ['KneeR','migihiza'],
    7: ['AnkleR','migiashikubi'],
    8: ['UpperBody','jouhanshin'],
    9: ['ArmL','hidariude'],
    10: ['ElbowL','hidarihiji'],
    11: ['WristL','hidarite(kubi)?'],
    12: ['ArmR','migiude'],
    13: ['ElbowR','migihiji'],
    14: ['WristR','migite(kubi)?'],
    15: ['Head','atama'],
    18: ['ShoulderL','hidarikata'],
    19: ['ShoulderR','migikata'],
    20: ['Neck','kubi'],
    23: ['UpperBody2','jouhanshin2'],
    45: ['ArmTwistL','hidariudemojiri'],
    46: ['WristTwistL','hidaritemojiri'],
    47: ['ArmTwistR','migiudemojiri'],
    48: ['WristTwistR','migitemojiri'],
    50: ['ThumbRoot0L','hidarioyayubi0M?'],
    51: ['Thumb1L','hidarioyayubi1'],
    52: ['Thumb2L','hidarioyayubi2'],
    53: ['ThumbTipL','hidarioyayubi.*saki'],
    54: ['Index1L','hidari(hitosashi|nin)yubi1'],
    55: ['Index2L','hidari(hitosashi|nin)yubi2'],
    56: ['Index3L','hidari(hitosashi|nin)yubi3'],
    57: ['IndexTipL','hidari(hitosashi|nin)yubi.*saki'],
    58: ['Middle1L','(sachuu|hidarinaka)yubi1'],
    59: ['Middle2L','(sachuu|hidarinaka)yubi2'],
    60: ['Middle3L','(sachuu|hidarinaka)yubi3'],
    61: ['MiddleTipL','(sachuu|hidarinaka)yubi.*saki'],
    62: ['Ring1L','hidarikusuriyubi1'],
    63: ['Ring2L','hidarikusuriyubi2'],
    64: ['Ring3L','hidarikusuriyubi3'],
    65: ['RingTipL','hidarikusuriyubi.*saki'],
    66: ['Pinky1L','hidarikoyubi1'],
    67: ['Pinky2L','hidarikoyubi2'],
    68: ['Pinky3L','hidarikoyubi3'],
    69: ['PinkyTipL','hidarikoyubi.*saki'],
    74: ['ThumbRoot0R','migioyayubi0M?'],
    75: ['Thumb1R','migioyayubi1'],
    76: ['Thumb2R','migioyayubi2'],
    77: ['ThumbTipR','migioyayubi.*saki'],
    78: ['Index1R','migi(hitosashi|nin)yubi1'],
    79: ['Index2R','migi(hitosashi|nin)yubi2'],
    80: ['Index3R','migi(hitosashi|nin)yubi3'],
    81: ['IndexTipR','migi(hitosashi|nin)yubi.*saki'],
    82: ['Middle1R','(uchuu|miginaka)yubi1'],
    83: ['Middle2R','(uchuu|miginaka)yubi2'],
    84: ['Middle3R','(uchuu|miginaka)yubi3'],
    85: ['MiddleTipR','(uchuu|miginaka)yubi.*saki'],
    86: ['Ring1R','migikusuriyubi1'],
    87: ['Ring2R','migikusuriyubi2'],
    88: ['Ring3R','migikusuriyubi3'],
    89: ['RingTipR','migikusuriyubi.*saki'],
    90: ['Pinky1R','migikoyubi1'],
    91: ['Pinky2R','migikoyubi2'],
    92: ['Pinky3R','migikoyubi3'],
    93: ['PinkyTipR','migikoyubi.*saki']
}

def kangkhaen(dic_chue):
    la = dic_chue[9] # 左腕
    lh = dic_chue[11] # 左手
    ra = dic_chue[12] # 右腕
    rh = dic_chue[14] # 右手
    # まず全部のジョイントの回転を0に戻す
    for kho in dic_chue.values():
        mc.setAttr(kho+'.r',0,0,0)

    xyz_la = mc.xform(la,query=True,translation=True,worldSpace=True)
    xyz_lh0 = mc.xform(lh,query=True,translation=True,worldSpace=True)
    xyz_ra = mc.xform(ra,query=True,translation=True,worldSpace=True)
    xyz_rh0 = mc.xform(rh,query=True,translation=True,worldSpace=True)

    atan_l = math.degrees(math.atan2(xyz_la[1]-xyz_lh0[1],xyz_lh0[0]-xyz_la[0]))
    atan_r = math.degrees(math.atan2(xyz_ra[1]-xyz_rh0[1],xyz_ra[0]-xyz_rh0[0]))

    mc.setAttr(la+'.rz',atan_l)
    mc.setAttr(ra+'.rz',-atan_r)

    xyz_lh1 = mc.xform(lh,query=True,translation=True,worldSpace=True)
    if(xyz_lh1[1]<xyz_lh0[1]):
        mc.setAttr(la+'.rz',-atan_l)
    xyz_rh1 = mc.xform(rh,query=True,translation=True,worldSpace=True)
    if(xyz_rh1[1]<xyz_rh0[1]):
        mc.setAttr(ra+'.rz',atan_r)

    xyz_lh1 = mc.xform(lh,query=True,translation=True,worldSpace=True)
    if(abs(xyz_lh1[1]-xyz_lh0[1])<abs(xyz_lh1[2]-xyz_lh0[2])):
        mc.setAttr(la+'.rz',0)
        mc.setAttr(la+'.rx',atan_l)
        xyz_lh1 = mc.xform(lh,query=True,translation=True,worldSpace=True)
        if(xyz_lh1[1]<xyz_lh0[1]):
            mc.setAttr(la+'.rx',-atan_l)
    xyz_rh1 = mc.xform(rh,query=True,translation=True,worldSpace=True)
    if(abs(xyz_rh1[1]-xyz_rh0[1])<abs(xyz_rh1[2]-xyz_rh0[2])):
        mc.setAttr(ra+'.rz',0)
        mc.setAttr(ra+'.rx',-atan_r)
        xyz_rh1 = mc.xform(rh,query=True,translation=True,worldSpace=True)
        if(xyz_rh1[1]<xyz_rh0[1]):
            mc.setAttr(ra+'.rx',atan_r)
