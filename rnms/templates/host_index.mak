<%inherit file="local:templates.master"/>

<%def name="title()">
Rosenberg NMS: Host List
</%def>
    
	<div class="row">
	  <div class="span12">
	    ${w.display() | n}
	  </div>
	</div>
