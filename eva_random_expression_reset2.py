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
        shape_key1 = bpy.data.shape_keys['Key.007'].key_blocks["lips-smile.R"].driver_add("value",-1)
        shape_key2 = bpy.data.shape_keys['Key.007'].key_blocks["lip-UP.C"].driver_add("value",-1)
        shape_key3 = bpy.data.shape_keys['Key.007'].key_blocks["lip.UP.L"].driver_add("value",-1)
        shape_key4 = bpy.data.shape_keys['Key.007'].key_blocks["lip.UP.R"].driver_add("value",-1)
        shape_key5 = bpy.data.shape_keys['Key.007'].key_blocks["lip.DN.C"].driver_add("value",-1)
        shape_key6 = bpy.data.shape_keys['Key.007'].key_blocks["lip.DN.L"].driver_add("value",-1)
        shape_key7 = bpy.data.shape_keys['Key.007'].key_blocks["lip.DN.R"].driver_add("value",-1)
        shape_key8 = bpy.data.shape_keys['Key.007'].key_blocks["lips-wide.L"].driver_add("value",-1)
        shape_key9 = bpy.data.shape_keys['Key.007'].key_blocks["lips-wide.R"].driver_add("value",-1)
        shape_key10 = bpy.data.shape_keys['Key.007'].key_blocks["lips-narrow.L"].driver_add("value",-1)
        shape_key11 = bpy.data.shape_keys['Key.007'].key_blocks["lips-narrow.R"].driver_add("value",-1)
        shape_key12 = bpy.data.shape_keys['Key.007'].key_blocks["brow_center_UP"].driver_add("value",-1)
        shape_key13 = bpy.data.shape_keys['Key.007'].key_blocks["brow_inner_UP.L"].driver_add("value",-1)
        shape_key14 = bpy.data.shape_keys['Key.007'].key_blocks["brow_inner_UP.R"].driver_add("value",-1)
        shape_key15 = bpy.data.shape_keys['Key.007'].key_blocks["brow_outer_UP.L"].driver_add("value",-1)
        shape_key16 = bpy.data.shape_keys['Key.007'].key_blocks["brow_center_DN"].driver_add("value",-1)
        shape_key17 = bpy.data.shape_keys['Key.007'].key_blocks["brow_inner_DN.L"].driver_add("value",-1)
        shape_key18 = bpy.data.shape_keys['Key.007'].key_blocks["brow_outer_DN.R"].driver_add("value",-1)
        shape_key19 = bpy.data.shape_keys['Key.007'].key_blocks["eye-blink.UP.L"].driver_add("value",-1)
        shape_key20 = bpy.data.shape_keys['Key.007'].key_blocks["eye-blink.LO.L"].driver_add("value",-1)
        shape_key21 = bpy.data.shape_keys['Key.007'].key_blocks["eye-blink.UP.R"].driver_add("value",-1)
        shape_key22 = bpy.data.shape_keys['Key.007'].key_blocks["eye-blink.LO.R"].driver_add("value",-1)
        shape_key23 = bpy.data.shape_keys['Key.007'].key_blocks["eye-flare.UP.L"].driver_add("value",-1)
        shape_key24 = bpy.data.shape_keys['Key.007'].key_blocks["eye-flare.LO.L"].driver_add("value",-1)
        shape_key25 = bpy.data.shape_keys['Key.007'].key_blocks["eye-flare.UP.R"].driver_add("value",-1)
        shape_key26 = bpy.data.shape_keys['Key.007'].key_blocks["eye-flare.LO.R"].driver_add("value",-1)
        shape_key27 = bpy.data.shape_keys['Key.007'].key_blocks["eyes-look.dn"].driver_add("value",-1)
        shape_key28 = bpy.data.shape_keys['Key.007'].key_blocks["eyes-look.up"].driver_add("value",-1)
        shape_key29 = bpy.data.shape_keys['Key.007'].key_blocks["wince.L"].driver_add("value",-1)
        shape_key30 = bpy.data.shape_keys['Key.007'].key_blocks["wince.R"].driver_add("value",-1)
        shape_key31 = bpy.data.shape_keys['Key.007'].key_blocks["sneer.L"].driver_add("value",-1)
        shape_key32 = bpy.data.shape_keys['Key.007'].key_blocks["sneer.R"].driver_add("value",-1) 
        shape_key33 = bpy.data.shape_keys['Key.007'].key_blocks["lips-frown.L"].driver_add("value",-1) 
        shape_key34 = bpy.data.shape_keys['Key.007'].key_blocks["lips-frown.R"].driver_add("value",-1) 
        shape_key35 = bpy.data.shape_keys['Key.007'].key_blocks["lips-smile.L"].driver_add("value",-1) 
        shape_key36 = bpy.data.shape_keys['Key.007'].key_blocks["brow_outer_up.R"].driver_add("value",-1)
        shape_key37 = bpy.data.shape_keys['Key.007'].key_blocks["brow_inner_DN.R"].driver_add("value",-1) 
        shape_key38 = bpy.data.shape_keys['Key.007'].key_blocks["brow_outer_DN.L"].driver_add("value",-1) 
        drv1=shape_key1.driver
        drv2=shape_key2.driver
        drv3=shape_key3.driver
        drv4=shape_key4.driver
        drv5=shape_key5.driver
        drv6=shape_key6.driver
        drv7=shape_key7.driver
        drv8=shape_key8.driver
        drv9=shape_key9.driver
        drv10=shape_key10.driver
        drv11=shape_key11.driver
        drv12=shape_key12.driver
        drv13=shape_key13.driver
        drv14=shape_key14.driver
        drv15=shape_key15.driver
        drv16=shape_key16.driver
        drv17=shape_key17.driver
        drv18=shape_key18.driver
        drv19=shape_key19.driver
        drv20=shape_key20.driver
        drv21=shape_key21.driver
        drv22=shape_key22.driver
        drv23=shape_key23.driver
        drv24=shape_key24.driver
        drv25=shape_key25.driver
        drv26=shape_key26.driver
        drv27=shape_key27.driver
        drv28=shape_key28.driver
        drv29=shape_key29.driver
        drv30=shape_key30.driver
        drv31=shape_key31.driver
        drv32=shape_key32.driver
        drv33=shape_key33.driver
        drv34=shape_key34.driver
        drv35=shape_key35.driver
        drv36=shape_key36.driver
        drv37=shape_key37.driver
        drv38=shape_key38.driver      

        drv1.expression="50*var"
        drv2.expression="50*var"       
        drv3.expression="50*var"        
        drv4.expression="50*var" 
        drv5.expression="50*var" 
        drv6.expression="50*var" 
        drv7.expression="50*var" 
        drv8.expression="50*var"        
        drv9.expression="50*var"
        drv10.expression="-50*var"
        drv11.expression="-50*var"
        drv12.expression="(50*fine) + (50*gross)"
        drv13.expression="(50*fine) + (50*gross)" 
        drv14.expression="(50*fine) + (50*gross)"      
        drv15.expression="(50*fine) + (50*gross)"        
        drv16.expression="(-50*fine) + (-50*gross)"
        drv17.expression="(-50*fine) + (-50*gross)"
        drv18.expression="(-50*fine) + (-50*gross)"
        drv19.expression="((-50*flare) + ((-50*blink) * (1 - (-50*flare))))"
        drv20.expression="((-50*flare) + ((-50*blink) * (1 - (-50*flare))))"
        drv21.expression="((-50*flare) + ((-50*blink) * (1 - (-50*flare))))"
        drv22.expression="((-50*flare) + ((-50*blink) * (1 - (-50*flare))))"
        drv23.expression="-1*((-50*flare) + ((-50*blink) * (1 - (-50*flare))))"
        drv24.expression="-1*((-50*flare) + ((-50*blink) * (1 - (-50*flare))))"        
        drv25.expression="-1*((-50*flare) + ((-50*blink) * (1 - (-50*flare))))"        
        drv26.expression="-1*((-50*flare) + ((-50*blink) * (1 - (-50*flare))))"
        drv27.expression="((eyes - 0.757) - (head - 0.552)) * -3 -0.002"
        drv28.expression="((eyes - 0.778) - (head - 0.554)) * 3" 
        drv29.expression="50*var"
        drv30.expression="50*var"        
        drv31.expression="50*var"
        drv32.expression="50*var"
        drv33.expression="50*var"
        drv34.expression="50*var"
        drv35.expression="50*var"
        drv36.expression="(-50*fine) + (-50*gross)"
        drv37.expression="(-50*fine) + (-50*gross)"
        drv38.expression="50*var"
    k= k + 1

#brow_inner_UP brow_outer_UP brow_center_D brow_inner_DN brow_outer_DN (50*fine) + (50*gross)
#eye-blink.UP.L eye-blink.LO.L eye-blink.UP.R   ((-50*flare) + ((-50*blink) * (1 - (-50*flare))))
# eye-flare.LO.R eye-flare.UP.L eye-flare.LO.L eye-flare.UP.R eye-flare.LO.R -1*((-50*flare) + ((-50*blink) * (1 - (-50*flare))))
# eyes-look.dn ((eyes - 0.757) - (head - 0.552)) * -3 -0.002
# eyes-look.up ((eyes - 0.778) - (head - 0.554)) * 3

#drv33=shape_key33.driver                       
#drv= driverData.driver
#var1 =0.0 
# var22 =0.01
# fine1=0.0
# gross1=0.0
# eyes1=0.0
# head1=0.0
# flare1=0.0
# blink1=0.0
# var=repr(var1)
# var2=repr(var22)
# fine=repr(fine1)
#gross=repr(gross1)
#eyes=repr(eyes1)
#head=repr(head1)
#flare=repr(flare1)
#blink=repr(blink1)
#drv.expression= 50*var


