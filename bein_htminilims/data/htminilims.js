$(document).ready(function(){
    $(".tab_content").hide(); //Hide all content
    $("ul.tabs li:first").addClass("active").show(); //Activate first tab
    $(".tab_content:first").show(); //Show first tab content
    
    //On Click Event
    $("ul.tabs li").click(function() {
	$("ul.tabs li").removeClass("active"); //Remove any "active" class
	$(this).addClass("active"); //Add "active" class to selected tab
	$(".tab_content").hide(); //Hide all tab content
	var activeTab = $(this).find("a").attr("href"); //Find the href attribute value to identify the active tab + content
	$(activeTab).fadeIn(); //Fade in the active ID content
	return false;
    });

});

var file_tab = function() {
    $('.tab_content').hide();
    $('#tabs-2').fadeIn();
    $('ul.tabs li').removeClass("active");
    $('ul.tabs li#t2').addClass("active");
}

var execution_tab = function() {
    $('.tab_content').hide();
    $('#tabs-1').fadeIn();
    $('ul.tabs li').removeClass("active");
    $('ul.tabs li#t1').addClass("active");
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