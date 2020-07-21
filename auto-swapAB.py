import nuke 
import nukescripts 

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
   
