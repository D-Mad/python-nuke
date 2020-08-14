

#help(nuke.setInput)
listcur = nuke.selectedNodes()  
m = nuke.nodes.Merge(inputs=(listcur[0],listcur[1]))
m.setXpos(int(listcur[1]['xpos'].value()))
m.setYpos(int(listcur[1]['ypos'].value())+200)
i =  2
t = range(2,len(listcur))


for i in t:  
    
     
    m = nuke.nodes.Merge(inputs=(m,listcur[i])) 
    m.setXpos(int(listcur[i]['xpos'].value()))
    m.setYpos(int(listcur[1]['ypos'].value())+200)
    
    print(i)  
    i = i+1
    if i > len(listcur):
       break ; 
    
    
