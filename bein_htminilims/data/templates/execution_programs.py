% for program in programs:
<p style="color: ${program['return_code'] == 0 and 'black' or 'red'};"><b>
${" ".join(program['arguments'])}</b></p>
<p>Pid ${program['pid']} exited with value ${program['return_code']}.</p>
<dl>
% if program['stdout'] != "":
    <dt>stdout</dt>
    <dd><pre>${program['stdout']}</pre></dd>
% endif
% if program['stderr'] != "":
    <dt>stderr</dt>
    <dd><pre>${program['stderr']}</pre></dd>
% endif
% endfor