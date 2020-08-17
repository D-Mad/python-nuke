#help(nuke.setInput)
listcur = nuke.selectedNodes()
print listcur
swapped = True
while swapped: 
      swapped = False
      for i in range(len(listcur)-1):
          if(int(listcur[i]['xpos'].value())) > (int(listcur[i+1]['xpos'].value())): 
                listcur[i],listcur[i+1]  =  listcur[i+1],listcur[i]
                swapped = True 
 
print listcur
m = nuke.nodes.Merge(inputs=(listcur[0],listcur[1]))
m.knob('operation').setValue('plus')
m.setXpos(int(listcur[1]['xpos'].value()))
m.setYpos(int(listcur[1]['ypos'].value())+200)
  
i =  2
t = range(2,len(listcur)) 
for i in t: 

       m = nuke.nodes.Merge(inputs=(m,listcur[i]))
       m.knob('operation').setValue('plus') 
       m.setXpos(int(listcur[i]['xpos'].value()))
       m.setYpos(int(listcur[1]['ypos'].value())+200)
    
      
       i = i+1
       if i > len(listcur):
        break ; 
    
