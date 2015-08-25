'''Insert the specific action's name('GST-happy-new'), the specific control points (keyframes_points[2])
 of the arrray curves.'''
import bpy
import random
x=3
while x<32:
    cp_val1=bpy.data.actions['GST-happy-new'].fcurves[x].keyframe_points[2].co[1]=random.uniform(0,0.02)
    cp_val2=bpy.data.actions['GST-happy-new'].fcurves[x].keyframe_points[3].co[1]=random.uniform(0,0.02)
    x=x+1
    print (cp_val1) 
    print (cp_val1)    
