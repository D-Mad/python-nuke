import nuke 
import nukescripts 

#auto update Read node
def autoUpdateRead():
    for node in nuke.allNodes():
        if node.Class() == "Read": 
           node['selected'].setValue(True)
           node.knob('localizationPolicy').setValue('on')
           node.knob("updateLocalization").execute()
           node.knob("reload").execute()

#auto update with selected
def autoUpdateSelected():
    for node in nuke.selectedNodes():
        if node.Class() == "Read" :
           node['selected'].setValue(True)
           node.knob('localizationPolicy').setValue('on')
           node.knob("updateLocalization").execute()
           node.knob("reload").execute()
               
#Auto reload file read
def autoReload():   
    for node in nuke.allNodes():
       if node.Class() == "Read": 
          node['selected'].setValue(True)
          node.knob('localizationPolicy').setValue('off')
          node.knob("reload").execute()


#auto swap
def autoSwapAB():
    names = [];
    a =  nuke.selectedNodes();
    for s in a:
     n = s['name'].value();
     names.append(n);
    i = 0;
    for i in range(0,len(a)):
     p = nuke.toNode(names[i]);
     p.knob('selected').setValue(True);
     nukescripts.swapAB(nuke.selectedNode());
     p.knob('selected').setValue(False);
     i = i+1;
     if i > len(a) :
       break;
       
       
       
       
       
       
       
#position node       
def scaleNodes(scalex,scaley):
    nodes = nuke.selectedNodes()    # GET SELECTED NODES
    amount = len( nodes )    # GET NUMBER OF SELECTED NODES
    if amount == 0:    return # DO NOTHING IF NO NODES WERE SELECTED

    allX = sum( [ n.xpos()+n.screenWidth()/2 for n in nodes ] )  # SUM OF ALL X VALUES
    allY = sum( [ n.ypos()+n.screenHeight()/2 for n in nodes ] ) # SUM OF ALL Y VALUES

    # CENTER OF SELECTED NODES
    centreX = allX / amount
    centreY = allY / amount

    # REASSIGN NODE POSITIONS AS A FACTOR OF THEIR DISTANCE TO THE SELECTION CENTER
    for n in nodes:
        n.setXpos( centreX + ( n.xpos() - centreX ) * (scalex) )
        n.setYpos( centreY + ( n.ypos() - centreY ) * (scaley) )




def autoMerge():

    listcur = nuke.selectedNodes()
    print(listcur)
  
    m = nuke.nodes.Merge(inputs=(listcur[0],listcur[1]))
    i =  2
    t = range(2,len(listcur))

    m.knob('selected').setValue(True)
    nukescripts.swapAB(nuke.selectedNode())
    for i in t:  
    
     
        m = nuke.nodes.Merge(inputs=(m,listcur[i])) 
        m.knob('selected').setValue(True)
        nukescripts.swapAB(nuke.selectedNode())
    
    
        i = i+1
        if i > len(listcur):
           break ; 
    scaleNodes(1,2)        
    
    
     

"""
 #How to install from NukeShare (nukepedia)

import Utilities

nuke.menu('Nuke').addCommand('Utilities/auto update', "Utilities.autoUpdateRead()")
nuke.menu('Nuke').addCommand('Utilities/Read/auto reload', "Utilities.autoReload()")
nuke.menu('Nuke').addCommand('Utilities/Selected/auto update', "Utilities.autoUpdateSelected()")
nuke.menu('Nuke').addCommand('Utilities/SwapAB/SwapAB', "Utilities.autoSwapAB()")
nuke.menu('Nuke').addCommand('Utilities/AutoMerge/AutoMerge', "Utilities.autoMerge()")
"""
