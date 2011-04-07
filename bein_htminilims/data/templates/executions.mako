<%!
   import math
   from datetime import datetime
   page_path = "executions"
%>
<%inherit file="layout.mako" />

<%def name="display_execution(i,v)">
<div class="execution" id="execution-${i}">
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
        <p class="exception-string">FAILED: ${v['exception_string'].splitlines()[-1]} 
                  <span class="small-link">more&rsaquo;&rsaquo;</span></p>
    % endif
    <p><span class="small-link">more&rsaquo;&rsaquo;</span></p>
    <ul class="file-list">
        % for fid in v['added_files']:
            <li><a href="files?include_file=${i}#file-${i}">${i} ${lims.fetch_file(i)['description']}</a> 
                 &nbsp;&nbsp;&nbsp; <span class="small-link">
                     [<a href="download?fileid=${i}">download</a>]</span></li>
        % endfor
    </ul>
</div>
</%def>

% for k,v in executions:
    ${display_execution(k,v)}
% endfor


