<%!
    page_path = "files"
%>
<%inherit file="layout.py" />

<%def name="display_file(i,v)">
<div class="file" id="${i}">
<a name="file-${i}"></a>
<p class="title">${i} - 
% if v['description'] != "":
    ${v['description']}
% else:
    <em>(No description)</em>
% endif
% if not(read_only):
    % if v['immutable']:
        <span class="delete_link">Immutable</span>
    % else:
        <input class="delete_link" type="button" value="Delete" 
               onclick="delete_entry('file',${i});">
    % endif
% endif
<p>
% if v['origin'] == 'import':
    Manually imported at ${v['created']}.
% elif v['origin'][0] == 'execution':
    Created by <a href="executions?include_execution=${v['origin'][1]}#execution-${v['origin'][1]}">
    execution ${v['origin'][1]}</a> at ${v['created']}.
% elif v['origin'][0] == 'copy':
    Copy of <a href="files?include_file=${v['origin'][1]}#file-${v['origin'][1]}">file 
    ${v['origin'][1]}</a> at ${v['created']}.
% endif
</p>
<div id="file-${i}-more-container" class="more-container">

</div>
</div>
</%def>

% for i,v in files:
    ${display_file(i,v)}
% endfor
