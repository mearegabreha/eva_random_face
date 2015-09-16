import bpy
bpy.context.object
'''rate1_val = bpy.data.scenes['Scene'].rate1
rate2_val = bpy.data.scenes['Scene'].rate2
rate3_val = bpy.data.scenes['Scene'].rate3
rate4_val = bpy.data.scenes['Scene'].rate4
rate5_val = bpy.data.scenes['Scene'].rate5
rate6_val = bpy.data.scenes['Scene'].rate6
rate7_val = bpy.data.scenes['Scene'].rate7
rate8_val = bpy.data.scenes['Scene'].rate8
rate9_val = bpy.data.scenes['Scene'].rate9
rate10_val = bpy.data.scenes['Scene'].rate10
rate11_val = bpy.data.scenes['Scene'].rate11
rate12_val = bpy.data.scenes['Scene'].rate12'''

rate1_val = 10 # bpy.data.scenes['Scene'].rate1
rate2_val = 2 #bpy.data.scenes['Scene'].rate2
rate3_val = 3 #bpy.data.scenes['Scene'].rate3
rate4_val = 10 #bpy.data.scenes['Scene'].rate4
rate5_val = 1 #bpy.data.scenes['Scene'].rate5
rate6_val = 1 #bpy.data.scenes['Scene'].rate6
rate7_val = 10 #bpy.data.scenes['Scene'].rate7
rate8_val = 2 #bpy.data.scenes['Scene'].rate8
rate9_val = 1 #bpy.data.scenes['Scene'].rate9
rate10_val = 3 #bpy.data.scenes['Scene'].rate10
rate11_val = 10 #bpy.data.scenes['Scene'].rate11
rate12_val = 10 #bpy.data.scenes['Scene'].rate12

items_dict = {'rate1_val':rate1_val,'rate2_val':rate2_val,'rate3_val':rate3_val,'rate4_val':rate4_val,'rate5_val':rate5_val,'rate6_val':rate6_val,'rate7_val':rate7_val,'rate8_val':rate8_val,'rate9_val':rate9_val,'rate10_val':rate10_val,'rate11_val':rate11_val,'rate12_val':rate12_val}
items_name = ['rate1_val','rate2_val','rate3_val','rate4_val','rate5_val','rate6_val','rate7_val','rate8_val','rate9_val','rate10_val','rate11_val','rate12_val']

items_val = [rate1_val, rate2_val, rate3_val, rate4_val, rate5_val, rate6_val, rate7_val, rate8_val, rate9_val,rate10_val, rate11_val, rate12_val]

items_val.sort() #it sorts it in descending order
par_selected = []
par_values = []

par_array = []
#par_dict = {}
array_val = [rate1_val, rate2_val, rate3_val, rate4_val, rate5_val, rate6_val, rate7_val, rate8_val, rate9_val, rate10_val,rate11_val, rate12_val]
array_name=['par1', 'par2', 'par3', 'par4', 'par5', 'par6', 'par7', 'par8', 'par9', 'par10', 'par11', 'par12']
#i=0
for items in range(0, len(array_val)):

    if 1 <= array_val[items] <= 6:
        #par_array[par_selected[items]] = array_val[items]
        par_values.append(array_val[items])
#par_values.sort()
        #i+=1
#par_dict[array_name[items]] = array_val# not necessary if we are to declare a dictionary below anyways

#par_array.sort()
p1= 10
p2= 10
p3= 10
p4= 10
p5= 10
p6= 10
p7= 10
p8= 10
p9= 10
p10= 10
p11= 10
p12= 10

array_p_str = []
array_p_val = []
par_dict={'par1': rate1_val, 'par2': rate2_val, 'par3': rate3_val, 'par4':rate4_val, 'par5':rate5_val, 'par6':rate6_val, 'par7':rate7_val, 'par8':rate8_val,'par9': rate9_val, 'par10': rate10_val, 'par11': rate11_val, 'par12': rate12_val}
par_dict_selected = {}
#count the members of the array; to know how often they repeat
for i in range(0, len(par_values)):
    if par_values[i] == par_dict['par1'] and p1 == 10:
        par_dict_selected['par1'] = rate1_val
        p1=i+1
        array_p_val.append(p1)
        array_p_str.append('p1')
        print ('p1')
        print (p1)


    if par_values[i] == par_dict['par2'] and p2 == 10:
        par_dict_selected['par2'] = rate2_val
        p2=i+1
        array_p_val.append(p2)
        array_p_str.append('p2')
        print ('p2')
        print (p2)
    if par_values[i] == par_dict['par3'] and p3 == 10:
        par_dict_selected['par3'] = rate3_val
        p3=i+1
        array_p_val.append(p3)
        array_p_str.append('p3')
        print ('p3')
        print (p3)


    if par_values[i] == par_dict['par4'] and p4 == 10:
        par_dict_selected['par4'] = rate4_val
        p4=i+1
        array_p_val.append(p4)
        array_p_str.append('p4')
        print ('p4')
        print (p4)


    if par_values[i] == par_dict['par5'] and p5 == 10:
        par_dict_selected['par5'] = rate5_val
        p5=i+1
        array_p_val.append(p5)
        array_p_str.append('p5')
        print ('p5')
        print (p5)

    if par_values[i] == par_dict['par6'] and p6 == 10:
        par_dict_selected['par6'] = rate6_val
        p6=i+1
        array_p_val.append(p6)
        array_p_str.append('p6')
        print ('p6')
        print (p6)


    if par_values[i] == par_dict['par7'] and p7 == 10:
        par_dict_selected['par7'] = rate7_val
        p7=i+1
        array_p_val.append(p7)
        array_p_str.append('p7')
        print ('p7')
        print (p7)


    if par_values[i] == par_dict['par8'] and p8 == 10:
        par_dict_selected['par8'] = rate8_val
        p8=i+1
        array_p_val.append(p8)
        array_p_str.append('p8')
        print ('p8')
        print (p8)

    if par_values[i] == par_dict['par9'] and p9 == 10:
        par_dict_selected['par9'] = rate9_val
        p9=i+1
        array_p_val.append(p9)
        array_p_str.append('p9')
        print ('p9')
        print (p9)

    if par_values[i] == par_dict['par10'] and p10 == 10:
        par_dict_selected['par10'] = rate10_val
        p10=i+1
        array_p_val.append(p10)
        array_p_str.append('p10')
        print ('p10')
        print (p10)


    if par_values[i] == par_dict['par11'] and p11 == 10:
        par_dict_selected['par11'] = rate11_val
        p11=i+1
        array_p_val.append(p11)
        array_p_str.append('p11')
        print ('p11')
        print (p11)


    if par_values[i] == par_dict['par12'] and p12 == 10:
        par_dict_selected['par12'] = rate12_val
        p12=i+1
        array_p_val.append(p12)
        array_p_str.append('p12')
        print ('p12')
        print (p12)

action1='action1'
action2='action2'
action3='action3'
action4='action4'
action5='action5'
action6='action6'
action7='action7'
action8='action8'
action9='action9'
action10='action10'
action11='action11'
action12='action12'
print ('array_p_val')
print (array_p_val)
print ('array_p_str')
print (array_p_str)
array_parents = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12']
actions_str = ['action1', 'action2', 'action3','action4', 'action5', 'action6', 'action7', 'action8', 'action9', 'action10', 'action11', 'action12']
array_actions_rated = []
for i in range(0, len(array_p_str)):
    for j in range(0, len(array_parents)):
        if array_p_str[i] == array_parents[j]:
            array_actions_rated.append(actions_str[j])

print ('array_actions_rated')
print (array_actions_rated)

#act1 = bpy.data.actions[GST-amused]

action_rated = []

array_p = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
array_p.sort()
count_rate = []
count_arr = []
for j in range(0, 6):
    for i in range(0, len(array_p_val)):
        count_var = array_p_val.count(j)
    if count_var > 0:
        count_arr.append(count_var)

print ('count_arr')
print (count_arr)
a = 0
b = 0
exp1 = bpy.data.actions['GST-amused']
exp2 = bpy.data.actions['GST-nod-1']
exp3 = bpy.data.actions['GST-nod-2']
exp4 = bpy.data.actions['GST-shake-3']
exp5 = bpy.data.actions['GST-blink-sleepy']
exp6 = bpy.data.actions['GST-blink-relaxed']
exp7 = bpy.data.actions['GST-blink-micro']
exp8 = bpy.data.actions['GST-thoughtful']
exp9 = bpy.data.actions['GST-yawn-1']
exp10 = bpy.data.actions['GST-shake-2']
exp11 = bpy.data.actions['GST-blink']
exp12 = bpy.data.actions['GST-nod-3']

expression_list = [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9, exp10, exp11, exp12]

expression_rated_array = []
#for i in range(0, len(count_arr)):
cc = len(count_arr)
print ('cc')
print (cc)
#cc = count_arr[i] #4,2,2
#lists the expressions that were rated by user
for act in range(0, len(array_actions_rated)):
    for i in range(0, len(actions_str)):
        if array_actions_rated[act] == actions_str[i]:
    #act1 = 'bpy.data.actions[\'GST-amused\']'
            act1 = expression_list[i]
            expression_rated_array.append(act1)

print ('expression_rated_array')
print (expression_rated_array)
#print(expression_list)
        #  else if array_actions_rated[act] == 'action2':
        #     act2 = bpy.data.actions['GST-amused']
        #
        #
#cross over function
action_counter = 0
while a < len(array_actions_rated):
    print ('expression')
    print (len(array_actions_rated))
    print (expression_rated_array[a])
    print (expression_rated_array[a+1])
    #print (expression_rated_array[0].fcurves[4].keyframe_points.items())
    print (len(expression_rated_array[a].fcurves.items()))
    print (len(expression_rated_array[1].fcurves[0].keyframe_points.items()))
    #print (expression_rated_array[1])
    #a +=1
    #print(bpy.data.actions['GST-amused'].fcurves.items())
    b += 1
    f = 0
    c = 0
    #while b < len(array_actions_rated) and action_counter < 12:
    for i in range(0, len(expression_rated_array[a].fcurves.items())):
        for j in range(0, action[a+1].fcurves.items()):
            for j in range(0, len(expression_rated_array[a].fcurves[i].keyframe_points.items())):
                for m in range(0, len(action[a].fcurves[i].keyframe_points.items())):
                    for n in range(0, len(action[a+1].fcurves[j].items())):
                        
                

               
                if action[a].fcurves[i].datapath == action[a+1].fcurves[j].datapath:
                    if c % 2 == 0:
                        keyframe = action[a+1].fcurves[i].keyframe_points[m].co[0]
                        val = action[a+1].fcurves[i].keyframe_points[m].co[1]
                        action[a].fcurves[i].keyframe_points[m].co == keyframe, val
                #controlpoint_no = expression_rated_array[a].fcurves[i].keyframe_points[j-1].co[0]
                #controlpoint_val = expression_rated_array[a].fcurves[i].keyframe_points[j-1].co[1]
                controlpointnew_no = expression_rated_array[a].fcurves[i].keyframe_points[j].co[0]
                controlpointnew_val = expression_rated_array[a].fcurves[i].keyframe_points[j].co[1]
                print (expression_rated_array[a].fcurves[i].keyframe_points[j].co[0])
                print (expression_rated_array[a].fcurves[i].keyframe_points[j].co[1])
                #print (expression_rated_array[b].fcurves[10])          
               #values here would automatically change the actions in blender
               
                #expression_rated_array[a].fcurves[i].keyframe_points[j-1].co[0] = controlpoint_no
                #expression_rated_array[a].fcurves[i].keyframe_points[j-1].co[1] = controlpoint_val
                
                #print ('controlpoint_no')
                #print (controlpoint_no)
                #print ('controlpoint_val')
                #print (controlpoint_val)
                #expression_rated_array[a].fcurves[i].keyframe_points[j].co[0] = controlpointnew_no 
                expression_rated_array[a].fcurves[i].keyframe_points[j].co[1] = controlpointnew_val + 0.02
                f = f +10
      
               action_counter += 1
               b += 1
    a += 1
#a = 0



