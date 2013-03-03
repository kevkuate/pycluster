//http://www.willmaster.com/blog/css/floating-layer-at-cursor-position.php

//http://stackoverflow.com/questions/6393518/javascript-and-ajax-floating-an-image-next-to-the-cursor-questions

//Copyright 2006,2007 Bontrager Connection, LLC

// http://bontragerconnection.com/ and http://www.willmaster.com/

var cXA = 0;
var cYA = 0;
var cXR = 0;
var cYR = 0;

//function UpdateCursorPosition(e)       { cX = e.pageX;       cY = e.pageY;       }
//function UpdateCursorPositionDocAll(e) { cX = event.clientX; cY = event.clientY; }
//if(document.all) { document.onmousemove = UpdateCursorPositionDocAll; }
//else             { document.onmousemove = UpdateCursorPosition;       }

document.onmousemove = updatemouse;

var dt=0.02;
//setInterval(updatemouse(window.event), dt*5000);

function updatemouse (e){
    e   = e || window.event;
    cXA = mouseX(e);
    cYA = mouseY(e);
    cXR = e.clientX;
    cYR = e.clientY;
    //scriptDebugger("X "+cXR+" Y "+cYR+"\n");
}

function mouseX(evt) {
    if (evt.pageX)
        return evt.pageX;
    else if (evt.clientX)
        return evt.clientX + (document.documentElement.scrollLeft ?
        document.documentElement.scrollLeft :
        document.body.scrollLeft);
    else
        return null;
}
function mouseY(evt) {
    if (evt.pageY)
        return evt.pageY;
    else if (evt.clientY)
       return evt.clientY + (document.documentElement.scrollTop ?
       document.documentElement.scrollTop :
       document.body.scrollTop);
    else
        return null;
}


function HideContent(d) {
    if(d.length < 1) { return; }
    //ModifyContent(d, '');

    var dd1 = document.getElementById(d);
    dd1.style.display = "none";
}

function ShowContent(d) {
    if(d.length < 1) { return; }

    updatemouse();

    var dd = document.getElementById(d);
        dd.style.display = "block";
    
    var vW  = ViewportWidth();
    var vH  = ViewportHeight();

    var borderW   = parseInt(dd.style.left.slice(0,-2))             +
                    parseInt(dd.style.paddingLeft.slice(0,-2))      +
                    parseInt(dd.style.paddingRight.slice(0,-2))     +
                    parseInt(dd.style.borderRightWidth.slice(0,-2)) +
                    parseInt(dd.style.borderLeftWidth.slice(0,-2));
    var borderH   = parseInt(dd.style.top.slice(0,-2))             +
                    parseInt(dd.style.paddingTop.slice(0,-2))      +
                    parseInt(dd.style.paddingBottom.slice(0,-2))   +
                    parseInt(dd.style.borderTopWidth.slice(0,-2))  +
                    parseInt(dd.style.borderBottomWidth.slice(0,-2));
    
    var oW  = dd.offsetWidth  + borderW;
    var oH  = dd.offsetHeight + borderH;
    var imgW = $(".imgdsp").width();
    var imgH = $(".imgdsp").height();

    var per = .95;

    //var border    = dd.style.paddingLeft;// + dd.style.padding-right + dd.style.border-right-width + dd.style.border-left-width;
    
    var debugText = "Cursor X R " + cXR     + " Cursor Y R " + cYR      + "\n" +
                    "Cursor X A " + cXA     + " Cursor Y A " + cYA      + "\n" +
                    "Off W      " + oW      + " Off H      " + oH       + "\n" +
                    "View W     " + vW      + " View H     " + vH       + "\n" +
                    "Img W      " + imgW    + " Img H      " + imgH     + "\n" +
                    "Border W   " + borderW + " Border H   " + borderH  + "\n";



    var maxW = Math.round( vW * per - borderW );
    var maxH = Math.round( vH * per - borderH );
    if ( imgW >=  maxW ) {
        resizerW('.imgdsp', maxW);
        debugText += "RESIZING 3 IMGW ("+imgW+") >= VW ("+maxW+") => "+maxW+"\n";

        dd   = document.getElementById(d);
        oW   = dd.offsetWidth  + borderW;
        oH   = dd.offsetHeight + borderH;
        imgW = $(".imgdsp").width();
        imgH = $(".imgdsp").height();
        debugText += "Off W      " + oW   + " Off H      " + oH    + "\n";
        debugText += "Img W      " + imgW + " Img H      " + imgH  + "\n";
    }


    if ( imgH >= maxH ) {
        resizerH('.imgdsp', maxH);
        debugText += "RESIZING 4 imgH ("+imgH+") >= VH ("+maxH+") => "+maxH+"\n";

        dd   = document.getElementById(d);
        oW   = dd.offsetWidth  + borderW;
        oH   = dd.offsetHeight + borderH;
        imgW = $(".imgdsp").width();
        imgH = $(".imgdsp").height();
        debugText += "Off W      " + oW   + " Off H      " + oH    + "\n";
        debugText += "Img W      " + imgW + " Img H      " + imgH  + "\n";
    }    

    var maxX = Math.round( cXR * per - borderW );
    var maxY = Math.round( cYR * per - borderH );
    if ( imgW >= maxX ) {
        resizerW('.imgdsp', maxX);
        debugText += "RESIZING 1 imgW ("+imgW+") >= CXR ("+maxX+") && imgH ("+imgH+") >= CYR("+maxY+") => "+maxX+"\n";

        dd   = document.getElementById(d);
        oW   = dd.offsetWidth  + borderW;
        oH   = dd.offsetHeight + borderH;
        imgW = $(".imgdsp").width();
        imgH = $(".imgdsp").height();
        debugText += "Off W      " + oW   + " Off H      " + oH    + "\n";
        debugText += "Img W      " + imgW + " Img H      " + imgH  + "\n";
    }

    if (( imgH >= maxY ) && ( imgW > maxX )) {
        resizerH('.imgdsp', maxY);
        debugText += "RESIZING 2 imgH ("+imgH+") >= CYR ("+maxY+") && imgW ("+imgW+") >= CXR("+maxX+") => "+maxY+"\n";

        dd   = document.getElementById(d);
        oW   = dd.offsetWidth  + borderW;
        oH   = dd.offsetHeight + borderH;
        imgW = $(".imgdsp").width();
        imgH = $(".imgdsp").height();
        debugText += "Off W      " + oW   + " Off H      " + oH    + "\n";
        debugText += "Img W      " + imgW + " Img H      " + imgH  + "\n";
    }

    scriptDebugger(debugText);    
}


function resizerW( selectors, w ) {
    //http://geekoutwith.me/2011/02/jquery-resizer-resize-objects-that-are-greater-than-a-specified-width/
    jQuery(selectors).each(function() {
        var owidth  = jQuery(this).width();
        var oheight = jQuery(this).height();
        if (owidth > w) {
            var newH = Math.round(oheight * w / owidth);
            jQuery(this).attr({
                width: w,
                height: newH
            });
        }; // endif
    });
}

function resizerH( selectors, h ) {
    //http://geekoutwith.me/2011/02/jquery-resizer-resize-objects-that-are-greater-than-a-specified-width/
    jQuery(selectors).each(function() {
        var oheight = jQuery(this).height();
        var owidth  = jQuery(this).width();
        if (oheight > h) {
            var newW = Math.round(owidth * h / oheight);
            jQuery(this).attr({
                width: newW,
                height: h
            });
        }; // endif
    });
}



function ViewportWidth() {
    if ( self.innerWidth )
        return self.innerWidth;
    else if (document.documentElement && document.documentElement.clientWidth)
        return document.documentElement.clientWidth;
    else if (document.body)
        return document.body.clientWidth;
    else
        return 0;
}

function ViewportHeight() {
    if ( self.innerHeight )
        return self.innerHeight;
    else if (document.documentElement && document.documentElement.clientHeight)
        return document.documentElement.clientHeight;
    else if (document.body)
        return document.body.clientHeight;
    else
        return 0;
}





// Version: July 28, 2007
//var cX = 0; var cY = 0; var rX = 0; var rY = 0; var vW = 0; var vH = 0;

//resizerH('.imgdsp', vH * .85);
//resizerW('.imgdsp', vW * .85);
//updateMouse();
//debugText += " Cursor X          " + cX    + " Cursor Y           " + cY    + "\n";

//var divW   = parseInt(dd1.offsetWidth);
//var divH   = parseInt(dd2.offsetHeight);

//if ( divW > maxWidth ) {
//    divW.style.width = maxWidth;
//}
//
//if ( divH > maxHeight ) {
//    divH.style.height = maxHeight;
//}

//var dd2 = document.getElementById(d);
//AssignPositionCorner(dd2);



//function updateMouse() {
//    if(self.pageYOffset) {
//        rX = self.pageXOffset;
//        rY = self.pageYOffset;
//    }
//    else if(document.documentElement && document.documentElement.scrollTop) {
//        rX = document.documentElement.scrollLeft;
//        rY = document.documentElement.scrollTop;
//    }
//    else if(document.body) {
//        rX = document.body.scrollLeft;
//        rY = document.body.scrollTop;
//    }
//
//    if(document.all) {
//        cX += rX; 
//        cY += rY;
//    }
//}

//function AssignPosition(dd) {
//    updateMouse();
//
//    var oW     = dd.offsetWidth;
//    var oH     = dd.offsetHeight;
//        vW     = ViewportWidth();
//        vH     = ViewportHeight();
//
//    var divW   = parseInt(dd.offsetWidth);
//    var divH   = parseInt(dd.offsetHeight);
//    var disRB  = vW - (cX + 30 + divW);
//    //           screen width - ( mouse x position + 30 + div width )
//    var disBB  = vH - (cY + 30 + divH);
//    //           screen height - ( mouse y position + 30 + div height)
//
//    var debugText  = " OffsetWidth       " + oW    + " OffsetHeight       " + oH    + "\n";
//        debugText += " ViewPortWidth     " + vW    + " ViewPortHeigth     " + vH    + "\n";
//        debugText += " DIV Width         " + divW  + " DIV Height         " + divH  + "\n";
//        debugText += " Cursor X          " + cX    + " Cursor Y           " + cY    + "\n";
//        debugText += " Dist Right Border " + disRB + " Dist Bottom Border " + disBB + "\n";
//
//    if ( disRB < 0) {
//        dd.style.left = (cX - 30 - divW) + 'px';
//        //              mouse pos - 30 - div width
//        debugText += " DIV Left 1 " + (cX - 30 - divW) + "\n";
//    }
//    else {
//        dd.style.left = (cX + 30) + 'px';
//        debugText += " DIV Left 2 " + (cX + 30) + "\n";
//    }
//
//    if ( disBB < 0) {
//        dd.style.top = (cY - divH - 30) + 'px';
//        debugText += " DIV Top 1  " + (cY - divH - 30) + "\n";
//    } 
//    else {
//        dd.style.top = (cY + 30 ) + 'px';
//        debugText += " DIV Top 1 " + (cY + 30)+ "\n";
//    }
//
//    scriptDebugger(debugText);
//}


//function AssignPositionCorner(dd) {
//    dd.style.left = 10 + 'px';
//    dd.style.top  = 60 + 'px';
//
//    scriptDebugger(debugText);
//}


//function ReverseContentDisplay(d) {
//    if( d.length < 1) { return; }
//
//    var dd = document.getElementById(d);
//    AssignPosition(dd);
//
//    if(dd.style.display == "none") { dd.style.display = "block"; }
//    else { dd.style.display = "none"; }
//}

