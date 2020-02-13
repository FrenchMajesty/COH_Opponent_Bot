class OverlayTemplates:

    overlayhtml = """
 <!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="overlaystyle.css">
<meta http-equiv="content-type" content="text-html; charset=utf-8">
<meta http-equiv="refresh" content="2">
</head>
<body>
<div id="container">
<div id = "playerTeam">
{0}
</div>
<div id = "opponentTeam">
{1}
</div>
</div>
<div style="clear: both;"></div>
</body>
</html> 
    """

    overlaycss = """




body {
	background-color: transparent;
  }
    
#container{width:100%;
	font-size: 30px; 

}


#countryflagimg{
	position: relative;
	display: inline;
	top: -2px;
}

#factionflagimg{
	position: relative;
	display: inline;
}


#rankimg {
		position: relative;
		top: 10px;
		display: inline;
}

#textVariables {
	position: relative;
	display: inline;
	top: -3px;
}

#nonVariableText{
	position: relative;
	display: inline;
	top: -3px;
}

#opponentTeam {

	  position : absolute;
	  top: -10px; /* This will move it px up */
	  color: white;
	  float: left;
	  margin-left: 58%;
	  background-color: rgba(0, 0, 0, 0.8);
	  }
  
#playerTeam {

	  position: relative;
	  top: -10px; /* This will move it px up */
	  color: white;
	  float: right;
	  margin-right: 58%;


	  background-color: rgba(0, 0, 0, 0.8);
  }

    



    """