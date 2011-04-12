<%!
    from datetime import datetime
%>

<p><span class="label">Ran</span> from ${datetime.fromtimestamp(ex_details['started_at']).strftime("%Y-%m-%d %H:%M:%S")} to ${datetime.fromtimestamp(ex_details['finished_at']).strftime("%Y-%m-%d %H:%M:%S")}</p>

<p><span class="label">Working directory</span> 
<span class="working_directory">${ex_details['working_directory']}</span></p>

% if ex_details['used_files'] != []:
    <p><span class="label">Used files</span>
      ${", ".join(["""<a href="files?include_file=%d#file-%d">%d</a>""" % (f,f,f) for f in ex_details['used_files']])}
     </p>
% endif
