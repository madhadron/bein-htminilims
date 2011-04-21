
function more_link(call) {
    return '<p><span class="small-link"><a href="javascript:' + call + '">details&rsaquo;&rsaquo;</a></span></p>';
}

function show_file_details(file_id) {
    var container = $("#" + file_id + " > div.more-container");
    container.html("<p>...</p>");
    $.ajax({url: "file_detail?id="+file_id,
	    success: function(data) {
		container.html(data);
	    }
	   });
}

function hide_file_details(file_id) {
    var container = $("#"+file_id+" > div.more-container");
    container.html(more_link('show_file_details('+file_id+')'));
}

function show_execution_panel(ex_id,panel) {
    var container = $("#"+ex_id+" > div."+panel+"-container");
    select_link = function(p) {
	$("#"+ex_id+" > div."+p+"-container").removeClass("hidden")
	$("#"+ex_id+" > p > span."+p+"-link").addClass("bold")
	    .html('<a href="javascript:hide_execution_panel('+ex_id+',\''+p+'\')">\
                   &lsaquo;&lsaquo;'+panel+'</a>');
    };
    unselect_link = function(p) {
	$("#"+ex_id+" > div." + p + "-container").addClass("hidden");
	$("#"+ex_id+" > p > span." + p + "-link")
            .removeClass("bold")
	    .html('<a href="javascript:show_execution_panel('+ex_id+',\'' + p + '\')">'+p+'&rsaquo;&rsaquo;</a>');
    };

    update_link = function(p) {
	if (p == panel) {
	    select_link(p);
	} else {
	    unselect_link(p);
	}
    }

    update_link("details");
    update_link("traceback");
    update_link("programs");

    if (container.html() == "") {
	container.html("<p>...</p>");
	$.ajax({
	    url: "execution_" + panel + "?id="+ex_id,
	    success: function(data) {
		container.html(data);
	    }
	});
    };
}

function hide_execution_panel(ex_id,panel) {
    var container = $("#"+ex_id+" > div." + panel + "-container");
    $("#"+ex_id+" > div." + panel + "-container").addClass("hidden")
    $("#"+ex_id+" > p > span." + panel + "-link").removeClass("bold")
	.html('<a href="javascript:show_execution_panel('+ex_id+',\'' + panel + '\')">' + panel + '&rsaquo;&rsaquo;</a>');
}

function show_execution_traceback(ex_id) {
    var container = $("#"+ex_id+" > div.traceback-container");
    $("#"+ex_id+" > div.traceback-container").removeClass("hidden");
    $("#"+ex_id+" > p > span.traceback-link").addClass("bold")
	.html('<a href="javascript:hide_execution_traceback('+ex_id+')">&lsaquo;&lsaquo;traceback</a>');
    $("#"+ex_id+" > div.programs-container").addClass("hidden");
    $("#"+ex_id+" > p > span.programs-link").removeClass("bold");
    $("#"+ex_id+" > div.details-container").addClass("hidden");
    $("#"+ex_id+" > p > span.details-link").removeClass("bold");
    container.html("<p>...</p>");
    $.ajax({
	url: "execution_traceback?id="+ex_id,
	success: function(data) {
	    container.html(data);
	}
    });
}

function delete_entry(t,i) {
    var a = confirm('Really delete ' + t + ' ' + i + '?');
    if (a) {
	$.ajax({
	    url: "delete",
	    data: {obj_type: t, obj_id: i},
	    success: function(data) {
		$('.'+t+'#'+i).remove();
	    },
	    error: function(x, type, exception) {
		alert('Deletion of ' + t + ' ' + i + ' failed: ' + exception);
	    }
	});
    } else {
      return false;
    }
}

$(document).ready(function(){
    $(".more-container").each(function(){
	this_id = $(this).parent().attr('id');
	$(this).html(more_link('show_file_details('+this_id+')'));
    });
});
