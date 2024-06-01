import hou
import os

# -------NODE-DECLARATION----------------------------------------------------#
class create_node:
    def __init__(self, nr:int = 3):
        self.nr = nr
    
    def create(self,def_node, name_node):
        return geo.createNode(def_node, name_node)
       
    def create_bool(self, name_node, def_node = "boolean::2.0"):
        return geo.createNode(def_node, name_node)
       
    def create_cal(self, name_node, def_node = "color", r=1, g=1, b=1):
        cal = geo.createNode(def_node, name_node)
        cal.setParms({"colorr":r, "colorg":g, "colorb":b})
        return cal     
        
    def __str__(self):
        return f"This class contains {self.nr} instances for node creation."
        
def create_clock_base(node_name = "circle"):
    global circle, scaleParm_circle
    def extrude_base(node_name = "extrude"):
        global baseVolume, distParm_base
        baseVolume = geo.createNode("polyextrude::2.0", node_name)
        distParm_base = baseVolume.parm("dist")
        closeCap = baseVolume.parm("outputback")
        distParm_base.set(0.25)
        closeCap.set(1)
           
    circle = geo.createNode("circle",node_name)
    circle.setParms({"rx":90, "ry":0, "rz":0}) 
    scaleParm_circle = circle.parm("scale")
    typeParm_circle = circle.parm("type")
    divsParm_circle = circle.parm("divs")
    typeParm_circle.set(1)
    divsParm_circle.set(48)
    extrude_base()

def create_hr_element(node_name = "box"): 
    global box
    box = geo.createNode("box", node_name) 
    box.setParms({"sizex":1, "sizey":1, "sizez":1})
    sizeParmY_box = box.parm("sizey")
    sizeParmZ_box = box.parm("sizez")
    centerParmY_box = box.parm("ty").set(sizeParmY_box.eval()*0.5) # starting position declar.
    centerParmZ_box = box.parm("tz").set(sizeParmZ_box.eval()*0.5)

def create_hand_element(node_name = "box"):
    global hand
    hand = geo.createNode("box", node_name)
    hand.setParms({"sizex":1, "sizey":1, "sizez":1})
    sizeParmX_hand = hand.parm("sizex")
    sizeParmY_hand = hand.parm("sizey")
    centerParmX_hand = hand.parm("tx").set(sizeParmX_hand.eval()*0.5)
    centerParmY_hand = hand.parm("ty").set(sizeParmY_hand.eval()*0.5)
    
def transform_hr_element(node_name = "transform1"):
    global boxes
    boxes = geo.createNode("xform", node_name) 
    boxes.setParms({"sx":0.1, "sy":0.05, "sz":0.1}) 
    heightBox = boxes.parm("ty")
    heightBox.set(distParm_base)
    
def create_hr_elements(node_name = "copyPoints"):
    global copyPoints
    copyPoints = geo.createNode("copytopoints::2.0", node_name)
    targetPoints = copyPoints.parm("targetgroup")
    targetPoints.set("group1")

def create_hr_hand(node_name = "transform2"):
    global hour
    hour = geo.createNode("xform", node_name) 
    hour.setParms({"sx":0.5, "sy":0.1, "sz":0.1}) 
    heightHour = hour.parm("ty")
    scaleHour = hour.parm("scale")
    defaultMin = hour.parm("ry").set(60)
    heightHour.set(distParm_base) # becasuse of procedural scailing
    scaleHour.set(scaleParm_circle)
    
def create_min_hand(node_name = "transform3"):
    global minute
    minute = geo.createNode("xform", node_name) 
    minute.setParms({"sx":0.75, "sy":0.1, "sz":0.1}) 
    heightMinute = minute.parm("ty")
    scaleMinute = minute.parm("scale")
    defaultMin = minute.parm("ry").set(300)
    heightMinute.set(distParm_base)
    scaleMinute.set(scaleParm_circle)
    
def create_grp_hr_small(node_name = "group_by_range1"):
    global grpRest
    grpRest = geo.createNode("grouprange", node_name)
    grp1 = grpRest.parm("groupname1")
    grpType1 = grpRest.parm("grouptype1")
    grpRangeIn1 = grpRest.parm("selectamount1")
    grpRangeOut1 = grpRest.parm("selecttotal1")
    grpOffset1 = grpRest.parm("selectoffset1")
    grp1.set("group1")
    grpType1.set(0)
    grpRangeIn1.set(1)
    grpRangeOut1.set(4)

def create_grp_hr_part(node_name = "group_by_range2"):
    global grpParts
    grpParts = geo.createNode("grouprange", node_name)
    grp2 = grpParts.parm("groupname1")
    grpType2 = grpParts.parm("grouptype1")
    grpRangeIn2 = grpParts.parm("selectamount1")
    grpRangeOut2 = grpParts.parm("selecttotal1")
    grpOffset2 = grpParts.parm("selectoffset1")
    grp2.set("group2")
    grpType2.set(1)
    grpRangeIn2.set(1)
    grpRangeOut2.set(18)
    grpOffset2.set(2)
   
def extrude_hr_elements(name_node = "extrude"):
    global parts
    parts = geo.createNode("polyextrude::2.0", name_node)
    grpParm_parts = parts.parm("group")
    grpParm_parts.set("group2")
    distParm_parts = parts.parm("dist")
    distParm_parts.set(0.12) 
    
def create_polyFrame(name_node, def_node = "polyframe"):
    global polyFrame
    polyFrame = geo.createNode(def_node , name_node)
    normal = polyFrame.parm("Non")
    normal.set(0)
    tg = polyFrame.parm("tangentu")
    tg.set("N")

def connect_nodes():
    output.setInput(0, normal)
    normal.setInput(0, merge)
    merge.setInput(1, col1) 
    merge.setInput(2, col2)
    col1.setInput(0, restBool)
    restBool.setInput(0, parts)
    restBool.setInput(1, baseVolume)
    baseVolume.setInput(0, circle)
    parts.setInput(0, grpParts)
    grpParts.setInput(0, copyPoints)
    copyPoints.setInput(0, boxes) 
    copyPoints.setInput(1, grpRest)
    boxes.setInput(0, box)
    grpRest.setInput(0, polyFrame)
    polyFrame.setInput(0, circle)
    col2.setInput(0, handsBool)
    handsBool.setInput(0, minute)
    handsBool.setInput(1, hour)
    hour.setInput(0,hand)
    minute.setInput(0, hand)

#-------CODE-INITIALIZATION-------------------------------------------------#
obj = hou.node("/obj") # enter to the obj. level workspace
geo = obj.createNode("geo", "Clock") # the whole clock geo
sub = geo.createNode("subnet", "asset_clock") # digital asset container
geo = sub # switch geometry level

newNode = create_node()
create_clock_base("circle_clock_base")
transform_hr_element("single_hour_element")
create_polyFrame("box_orientation")
create_hr_element("box_main_clock")
create_grp_hr_small("grp_hour_elements_rest")
create_hr_elements("hour_elements")
create_grp_hr_part("grp_hour_elements_quarters")
extrude_hr_elements("hour_parts")
restBool = newNode.create_bool("connect_rest_parts")
col1 = newNode.create_cal("clock_color")

create_hand_element("box_main_hands")
create_min_hand("minute_hand")    
create_hr_hand("hour_hand")
handsBool = newNode.create_bool("connect_hands")
col2 = newNode.create_cal("hands_color",r=0,b=0)

merge = newNode.create("merge", "merge")
normal = newNode.create("normal", "surface_normal")
output = newNode.create("null", "output")

#......Node-Connection......................................................#
connect_nodes()

#......Vizualization........................................................#
geo.layoutChildren() # rearange nodes in view
output.setDisplayFlag(True)
output.setRenderFlag(True)

#......Digital-Asset(DA)....................................................#
hda_name = sub.name() # my "asset_clock" name
file_loc = r"C:\Users\Admin\Desktop" # SET YOUR OWN PATH
file_loc = file_loc.replace(os.path.sep, "/")
file_loc = file_loc + "/" + hda_name + ".hda" # create .hda file -> drag & drop to Unreal 
# creating of DA
hda_asset = sub.createDigitalAsset(hda_name, file_loc)
hda_def = hda_asset.type().definition()
hda_ptg = hda_def.parmTemplateGroup()
# group of parameters
folder = hou.FolderParmTemplate("settings", "Settings")
min_int = hou.IntParmTemplate("minute", "Minute",1 , default_value=(0,0,0), min=0, max=360)
min_int.setDefaultExpression(("ch('../asset_clock/minute_hand/ry')",))
hr_int = hou.IntParmTemplate("hour", "Hour",1 , default_value=(0,0,0), min=0, max=360)
hr_int.setDefaultExpression(("ch('../asset_clock/hour_hand/ry')",))

folder.addParmTemplate(min_int)
folder.addParmTemplate(hr_int)
hda_ptg.addParmTemplate(folder) 
# update UI grp of parameters
hda_def.setParmTemplateGroup(hda_ptg) 
#----CODE-END---------------------------------------------------------------#
