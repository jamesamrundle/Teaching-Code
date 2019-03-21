# Teaching-Code
Starting project to create a simple codebase of a visual and interactive aid for teaching introductory coding skills 

canvase is 150 X 150 px canvase
code is written to translate into a 15x15 grid for ease of use.

Summary of basic turtle commands at end of readme but i coded a move method for detecting collisions,
      and allowing user to move by GRID BLOCKS instead of pixels. 
      for example move(timmy,1) will move the turtle timmy forward 1 grid or 10 actual pixels.

running as is, just lets you draw simple rectangles by clicking upper left and lower right corners on grid. 
  use left mouse button to draw red barriers, use wheel(or both left and right mouse buttons) to draw blue goal rectangles
  
<table class="table" border="0">
<colgroup>
<col width="12%">
<col width="12%">
<col width="76%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Method</th>
<th class="head">Parameters</th>
<th class="head">Description</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>Turtle</td>
<td>None</td>
<td>Creates and returns a new turtle object</td>
</tr>
<tr class="row-odd"><td>forward</td>
<td>amount</td>
<td>Moves the turtle forward by the specified amount</td>
</tr>
<tr class="row-even"><td>backward</td>
<td>amount</td>
<td>Moves the turle backward by the specified amount</td>
</tr>
<tr class="row-odd"><td>right</td>
<td>angle</td>
<td>Turns the turtle clockwise</td>
</tr>
<tr class="row-even"><td>left</td>
<td>angle</td>
<td>Turns the turtle counter clockwise</td>
</tr>
<tr class="row-odd"><td>penup</td>
<td>None</td>
<td>Picks up the turtle’s pen</td>
</tr>
<tr class="row-even"><td>pendown</td>
<td>None</td>
<td>Puts down the turtle’s pen</td>
</tr>
<tr class="row-odd"><td>up</td>
<td>None</td>
<td>Picks up the turtle’s pen</td>
</tr>
<tr class="row-even"><td>down</td>
<td>None</td>
<td>Puts down the turtle’s pen</td>
</tr>
<tr class="row-odd"><td>color</td>
<td>color name</td>
<td>Changes the color of the turtle’s pen</td>
</tr>
<tr class="row-even"><td>fillcolor</td>
<td>color name</td>
<td>Changes the color of the turtle will use to fill a polygon</td>
</tr>
<tr class="row-odd"><td>heading</td>
<td>None</td>
<td>Returns the current heading</td>
</tr>
<tr class="row-even"><td>position</td>
<td>None</td>
<td>Returns the current position</td>
</tr>
<tr class="row-odd"><td>goto</td>
<td>x,y</td>
<td>Move the turtle to position x,y</td>
</tr>
<tr class="row-even"><td>begin_fill</td>
<td>None</td>
<td>Remember the starting point for a filled polygon</td>
</tr>
<tr class="row-odd"><td>end_fill</td>
<td>None</td>
<td>Close the polygon and fill with the current fill color</td>
</tr>
<tr class="row-even"><td>dot</td>
<td>None</td>
<td>Leave a dot at the current position</td>
</tr>
<tr class="row-odd"><td>stamp</td>
<td>None</td>
<td>Leaves an impression of a turtle shape at the current location</td>
</tr>
<tr class="row-even"><td>shape</td>
<td>shapename</td>
<td>Should be ‘arrow’, ‘classic’, ‘turtle’, or ‘circle’</td>
</tr>
</tbody>
</table>
