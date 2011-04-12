<%
   executions_class = ""
   files_class = ""
   if self.attr.page_path == "executions":
       executions_class = "active"
   elif self.attr.page_path == "files":
       files_class = "active" 
%>

<%def name="older_newer_links(older_newer)">
    % if older_newer != None:
        <p class="older_newer_links">
            % if older_newer[0]:
                <a href="${self.attr.page_path}?page=${page-1}">&lt;&lt; Newer</a>
            % endif
            % if older_newer[1]:
                <a href="${self.attr.page_path}?page=${page+1}">Older &gt;&gt;</a>
            % endif
        </p>
    % endif
</%def>

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
      ${older_newer_links(older_newer)}
      ${self.body()}
      ${older_newer_links(older_newer)}
    </div>

% if wrapped:
  </body>
</html>
% endif
