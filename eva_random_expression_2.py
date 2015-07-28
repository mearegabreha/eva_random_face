import bpy
import random
selectedObj= bpy.context.object
selectedObjShapeKeys= selectedObj.data.shape_keys
selectedObjShapeKeysNameArray= selectedObjShapeKeys.key_blocks
k=0
y=0
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
        drv.type="SCRIPTED"
        var1=random.uniform(min, max)
        var=repr(var1)
        drv.expression=var
        if y==0:# the idea in this condition will create 'var' variable only if it doesn't already exist in drv.variables
            var= drv.variables.new()
            var.name="var"
            var.type="TRANSFORMS"
            y=1
    k= k + 1
