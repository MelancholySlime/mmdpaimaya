# -*- coding: utf-8 -*-
'''
Human IKに使うジョイントの名前の正規表現の辞書。
'''
import maya.cmds as mc
import math

dic_hik = {
    0: ['Root','(Root|.*sentaa)'],
    1: ['Pelvis','(Pelvis|kahanshin)'],
    2: ['L_Hip','(L_Hip|hidariashi)'],
    3: ['L_KneeUp','(L_KneeUpper|hidarihiza)'],
    4: ['L_Foot','(L_Foot|hidariashikubi)'],
    5: ['R_Hip','(R_Hip|migiashi)'],
    6: ['R_KneeUp','(R_KneeUpper|migihiza)'],
    7: ['R_Foot','(R_Foot|migiashikubi)'],
    8: ['Spine1','(Spine1|jouhanshin)'],
    9: ['L_Shoulder','(L_Shoulder|hidariude)'],
    10: ['L_Elbow','(L_Elbow|hidarihiji)'],
    11: ['L_Hand','(L_Hand|hidarite(kubi)?)'],
    12: ['R_Shoulder','(R_Shoulder|migiude)'],
    13: ['R_Elbow','(R_Elbow|migihiji)'],
    14: ['R_Hand','(R_Hand|migite(kubi)?)'],
    15: ['Head','(Head|atama)'],
    18: ['L_Clavicle','(L_Clavicle|hidarikata)'],
    19: ['R_Clavicle','(R_Clavicle|migikata)'],
    20: ['Neck','(Neck|kubi)'],
    23: ['Spine2','(Spine2|jouhanshin2)'],
    45: ['L_ArmTwist','(L_ArmTwist|hidariudemojiri)'],
    46: ['L_WristTwist','(L_WristTwist|hidaritemojiri)'],
    47: ['R_ArmTwist','(R_ArmTwist|migiudemojiri)'],
    48: ['R_WristTwist','(R_WristTwist|migitemojiri)'],
    50: ['L_Thumb1','(L_Thumb1|hidarioyayubi0M?)'],
    51: ['L_Thumb2','(L_Thumb2|hidarioyayubi1)'],
    52: ['L_Thumb3','(L_Thumb3|hidarioyayubi2)'],
    53: ['L_ThumbTip','(L_ThumbTip|hidarioyayubi.*saki)'],
    54: ['L_Index1','(L_Index1|hidari(hitosashi|nin)yubi1)'],
    55: ['L_Index2','(L_Index2|hidari(hitosashi|nin)yubi2)'],
    56: ['L_Index3','(L_Index3|hidari(hitosashi|nin)yubi3)'],
    57: ['L_IndexTip','(L_IndexTip|hidari(hitosashi|nin)yubi.*saki)'],
    58: ['L_Middle1','(L_Middle1|(sachuu|hidarinaka)yubi1)'],
    59: ['L_Middle2','(L_Middle2|(sachuu|hidarinaka)yubi2)'],
    60: ['L_Middle3','(L_Middle3|(sachuu|hidarinaka)yubi3)'],
    61: ['L_MiddleTip','(L_MiddleTip|(sachuu|hidarinaka)yubi.*saki)'],
    62: ['L_Ring1','(L_Ring1|hidarikusuriyubi1)'],
    63: ['L_Ring2','(L_Ring2|hidarikusuriyubi2)'],
    64: ['L_Ring3','(L_Ring3|hidarikusuriyubi3)'],
    65: ['L_RingTip','(L_RingTip|hidarikusuriyubi.*saki)'],
    66: ['L_Pinky1','(L_Pinky1|hidarikoyubi1)'],
    67: ['L_Pinky2','(L_Pinky2|hidarikoyubi2)'],
    68: ['L_Pinky3','(L_Pinky3|hidarikoyubi3)'],
    69: ['L_PinkyTip','(L_PinkyTip|hidarikoyubi.*saki)'],
    74: ['R_Thumb1','(R_Thumb1|migioyayubi0M?)'],
    75: ['R_Thumb2','(R_Thumb2|migioyayubi1)'],
    76: ['R_Thumb3','(R_Thumb3|migioyayubi2)'],
    77: ['R_ThumbTip','(R_ThumbTip|migioyayubi.*saki)'],
    78: ['R_Index1','(R_Index1|migi(hitosashi|nin)yubi1)'],
    79: ['R_Index2','(R_Index2|migi(hitosashi|nin)yubi2)'],
    80: ['R_Index3','(R_Index3|migi(hitosashi|nin)yubi3)'],
    81: ['R_IndexTip','(R_IndexTip|migi(hitosashi|nin)yubi.*saki)'],
    82: ['R_Middle1','(R_Middle1|(uchuu|miginaka)yubi1)'],
    83: ['R_Middle2','(R_Middle2|(uchuu|miginaka)yubi2)'],
    84: ['R_Middle3','(R_Middle3|(uchuu|miginaka)yubi3)'],
    85: ['R_MiddleTip','(R_MiddleTip|(uchuu|miginaka)yubi.*saki)'],
    86: ['R_Ring1','(R_Ring1|migikusuriyubi1)'],
    87: ['R_Ring2','(R_Ring2|migikusuriyubi2)'],
    88: ['R_Ring3','(R_Ring3|migikusuriyubi3)'],
    89: ['R_RingTip','(R_RingTip|migikusuriyubi.*saki)'],
    90: ['R_Pinky1','(R_Pinky1|migikoyubi1)'],
    91: ['R_Pinky2','(R_Pinky2|migikoyubi2)'],
    92: ['R_Pinky3','(R_Pinky3|migikoyubi3)'],
    93: ['R_PinkyTip','(R_PinkyTip|migikoyubi.*saki)']
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
