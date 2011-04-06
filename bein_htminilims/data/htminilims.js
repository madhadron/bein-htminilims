$(document).ready(function(){})

var delete_entry = function(t,i) {
    var a = confirm('Really delete ' + t + ' ' + i + '?');
    if (a) { 
      $.get('delete', {obj_type: t, obj_id: i}, 
            function(data) { $('#' + t + '-' + i).remove(); });
      if (t == 'execution') {
          $('div.created-by-ex'+i).each(function(i) { $(this).remove(); });
      }
    } else {
      return false;
    }
}