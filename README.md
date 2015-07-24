# insert the following function definition in the commands.py of the Eva's rigControl directory
# this function calls the random facial expression generator .py script

    def setRandomface(self):
        text= bpy.data.texts.load('/home/meareg/eva_random/Eva_random_expression.py') # here put the file path of the python script generator
        ctx = bpy.context.copy()
        ctx['edit_text'] = text
        bpy.ops.text.run_script(ctx)   
        return 0

# this function calls the randomly generated facial expression resetter .py script

 # to reset back the random facial expression generated (to default facial expression)
    def resetRandomface(self):
        text= bpy.data.texts.load('/home/meareg/eva_random/Eva_random_expression_reset.py')
        ctx = bpy.context.copy()
        ctx['edit_text'] = text
        bpy.ops.text.run_script(ctx)
        return 0

# insert the following lines into the blenderUI.py of the Eva's rigControl directory

# custom buttons which execute the setRandomface() and resetRandomfce() functions we defined in the commands.py file 

col.operator('eva.debug', text = 'Generate Random Expression').action =  'commands.EvaAPI().setRandomface()'
col.operator('eva.debug', text = 'Reset Random Expression').action =  'commands.EvaAPI().resetRandomface()'


