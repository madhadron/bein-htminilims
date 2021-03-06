body {
    padding-top: 0;
    margin-top: 0;
}

p {
    margin: 0;
    padding: 0;
}

span.label {
//    position: absolute;
    float: left;
    font-weight: bold;
    width: 15em;
    text-align: right;
    margin-right: 10pt;
}

.delete_link {
    float: right;
    line-height: 1em;
}

.download_link {
    color: white;
    font-size: 80%;
}

h2 {
    background-color: #000096;
    color: #ffffff;
    padding: 4pt;
    border-top-left-radius: 3pt;
    border-top-right-radius: 3pt;
    -moz-border-top-left-radius: 3pt;
    -moz-border-top-right-radius: 3pt;
    margin-bottom: 5pt;
    margin-top: 10pt;
}

div.program {
    border-top: 1px;
    border-bottom: 0;
    border-left: 0;
    border-right: 0;
    border-color: #aaaaaa;
    border-style: solid;
    margin-top: 10pt;
    margin-bottom: 0;
    padding-top: 0;
    padding-left: 60pt;
}

h3 {
    padding: 0;
    margin: 0;
}

div.output {
    display: table;
    margin-top: 3pt;
    table-layout: fixed;
    width: 100%;
}

div.row {
    display: table-row;
}


div.stdout {
    margin: 5pt;
    display: table-cell;
    width: 50%;
    font-family: monospace;
    border-style: none solid none none;
    border-width: 1px;
    border-color: #aaa;
    padding-right: 10pt;
}

div.stderr {
    display: table-cell;
    padding-left: 10pt;
    width: 50%;
    font-family: monospace;
}

ul.tabs {
    position: fixed;
    background: white;
    width: 100%;
	margin: 0;
	padding: 0;
	float: left;
	list-style: none;
	height: 32px; /*--Set height of tabs--*/
	border-bottom: 1px solid #999;
	border-left: 1px solid #999;
	width: 100%;
}
ul.tabs li {
	float: left;
	margin: 0;
	padding: 0;
	height: 31px; /*--Subtract 1px from the height of the unordered list--*/
	line-height: 31px; /*--Vertically aligns the text within the tab--*/
	border: 1px solid #999;
	border-left: none;
	margin-bottom: -1px; /*--Pull the list item down 1px--*/
	overflow: hidden;
	position: relative;
	background: #e0e0e0;
}
ul.tabs li a {
	text-decoration: none;
	color: #000;
	display: block;
	font-size: 1.2em;
	padding: 0 20px;
	border: 1px solid #fff; /*--Gives the bevel look with a 1px white border inside the list item--*/
	outline: none;
}
ul.tabs li a:hover {
	background: #ccc;
}
html ul.tabs li.active, html ul.tabs li.active a:hover  { /*--Makes sure that the active tab does not listen to the hover properties--*/
	background: #fff;
	border-bottom: 1px solid #fff; /*--Makes the active tab look like it's connected with its content--*/
}

.tab_container {
	border: 1px solid #999;
	border-top: none;
	overflow: hidden;
	clear: both;
	float: left; width: 100%;
	background: #fff;
	margin-top: 36px;
}

p.older_newer_links {
    text-align: center;
}

p.title {
    background: #eee;
}

div.execution {
    padding-left: 0.3em;
    margin-bottom: 0.3em;
}

p.exception-string {
    color: #f00;
}

span.small-link {
    font-size: 50%;
}

ul.file-list {
    margin-top: 0;
    margin-bottom: 0;
    padding-top: 0;
    padding-bottom: 0;
    list-style: none;
    padding-left: 2em;
}

div.file {
    margin-bottom: 0.3em;
}

.bold {
    font-weight: bold;
}

.grey {
    color: #999;
}

.hidden {
    display: none;
}

