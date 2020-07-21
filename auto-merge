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






#help(nuke.setInput)
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
    
    print(i)  
    i = i+1
    if i > len(listcur):
       break ; 
    
    
scaleNodes(2,7)
