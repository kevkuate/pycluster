$(function() {
    $("#results2").delegate('td[colname]','mouseover mouseleave', function(e) {
        if (e.type == 'mouseover') {

          $(this).parent().not(".titles").addClass("hover");

          $("td[colname='"+$(this).attr("colname")+"']").not(".rowtitle").addClass("hover");
          
          $(this).not(".coltitle").not(".rowtitle").addClass("hoverSelected");
          
          //$(this).parent().addClass("hover");
          //tr:not(" + $(this) + ")"
          //$("td[colname="$(this).attr("colname")"]").eq( $(this).index() ).addClass("hover");
        } else {
          $(this).parent().not(".titles").removeClass("hover");
          
          $("td[colname='"+$(this).attr("colname")+"']").not(".rowtitle").removeClass("hover");
          
          $(this).not(".coltitle").not(".rowtitle").removeClass("hoverSelected");
          
          //$("td[colname=label]").eq( $(this).index() ).removeClass("hover");
        }
    });

});
