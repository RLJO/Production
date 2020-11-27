odoo.define('website_image_popup.image_popup', function (require) {
	'use strict';
	var ajax = require('web.ajax');
	var core = require('web.core');
	var s_options = require('web_editor.snippets.options');
	var image_dialog = require('web_editor.widget');
	var check = false;
	var logo = '';
	var bg_image = '';
	var prev_extension;
	var core = require('web.core');
	var QWeb = core.qweb;
	s_options.registry.popup_snippet = s_options.Class.extend({
		start: function(){
			var self = this;
			$(this.$el).find('.add-magnify').click(function(){
				self.zoom_image(self.$target[0]);
			});
			$(this.$el).find('.remove-magnify').click(function(){
				self.remove_zoom_image(self.$target[0]);
			});
			return this._super.apply(this, arguments);
		},
		
		zoom_image : function(target){
			var self = this;
			var current_el = self.$target;
            var new_el = "<a id='zoomImg' href=" + current_el[0].currentSrc + " data-imagelightbox='a' class='zoomImg'>";
            new_el += current_el[0].outerHTML +" </a>";
            var parent_el = self.$target.parent();
            if (!parent_el.hasClass('zoomImg')) {
                current_el.replaceWith(new_el);
            }
            $(self.$target).closest('.o_editable').trigger('content_changed');
		},
		
		remove_zoom_image : function(target){
			var self = this;
			var parent_el = self.$target.parent();
			if (parent_el.hasClass('zoomImg')) {
				self.$target.unwrap();
            }
			$(self.$target).closest('.o_editable').trigger('content_changed');
		}
	});
});
