import maya.cmds as cmds
'''
It was made to change the namespace of a mixamorig
see it in action
https://twitter.com/musto_zack/status/1517278811276075016?s=20&t=J5fLwCN1iMrZVU55qVrH-A
'''

def rename_joints(joint_namespace_input, new_namespace_input):
    joint_namespace = cmds.textField(joint_namespace_input, query=True, text=True)
    new_namespace   = cmds.textField(new_namespace_input, query=True, text=True)
    
    cmds.namespace( set=':' )   #root name space
    
    #joint_namespace = current_namespace 
    #new_namespace = new_namespace
    
    joints = cmds.ls(joint_namespace +":*") #list of all joints within the namespace 
    
    if not(cmds.namespace( exists= new_namespace )):
        cmds.namespace( add=new_namespace ) #add an new namespace
    
    for jnt in joints :    
        name = jnt.split(':') #split joint name
        cmds.rename(jnt, new_namespace+':'+name[-1]) #rename to put them in the new name space
    
    cmds.namespace(removeNamespace=joint_namespace, mergeNamespaceWithRoot=True)
    cmds.namespace( set=':' )   #root name space
    

def create_window():
    #    Create a window with a some fields for entering text.
    #
    if cmds.window("Rename Joints",exists = True):
        print("It's already created")
        return 

    mywindow = cmds.window("Rename Joints")
    cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )
    cmds.text( label='joint namespace' )
    joint_namespace_input = cmds.textField()
    cmds.text( label='new namespace' )
    new_namespace_input = cmds.textField()
    
    
    #    Attach commands to pass focus to the next field if the Enter
    #    key is pressed. Hitting just the Return key will keep focus
    #    in the current field.
    #
    cmds.textField( joint_namespace_input, edit=True, enterCommand=('cmds.setFocus(\"' + new_namespace_input + '\")') )
    cmds.textField( new_namespace_input, edit=True, enterCommand=('cmds.setFocus(\"' + joint_namespace_input + '\")') )
    
    btn_command = "rename_joints('{0}','{1}')".format(joint_namespace_input,new_namespace_input)
    
    cmds.text( label='' )
    cmds.button( label='Rename', command= btn_command )
    cmds.text( label='' )
    cmds.button( label='Close', command=('cmds.deleteUI(\"' + mywindow + '\", window=True)') )
    cmds.setParent( '..' )
    
    
    
    cmds.showWindow( mywindow )

create_window()
