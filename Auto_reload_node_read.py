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

"""
 #How to install from NukeShare (nukepedia)

import Utilities

nuke.menu('Nuke').addCommand('Utilities/auto update', "Utilities.autoUpdateRead()")
nuke.menu('Nuke').addCommand('Utilities/Read/auto reload', "Utilities.autoReload()")
nuke.menu('Nuke').addCommand('Utilities/Selected/auto update', "Utilities.autoUpdateSelected()")
nuke.menu('Nuke').addCommand('Utilities/SwapAB/SwapAB', "Utilities.autoSwapAB()")
"""
