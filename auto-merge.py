#help(nuke.setInput)
listcur = nuke.selectedNodes()  
 
if(int(listcur[0]['xpos'].value())) >  (int(listcur[len(listcur)-1]['xpos'].value())):
   n = nuke.nodes.Merge(inputs=(listcur[len(listcur)-1],listcur[len(listcur)-2]))
   n.setXpos(int(listcur[len(listcur)-2]['xpos'].value()))
   n.setYpos(int(listcur[len(listcur)-2]['ypos'].value())+200)
   k = 0
   t1= range(0,len(listcur)-2)
   for  k in t1:
     n = nuke.nodes.Merge(inputs=(n,listcur[len(listcur)-3-k])) 
     n.setXpos(int(listcur[len(listcur)-3-k]['xpos'].value()))
     n.setYpos(int(listcur[len(listcur)-2]['ypos'].value())+200)
     k = k+1
     if k > (len(listcur)-2):
        break ;          
else:
    m = nuke.nodes.Merge(inputs=(listcur[0],listcur[1]))
    m.setXpos(int(listcur[1]['xpos'].value()))
    m.setYpos(int(listcur[1]['ypos'].value())+200)
  
    i =  2
    t = range(2,len(listcur)) 
    for i in t: 

       m = nuke.nodes.Merge(inputs=(m,listcur[i])) 
       m.setXpos(int(listcur[i]['xpos'].value()))
       m.setYpos(int(listcur[1]['ypos'].value())+200)
    
      
       i = i+1
       if i > len(listcur):
        break ; 
    
