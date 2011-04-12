<%!
   import math
   from datetime import datetime
   page_path = "executions"
%>
<%inherit file="layout.py" />

<%def name="display_execution(i,v)">
<div class="execution" id="${i}">
    <a name="execution-${i}"></a>
    <p class="title">${i} - 
       (${datetime.fromtimestamp(v['finished_at']).strftime("%d %b %Y")})
       % if v['description'] == "":
           <em>(no description)</em>
       % else:
           ${v['description']}
       % endif
       % if not(read_only):
           % if v['immutable']:
               <span class="delete_link">Immutable</span>
           % else:
               <input class="delete_link" type="button" value="Delete" 
                      onclick="delete_entry('execution',${i});">
           % endif
       % endif
    </p>
    % if v['exception_string'] != None:
        <p class="exception-string">FAILED: ${v['exception_string'].splitlines()[-1]}</p>
    % endif
    <p>
        <span class="small-link details-link"><a href="javascript:show_execution_panel(${i},'details')">details&rsaquo;&rsaquo;</a></span>&nbsp;&nbsp;&nbsp;
	% if v['programs'] != []:
            <span class="small-link programs-link"><a href="javascript:show_execution_panel(${i},'programs')">programs&rsaquo;&rsaquo;</a></span>&nbsp;&nbsp;&nbsp;
        % else:
            <span class="small-link grey">programs&rsaquo;&rsaquo;</span>&nbsp;&nbsp;&nbsp;
        % endif
        % if v['exception_string'] != None:
	    <span class="small-link traceback-link"><a href="javascript:show_execution_panel(${i},'traceback')">traceback&rsaquo;&rsaquo;</a></span>&nbsp;&nbsp;&nbsp;
        % else:
   	    <span class="small-link grey">traceback&rsaquo;&rsaquo;</span>&nbsp;&nbsp;&nbsp;
        % endif
    </p>
    <div class="details-container"></div>
    <div class="programs-container"></div>
    <div class="traceback-container"></div>

    <ul class="file-list">
        % for fid in v['added_files']:
            <li><a href="files?include_file=${i}#file-${i}">${i} ${lims.fetch_file(fid)['description'] == '' and '<em>(no description)</em>' or lims.fetch_file(fid)['description']}</a> 
                 &nbsp;&nbsp;&nbsp; <span class="small-link">
                     [<a href="download?fileid=${i}">download</a>]</span></li>
        % endfor
    </ul>
</div>
</%def>

% for k,v in executions:
    ${display_execution(k,v)}
% endfor


