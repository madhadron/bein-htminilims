$(document).ready(function(){
    $(".more-container").each(function(){
	this_id = $(this).parent().attr('id');
	$(this).html(more_link('show_file_details('+this_id+')'));
    });
})

var more_link = function(call) {
    return '<p><span class="small-link">\
   <a href="javascript:'+call+'">\
  more&rsaquo;&rsaquo;</a></span></p>';
}

var show_file_details = function(file_id) {
    container = $("#"+file_id+" > div.more-container");
    container.html("<p>...</p>")
    $.ajax({
	url: "file_detail?id="+file_id,
	success: function(data) {
	    container.html(data);
	}
    });
}

var hide_file_details = function(file_id) {
    container = $("#"+file_id+" > div.more-container");
    container.html(more_link('show_file_details('+file_id+')'));
}

var show_execution_details = function(ex_id) {
    container = $("#"+ex_id+" > div.details-container");
    $("#"+ex_id+" > div.details-container").removeClass("hidden")
    $("#"+ex_id+" > p > span.details-link").addClass("bold")
	.html('<a href="javascript:hide_execution_details('+ex_id+')">&lsaquo;&lsaquo;details</a>');
    $("#"+ex_id+" > div.programs-container").addClass("hidden");
    $("#"+ex_id+" > p > span.programs-link").removeClass("bold");
    $("#"+ex_id+" > div.traceback-container").addClass("hidden");
    $("#"+ex_id+" > p > span.traceback-link").removeClass("bold");
    container.html("<p>...</p>");
    $.ajax({
	url: "execution_detail?id="+ex_id,
	success: function(data) {
	    container.html(data);
	}
    });
}

var hide_execution_details = function(ex_id) {
    container = $("#"+ex_id+" > div.details-container");
    $("#"+ex_id+" > div.details-container").addClass("hidden")
    $("#"+ex_id+" > p > span.details-link").removeClass("bold")
	.html('<a href="javascript:show_execution_details('+ex_id+')">details&rsaquo;&rsaquo;</a>');
}

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