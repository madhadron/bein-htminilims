<%!
    page_path = "files"
%>
<%inherit file="layout.mako" />

% for i in file_ids:
    <p>${i}</p>
% endfor