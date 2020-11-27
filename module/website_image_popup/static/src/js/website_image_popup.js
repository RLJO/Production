$(document).ready(function () {
	activityIndicatorOn = function() {
		if ($('#imagelightbox-loading').length) {
		}else{
			$( '<div id="imagelightbox-loading"><div></div></div>' ).appendTo( 'body' );
		}
	}
	activityIndicatorOff = function() {
		$( '#imagelightbox-loading' ).remove();
	}
    overlayOn = function() {
    	if ($('#imagelightbox-overlay').length) {
		}else{
			$('<div id="imagelightbox-overlay"></div>').appendTo('body');
		}
    }
    overlayOff = function() {
        $('#imagelightbox-overlay').remove();
    }
	closeButtonOn = function(instance) {
		if ($('imagelightbox-close').length) {
		}else{
			$( '<button type="button" id="imagelightbox-close" title="Close"></button>' ).appendTo( 'body' ).on( 'click touchend', function(){ $(this).remove(); instance.quitImageLightbox(); });
		}
	}
	closeButtonOff = function() {
		$( '#imagelightbox-close' ).remove();
	}
    var instanceImage = $('.zoomImg').imageLightbox({
			onStart: function(){overlayOn();closeButtonOn(instanceImage);},
			onEnd: function(){closeButtonOff();overlayOff();activityIndicatorOff();},
			onLoadStart: function(){activityIndicatorOn();},
			onLoadEnd: function(){activityIndicatorOff();}
        });
});
