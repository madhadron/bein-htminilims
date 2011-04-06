<%
   executions_class = ""
   files_class = ""
   if self.attr.active_tab == "executions":
       executions_class = "active"
   elif self.attr.active_tab == "files":
       files_class = "active" 
%>

% if wrapped:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>MiniLIMS Client</title>
    <link rel="stylesheet" href="htminilims.css" type="text/css">
    <script src="jquery.js" type="text/javascript"></script>
    <script src="htminilims.js" type="text/javascript"></script>
  </head>
  <body>

    <div id="tabs">
      <ul class="tabs">
          <li class="${executions_class}"><a href="executions">Executions</a></li>
          <li class="${files_class}"><a href="files">Files</a></li>
      </ul>
    </div>
% endif # Wrapped

    <div class="tab_container">
      ${self.body()}
    </div>

% if wrapped:
  </body>
</html>
% endif
