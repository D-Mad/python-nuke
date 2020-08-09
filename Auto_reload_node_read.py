#Auto reload file read
for node in nuke.allNodes():
    
    if node.Class() == "Read": 
        node['selected'].setValue(True)
        node.knob('localizationPolicy').setValue('off')
        node.knob("reload").execute()
