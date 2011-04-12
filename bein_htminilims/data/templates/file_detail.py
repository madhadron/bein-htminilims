<%def name="hide_link()">
<p><span class="small-link">
       <a href="javascript:hide_file_details(${id})">&lsaquo;&lsaquo;details</a></span></p>
</%def>

${hide_link()}

<p><span class="label">Aliases</span>
<span class="aliases">
% if file_details['aliases'] == []:
    <em>(no aliases)</em>
% else:
    ${', '.join(['"'+alias+'"' for alias in file_details['aliases']])}
% endif
</span>
</p>

<p><span class="label">Associations</span>
<span class="associations">
% if file_details['associations'] == []:
    <em>(no associations)</em>
% else:
    ${", ".join(["""'%s' on file <a href="files?include_file=%d#file-%d">%d</a> """ % (t,f,f,f)
                 for (f,t) in file_details['associations']])}
% endif
</span></p>

<p><span class="label">Associated to</span>
<span class="associated_to">
% if file_details['associated_to'] == []:
    <em>(not associated to any files)</em>
% else:
    ${", ".join(["""'%s' on file <a href="files?include_file=%d#file-%d">%d</a> """ % (t,f,f,f)
                 for (f,t) in file_details['associated_to']])}
% endif
</span></p>

<p><span class="label">External name</span>
<span class="external_name">${file_details['external_name']}</span></p>

<p><span class="label">Repository name</span>
<span class="repository_name">${file_details['repository_name']}</span></p>

