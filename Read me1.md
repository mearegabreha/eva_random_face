###Highlight on Eva's armature structure###
Control armature
A set of bones that are related to a set of actions which their names start with 'EMO-'. such as 'EMO-happy', 'EMO-surprised' etc.
Deform armature
A set of bones which control the head, eye and and specifically the facial bones by driving the shape keys which directly drive/control the parts of the face mesh.

###Random facial expression were derived through a python script, Eva_random_action_generator.py script###
A python script that generates an action,adds curves, adds key frame points
Adds an action:
We can name an action anything we like but following some Eva's blender_api specific naming styles would be good specially if we want the action to be called from a button. 
So giving the action a unique name but one that starts with 'GST-' would create an action that can be added, automatically, to the gesture buttons in the blender UI.  

Adds an array of curves to the deform armature. Each curve is related to a single bone in the deform armature.
Adds a data_path to the curves. The data_path refers to a specific bone in the deform armature. Since the shape keys, which directly control the face mesh, are driven by values of bones in the deform armature.
Adds a set of key frame points to each curve.

key frame points have two coordinates which refer to the number of keyframe point position and the value of the keyframe point in their index order respectively.
So the set of inserted keyframe/control points' values are assigned random values by using the python's random function which the value on the first index would indicate the length of keyframe points inserted.
These random values would create a randomized expression on the face.


 
