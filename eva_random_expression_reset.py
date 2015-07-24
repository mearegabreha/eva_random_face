# This function resets back the Eva face back to its default expression. 
# But it has to be modified in a way that is related to setting back each shape key in a way 
import bpy
import random
selectedObj= bpy.context.object
selectedObjShapeKeys= selectedObj.data.shape_keys
selectedObjShapeKeysNameArray= selectedObjShapeKeys.key_blocks
k=0
for each in selectedObjShapeKeysNameArray:
    print(each)
    if k==0:
    #print(each)
        x=1
    else:
        min=bpy.data.shape_keys["Key.007"].key_blocks[k].slider_min # replace with k 
        max=bpy.data.shape_keys["Key.007"].key_blocks[k].slider_max # replace with k
        print(min)
        print(max)
        driverData= bpy.data.shape_keys["Key.007"].key_blocks[k].driver_add("value",-1)
        drv= driverData.driver
        var1=0.00
        var2=repr(var1)
        drv.expression=var2
    k= k + 1

  
