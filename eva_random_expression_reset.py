# This function resets back the Eva face back to its default expression. 
# But it has to be modified in a way that is related to setting back each shape key in a way 
import bpy
import random
from array import array
from numpy import ndarray
#selectedObj= bpy.context.object
selectedObj= bpy.data.objects['Eva']
selectedObjShapeKeys= selectedObj.data.shape_keys
selectedObjShapeKeysNameArray= selectedObjShapeKeys.key_blocks
k=0
#drv=[50]
drv = ndarray((40,),int)
#drv = ndarray.empty(40, dtype=object)
#drv = [None] * 40
expr1="50*var"
expr2="-50*var"
expr3="(50*fine) + (50*gross)"
expr4="(-50*fine) + (-50*gross)"
expr5="((-50*flare) + ((-50*blink) * (1 - (-50*flare))))"
expr6="-1*((-50*flare) + ((-50*blink) * (1 - (-50*flare))))"
expr7="((eyes - 0.757) - (head - 0.552)) * -3 -0.002"
expr8="((eyes - 0.778) - (head - 0.554)) * 3"   
bpy.data.shape_keys['Key.007'].key_blocks["lip-UP.C"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["lip.UP.L"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["lip.UP.R"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["lip.DN.C"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["lip.DN.L"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["lip.DN.R"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["lips-wide.L"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["lips-wide.R"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["lips-narrow.L"].driver_add("value",-1).driver.expression=expr2
bpy.data.shape_keys['Key.007'].key_blocks["lips-narrow.R"].driver_add("value",-1).driver.expression=expr2
bpy.data.shape_keys['Key.007'].key_blocks["brow_center_UP"].driver_add("value",-1).driver.expression=expr3
bpy.data.shape_keys['Key.007'].key_blocks["brow_inner_UP.L"].driver_add("value",-1).driver.expression=expr3
bpy.data.shape_keys['Key.007'].key_blocks["brow_inner_UP.R"].driver_add("value",-1).driver.expression=expr3
bpy.data.shape_keys['Key.007'].key_blocks["brow_outer_UP.L"].driver_add("value",-1).driver.expression=expr3
bpy.data.shape_keys['Key.007'].key_blocks["brow_center_DN"].driver_add("value",-1).driver.expression=expr4
bpy.data.shape_keys['Key.007'].key_blocks["brow_inner_DN.L"].driver_add("value",-1).driver.expression=expr4
bpy.data.shape_keys['Key.007'].key_blocks["brow_outer_DN.R"].driver_add("value",-1).driver.expression=expr4
bpy.data.shape_keys['Key.007'].key_blocks["eye-blink.UP.L"].driver_add("value",-1).driver.expression=expr5
bpy.data.shape_keys['Key.007'].key_blocks["eye-blink.LO.L"].driver_add("value",-1).driver.expression=expr5
bpy.data.shape_keys['Key.007'].key_blocks["eye-blink.UP.R"].driver_add("value",-1).driver.expression=expr5
bpy.data.shape_keys['Key.007'].key_blocks["eye-blink.LO.R"].driver_add("value",-1).driver.expression=expr5
bpy.data.shape_keys['Key.007'].key_blocks["eye-flare.UP.L"].driver_add("value",-1).driver.expression=expr6
bpy.data.shape_keys['Key.007'].key_blocks["eye-flare.LO.L"].driver_add("value",-1).driver.expression=expr6
bpy.data.shape_keys['Key.007'].key_blocks["eye-flare.UP.R"].driver_add("value",-1).driver.expression=expr6
bpy.data.shape_keys['Key.007'].key_blocks["eye-flare.LO.R"].driver_add("value",-1).driver.expression=expr6
bpy.data.shape_keys['Key.007'].key_blocks["eyes-look.dn"].driver_add("value",-1).driver.expression=expr7
bpy.data.shape_keys['Key.007'].key_blocks["eyes-look.up"].driver_add("value",-1).driver.expression=expr8
bpy.data.shape_keys['Key.007'].key_blocks["wince.L"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["wince.R"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["sneer.L"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["sneer.R"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["lips-frown.L"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["lips-frown.R"].driver_add("value",-1).driver.expression=expr1
bpy.data.shape_keys['Key.007'].key_blocks["lips-smile.L"].driver_add("value",-1).driver.expression=expr1 
bpy.data.shape_keys['Key.007'].key_blocks["brow_outer_up.R"].driver_add("value",-1).driver.expression=expr4
bpy.data.shape_keys['Key.007'].key_blocks["brow_inner_DN.R"].driver_add("value",-1).driver.expression=expr4
bpy.data.shape_keys['Key.007'].key_blocks["brow_outer_DN.L"].driver_add("value",-1).driver.expression=expr1

  
