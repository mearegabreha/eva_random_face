import bpy
import random

selectedObj = bpy.context.object
selectedObj.animation_data_create()
selectedObj.animation_data.action = bpy.data.actions.new(name="GST-random1")
curve = selectedObj.animation_data.action.fcurves

head_L_X = curve.new(data_path='pose.bones["head"].location[0]', index=0, action_group='head')
head_L_Z = curve.new(data_path='pose.bones["head"].location[2]', index=2, action_group='head')
head_E_Y = curve.new(data_path='pose.bones["head"].rotation_euler[1]', index=1, action_group='head')
chin_Y = curve.new(data_path='pose.bones["chin"].location[1]', index=1, action_group='chin')
lip_D_L_Y = curve.new(data_path='pose.bones["lip_D_L"].location[1]', index=1, action_group='lip_D_L')
lip_D_Y = curve.new(data_path='pose.bones["lip_D"].location[1]', index=1, action_group='lip_D')
mouth_D_L_Y = curve.new(data_path='pose.bones["mouth_D_L"].location[1]', index=1, action_group='mouth_D_L')
lip_D_R_Y = curve.new(data_path='pose.bones["lip_D_R"].location[1]', index=1, action_group='lip_D_R')
mouth_D_R_Y = curve.new(data_path='pose.bones["mouth_D_R"].location[1]', index=1, action_group='mouth_D_R')
lip_U_Y = curve.new(data_path='pose.bones["lip_U"].location[1]', index=1, action_group='lip_U')
lip_U_L_Y = curve.new(data_path='pose.bones["lip_U_L"].location[1]', index=1, action_group='lip_U_L')
mouth_U_L_Y = curve.new(data_path='pose.bones["mouth_U_L"].location[1]', index=1, action_group='mouth_U_L')
lip_U_R_Y = curve.new(data_path='pose.bones["lip_U_R"].location[1]', index=1, action_group='lip_U_R')
mouth_U_R_Y = curve.new(data_path='pose.bones["mouth_U_R"].location[1]', index=1, action_group='mouth_U_R')
brow_R_Y = curve.new(data_path='pose.bones["brow.R"].location[1]', index=1, action_group='brow.R')
brow_L_Y = curve.new(data_path='pose.bones["brow_L"].location[1]', index=1, action_group='brow.L')
brow_C_Y = curve.new(data_path='pose.bones["brow.C"].location[1]', index=1, action_group='brow.C')
brow_inner_L_Y = curve.new(data_path='pose.bones["brow.inner.L"].location[1]', index=1, action_group='brow.inner.L')
brow_inner_R_Y = curve.new(data_path='pose.bones["brow.inner.R"].location[1]', index=1, action_group='brow.inner.R')
cheek_L_Y = curve.new(data_path='pose.bones["cheek_L"].location[1]', index=1, action_group='cheek_L')
eyelid_LO_L_Y = curve.new(data_path='pose.bones["eyelid_LO_L"].location[1]', index=1, action_group='eyelid_LO_L')
nostril_L_Y = curve.new(data_path='pose.bones["nostril_L"].location[1]', index=1, action_group='nostril_L')
cheek_R_Y = curve.new(data_path='pose.bones["cheek_R"].location[1]', index=1, action_group='cheek_R')
eyelid_LO_R_Y = curve.new(data_path='pose.bones["eyelid_LO_R"].location[1]', index=1, action_group='eyelid_LO_R')
nostril_R_Y = curve.new(data_path='pose.bones["nostril_R"].location[1]', index=1, action_group='nostril_R')
mouth_C_R_Y = curve.new(data_path='pose.bones["mouth_C_R"].location[1]', index=1, action_group='mouth_C_R')
mouth_C_L_Y = curve.new(data_path='pose.bones["mouth_C_L"].location[1]', index=1, action_group='mouth_C_L')
eye_offset_Y = curve.new(data_path='pose.bones["eye.offset"].location[1]', index=1, action_group='eye.offset')
eyelid_UP_L_Y = curve.new(data_path='pose.bones["eyelid_UP_L"].location[1]', index=1, action_group='eyelid_UP_L')
eyelid_UP_R_Y = curve.new(data_path='pose.bones["eyelid_UP_R"].location[1]', index=1, action_group='eyelid_UP_R')
eyelid_blink_LO_L_Y = curve.new(data_path='pose.bones["eyelid_blink_LO_L"].location[1]', index=1, action_group='eyelid_blink_LO_L')
eyelid_blink_LO_R_Y = curve.new(data_path='pose.bones["eyelid_blink_LO_R"].location[1]', index=1, action_group='eyelid_blink_LO_R')
eyelid_blink_UP_L_Y = curve.new(data_path='pose.bones["eyelid_blink_UP_L"].location[1]', index=1, action_group='eyelid_blink_UP_L')
eyelid_blink_UP_R_Y = curve.new(data_path='pose.bones["eyelid_blink_UP_R"].location[1]', index=1, action_group='eyelid_blink_UP_R')
head_L_X.keyframe_points.add(6)
head_L_Z.keyframe_points.add(6)
head_E_Y.keyframe_points.add(6)
chin_Y.keyframe_points.add(6)
lip_D_L_Y.keyframe_points.add(6)
lip_D_Y.keyframe_points.add(6)
mouth_D_L_Y.keyframe_points.add(6)
lip_D_R_Y.keyframe_points.add(6)
mouth_D_R_Y.keyframe_points.add(6)
lip_U_Y.keyframe_points.add(6)
lip_U_L_Y.keyframe_points.add(6)
mouth_U_L_Y.keyframe_points.add(6)
lip_U_R_Y.keyframe_points.add(6)
mouth_U_R_Y.keyframe_points.add(6)
brow_R_Y.keyframe_points.add(6)
brow_L_Y.keyframe_points.add(6)
brow_C_Y.keyframe_points.add(6)
brow_inner_L_Y.keyframe_points.add(6)
brow_inner_R_Y.keyframe_points.add(6)
cheek_L_Y.keyframe_points.add(6)
eyelid_LO_L_Y.keyframe_points.add(6)
nostril_L_Y.keyframe_points.add(6)
cheek_R_Y.keyframe_points.add(6)
eyelid_LO_R_Y.keyframe_points.add(6)
nostril_R_Y.keyframe_points.add(6)
mouth_C_R_Y.keyframe_points.add(6)
mouth_C_L_Y.keyframe_points.add(6)
eye_offset_Y.keyframe_points.add(6)
eyelid_UP_L_Y.keyframe_points.add(6)
eyelid_UP_R_Y.keyframe_points.add(6)
eyelid_blink_LO_L_Y.keyframe_points.add(6)
eyelid_blink_LO_R_Y.keyframe_points.add(6)
eyelid_blink_UP_L_Y.keyframe_points.add(6)
eyelid_blink_UP_R_Y.keyframe_points.add(6)

x=0
while x<34:
    i=0
    keyframe_num=5
    while i<6:
        val=random.uniform(0, 0.02)
        head_L_X.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.3)
        head_L_Z.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        head_E_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.3)
        chin_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        lip_D_L_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        lip_D_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.03)
        mouth_D_L_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        lip_D_R_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        mouth_D_R_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        lip_U_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        lip_U_L_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        mouth_U_L_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        lip_U_R_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        mouth_U_R_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        brow_R_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        brow_L_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        brow_C_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        brow_inner_L_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        brow_inner_R_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        cheek_L_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        eyelid_LO_L_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        nostril_L_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        cheek_R_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        eyelid_LO_R_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        nostril_R_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        mouth_C_R_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        mouth_C_L_Y.keyframe_points[i].co=keyframe_num, val
        val=random.uniform(0, 0.07)
        eye_offset_Y.keyframe_points[i].co=keyframe_num, val
        eyelid_UP_L_Y.keyframe_points[i].co=keyframe_num, val
        eyelid_UP_R_Y.keyframe_points[i].co=keyframe_num, val
        eyelid_blink_LO_L_Y.keyframe_points[i].co=keyframe_num, val
        eyelid_blink_LO_R_Y.keyframe_points[i].co=keyframe_num, val
        eyelid_blink_UP_L_Y.keyframe_points[i].co=keyframe_num, val
        eyelid_blink_UP_R_Y.keyframe_points[i].co=keyframe_num, val
        keyframe_num=keyframe_num+20
        i=i+1
    x=x+1
