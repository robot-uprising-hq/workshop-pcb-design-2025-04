# Instructions

## Make PCB layout

Open the KiCad Project. From the main page open either the schematic editor if you are interested in the schematic or the PCB editor if not. Would recommend checking the schematic.
In the schematic editor the right most icon is opens the schematic in PCB editor. This is where we do the PCB layout.
While the schematic is fully done for you the PCB editor page is empty.

### Add components

Add the components in the schematic by pressing the 4th icon from right which says Update PCB from schematic. Or alternatively press F8. A dialog will open, press "update PCB". The components should now be visible.

### Add outline

In the right hand side there are layers of the PCB listed. The Edge.Cuts layer is the board outline. Click the Edge.Cuts to select and draw on it. Add some shape that is large enough for the components plus bit more on that layer. Use the Draw lines/arcs/rectangels/circles/polygons tools.
Fancy shapes are easier to draw in other programs and import to KiCad. This is explained later.

### Connect components

Between the components there are blue lines. Those show which pads of the components should be connected to which. Connect the componets by using Route single track tool (hotkey X). Remember to select which layer the wire is drawn, the options here are top and bottom but sometimes there are also inner layers.
The inner layers can have tracks on top of each other since they are separete layers and not conducting to each other. For this simple design several layers are not needed but the more complex desing the more inner layers are needed. The layers are connected to each other using vias (hotkey ctrl+shift+x).

### Check the 3D model
You can check how the board looks by pressing the 3D viewer button or Alt + 3.

### Add graphichs

You can add grapchis either drawn on the PCB silkscreen or the board outline or copper traces using the import tool. Go to file -> import -> graphics. Supported file types are .svg and .dxf. Dxf files are easier to edit in KiCad editor but both work fine.
In the import dialog select the file to import, the scaling if needed, maybe the DXF unit to mm and the layer where to import the graphic. Others can be defaults.

### Zones

Typically ground plane is done to be as large as possible. Using filled zones is the easiest way of doing it.
Zones can be also used as rule areas if there is not allowed to be copper in some areas.
Select either of the copper layers, typically bottom and use Draw Filled Zones.
In the dialog select the layer again and the plane it is connected to (ground). Press OK and draw the zone by clicking, double click stops the zone making.

## Final notes

Play around and test to press different buttons and what they do.
Dont be afraid that something breaks, you can just ctrl+z and all is good.
KiCad is often a bit stiff tool to work with.
Drawing things in KiCad for example is painful. But it works. But dont be surprised if something simple is more annyoing to do than expected
 A lot of work is manual.
 There are externsions, feel free to read and test any of them.
