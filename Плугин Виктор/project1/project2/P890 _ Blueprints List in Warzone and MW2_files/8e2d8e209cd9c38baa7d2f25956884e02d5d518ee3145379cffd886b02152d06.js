
/***!  /components/com_jlexcomment/assets/script.js?v=3.3.8  !***/

function jlexcomment($,config,settings)
{var _this=this,config=config||{};this.config={key:null,sort:'best',timestamp:0,box:null,id:0,request:'/component/jlexcomment',page_comment:1,timestamp_offset:0,parent_id:0};this.browser={contenteditable:null,guest:{name:'',email:''}};this.timestamp={};this.tmpCache={};this.tpl={};String.prototype.hexEncode=function(){var hex,i;var result="";for(i=0;i<this.length;i++){hex=this.charCodeAt(i).toString(16);result+=("000"+hex).slice(-4);}
return result}
$.each(_this.config,function(k,v)
{if(config.hasOwnProperty(k))
{_this.config[k]=config[k];}});if(settings.readmore==1)
{!function(t){"function"==typeof define&&define.amd?define(["jquery"],t):"object"==typeof exports?module.exports=t(require("jquery")):t(jQuery)}(function(t){"use strict";function e(t,e,i){var o;return function(){var n=this,a=arguments,s=function(){o=null,i||t.apply(n,a)},r=i&&!o;clearTimeout(o),o=setTimeout(s,e),r&&t.apply(n,a)}}function i(t){var e=++h;return String(null==t?"rmjs-":t)+e}function o(t){var e=t.clone().css({height:"auto",width:t.width(),maxHeight:"none",overflow:"hidden"}).insertAfter(t),i=e.outerHeight(),o=parseInt(e.css({maxHeight:""}).css("max-height").replace(/[^-\d\.]/g,""),10),n=t.data("defaultHeight");e.remove();var a=o||t.data("collapsedHeight")||n;t.data({expandedHeight:i,maxHeight:o,collapsedHeight:a}).css({maxHeight:"none"})}function n(t){if(!d[t.selector]){var e=" ";t.embedCSS&&""!==t.blockCSS&&(e+=t.selector+" + [data-readmore-toggle], "+t.selector+"[data-readmore]{"+t.blockCSS+"}"),e+=t.selector+"[data-readmore]{transition: height "+t.speed+"ms;overflow: hidden;}",function(t,e){var i=t.createElement("style");i.type="text/css",i.styleSheet?i.styleSheet.cssText=e:i.appendChild(t.createTextNode(e)),t.getElementsByTagName("head")[0].appendChild(i)}(document,e),d[t.selector]=!0}}function a(e,i){this.element=e,this.options=t.extend({},r,i),n(this.options),this._defaults=r,this._name=s,this.init(),window.addEventListener?(window.addEventListener("load",c),window.addEventListener("xresize",c)):(window.attachEvent("load",c),window.attachEvent("resize",c))}var s="readmore",r={speed:100,collapsedHeight:200,heightMargin:16,moreLink:'<a href="#">Read More</a>',lessLink:'<a href="#">Close</a>',embedCSS:!0,blockCSS:"display: block; width: 100%;",startOpen:!1,blockProcessed:function(){},beforeToggle:function(){},afterToggle:function(){}},d={},h=0,c=e(function(){t("[data-readmore]").each(function(){var e=t(this),i="true"===e.attr("aria-expanded");o(e),e.css({height:e.data(i?"expandedHeight":"collapsedHeight")})})},100);a.prototype={init:function(){var e=t(this.element);e.data({defaultHeight:this.options.collapsedHeight,heightMargin:this.options.heightMargin}),o(e);var n=e.data("collapsedHeight"),a=e.data("heightMargin");if(e.outerHeight(!0)<=n+a)return this.options.blockProcessed&&"function"==typeof this.options.blockProcessed&&this.options.blockProcessed(e,!1),!0;var s=e.attr("id")||i(),r=this.options.startOpen?this.options.lessLink:this.options.moreLink;e.attr({"data-readmore":"","aria-expanded":this.options.startOpen,id:s}),e.after(t(r).on("click",function(t){return function(i){t.toggle(this,e[0],i)}}(this)).attr({"data-readmore-toggle":s,"aria-controls":s})),this.options.startOpen||e.css({height:n}),this.options.blockProcessed&&"function"==typeof this.options.blockProcessed&&this.options.blockProcessed(e,!0)},toggle:function(e,i,o){o&&o.preventDefault(),e||(e=t('[aria-controls="'+this.element.id+'"]')[0]),i||(i=this.element);var n=t(i),a="",s="",r=!1,d=n.data("collapsedHeight");n.height()<=d?(a=n.data("expandedHeight")+"px",s="lessLink",r=!0):(a=d,s="moreLink"),this.options.beforeToggle&&"function"==typeof this.options.beforeToggle&&this.options.beforeToggle(e,n,!r),n.css({height:a}),n.on("transitionend",function(i){return function(){i.options.afterToggle&&"function"==typeof i.options.afterToggle&&i.options.afterToggle(e,n,r),t(this).attr({"aria-expanded":r}).off("transitionend")}}(this)),t(e).replaceWith(t(this.options[s]).on("click",function(t){return function(e){t.toggle(this,i,e)}}(this)).attr({"data-readmore-toggle":n.attr("id"),"aria-controls":n.attr("id")}))},destroy:function(){t(this.element).each(function(){var e=t(this);e.attr({"data-readmore":null,"aria-expanded":null}).css({maxHeight:"",height:""}).next("[data-readmore-toggle]").remove(),e.removeData()})}},t.fn.readmore=function(e){var i=arguments,o=this.selector;return e=e||{},"object"==typeof e?this.each(function(){if(t.data(this,"plugin_"+s)){var i=t.data(this,"plugin_"+s);i.destroy.apply(i)}e.selector=o,t.data(this,"plugin_"+s,new a(this,e))}):"string"==typeof e&&"_"!==e[0]&&"init"!==e?this.each(function(){var o=t.data(this,"plugin_"+s);o instanceof a&&"function"==typeof o[e]&&o[e].apply(o,Array.prototype.slice.call(i,1))}):void 0}});}
this.box=this.config.box==null?null:$(this.config.box);this.dialog=function(options)
{var _dialog=this,settings={caption:_this.lang.get('dialog'),submitLabel:_this.lang.get('submit'),cancelLabel:_this.lang.get('cancel'),content:'',loadfn:null,submitfn:null,cancelfn:null};if(typeof options=='object')$.extend(settings,options);_dialog.init=function()
{var html='<div class="jcm-overlay">';html+='<div class="jcm-dialog">';html+='<div class="jcm-dg-caption">'+settings.caption+'</div>';html+='<div class="jcm-dg-error"></div>';html+='<div class="jcm-dg-content">'+settings.content+'</div>';html+='<div class="jcm-dg-footer">';if(settings.submitLabel!==false)
{html+='<button class="jcm-dg-submit">'+settings.submitLabel+'</button>';}
html+='<button class="jcm-dg-cancel">'+settings.cancelLabel+'</button>';html+='</div>';html+='</div>';html+='</div>';_dialog.el=$(html);_dialog.el.appendTo('body');if(typeof settings.loadfn=='function')
settings.loadfn(_dialog);_dialog.el.on('click','.jcm-dg-submit',function(){if(typeof settings.submitfn=='function')
settings.submitfn(_dialog);});_dialog.el.on('click','.jcm-dg-cancel',function(){if(typeof settings.cancelfn=='function')
{var rn=settings.cancelfn(_dialog);if(rn!==false)
{_dialog.off();}}else{_dialog.off();}});var resizeEvent=function()
{if(!$('.jcm-dialog').length)
{return false;}
var widthOfScreen=$(window).width(),heightOfScreen=$(window).width();if(widthOfScreen<=450)
{_dialog.el.find('.jcm-dialog').removeClass('wide touch').removeAttr('style').addClass('touch');$('html,body').addClass('disableScroll');}else{_dialog.el.find('.jcm-dialog').removeClass('wide touch').removeAttr('style').addClass('wide');var widthOfdialog=widthOfScreen>650?600:(widthOfScreen-40),left=(widthOfScreen-widthOfdialog)/2,maxHeight=heightOfScreen-50-30;_dialog.el.find('.jcm-dialog').css({width:widthOfdialog+'px',left:left+'px','max-height':maxHeight+'px'});$('html,body').removeClass('disableScroll');}}
resizeEvent();$(window).resize(function(){resizeEvent();});};_dialog.off=function()
{_dialog.el.off();_dialog.el.fadeOut('fast',function(){$(this).remove();$('html,body').removeClass('disableScroll');});};_dialog.setError=function(msg)
{_dialog.el.find('.jcm-dg-error').addClass('active').html(msg);};_dialog.clearError=function()
{_dialog.el.find('.jcm-dg-error').removeClass('active').html('');};_dialog.overlay=function()
{if(!_dialog.el.find('.jcm-dg-overlay').length)
{_dialog.el.find('.jcm-dg-content').append('<div class="jcm-dg-overlay"></div>');_dialog.el.find('button').attr('disabled','disabled');}};_dialog.unOverlay=function()
{_dialog.el.find('.jcm-dg-overlay').remove();_dialog.el.find('button').removeAttr('disabled');};_dialog.init();};this.sticker_data=null;this.sticker_found={};this.sticker=function(options)
{var _sticker=this,stCf={parent:null,selected:null},state={gid:0,query:''};if(typeof options=='object')$.extend(stCf,options);this.el=null;this.init=function()
{var html='<div class="jcm-sticker">';html+='<div class="_header"></div>';html+='<div class="_content"></div>';html+='</div>';_sticker.el=$(html);if(_this.sticker_data==null)
{$.get(_this.helper.url({task:'sticker.group'}),function(d){if(typeof d=='object')
_this.sticker_data=d;_sticker.createHeader();_sticker.loadStickers();},'json');}else{_sticker.createHeader();_sticker.loadStickers();}
stCf.parent.empty();_sticker.el.appendTo(stCf.parent);_sticker.events();};this.events=function()
{_sticker.el.on('click','.jcm-sticker-group a',function(){var gid=$(this).attr('data-id')*1;state.gid=gid;_sticker.loadStickers();});_sticker.el.on('click','.jcm-sticker-home',function(e){e.preventDefault();state.gid=0;state.query='';_sticker.el.find('.jcm-sticker-active').parent().remove();_sticker.el.find('input[type=text]').val('');_sticker.loadStickers();}).on('click','.jcm-btn-image',function(e){e.preventDefault();var _el=$('<input type="file" style="width:1px;height:1px;overflow:hidden">');_el.appendTo('body');_el.change(function(evt){if(evt.target.files.length!=1||typeof stCf.selected!='function')return false;var oUrl=window.webkitURL||window.URL;stCf.selected(0,oUrl.createObjectURL(evt.target.files[0]),function($imger){var stDt=new FormData();stDt.append('file',evt.target.files[0]);var xhr=$.ajax({url:_this.helper.url({task:'sticker.upload'}),data:stDt,processData:false,contentType:false,dataType:'json',xhr:function(){var xhrobj=$.ajaxSettings.xhr();if(xhrobj.upload){var prs='<div class="_process_bar">';prs+='<div class="_process_result"><span class="_moved"><span class="_tx">0</span>/100</span></div>';prs+='</div>';$imger.find('._stir_loading').append(prs);xhrobj.upload.addEventListener('progress',function(event){var percent=0;var position=event.loaded||event.position;var total=event.total;if(event.lengthComputable)
{percent=Math.ceil(position/total*100);}
$imger.find('._process_result').css('width',percent+'%');$imger.find('._tx').text(percent);},false);}
return xhrobj;},type:'POST',success:function(d){if(d.status==200)
{$imger.find('input[name=sticker_id]').val(d.data.id);$imger.find('._stir_loading').fadeOut('fast',function(){$(this).remove();});}}});});});_el.trigger('click');}).on('keypress','input[type=text]',function(e){if(e.which==13)
{state.query=$(this).val();_sticker.loadStickers();return false;}}).on('click','.jcm-sticker-id',function(){var id=$(this).attr('data-id')*1;if(typeof stCf.selected=='function')
stCf.selected(id,$(this).find('img').attr('src'));});};this.createHeader=function()
{var html='<ul class="jcm-sticker-gp-hl">';html+='<li><a href="javascript:void(0)" class="jcm-sticker-home"><i class="fas fa-home"></i> '+_this.lang.get('home')+'</a></li>';if(settings.sticker_photo)
{html+='<li><a href="javascript:void(0)" class="jcm-btn-image"><i class="fas fa-upload"></i> '+_this.lang.get('use_your_image')+'</a></li>';}
html+='</ul>';html+='<input type="text" placeholder="'+_this.lang.get('search_sticker')+'" />';_sticker.el.find('._header').empty().append(html);};this.loadStickers=function()
{if(state.gid==0&&/^\s*$/.test(state.query))
{var html='';if(!_this.sticker_data.length)
{html='<span>'+_this.lang.get('no_sticker_found')+'.</span>';}else{html='<ul class="jcm-sticker-group">';$.each(_this.sticker_data,function(k,v){html+='<li><a href="javascript:void(0)" data-id="'+v.id+'">'+v.name+'</a></li>';});html+='</ul>';}
_sticker.el.find('._content').empty().append(html);}else{state.query=/^\s*$/.test(state.query)?'':$.trim(state.query);var key=state.gid+'_'+state.query.hexEncode(),bind=function(data)
{var html='';if(typeof data=='object'&&data.length)
{html+='<ul class="_list-stickers">';$.each(data,function(k,v){html+='<li>';html+='<a href="javascript:void(0)" class="jcm-sticker-id" data-id="'+v.id+'">';html+='<img src="'+v.url+'" alt="" />';html+='</a>';html+='</li>';});html+='</ul>';}else{html='<span>'+_this.lang.get('no_sticker_found')+'.</span>';}
_sticker.el.find('._content').empty().append(html);};if(state.query=='')
{var group_name='';$.each(_this.sticker_data,function(k,v){if(v.id==state.gid)
group_name=v.name;});var group_active='<li><a href="javascript:void(0)" class="jcm-sticker-active">'+group_name+'</a></li>';_sticker.el.find('.jcm-sticker-gp-hl').append(group_active);}
if(_this.sticker_found.hasOwnProperty(key))
{bind(_this.sticker_found[key]);}else{$.get(_this.helper.url({task:'sticker.load'}),{id:state.gid,query:state.query},function(d){_this.sticker_found[key]=d;bind(_this.sticker_found[key]);},'json');}}};this.init();};this.lang={data:{},load:function(langs)
{_this.lang.data=langs;},get:function()
{if(!arguments.length)return'';if(_this.lang.data.hasOwnProperty(arguments[0]))
{if(arguments.length==1)
{return _this.lang.data[arguments[0]];}else{var str=_this.lang.data[arguments[0]];for(var i=1;i<=arguments.length;i++){str=str.replace(/(\%s)/,arguments[i]);}
return str;}}
return arguments[0];}};this.helper={url:function(params)
{params['t']=new Date().getTime();return _this.config.request
+(_this.config.request.indexOf('?')==-1?'?':'&')
+$.param(params);},cookie:{set:function(cname,cvalue,exdays)
{var d=new Date();d.setTime(d.getTime()+(exdays*24*60*60*1000));var expires="expires="+d.toUTCString();document.cookie=cname+"="+cvalue+";"+expires+";path=/";},get:function(cname)
{var name=cname+"=";var decodedCookie=decodeURIComponent(document.cookie);var ca=decodedCookie.split(';');for(var i=0;i<ca.length;i++){var c=ca[i];while(c.charAt(0)==' '){c=c.substring(1);}
if(c.indexOf(name)==0){return c.substring(name.length,c.length);}}
return null;},earse:function(cname)
{document.cookie=cname+"=0; expires=Thu, 18 Dec 2013 12:00:00 UTC";}},};this.createCmform=function(dest,data,openform)
{var form=_this.tpl.form.clone();form.removeAttr("id");setTimeout(function(){if(form.width()<=450){form.addClass('jcm-form-xs');}},500);if(typeof data=="object")
{if(!data.member)
{form.find('#jcm-input-name-field').val(data.guest_name);form.find('#jcm-input-email-field').val(data.guest_email);}
delete data.member;delete data.guest_name;delete data.guest_email;if(data.locked==1)
form.find('[name=locked]').prop('checked',true);delete data.locked;$.each(data,function(k,v)
{if(v==null||typeof v=='object')return true;if(form.find('[name="'+k+'"]').length||form.find('[data-name="'+k+'"]').length)
{if(k=='comment'&&_this.browser.contenteditable)
{form.find('.jcm-textarea').html(v.replace(/\n/g,'<br>'));if(typeof twemoji=='object')
{twemoji.parse(form.find('.jcm-textarea')[0]);}}else{if(form.find('[name="'+k+'"]').length)
{form.find('[name="'+k+'"]').val(v);}else{form.find('[data-name="'+k+'"]').text(v);}}
delete data[k];}});$.each(data,function(k,v)
{if(v==null||typeof v=='object')
{return true;}
var input=$('<input type="hidden" />');input.attr('name',k);input.attr('value',v);input.appendTo(form.find('form'));});}
_this.createFormEvents(form,data,openform);form.appendTo(dest);return form;};this.emoji={loaded:false,input:null,init:function(){if(typeof EmojiPanel=="undefined")return;$('#jcm-emoji').appendTo('body');ej=new EmojiPanel({container:'#jcm-emoji',trigger:'.jcm-uk',json_url:settings.url_base+'/components/com_jlexcomment/assets/emojis.json'});setTimeout(function(){if(typeof twemoji=='object')
twemoji.parse($('#jcm-emoji')[0],{className:"ej"});},1000);ej.addListener('select',function(emoji){if(_this.emoji.input==null)return;_this.emoji.input.focus();if(_this.browser.contenteditable==true)
{var sel,range,ejCt='<img draggable="false" class="emoji" alt="'+emoji.char+'" src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/72x72/'+emoji.unicode+'.png">',node=$(ejCt)[0];if(window.getSelection){sel=window.getSelection();if(sel.getRangeAt&&sel.rangeCount)
{range=sel.getRangeAt(0);range.deleteContents();range.insertNode(node);range=range.cloneRange();range.setStartAfter(node);range.collapse(true);sel.removeAllRanges();sel.addRange(range);}}else if(document.selection&&document.selection.type!="Control"){document.selection.createRange().pasteHTML(ejCt);}}else{var field=_this.emoji.input[0];if(document.selection){document.selection.createRange().text=emoji.char;}else if(field.selectionStart||field.selectionStart=='0'){var startPos=field.selectionStart,endPos=field.selectionEnd;field.value=field.value.substring(0,startPos)
+emoji.char
+field.value.substring(endPos,field.value.length);}else{field.value+=emoji.char;}}});$('body').on('click',function(e){if(!$(e.target).closest('#jcm-emoji.active').length&&!$(e.target).closest('.jcm-btn-emoticon').length){$('#jcm-emoji.active, .jcm-btn-emoticon.active').removeClass('active');}});},toggle:function($btn){if($btn.hasClass('active'))
{$btn.removeClass('active');$('#jcm-emoji').removeClass('active');}else{$('.jcm-btn-emoticon').not($btn).removeClass('active');$btn.addClass('active');$('#jcm-emoji').addClass('active');_this.emoji.follow($btn);}},follow:function($btn)
{var $ej=$('#jcm-emoji');var ejTop=$btn.offset().top-$ej.height(),ejLeft=$btn.offset().left;if(ejLeft+$ej.width()>$(window).width())
ejLeft=0;$ej.css('left',ejLeft+'px');$ej.css('top',ejTop+'px');}};this.styles=null;this.createFormEvents=function(form,cdata,openform)
{var html_sticker=function(id,url){form.find('.jcm-sticker-preview').off();form.find('.jcm-sticker-preview').remove();var preview='<div class="jcm-sticker-preview">';preview+='<div class="_img_box">';preview+='<img src="'+url+'" alt="">';if(id==0)
{preview+='<div class="_stir_loading"></div>';}
preview+='<input type="hidden" name="sticker_id" value="'+id+'" />';preview+='</div>';preview+='<div class="clearfix"></div>';preview+='<a href="javascript:void(0)" class="_remove jcm-tooltip" title="'+_this.lang.get('remove')+'"><i class="fas fa-times" style="font-size:20px;color:#777"></i></a>';preview+='</div>';preview=$(preview);preview.on('click','._remove',function(){preview.off();preview.remove();});form.find('.jcm-input-cm').after(preview);return preview;},html_media=function(file,state)
{var state=typeof state=='undefined'?'_rlt_process':state,getExtension=function(name)
{var result=name.match(/\.([A-z0-9]+)$/);if(result==null)
{return'unknown';}
return result[1];},formatSize=function(size){if(size>1000*1000*1000){size=parseInt(size/(1000*1000*1000))+' Gb';}else if(size>1000*1000){size=parseInt(size/(1000*1000))+' Mb';}else{size=parseInt(size/1000)+' Kb';}
return size;},preview='<div class="jcm-media-preview '+state+'">';preview+='<span class="jcm-ext _ext_">'+getExtension(file.name)+'</span>';preview+='<div class="jcm-info">';preview+='<span class="_caption">'+file.name+'</span>';preview+='<span class="_size">'+formatSize(file.fileSize)+'</span>';preview+='<a href="javascript:void(0)" class="_edit">'+_this.lang.get('edit')+'</a>';preview+='<div class="_error"></div>';preview+='<div class="_process_cont">';preview+='<div class="_process_box">';preview+='<div class="_process_bar"></div>';preview+='</div>';preview+='<span class="_process_text"><span class="_process_result">0</span>/100%</span>';preview+='</div>';preview+='<span class="_desc">'+file.description+'</span>';preview+='<div class="_form_edit">';preview+='<span class="_form_error"></span>';preview+='<label>'+_this.lang.get('caption')+'</label>';preview+='<input type="text" />';preview+='<label>'+_this.lang.get('description')+'</label>';preview+='<textarea></textarea>';preview+='<button type="button" class="jcm-button-hl _submit_edit">'+_this.lang.get('update')+'</button>';preview+='<button type="button" class="jcm-button _cancel_edit">'+_this.lang.get('cancel')+'</button>';preview+='</div>';preview+='<div class="_task">';preview+='<a href="javascript:void(0)" class="_remove fas fa-times jcm-tooltip" style="font-size:20px" title="'+_this.lang.get('remove')+'"></a>';preview+='<a href="javascript:void(0)" class="_cancel fas fa-times jcm-tooltip" style="font-size:20px" title="'+_this.lang.get('cancel')+'"></a>';preview+='</div>';preview+='</div>';preview+='<div class="clearfix"></div>';preview+='<input type="hidden" class="_media_id" name="media_cid[]" value="'+(file.hasOwnProperty('id')?file.id:'')+'" />';preview+='</div>';preview=$(preview);preview.on('click','._remove',function(){preview.off();preview.remove();if(!form.find('.jcm-media-preview').length)
{form.find('._media_box').remove();}}).on('click','._edit',function(){preview.removeClass('_rlt_completed').addClass('_rlt_editing');preview.find('input[type=text]').val(preview.find('._caption').text());var desc=preview.find('._desc').text();preview.find('textarea').val(desc.replace(/<br\s*[\/]?>/gi,"\n"));}).on('click','._submit_edit',function(){var data={id:preview.find('._media_id').val()*1,name:preview.find('input[type=text]').val(),description:preview.find('textarea').val()};if(/^\s*$/.test(data.name))
{preview.find('input[type=text]').focus();return false;}
preview.find('button,input,textarea').attr('disabled','disabled');$.post(_this.helper.url({task:'media.update'}),data,function(d){preview.find('button,input,textarea').removeAttr('disabled');if(d.status==200)
{preview.find('._caption').text(data.name);preview.find('._desc').html(data.description.replace("\n","<br>"));preview.addClass('_rlt_completed').removeClass('_rlt_editing');preview.find('._form_edit ._form_error').hide();}else{preview.find('._form_edit ._form_error').show().text(d.error);}},'json');}).on('click','._cancel_edit',function(){preview.addClass('_rlt_completed').removeClass('_rlt_editing');});if(!form.find('._media_box').length)
{form.find('._controller').before('<div class="_media_box"></div>');}
preview.appendTo(form.find('._media_box'));return preview;},html_giphy=function(giphyId){var regexGiphy=/^([A-z0-9]+),([1-9][0-9]*),([1-9][0-9]*)$/;if(!regexGiphy.test(giphyId))return;var attrs=giphyId.match(regexGiphy);form.find('.jcm-sticker-preview').off();form.find('.jcm-sticker-preview').remove();form.find('input[name=giphy_id]').remove();var gp='<div class="jcm-sticker-preview">';gp+='<div class="giphy-item">';gp+='<div style="width:100%;height:0;padding-bottom:'+parseInt(attrs[3]*100/attrs[2])+'%;position:relative;"><iframe src="https://giphy.com/embed/'+attrs[1]+'" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>';gp+='<div class="gif-overlay"></div>';gp+='</div>';gp+='<input type="hidden" name="giphy_id" value="'+giphyId+'" />';gp+='<div class="clearfix"></div>';gp+='<a href="javascript:void(0)" class="_remove jcm-tooltip" title="'+_this.lang.get('remove')+'"><i class="fas fa-times" style="font-size:20px;color:#777"></i></a>';gp+='</div>';gp=$(gp);gp.on('click','._remove',function(){gp.off();gp.remove();});form.find('.jcm-input-cm').after(gp);},mapData={name:'',icon:'',address:'',lat:null,lng:null};if(typeof cdata=='object')
{if(cdata.hasOwnProperty('sticker'))
{html_sticker(cdata.sticker.id,cdata.sticker.url);}
if(cdata.hasOwnProperty('giphy_id'))html_giphy(cdata.giphy_id);if(cdata.params!=null&&cdata.params.hasOwnProperty('map')&&!/^\s*$/.test(cdata.params.map.address))
{mapData=cdata.params.map;form.find('.jcm-map-status,.jcm-btn-geo').addClass('active');if(mapData.hasOwnProperty('name'))
{form.find('.jcm-btn-geo-status').html('<b>'+mapData.name+'</b> ('+mapData.address+')');}else{form.find('.jcm-btn-geo-status').text(mapData.address);}}
if(cdata.media!=null&&cdata.media.length)
{$.each(cdata.media,function(k,file){html_media(file,'_rlt_completed');});}
if(typeof openform=='undefined'||openform==true)
{window.setTimeout(function(){form.find('.jcm-textarea').focus();},200);}
form.on('click','.jcm-btn-cancel',function(){if(form.find('.jcm-btn-emoticon').hasClass('active'))form.find('.jcm-btn-emoticon').trigger('click');var bodyCm=_this.box.find('#comment-'+cdata.id+' > .jcm-post-content');bodyCm.children('.jcm-comment-edit').remove();bodyCm.children('.jcm-flex-content').show();$('#comment-'+cdata.id).removeClass('editing');});}
if(!settings.member&&(typeof cdata!='object'||(typeof cdata=='object'&&!cdata.hasOwnProperty('guest_name'))))
{var guestName=_this.helper.cookie.get('jcmGuestName'),guestEmail=_this.helper.cookie.get('jcmGuestEmail');if(guestName!=null)form.find('#jcm-input-name-field').val(guestName);if(guestEmail!=null)form.find('#jcm-input-email-field').val(guestEmail);}
let mdialog=null;form.on('click','.jcm-btn-upload',function(){mdialog=new _this.dialog({caption:_this.lang.get('notice'),content:_this.lang.get('media_msg')+'<button class="jup">'+_this.lang.get('select_files')+'</button><div class="or_text">'+_this.lang.get('or')+'</div><div class="dropHere">'+_this.lang.get('drag_drop')+'</div>',loadfn:function(dialog){let handleFileUpload=function(files,callback)
{let _elbusy=false;if(!files)return false;let numfile=form.find('._media_box').find('._rlt_completed, ._rlt_editing, ._rlt_process').length;if(settings.maxfilenum>0&&(numfile+files.length)>settings.maxfilenum)
{alert(_this.lang.get('maxfilenum_alert'));return;}
$.each(files,function(k,file){var data=new FormData(),filePreview=html_media({name:file.name,description:'',fileSize:file.size});if(typeof FormData=='undefined')
{alert(_this.lang.get('upgrade_client_browser'));}else{data.append('file',file);let _elTm=window.setInterval(function(){if(_elbusy)return;_elbusy=true;clearInterval(_elTm);var xhr=$.ajax({url:_this.helper.url({task:'media.upload'}),data:data,processData:false,contentType:false,dataType:'json',xhr:function(){var xhrobj=$.ajaxSettings.xhr();if(xhrobj.upload){xhrobj.upload.addEventListener('progress',function(event){var percent=0;var position=event.loaded||event.position;var total=event.total;if(event.lengthComputable){percent=Math.ceil(position/total*100);}
filePreview.find('._process_bar').css('width',percent+'%');filePreview.find('._process_result').text(percent);},false);}
return xhrobj;},type:'POST',success:function(d){_elbusy=false;if(d.status==200){filePreview.removeClass('_rlt_process').addClass('_rlt_completed');filePreview.find('._media_id').val(d.id);}else{filePreview.removeClass('_rlt_process').addClass('_rlt_error');filePreview.find('._error').text(d.error);}}});filePreview.on('click','._cancel',function(){if(typeof xhr!='undefined'){xhr.abort();_elbusy=false;}
filePreview.fadeOut(function(){$(this).remove();});});},100);}});};let checkValidFile=function(){let numfile=form.find('._media_box').find('._rlt_completed, ._rlt_editing, ._rlt_process').length;if(typeof mdialog!=null)
mdialog.off();if(settings.maxfilenum>0&&numfile>=settings.maxfilenum)
{alert(_this.lang.get('maxfilenum_alert'));return false;}
return true;};dialog.el.find('.dropHere').on('dragenter',function(e){e.stopPropagation();e.preventDefault();$(this).addClass('active');}).on('dragover',function(e){e.stopPropagation();e.preventDefault();}).on('drop',function(e){$(this).removeClass('active');e.preventDefault();if(!checkValidFile())return;handleFileUpload(e.originalEvent.dataTransfer.files);});$(document).on('dragenter',function(e){e.stopPropagation();e.preventDefault();}).on('dragover',function(e){e.stopPropagation();e.preventDefault();dialog.el.find('.dropHere').removeClass('active');}).on('drop',function(e){e.stopPropagation();e.preventDefault();});dialog.el.find('.jcm-dialog').addClass('uploadFile');dialog.el.find('.jup').click(function(){let _el=$('<input type="file" multiple style="width:1px;height:1px;overflow:hidden" />');let _elbusy=false;_el.appendTo('body');if(!checkValidFile())return;_el.change(function(evt){handleFileUpload(evt.target.files);});_el.trigger('click');});},submitLabel:false,cancelLabel:_this.lang.get('ok')});});if(_this.browser.contenteditable)
{var $tools=form.find('.jcm-text-fm'),editorFocus=false,getSelectedNode=function(){if(document.selection)
return document.selection.createRange().parentElement();else
{var selection=window.getSelection();if(selection.rangeCount>0)
return selection.getRangeAt(0).startContainer.parentNode;}};form.find('.jcm-textarea').on('focus blur',function(e){editorFocus=e.type=='focus';});$tools.removeClass('hide');window.setInterval(function(){if(!editorFocus)return;var $el=$(getSelectedNode());if($el.is('a')){$tools.find('[data-tag=unlink]').show();$tools.find('[data-tag=createLink]').removeAttr('disabled').addClass('active');}else{$tools.find('[data-tag=unlink]').hide();$tools.find('[data-tag=createLink]').removeClass('active');if(window.getSelection().toString()!=''){$tools.find('[data-tag=createLink],[data-tag=code],[data-tag=quote]').removeAttr('disabled');}else{$tools.find('[data-tag=createLink],[data-tag=code],[data-tag=quote]').attr('disabled','disabled');}}
var listCmd=['bold','italic','underline','strikeThrough'];$.each(listCmd,function(k,cmd){if(document.queryCommandState(cmd)){$tools.find('[data-tag='+cmd+']').addClass('active');}else{$tools.find('[data-tag='+cmd+']').removeClass('active');}});},500);$tools.on('click','[data-tag]',function(e){e.preventDefault();var tag=$(this).attr('data-tag');switch(tag)
{case'createLink':var $el=$(getSelectedNode()),oldlink='';if($el.is('a'))
{oldlink=$el.attr('href');var range=document.createRange();range.selectNodeContents($el[0]);var sel=window.getSelection();sel.removeAllRanges();sel.addRange(range);}
var link=prompt(_this.lang.get('insert_your_link'),oldlink);if(link!=null){if(!/(https?:\/\/[^\s]+)/g.test(link)){alert(_this.lang.get('link_format_incorrect'));return;}
document.execCommand("CreateLink",false,link);}
break;case'unlink':var $el=$(getSelectedNode());if(!$el.is('a'))return;$el.contents().unwrap('a');break;case'quote':case'code':document.execCommand("insertHTML",false,'<div data-tag="'+tag+'">'+document.getSelection().toString().replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#039;").replace(/\t/g,'&nbsp;&nbsp;&nbsp;&nbsp;')+'</div><br>');break;default:document.execCommand(tag,false,null);if(window.getSelection().toString()=='')
form.find('.jcm-textarea').focus();break;}});}
var dialogSticker=null;form.on('click','.jcm-btn-sticker',function(){if(dialogSticker!=null)
return false;dialogSticker=new _this.dialog({caption:_this.lang.get('sticker'),content:_this.lang.get('please_wait'),submitLabel:false,cancelfn:function(dialog)
{dialogSticker=null;},loadfn:function(dialog)
{dialog.el.find('.jcm-dialog').addClass('sticker');new _this.sticker({parent:dialog.el.find('.jcm-dg-content'),selected:function(id,url,cb){var comment=form.find('.jcm-textarea').is('textarea')?form.find('.jcm-textarea').val():form.find('.jcm-textarea').text();if(settings.sticker_autopost==1&&typeof cb=='undefined')
{if(/^\s*$/.test(comment)&&!form.find('.forGuest').length)
{form.find('form').append('<input type="hidden" name="sticker_id" value="'+id+'" />');form.find('form').trigger('submit');}else{html_sticker(id,url);}}else{$imger=html_sticker(id,url);if(typeof cb=='function')cb($imger);}
dialog.off();dialogSticker=null;}});}});});var dialogMap=null;form.on('click','.jcm-btn-geo,.jcm-btn-geo-status',function(){if(dialogMap!=null)
return false;var mapDataTmp=mapData;dialogMap=new _this.dialog({caption:_this.lang.get('embed_location'),content:'<div class="mapContent">'+_this.lang.get('please_wait')+'</div>',submitLabel:_this.lang.get('add'),submitfn:function(dialog)
{mapData=mapDataTmp;dialog.off();dialogMap=null;if(!form.find('input[name=map_lat]').length)
{var html='<input type="hidden" name="map_lat" value= ""/>';html+='<input type="hidden" name="map_lng" value= ""/>';html+='<input type="hidden" name="map_address" value= ""/>';html+='<input type="hidden" name="map_name" value= ""/>';html+='<input type="hidden" name="map_icon" value= ""/>';form.find('form').append(html);}
form.find('input[name=map_lat]').val(mapData.lat);form.find('input[name=map_lng]').val(mapData.lng);form.find('input[name=map_address]').val(mapData.address);form.find('input[name=map_name]').val(mapData.name);form.find('input[name=map_icon]').val(mapData.icon);form.find('.jcm-map-status,.jcm-btn-geo').addClass('active');if(mapData.hasOwnProperty('name'))
{form.find('.jcm-btn-geo-status').html('<b>'+mapData.name+'</b> ('+mapData.address+')');}else{form.find('.jcm-btn-geo-status').text(mapData.address);}},cancelfn:function(dialog)
{dialogMap=null;},loadfn:function(dialog)
{dialog.el.find('.jcm-dialog').addClass('map');window.setTimeout(function()
{var map=new google.maps.Map(dialog.el.find(".mapContent")[0],{center:{lat:-33.8688,lng:151.2195},zoom:13}),html='<div class="pac-box"><input type="text" class="pac-input" /></div>';html+='<div class="infowindow-content">';html+='<img src="" alt="" width="16" height="16" class="_icon">';html+='<span class="_name"  class="title"></span><br>';html+='<span class="_address"></span></div>';dialog.el.find('.jcm-dg-content').prepend(html);var input=dialog.el.find('input.pac-input'),pac_box=dialog.el.find('.pac-box')[0];map.controls[google.maps.ControlPosition.TOP_RIGHT].push(pac_box);var autocomplete=new google.maps.places.Autocomplete(input[0]);autocomplete.bindTo('bounds',map);var infowindow=new google.maps.InfoWindow(),infowindowContent=dialog.el.find('.infowindow-content');infowindow.setContent(infowindowContent[0]);var marker=new google.maps.Marker({map:map,anchorPoint:new google.maps.Point(0,-29)});if(mapData.lat!=null)
{var marker_loc=new google.maps.LatLng(mapData.lat,mapData.lng);marker.setPosition(marker_loc);marker.setVisible(true);input.val(mapData.address);if(mapData.hasOwnProperty('name'))
{infowindowContent.find('._name').text(mapData.name);}
infowindowContent.find('._address').text(mapData.address);infowindowContent.find('._icon').attr("src",mapData.icon);infowindow.open(map,marker);}
autocomplete.addListener('place_changed',function(){infowindow.close();marker.setVisible(false);var place=autocomplete.getPlace();if(!place.geometry)
{window.alert(_this.lang.get("map_not_found")+": '"+place.name+"'");return;}
if(place.geometry.viewport)
{map.fitBounds(place.geometry.viewport);}else{map.setCenter(place.geometry.location);map.setZoom(17);}
marker.setPosition(place.geometry.location);marker.setVisible(true);var address='';if(place.address_components)
{address=[(place.address_components[0]&&place.address_components[0].short_name||''),(place.address_components[1]&&place.address_components[1].short_name||''),(place.address_components[2]&&place.address_components[2].short_name||'')].join(' ');}
infowindowContent.find('._icon').attr("src",place.icon);infowindowContent.find('._name').text(place.name);infowindowContent.find('._address').text(address);infowindow.open(map,marker);mapDataTmp.lat=marker.getPosition().lat();mapDataTmp.lng=marker.getPosition().lng();mapDataTmp.name=place.name;mapDataTmp.address=address;mapDataTmp.icon=place.icon;});},300);}});}).on('click','.jcm-empty-geo',function(){form.find('[name="map_lat"],[name="map_lng"],[name="map_address"]').remove();mapData={name:'',icon:'',address:'',lat:null,lng:null};form.find('.jcm-map-status,.jcm-btn-geo').removeClass('active');});form.on('click','.jcm-btn-emoticon',function(){_this.emoji.input=form.find('.jcm-textarea');_this.emoji.toggle($(this));});form.on('click','.jcm-btn-style',function(){var sl=null,slId=parseInt(form.find('[name=style_id]').val());slId=(isNaN(slId)||slId<1)?0:slId;_this.dialog({caption:_this.lang.get('cm_style'),content:_this.lang.get('please_wait'),submitLabel:_this.lang.get('apply'),loadfn:function(dialog)
{var slCallback=function(){var ls=$('<div class="jcm-styles"></div>');$.each(_this.styles,function(k,v)
{var item='<div class="jcm-style-item'+(v.id==slId?' active':'')+'">'+v.caption+'</div>';item=$(item);if(v.id==slId)sl=v;item.attr('style',v.css);item.appendTo(ls);item.click(function(){if(item.hasClass('active'))
{item.removeClass('active');slId=0;sl=null;return;}
item.addClass('active');item.siblings().removeClass('active');slId=v.id;sl=v;});});dialog.el.find('.jcm-dg-content').empty().append(ls);};if(_this.styles==null){$.post(_this.helper.url({task:'others.styles'}),function(d){_this.styles=d;if(d==null)
{dialog.el.find('.jcm-dg-content').html('<span>'+_this.lang.get('no_style')+'</span>');return;}
slCallback();},'json');}else{slCallback();}},submitfn:function(dialog)
{if(form.find('[name=style_id]').length)
{form.find('[name=style_id]').val(slId);}else{form.find('.jcm_form_input').append('<input type="hidden" name="style_id" value="'+slId+'">');}
if(sl)
{form.find('.jcm-textarea').attr('style',sl.css);form.find('.jcm-input-cm').addClass('_style');if(sl.maxlength>0)settings.cm_max_length=sl.maxlength*1;}else{form.find('.jcm-textarea').removeAttr('style');form.find('.jcm-input-cm').removeClass('_style');settings.cm_max_length=0;}
form.find('.jcm-textarea').focus();dialog.off();}});});form.on('click','.jcm-btn-gif',function(){if(settings.giphy=='')return;var gh='<div>';gh+='<div class="gif-input">';gh+='<input type="text" placeholder="'+_this.lang.get('find_gif_image')+'">'
gh+='</div>';gh+='<div class="gif-output"></div>';gh+='</div>';var dialogGif=new _this.dialog({caption:_this.lang.get('giphy'),content:gh,submitLabel:false,loadfn:function(dialog)
{dialog.el.find('.jcm-dialog').addClass('giphy');let giphyId=null,giphyFinder=null;dialog.el.find('input[type="text"]').keypress(function(){if(giphyFinder!=null)clearTimeout(giphyFinder);giphyFinder=setTimeout(function(){var giphyQuery=$.trim(dialog.el.find('input[type="text"]').val());if(giphyQuery.length<3)return;var giphyOutput=dialog.el.find('.gif-output');giphyOutput.empty().append(_this.lang.get('please_wait'));$.get('https://api.giphy.com/v1/gifs/search?api_key='+settings.giphy+'&limit=15&q='+giphyQuery,function(d){giphyOutput.empty();if(!d.hasOwnProperty('data')){giphyOutput.append('Error: '+d.message);return;}
if(!d.data.length)
{giphyOutput.append(_this.lang.get('gif_empty_result'));return;}
var ghOutput='';$.each(d.data,function(k1,v1){ghOutput+='<div class="giphy-item" data-id="'+v1.id+','+v1.images.original.width+','+v1.images.original.height+'">';ghOutput+='<div style="width:100%;height:0;padding-bottom:'+parseInt(v1.images.original.height*100/v1.images.original.width)+'%;position:relative;"><iframe src="https://giphy.com/embed/'+v1.id+'" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>';ghOutput+='<div class="gif-overlay"></div>';ghOutput+='</div>';});giphyOutput.append(ghOutput);},'json');},500);});dialog.el.on('click','.giphy-item',function(){html_giphy($(this).attr('data-id'));dialog.off();});dialog.el.find('input[type="text"]').focus();}});});form.find('._controller').attr('data-tool',form.find('._controller .jcm-btn-open').length);form.on('focus','.jcm-textarea',function(){form.addClass('active');form.find('.jcm-text-placeholder').removeClass('active');_this.box.trigger('emoji');}).on('blur','.jcm-textarea',function(){if($(this).html()=='')
form.find('.jcm-text-placeholder').addClass('active');});if(settings.cm_max_length>0)
{var maxSb=form.find('.symbol-count').attr('data-max')*1;form.on('keydown paste focus','.jcm-textarea',function(e){var _el=$(this);window.setTimeout(function(){var lengthSb=0;if(_el.is('textarea')){lengthSb=_el.val().length;}else{var $cc=_el.clone();$cc.find('img.emoji').each(function(){$(this).replaceWith('-');});lengthSb=$cc.text().length;}
if(lengthSb>maxSb)
{form.find('.symbol-count').addClass('error');}else{form.find('.symbol-count').removeClass('error');}
form.find('.symbol-count').text(maxSb-lengthSb);},e.type=='focusin'?300:100);});}
if(_this.browser.contenteditable)
{!function(a){a.fn.caret=function(a){var b=this[0],c=b&&"true"===b.contentEditable;if(0!=arguments.length){if(b){if(a==-1&&(a=this[c?"text":"val"]().length),window.getSelection)c?(b.focus(),window.getSelection().collapse(b.firstChild,a)):b.setSelectionRange(a,a);else if(document.body.createTextRange)if(c){var f=document.body.createTextRange();f.moveToElementText(b),f.moveStart("character",a),f.collapse(!0),f.select()}else{var f=b.createTextRange();f.move("character",a),f.select()}c||b.focus()}return this}if(b){if(window.getSelection){if(c){b.focus();var d=window.getSelection().getRangeAt(0),e=d.cloneRange();return e.selectNodeContents(b),e.setEnd(d.endContainer,d.endOffset),e.toString().length}return b.selectionStart}if(document.selection){if(b.focus(),c){var d=document.selection.createRange(),e=document.body.createTextRange();return e.moveToElementText(b),e.setEndPoint("EndToEnd",d),e.text.length}var a=0,f=b.createTextRange(),e=document.selection.createRange().duplicate(),g=e.getBookmark();for(f.moveToBookmark(g);0!==f.moveStart("character",-1);)a++;return a}if(b.selectionStart)return b.selectionStart}}}(jQuery);var __pasteHtml=function(html){var sel,range;if(window.getSelection){sel=window.getSelection();if(sel.getRangeAt&&sel.rangeCount){range=sel.getRangeAt(0);range.deleteContents();var el=document.createElement("div");el.innerHTML=html;var frag=document.createDocumentFragment(),node,lastNode;while((node=el.firstChild)){lastNode=frag.appendChild(node);}
range.insertNode(frag);if(lastNode){range=range.cloneRange();range.setStartAfter(lastNode);range.collapse(true);sel.removeAllRanges();sel.addRange(range);}}}else if(document.selection&&document.selection.type!="Control"){document.selection.createRange().pasteHTML(html);}},__lastChr=0;form.on('paste','.jcm-textarea',function(e){if(typeof window.clipboardData=='undefined')
{e.stopPropagation();e.preventDefault();document.execCommand('insertHTML',false,e.originalEvent.clipboardData.getData('text').replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#039;").replace(/(?:\r\n|\r|\n)/g,'<br>').replace(/\t/g,'&nbsp;&nbsp;&nbsp;&nbsp;'));}else{var _content='',_input=$(this),_textarea=document.createElement('textarea'),_caretPos=_input.caret();$(_textarea).attr("style","width:1px;height:1px;overflow:hidden;opacity:0");$(_textarea).appendTo(form);$(_textarea).focus();window.setTimeout(function(){_content=$(_textarea).val();_content=_content.replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g,'$1'+'<br>'+'$2');$(_textarea).remove();_input.focus();if(_caretPos>0)
{_input.caret(_caretPos);}
__pasteHtml(_content);},100);}});}
if(typeof settings.peoples=='object'&&settings.peoples.length&&_this.browser.contenteditable==true)
{var peoplesfm=[];$.each(settings.peoples,function(k,v){v.value=v.id;v.key=v.name+' '+v.username;peoplesfm.push(v);});var tribute=new Tribute({menuContainer:document.getElementById('content'),values:peoplesfm,selectTemplate:function(item){if(this.range.isContentEditable(this.current.element)){return'<span class="jcm-mention" contenteditable="false" data-id="'+item.original.id+'">'+(settings.author_name==1?item.original.name:item.original.username)+'</span>';}
return'@'+(settings.author_name==1?item.original.name:item.original.username);},noMatchTemplate:function(tribute){return'<li>'+_this.lang.get('no_match')+'</li>';},menuItemTemplate:function(item){var _fm='<img src="'+item.original.thumb+'" alt=""/>';if(settings.author_name==1)
{_fm+='<span class="_name">'+item.original.name+'</span>';_fm+='<span class="_uname">@'+item.original.username+'</span>';}else{_fm+='<span class="_name">@'+item.original.username+'</span>';_fm+='<span class="_uname">'+item.original.name+'</span>';}
return _fm;},});tribute.attach(form.find('.jcm-textarea')[0]);}
form.find('input.__fm').each(function(){var _el=$(this),_cOn='fas fa-check-square',_cOff='far fa-square',_nel=$('<i class="'+(_el.is(':checked')?_cOn:_cOff)+'"></i>');_el.change(function(){if(_el.is(':checked')){_nel.addClass(_cOn).removeClass(_cOff);}else{_nel.addClass(_cOff).removeClass(_cOn);}});_nel.insertAfter(_el);_el.hide();});form.on('submit','.jcm_form_input',function(e){e.preventDefault();var _form=$(this),data=_form.serializeArray();if(!_form.find('textarea.jcm-textarea').length)
{var CmClone=_form.find('.jcm-textarea').clone();CmClone.find('img.emoji').each(function(){$(this).replaceWith($(this).attr('alt'));});data.push({name:'comment',value:CmClone.html()});data.push({name:'plaintext',value:0});}
data.push({name:'key',value:_this.config.key});if(form.find('.forGuest').length)
{var author_name=form.find('#jcm-input-name-field').val(),author_email=form.find('#jcm-input-email-field').val();data.push({name:'guest_name',value:author_name});data.push({name:'guest_email',value:author_email});_this.helper.cookie.set('jcmGuestName',author_name,5);_this.helper.cookie.set('jcmGuestEmail',author_email,5);}
var formfn={countEvent:0,passEvent:0,el:form,data:data};formfn.submit=function(callback)
{if(formfn.countEvent!=formfn.passEvent)return false;if(form.find('.jcm-btn-emoticon.active').length)
{form.find('.jcm-btn-emoticon').trigger('click');}
form.find('.jcm-protect-layer').addClass('active');$.post(_form.attr('action'),data,function(response){form.find('.jcm-protect-layer').removeClass('active');if(typeof callback=='function')
{callback(response);}
if(typeof response!='object'||response.status==400)
{form.find('.jcm_form_error').addClass('active').text(response.error);$("html, body").animate({scrollTop:form.find('.jcm_form_error').offset().top-50},500);return false;}
var parent_id=form.find('[name=parent_id]').length==1?form.find('[name=parent_id]:eq(0)').val()*1:0,cm_id=form.find('[name=id]').length==1?form.find('[name=id]:eq(0)').val()*1:0;if(cm_id>0)
{$.get(_this.helper.url({task:'items.loadCm',id:cm_id}),function(d){if(typeof d!='object'||d.status==400)
{return;}
var cmBlock=_this.box.find('#comment-'+cm_id+'>.jcm-post-content>.jcm-flex-content');cmBlock.empty().append(d.html);form.closest('.jcm-block').children('.jcm-post-content').find('jcm-post-footer .jcm-edit').removeClass('active');form.parent().remove();cmBlock.show();$('#comment-'+cm_id).removeClass('editing');},'json');return;}
if(form.find('input[name=__sub]:checked').length)
{if(typeof response.sub=='object'&&response.sub.status==200)
{if(response.sub.hasOwnProperty('hash'))
{_this.box.find('.jcm-subscribe').attr('data-hash',response.sub.hash);}
if(response.sub.hasOwnProperty('verifyRequire')&&response.sub.verifyRequire==1)
{window.setTimeout(function(){var dialog=new _this.dialog({caption:_this.lang.get('subscribe'),content:_this.lang.get('subscribe_verify',response.sub.email),submitLabel:false,cancelLabel:_this.lang.get('ok')});},1000);}
_this.box.find('.jcm-subscribe').addClass('_on').removeClass('_off');_this.tpl.form.find('.jcm-suggest-follow').remove();}}
var _config={timestamp:0,sort:'desc',page_comment:1,timestamp_offset:_this.timestamp.hasOwnProperty(parent_id)?_this.timestamp[parent_id]:_this.config.timestamp}
if(parent_id>0)
{_config.parent_id=parent_id;if(settings.child_style=='1'&&form.find('[name=root_id]').length)
{var rootId=form.find('[name=root_id]').val();if(/^[1-9][0-9]*$/.test(rootId))
{parent_id=rootId;_config.parent_id=rootId;_config.timestamp_offset=_this.timestamp.hasOwnProperty(rootId)?_this.timestamp[rootId]:_this.config.timestamp;}}}
var showDir=parent_id>0?(settings.sortC=='desc'?'up':'down'):(settings.sort=='desc'?'up':'down');_this.reload(_config,function(d){if(_config.hasOwnProperty('parent_id')){_this.timestamp[_config.parent_id]=d.timestamp;}else{_this.timestamp[parent_id]=d.timestamp;}
if(parent_id>0)
{var replyBox=_this.box.find('#comment-'+parent_id+'>.jcm-post-content');if(!replyBox.children('.jcm-list-reply').length)
{replyBox.append('<div class="jcm-list-reply"><ul class="jcm-childs"></ul></div>');}
if(showDir=='up'){replyBox.children('.jcm-list-reply').children('.jcm-childs').prepend(d.html);}else{replyBox.children('.jcm-list-reply').children('.jcm-childs').append(d.html);}
form.parent().prev('ul.inline').find('.jcm-reply').removeClass('active');form.parent().remove();}else{if(!_this.box.find('.jcm-root').length)
{_this.box.find('.jcm-empty-cm').fadeOut('fast',function(){$(this).remove();});_this.box.find('#jcm-comments').append('<ul class="jcm-root"></ul>');}
if(showDir=='up'){_this.box.find('.jcm-root').prepend(d.html);}else{_this.box.find('.jcm-root').append(d.html);}
var _el=_this.tpl.form.clone();form.replaceWith(_el);_this.createFormEvents(_el);}
_this.tmpCache={};var latestId=$(d.html).filter('.jcm-block:eq(0)').attr('id');if(!settings.dis_scroll)
{$('html, body').animate({scrollTop:_this.box.find('#'+latestId).offset().top-100},200,function(){_this.box.find('#'+latestId).addClass('_light');});}});},'json');};var formError=[];(function()
{if(form.find('#jcm-input-name-field').length&&/^\s*$/.test(form.find('#jcm-input-name-field').val()))
{formError.push(_this.lang.get('fill_your_name'));}
var regexEmail=/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,__elEmail=form.find('#jcm-input-email-field');if(__elEmail.length)
{if((__elEmail.attr('data-require')==1&&!regexEmail.test(__elEmail.val()))||(__elEmail.attr('data-require')==0&&!regexEmail.test(__elEmail.val())&&!/^\s*$/.test(__elEmail.val())))
{formError.push(_this.lang.get('email_incorrect'));}}
var _el=form.find('.jcm-textarea'),lengthCm=0;if(_el.is('textarea')){lengthCm=_el.val().length;}else{var $cc=_el.clone();$cc.find('img.emoji').each(function(){$(this).replaceWith('-');});lengthCm=$cc.text().length;}
if(settings.cm_min_length>0)
{if(lengthCm<settings.cm_min_length)
{formError.push(_this.lang.get('min_comment_length',settings.cm_min_length));}}else{var sticker=form.find('input[name=sticker_id]');if((!sticker.length||sticker.val()<1)&&lengthCm<1)
{formError.push(_this.lang.get('comment_empty'));}}
if(settings.cm_max_length>0&&lengthCm>settings.cm_max_length)
{formError.push(_this.lang.get('comment_too_long'));}
if(settings.member==0&&form.find('input[name=__sub]:checked').length&&(!__elEmail.length||(__elEmail.length&&!regexEmail.test(__elEmail.val()))))
{formError.push(_this.lang.get('subscribe_email_require'));}
if(form.find('input[name=__term]').length&&!form.find('input[name=__term]:checked').length)
{formError.push(_this.lang.get('term_checkbox_err'));}})();if(formError.length>0)
{form.find('.jcm_form_error').addClass('active').html(formError.join("<br/>"));if(!settings.dis_scroll)
{$("html, body").animate({scrollTop:form.find('.jcm_form_error').offset().top-50},500);}
return false;}else{form.find('.jcm_form_error').removeClass('active');}
_this.listenEvent('jcm.submit',{$:$,jcm:_this,form:formfn});if(formfn.countEvent==0)
{formfn.submit();}});form.on('click','.jcm-btn-submit',function(){form.find('.jcm_form_input').trigger('submit');});};this.sharefn=function()
{_this.box.on('click','.jcm-share',function(){var _el=$(this),id=_el.attr('data-id'),comment_preview=_this.box.find('#comment-'+id+' .jcm-post-body:eq(0)').text();let url='';comment_preview=$.trim(comment_preview);if(settings.linkshare=='query'){url=settings.url+(settings.url.indexOf('?')==-1?'?':'&')+'comment_id='+id;}else{url=settings.url+'#comment-'+id;}
var content='<input type="text" readonly value="'+url+'" style="margin: 10px auto;background: #fff;" />',shareTools=[];content+='<div style="text-align: center; font-weight: bold; margin: -5px 0 5px 0;"><span class="cp-stt" style="display:none">'+_this.lang.get('copied')+'</span></div>';if(_el.attr('data-fb')==1)
{shareTools.push('<li><a href="javascript:void(0)" class="jcm-share-fb jcm-share-item" data-type="fb"><i class="fab fa-facebook-f"></i></a></li>');}
if(_el.attr('data-tw')==1)
{shareTools.push('<li><a href="javascript:void(0)" class="jcm-share-tw jcm-share-item" data-type="tw"><i class="fab fa-twitter"></i></a></li>');}
if(_el.attr('data-gg')==1)
{shareTools.push('<li><a href="javascript:void(0)" class="jcm-share-gg jcm-share-item" data-type="gg"><i class="fab fa-google"></i></a></li>');}
if(shareTools.length)
{content+='<ul class="jcm-inline" style="text-align:center">';content+=shareTools.join('');content+='</ul>';}
new _this.dialog({caption:_this.lang.get('permalink'),submitLabel:false,content:content,loadfn:function(dialog)
{dialog.el.find('.jcm-dialog').addClass('permalink');dialog.el.find('input[type="text"]').click(function(){dialog.el.find('input[type="text"]').select();});dialog.el.find('input[type="text"]').focus().select();try{var cptrue=document.execCommand('copy');if(cptrue){setTimeout(function(){dialog.el.find('.cp-stt').fadeIn();},300);}}catch(err){console.log('Oops, unable to copy');}
dialog.el.on('click','.jcm-share-item',function(){var t=$(this).attr('data-type'),url2share=null;switch(t){case'fb':if(typeof FB!='undefined'){var fbOptions={method:'feed',link:url};if(!/^\s*$/.test(comment_preview))
{fbOptions['caption']=comment_preview;}
FB.ui(fbOptions,function(response){});return;}
url2share='https://www.facebook.com/sharer.php?s=100&p[url]'+encodeURIComponent(url)+(!/^\s*$/.test(comment_preview)?'&p[message]='+encodeURIComponent(comment_preview):'');break;case'tw':url2share='https://twitter.com/intent/tweet?tw_p=tweetbutton'+(!/^\s*$/.test(comment_preview)?'&text='+encodeURIComponent(comment_preview):'')+'&url='+encodeURIComponent(url);break;case'gg':url2share='https://plus.google.com/share?url='+encodeURIComponent(url);break;}
if(url2share!=null)
{window.open(url2share,'jcm_sharer','top=200,left=200,toolbar=0,status=0,width=600,height=450');}});}});});};this.user=function(){var _ob=this,notifications=[],notifications_timeoffset=0;this.notifications=function()
{if(settings.member==0||!settings.alert)return;$.get(_this.helper.url({task:'user.list_notification',timestamp:notifications_timeoffset}),function(d){if(d.total>0)
{_this.box.find('.jcm-count-nof').empty().append('<span>'+d.total+'</span>');notifications=$.merge(d.notifications,notifications);}
notifications_timeoffset=d.timestamp;},'json');};this.notifications();window.setInterval(function(){_ob.notifications();},300000);_this.box.on('click','#jcm-notifications',function(){var content='<div class="jcm-dg-full">',nof2html=function(notifications)
{var html='';$.each(notifications,function(k,v){html+='<li class="'+(v.unread==1?'unread':'')+'">';html+='<a href="'+v.url+'">';html+='<span class="_msg">'+v.caption+'</span>';html+='<span class="jcm-dg-bullet">&middot;</span>';html+='<span class="_date">'+v.created_time+'</span>';html+='<span class="jcm-dg-bullet">&middot;</span>';html+='<b>'+v.object_name+'</b>';html+='<span class="_comment">'+v.comment+'</span>';html+='</a>';html+='</li>';});return html;};_this.box.find('.jcm-count-nof').empty();content+='<div class="jcm-box">';if(notifications.length)
{content+='<a href="javascript:void(0)" class="nof-mark-all">'+_this.lang.get('mark_all_read')+'</a>';content+='<ul class="jcm-list-notifications">';content+=nof2html(notifications);content+='</ul>';}else{content+='<div style="padding:10px;text-align:center;min-height:80px;">'+_this.lang.get('no_notification')+'</div>';content+='<ul class="jcm-list-notifications"></ul>';}
content+='</div>';content+='<a href="javascript:void(0)" class="jcm-plg nof-see-all">'+_this.lang.get('all_notification')+'</a>';content+='</div>';new _this.dialog({caption:_this.lang.get('notification'),submitLabel:false,content:content,loadfn:function(dialog)
{dialog.el.find('.jcm-dialog').addClass('alert');var offset=0,total=0;dialog.el.on('click','.nof-see-all',function(){var _el=$(this);if(_el.hasClass('loading'))
{return false;}
_el.addClass('loading');_el.text(_this.lang.get('please_wait'));if(offset==0)
{dialog.el.find('.jcm-box').empty().append('<ul class="jcm-list-notifications"></ul>');}
$.get(_this.helper.url({task:'user.list_notification',offset:offset,all:1}),function(d){if(d.total>0)
{dialog.el.find('.jcm-list-notifications').append(nof2html(d.notifications));}else{dialog.el.find('.jcm-dg-content').empty().append(_this.lang.get('no_notification'));}
_el.removeClass('loading');total=d.total;offset=d.offset+d.limit;if(offset>=total)
{_el.fadeOut(function(){$(this).remove();});}
_el.text(_this.lang.get('see_more'));},'json');}).on('click','.jcm-list-notifications a',function(){$(this).parent().removeClass('unread');}).on('click','.nof-mark-all',function(){dialog.el.find('.unread').removeClass('unread');$.post(_this.helper.url({task:'user.mark_read'}));$(this).fadeOut(function(){$(this).remove();});});}});});if(settings.profile==1)
{_this.box.on('click','#jcm-thumb-edit',function(){var content='<div class="jcm-dg-thumb">';content+='<div>';content+='<div class="thumb-current"></div>';content+='<div class="thumb-row">';content+='<label class="thumb-remove"><input type="checkbox" name="remove" value="1" />';content+=_this.lang.get('thumb_remove_desc')+'</label>';content+='<a href="javascript:void(0)" class="upload-thumb">'+_this.lang.get('upload_image')+'</a>';content+='</div>';content+='<div class="clearfix"></div>';content+='</div>';content+='<div class="thumb-box"></div>';content+='</div>';var cropData={},cropFile=null;new _this.dialog({caption:_this.lang.get('thumb_editing'),submitfn:_this.lang.get('update'),content:content,submitfn:function(dialog)
{var is_del=dialog.el.find('input[name=remove]:checked').length>0?1:0;if(cropFile==null&&!is_del)
{dialog.off();return;}
var data=new FormData();if(cropFile!=null)
{data.append('file',cropFile);data.append('x',cropData.x);data.append('y',cropData.y);data.append('width',cropData.width);data.append('height',cropData.height);}else{data.append('is_del',is_del);}
dialog.overlay();$.ajax({url:_this.helper.url({task:'user.thumb',action:(cropFile!=null?'upload':'remove')}),type:"POST",dataType:"json",data:data,xhr:function(){var xhrobj=$.ajaxSettings.xhr();return xhrobj;},success:function(response){dialog.unOverlay();if(response.status==200)
{dialog.off();}else{dialog.setError(response.error);}},error:function(xhr,ajaxOptions,thrownError){dialog.unOverlay();},cache:false,contentType:false,processData:false});},loadfn:function(dialog)
{dialog.el.find('.jcm-dialog').addClass('thumb');$.get(_this.helper.url({task:'user.thumb',action:'load'}),function(d){if(d.url!=null)
{dialog.el.find('.thumb-current').prepend('<img src="'+d.url+'" alt="" />');dialog.el.find('.jcm-dg-thumb').addClass('exists');}},'json');dialog.el.on('click','.upload-thumb',function(){var _el=$('<input type="file" style="width:1px;height:1px;overflow:hidden" />');_el.appendTo('body');_el.on('change',function(){var fileObject=$(this)[0].files[0];var urlObject=window.URL||window.webkitURL;var img_types=['image/png','image/jpeg','image/jpg','image/gif'];if($.inArray(fileObject.type,img_types)==-1)
{dialog.setError(_this.lang.get('file_must_img'));return;}
dialog.clearError();cropFile=fileObject;var url=urlObject.createObjectURL(fileObject);dialog.el.find('.thumb-box').empty().append('<img src="'+url+'" alt="" />');dialog.el.find('.thumb-box img').cropper({aspectRatio:1,rotatable:false,scalable:false,minCropBoxWidth:200,minCropBoxHeight:200,crop:function(e){cropData.x=e.x;cropData.y=e.y;cropData.width=e.width;cropData.height=e.height;}});});_el.trigger('click');});}})});}
_this.box.on('click','.jcm-user-cm',function(){var offset=0,uid=$(this).attr('data-id')*1,content='<div class="jcm-dg-comments">';content+='<div class="user-profile"></div>';content+='<div class="user-comments">'+_this.lang.get('please_wait')+'</div>';content+='<a href="javascript:void(0)" class="load_more_cm">'+_this.lang.get('load_more_cm')+'</a>';content+='</div>';if(uid<1)
{return;}
new _this.dialog({caption:_this.lang.get('comment_title'),submitLabel:false,content:content,loadfn:function(dialog){dialog.el.find('.jcm-dialog').addClass('profile');var profile=null;var loadCm=function()
{if(profile==null)
{$.get(_this.helper.url({task:'user.profile',uid:uid}),function(d){var html='<div class="uc-thumb">';html+='<img src="'+d.profile.thumb+'" alt="" />';html+='</div>';html+='<div class="uc-info">';html+='<h4>';if(d.profile.hasOwnProperty("link")&&d.profile.link)
{html+='<a href="'+d.profile.link+'">'+(settings.author_name==1?d.name:d.username)+'</a>';}else{html+=settings.author_name==1?d.name:d.username;}
html+='</h4>';html+='<h6><span class="uc-count-cm">0</span> <span class="_zero">'+_this.lang.get('comment')+'</span><span class="_zerogt" style="display:none">'+_this.lang.get('comments')+'</span>.</h6>';html+='</div>';html+='<div class="clearfix"></div>';dialog.el.find('.user-profile').empty().append(html);profile=d;loadCm();},'json');return;}
$.get(_this.helper.url({task:'user.list_comments',uid:uid,offset:offset}),function(d){if(d.status==400)
{dialog.setError(d.error);return;}
dialog.el.find('.uc-count-cm').text(d.data.total);if(d.data.total>1)
{dialog.el.find('._zero').hide();dialog.el.find('._zerogt').show();}else{dialog.el.find('._zero').show();dialog.el.find('._zerogt').hide();}
if(d.data.comments.length>0)
{var html='';$.each(d.data.comments,function(k,v){html+='<div class="uc-item">';html+='<span class="uc-author">'+(settings.author_name==1?profile.name:profile.username)+'</span> ';html+='<span class="uc-action">';if(v.parent_id>0)
{html+=_this.lang.get('replied_comment');}else{html+=_this.lang.get('comment_verb').toLocaleLowerCase();}
html+='</span>';html+=' '+_this.lang.get('in')+' <a href="'+v.object_url+'"><b>'+v.object_name+'</b></a>';html+='<span class="uc-date">'+v.created_time+'</span>';html+='<p class="uc-comment">'+v.comment+'</p>';html+='</div>';});if(offset==0)
{dialog.el.find('.user-comments').empty().append(html);}else{dialog.el.find('.user-comments').append(html);}}else{if(offset==0)
{dialog.el.find('.user-comments').empty().append(_this.lang.get('no_comment'));}}
offset=offset+d.data.limit;if(offset>=d.data.total)
{dialog.el.find('.load_more_cm').removeClass('active');}else{dialog.el.find('.load_more_cm').addClass('active');}},'json');};loadCm();dialog.el.on('click','.load_more_cm.active',function(){loadCm();});}});});_this.box.on('click','#jcm-u-logout',function(){$.get(_this.helper.url({task:'user.logout'}),function(d){window.location.reload();});});_this.box.on('click','.jcm-u-login',function(){if(settings.login_type=='url')
{window.location=settings.login_url;return;}
var content='<div id="jcm-ulogin-box">';content+='<label for="jcm-ulogin-uname">'+_this.lang.get('username')+'</label>';content+='<input type="text" id="jcm-ulogin-uname" name="username" />';content+='<label for="jcm-ulogin-pw">'+_this.lang.get('password')+'</label>';content+='<input type="password" id="jcm-ulogin-pw" name="password" />';content+='</div>';new _this.dialog({caption:_this.lang.get('login'),submitLabel:_this.lang.get('login'),content:content,loadfn:function(dialog)
{dialog.el.find('.jcm-dialog').addClass('login');dialog.el.find('input[name="username"]').trigger('click').focus();},submitfn:function(dialog)
{var request={username:dialog.el.find('input[name="username"]').val(),password:dialog.el.find('input[name="password"]').val()};if(/^\s*$/.test(request.username))
{dialog.setError(_this.lang.get('username_not_blank'));return false;}
if(request.password=='')
{dialog.setError(_this.lang.get('pw_not_blank'));return false;}
dialog.clearError();dialog.overlay();dialog.el.find('.jcm-dg-submit').text(_this.lang.get('please_wait'));$.post(_this.helper.url({task:'user.login'}),request,function(d){if(d.status==200)
{dialog.el.find('.jcm-dg-submit').text(_this.lang.get('success'));window.location.reload();}else{dialog.unOverlay();dialog.setError(d.error);dialog.el.find('.jcm-dg-submit').text(_this.lang.get('login'));}},'json');}});});_this.box.on('click','.jcm-u-oauth',function(){var type=$(this).attr('data-action'),url='',name='';switch(type)
{case'facebook':url=_this.helper.url({task:'user.oauth',type:'fb',popup:1});name="jlex_popup_fb";break;case'google':url=_this.helper.url({task:'user.oauth',type:'google',popup:1});name="jlex_popup_google";break;case'twitter':url=_this.helper.url({task:'user.oauth',type:'twitter',popup:1});name="jlex_popup_twitter";break;case'vk':url=_this.helper.url({task:'user.oauth',type:'vk'});name="jlex_popup_vk";break;}
window.open(url,name,"width=500, height=350");});};this.listenEvent=function(name,data){if(typeof CustomEvent=='undefined')return false;data=data||{};var evt=new CustomEvent(name,{detail:data});window.dispatchEvent(evt);}
this.events=function()
{new _this.user();window.setInterval(function(){_this.paginationChild();if(!$('.jcm-post-body:visible').not('._loaded').length)return;var _els=$('.jcm-post-body:visible').not('._loaded');_els.each(function(){var $i=$(this);if(settings.styles!=null)
{var sid=$i.attr('data-style');if(settings.styles.hasOwnProperty(sid))
{$i.addClass('_styled');$i.attr('style',(settings.styles[sid].css));}}
$i.find('a').attr('target','_blank').attr('rel','nofollow');if(typeof twemoji=='object')
{twemoji.parse($i[0]);}
if(settings.child_style=='1'&&$i.find('.jcm-hl').length)
{var pEl=$i.find('.jcm-hl');pEl.attr('href','#comment-'+pEl.attr('data-id'));if($('#comment-'+pEl.attr('data-id')).attr('data-parent-id')=='0')pEl.remove();}
if(settings.reactions)
{var rcEl=$i.parent().next('.jcm-post-footer').find('.jcm-reaction-data'),_cmid=rcEl.parents('.jcm-voting').attr('data-id'),_firstE=settings.reactions[Object.keys(settings.reactions)[0]],_total=0,_removeReact=function(ignore)
{rcEl.find('._react').removeClass('active').removeAttr('style').text(_firstE.label);rcEl.find('.reaction-btn').removeClass('active');if(_total>0)
{_total-=1;rcEl.find('.react-total').text(_total);if(_data!=null)_data.set=null;if(_total<1)rcEl.find('.react-stic').remove();}
if(typeof ignore=='undefined')
{$.post(_this.helper.url({task:'item.vote'}),{id:_cmid,point:0});}},_setReact=function(id)
{var _elc=rcEl.find('.reaction-btn[data-id='+id+']');if(_elc.hasClass('active'))
{_removeReact();return;}
_elc.addClass('active');_elc.siblings().removeClass('active');rcEl.find('._react').addClass('active').text((settings.reactions[id]).label).css('color','#'+(settings.reactions[id]).color);try{if(_data.set>0&&_total==1)
rcEl.find('.react-stic').remove();}catch(err){}
if(_data==null||_data.set==null)
{_total+=1;rcEl.find('.react-total').text(_total);}
if(_data==null)_data={};_data.set=id;$.post(_this.helper.url({task:'item.vote'}),{id:_cmid,point:id},function(d){if(d.status==400)
{alert(d.error);_removeReact(true);}},'json');},_data=rcEl.text();try{_data=$.parseJSON(_data);}catch(err){_data=null;}
if(_data!=null)
{rcEl.empty().removeAttr('style');rcEl.append('<span class="_tbox"></span>');rcEl.find('._tbox').append('<a href="javascript:void(0)" class="_react"></a>');var action=_firstE.label;if(_data!=null&&_data.set!=null&&_data.set>1)
{if(settings.reactions.hasOwnProperty(_data.set))
{action=settings.reactions[_data.set].label;rcEl.find('._react').addClass('active').css('color','#'+settings.reactions[_data.set].color);}}
rcEl.find('._react').text(action);rcEl.find('._tbox').append('<div class="react-box"></div>');var _idexReact=1;$.each(settings.reactions,function(k,v){var _set=_data!=null&&_data.set!=null?_data.set:-1,_elc=$('<span class="reaction-btn'+(_set==k?' active':'')+'" data-id="'+k+'" style="transition-delay:'+(_idexReact*0.03)+'s;"><span class="_act"><img src="'+v.icon+'" alt="" /></span><span class="_label">'+v.label+'</span></span>');_elc.on('click','._act',function(){_setReact(k);});_elc.appendTo(rcEl.find('.react-box'));_idexReact++;});var reactBoxWid=(_idexReact-1)*32+(_idexReact-2)*10+6;rcEl.find('.react-box').css('width',reactBoxWid+'px');try{if(reactBoxWid+10>$(window).width()-rcEl.offset().left)
{var reactBoxOff=reactBoxWid+10-$(window).width()+rcEl.offset().left;rcEl.find('.react-box').css('left','-'+reactBoxOff+'px');}}catch(err){};if(_data!=null&&_data.list!=null)
{var _html='';_html+='<div class="react-stic">';$.each(_data.list,function(k,v){if(v<=0)return true;var _react=settings.reactions[k];if(typeof _react=='undefined')
{return true;}
_html+='<span class="react-set" data-id="'+k+'" data-count="'+v+'">';_html+='<span class="react-icon"><img src="'+_react.icon+'" alt="" /></span>';_html+='<span class="react-count">'+_react.label+'</span>';_html+='</span>';_total+=v*1;});if(_total>0)
_html+='<span class="react-total">'+_total+'</span>';_html+='</div>';rcEl.append(_html);if(_total<1)rcEl.find('.react-stic').remove();}
rcEl.on('click','._react',function(e){e.preventDefault();$(this).hasClass('active')?_removeReact():_setReact(Object.keys(settings.reactions)[0]);});var _cache={},__request=null;rcEl.find('.react-set').mouseenter(function(){var __id=$(this).attr('data-id'),__el=$(this).find('.__extra'),_toHtml=function(id)
{var dt=_cache[id],_else=dt.total*1,_html=[];if(dt.you==1)
{_html.push(_this.lang.get('you'));_else-=1;}
if(dt.members!=null&&dt.members.length)
{$.each(dt.members,function(k,v){_html.push(v);});_else-=dt.members.length;}
if(_else>0)
{if(_else==1)
{_html.push(_this.lang.get(!_html.length?'more_one_pp_line':'more_one_pp'));}else{_html.push(_this.lang.get((!_html.length?'more_many_pp_line':'more_many_pp'),_else));}}
var _output='<ul><li>'+_html.join('</li><li>')+'</li></ul>';return _output;};if($(this).attr('data-total')*1<1)return false;if(__el.length)
{__el.show();}else{$(this).append('<div class="__extra"></div>');__el=$(this).find('.__extra');}
__el.empty();if(_cache.hasOwnProperty(__id))
{__el.append(_toHtml(__id));}else{__el.append('<span>'+_this.lang.get('please_wait')+'</span>');__request=$.get(_this.helper.url({task:'others.reaction_stic'}),{cmid:_cmid,id:__id},function(d){if(d.status==200)
{_cache[__id]=d.data;__el.empty().append(_toHtml(__id));}},'json');}}).mouseleave(function(){$(this).find('.__extra').hide();if(__request!=null)__request.abort();});}}
if(settings.openform!='0')
{var $pi=$i.closest('li.jcm-block');if($pi.attr('data-parent-id')==0)
{$pi.find('>.jcm-post-content>.jcm-post-footer .jcm-reply').trigger('click',false);}}
if(typeof lightGallery!="undefined")
{if(!$i.next('.jcm-images-slideshow').length)return;lightGallery($i.next('.jcm-images-slideshow')[0]);}});if(settings.readmore&&typeof $.fn.readmore=='function')
{window.setTimeout(function(){var s=function(){_els.each(function(){$(this).css('height','auto');if(!$(this).find('.__i').length)
{$(this).wrapInner('<div class="__i"></div>');}
$(this).find('.__i').removeAttr('style').css('height',$(this).height());});try{_els.readmore('destroy');}catch(error){}
_els.readmore({speed:75,moreLink:'<a class="jcm-readmore jcm-i3" href="#"><span>'+_this.lang.get('readmore')+'</span></a>',lessLink:'<a class="jcm-readless jcm-i3" href="#"><span>'+_this.lang.get('close')+'</span></a>'});};s();},1000);}
_els.addClass('_loaded');},500);var _elEditable=_this.box.find('.jcm-textarea')[0];if(_this.browser.contenteditable==null&&_elEditable)
{_this.browser.contenteditable=typeof(_elEditable.contentEditable)=='undefined'?false:true;}
if(_this.browser.contenteditable==false)
{var _elReplace='<textarea class="jcm-textarea" name="comment"></textarea>';_this.box.find('.jcm-textarea').replaceWith(_elReplace);}
$('.jcm-terms').click(function(e){e.preventDefault();new _this.dialog({caption:_this.lang.get('cm_terms'),content:_this.lang.get('please_wait'),submitLabel:false,cancelLabel:'Ok',loadfn:function(dialog){dialog.el.find('.jcm-dialog').addClass('terms');$.get(_this.helper.url({task:'others.terms'}),function(d){dialog.el.find('.jcm-dg-content').empty().append(d.content);},'json');}});});_this.box.on('click','.jcm-reply',function(e,fa){e.preventDefault();let root_id=$(this).attr('data-root')*1;if(typeof fa=='undefined')fa=true;if(root_id==0&&settings.openform=='bottom')
{let fc=$(this).closest('.jcm-post-content');if(fc.find('>.jcm-reply-form').length)
{if(fc.find('.jcm-btn-emoticon').hasClass('active'))
fc.find('.jcm-btn-emoticon').trigger('click');}else{let parent_id=$(this).attr('data-pid')*1;fc.append('<div class="jcm-reply-form"></div>');_this.createCmform(fc.find('.jcm-reply-form'),{parent_id:parent_id,root_id:$(this).attr('data-root')},fa);}
if(fa)
{let fcf=fc.find('>.jcm-reply-form .jcm-form-cp');fcf.find('.jcm-textarea').focus();$("html, body").animate({scrollTop:fcf.offset().top-50},500);}}else{let fc=$(this).closest('.jcm-post-footer');if(fc.find('.jcm-reply-form').length)
{if(root_id==0&&settings.openform=='top')
{if(fa)fc.find('.jcm-textarea').focus();}else{fc.find('.jcm-reply-form').toggle();}
if(fc.find('.jcm-btn-emoticon').hasClass('active'))
fc.find('.jcm-btn-emoticon').trigger('click');}else{let parent_id=$(this).attr('data-pid')*1;fc.append('<div class="jcm-reply-form"></div>');_this.createCmform(fc.find('.jcm-reply-form'),{parent_id:parent_id,root_id:$(this).attr('data-root')},fa);}}
if(root_id==0&&$.inArray(settings.openform,['bottom','top'])!=-1)
{$(this).addClass('active');}else{$(this).toggleClass('active');}}).on('click','.jcm-edit',function(e){e.preventDefault();var id=$(this).parent().attr('data-id')*1,bodyCm=$(this).closest('.jcm-post-content');$(this).closest('.jcm-dropdown').toggleClass('active');$('#comment-'+id).addClass('editing');$.get(_this.helper.url({task:'item.edit',id:id}),function(d){if(d.status==200)
{bodyCm.children('.jcm-comment-edit').remove();bodyCm.children('.jcm-flex-content').hide();bodyCm.prepend('<div class="jcm-comment-edit"></div>');_this.createCmform(bodyCm.children('.jcm-comment-edit'),d.data);}},'json');}).on('click','.jcm-delete',function(e){e.preventDefault();var id=$(this).parent().attr('data-id')*1;$(this).closest('.jcm-dropdown').toggleClass('active');var dialog=new _this.dialog({caption:_this.lang.get('warning'),submitLabel:_this.lang.get('delete'),content:_this.lang.get('delete_confirm'),submitfn:function(dialog)
{dialog.overlay();$.post(_this.helper.url({task:'item.remove',id:id}),function(d){if(d.status==200)
{_this.box.find('#comment-'+id).fadeOut(function(){$(this).remove();});dialog.off();}else{dialog.unOverlay();dialog.setError(d.error);}},'json');},loadfn:function(dialog){dialog.el.find('.jcm-dialog').addClass('warning');}});}).on('click','.jcm-state',function(e){e.preventDefault();var _el=$(this),id=_el.parent().attr('data-id')*1,state=_el.hasClass('_off')?0:1;_el.addClass('_loading');$.post(_this.helper.url({task:'item.state',id:id,state:state}),function(d){_el.removeClass('_loading');if(d.status==200)
{if(state==0)
{_this.box.find('#comment-'+id).addClass('jcm-unpublished');}else{_this.box.find('#comment-'+id).removeClass('jcm-unpublished');}
_el.closest('.jcm-dropdown').toggleClass('active');_el.toggleClass('_on').toggleClass('_off');}else{alert(d.error);}},'json');}).on('click','.jcm-feature',function(e){e.preventDefault();var _el=$(this),id=_el.parent().attr('data-id')*1,state=_el.hasClass('_off')?0:1;_el.addClass('_loading');$.post(_this.helper.url({task:'item.feature',id:id,state:state}),function(d){_el.removeClass('_loading');if(d.status==200)
{if(state==1)
{_this.box.find('#comment-'+id).addClass('jcm-featured');}else{_this.box.find('#comment-'+id).removeClass('jcm-featured');}
_el.closest('.jcm-dropdown').toggleClass('active');_el.toggleClass('_on').toggleClass('_off');}else{alert(d.error);}},'json');}).on('click','.jcm-report',function(e)
{e.preventDefault();var _el=$(this),id=_el.attr('data-id')*1,request={id:id};if(_el.hasClass('loading'))return false;if(_el.hasClass('active'))
{var dialog=new _this.dialog({caption:_this.lang.get('reporting'),content:_this.lang.get('cancel_reporting'),submitLabel:_this.lang.get('ignore'),loadfn:function(dialog){dialog.el.find('.jcm-dialog').addClass('cancel-report');},submitfn:function(dialog)
{dialog.el.find('.jcm-dg-content').empty().append('<span>'+_this.lang.get('please_wait')+'</span>');_el.addClass('loading');dialog.overlay();$.post(_this.helper.url({task:'report.ignore'}),request,function(d){_el.removeClass('loading');dialog.unOverlay();if(d.status==200)
{_el.removeClass('active');dialog.off();}else{dialog.el.find('.jcm-dg-content').empty().append(d.error);dialog.el.find('.jcm-dg-submit').remove();}},'json');}});}else{var content='<div class="jcm-report-box">';content+='<label>'+_this.lang.get('report_reason')+'</label><textarea></textarea>';if(settings.member==0)
{content+='<label>'+_this.lang.get('your_name')+'</label>';content+='<input type="text" name="guest_name" value="'+_this.browser.guest.name+'">';content+='<label>'+_this.lang.get('your_email')+'</label>';content+='<input type="email" name="guest_email" value="'+_this.browser.guest.email+'">';}
content+='</div>';new _this.dialog({caption:_this.lang.get('reporting'),content:content,submitLabel:_this.lang.get('report'),loadfn:function(dialog){dialog.el.find('.jcm-dialog').addClass('report');},submitfn:function(dialog)
{var msg=dialog.el.find('textarea').val();dialog.clearError();if(/^\s*$/.test(msg))
{dialog.setError(_this.lang.get('fill_your_report'));dialog.el.find('textarea').focus();return;}
if(settings.member==0)
{request.name=dialog.el.find('input[name="guest_name"]').val();request.email=dialog.el.find('input[name="guest_email"]').val();if(/^\s*$/.test(request.name))
{dialog.el.find('input[name="guest_name"]').focus();return;}
if(/^\s*$/.test(request.email))
{dialog.el.find('input[name="guest_email"]').focus();return;}}
dialog.el.find('.jcm-dg-content').find('.jcm-report-box').hide();dialog.el.find('.jcm-dg-content').append('<span class="_loading">'+_this.lang.get('please_wait')+'</span>');request.msg=msg;_el.addClass('loading');dialog.overlay();$.post(_this.helper.url({task:'report.post'}),request,function(d){dialog.unOverlay();_el.removeClass('loading');if(d.status==200)
{_el.addClass('active');dialog.el.find('.jcm-dg-content').empty().append('<span>'+_this.lang.get('thanks_feedback')+'</span>');dialog.el.find('.jcm-dg-submit').remove();window.setTimeout(function(){dialog.off();},3000);}else{dialog.el.find('.jcm-dg-content').find('.jcm-report-box').show();dialog.el.find('.jcm-dg-content').find('._loading').remove();dialog.setError(d.error);}},'json');}});}}).on('mouseenter','.jcm-tooltip',function(){if(!$(this).find('.jcm-tooltip-body').length)
{var content=$(this).attr('title'),_el=$('<span class="jcm-tooltip-body">'+content+'</span>');$(this).append(_el);$(this).removeAttr('title');var _elWidth=typeof $.fn.outerWidth=='function'?_el.outerWidth():_el.width();if(_elWidth>=120)
{_el.css('white-space','normal');_el.css('width','120px');}
_el.css('margin-left',(_elWidth/-2)+'px');}});if(!settings.reactions)
{_this.box.on('click','.jcm-vote-up .jcm-control, .jcm-vote-down .jcm-control',function(e){e.preventDefault();var _el=$(this),_parent=_el.closest('.jcm-voting');cm_id=_parent.attr('data-id')*1,point=_el.parent().attr('data-action')=='upvote'?1:-1;if(_el.hasClass('active'))point=0;if(_el.hasClass('disabled'))return;_el.addClass('disabled');$.post(_this.helper.url({task:'item.vote'}),{id:cm_id,point:point},function(d){_el.removeClass('disabled');if(typeof d!='object')return;if(d.status==400)
{alert(d.error);return;}
_parent.find('.jcm-vote-up .jcm-control, .jcm-vote-down .jcm-control').removeClass('active');switch(d.data.vote*1)
{case 1:_parent.find('.jcm-vote-up .jcm-control').addClass('active');break;case-1:_parent.find('.jcm-vote-down .jcm-control').addClass('active');break;}
var oldPointUp=_parent.find('.jcm-vote-up .jcm-count').text()*1,oldPointDown=_parent.find('.jcm-vote-down .jcm-count').text()*1;if(d.data.up!=0)
{_parent.find('.jcm-vote-up .jcm-count').text(oldPointUp+d.data.up*1);if(oldPointUp+d.data.up*1==0)
{_parent.find('.jcm-vote-up').addClass('count-0');}else{_parent.find('.jcm-vote-up').removeClass('count-0');}}
if(d.data.down!=0)
{_parent.find('.jcm-vote-down .jcm-count').text(oldPointDown+d.data.down*1);if(oldPointDown+d.data.down*1==0)
{_parent.find('.jcm-vote-down').addClass('count-0');}else{_parent.find('.jcm-vote-down').removeClass('count-0');}}},'json');});}
var urlRoot=settings.url;_this.box.on('click','.jcm-sortby a',function(){var _el=$(this),sort=_el.attr('data-sort');if(_el.hasClass('active'))
{_el.closest('.jcm-dropdown').removeClass('active');return false;}
_el.addClass('active');_el.parent().siblings().find('a').removeClass('active');if(_el.closest('.jcm-dropdown').find('.jcm-dropdown-val').length)
{_el.closest('.jcm-dropdown').find('.jcm-dropdown-val').text(_el.text());}
_el.closest('.jcm-dropdown').removeClass('active');_this.config.sort=sort;_this.config.page_comment=1;_this.reload({unwrap:0},function(d){_this.config.timestamp=d.timestamp;_this.timestamp[0]=d.timestamp;_this.box.find('#jcm-comments').empty().append(d.html);_this.box.find('.jcm-root-page a').each(function(){var page=$(this).attr('data-page')*1,newUrl='';if(/page_comment=[1-9][0-9]*/.test(urlRoot))
{newUrl=urlRoot.replace(/page_comment=[1-9][0-9]*/,'page_comment='+page);}else{newUrl=(urlRoot.indexOf('?')==-1?'?':'&')+'page_comment='+page;}
$(this).attr('href',newUrl);});});}).on('click','.jcm-subscribe',function(){var _el=$(this);if(_el.hasClass('_on'))
{var dialog=new _this.dialog({caption:_this.lang.get('unsubscribe'),content:_this.lang.get('unsubscribe_confirm'),submitLabel:'Ok',submitfn:function(dialog)
{var request={key:_this.config.key};if(typeof _el.attr('data-hash')!='undefined')
{request.hash=_el.attr('data-hash');}
dialog.overlay();$.post(_this.helper.url({task:'subscribe.remove'}),request,function(d){dialog.unOverlay();if(d.status==200)
{var msg=settings.subscribe_verify==1?_this.lang.get('subscribe_verify'):_this.lang.get('unsubscribe_msg');dialog.el.find('.jcm-dg-content').empty().append(msg);_el.removeClass('_on').addClass('_off');_el.removeAttr('data-hash');window.setTimeout(function(){dialog.off();},30000);}else if(d.status==400)
{dialog.el.find('.jcm-dg-content').empty().append(d.error);}
dialog.el.find('.jcm-dg-submit').remove();},'json')}});}else{var dialog=new _this.dialog({caption:_this.lang.get('subscribe'),content:'<span>'+_this.lang.get('please_wait')+'</span>',submitLabel:_this.lang.get('subscribe'),loadfn:function(dialog)
{$.get(_this.helper.url({task:'subscribe.suggest'}),{key:_this.config.key},function(d){if(d.status==200)
{if(d.data.followed==1)
{var msg=_this.lang.get('followed_status');dialog.el.find('.jcm-dg-content').empty().append(msg);dialog.el.find('.jcm-dg-submit').remove();_el.addClass('_on').removeClass('_off');}else{var html='<span>'+_this.lang.get('fill_your_info')+'</span><br/>';html+='<span>'+_this.lang.get('your_name')+'</span><input type="text" name="name" value="'+d.data.name+'" />';html+='<span>'+_this.lang.get('your_email')+'</span><input type="email" name="email" value="'+d.data.email+'" />';dialog.el.find('.jcm-dg-content').empty().append(html);}}else if(d.status==400){dialog.el.find('.jcm-dg-content').empty().append(d.error);}},'json');},submitfn:function(dialog)
{var _nameEl=dialog.el.find('[name=name]'),_emailEl=dialog.el.find('[name=email]');if(/^\s*$/.test(_nameEl.val()))
{_nameEl.focus();return false;}
if(/^\s*$/.test(_emailEl.val))
{_emailEl.focus();return false;}
dialog.el.find('.jcm-dg-submit,.jcm-dg-cancel').attr('disabled','disabled');$.post(_this.helper.url({task:'subscribe.add'}),{key:_this.config.key,name:_nameEl.val(),email:_emailEl.val()},function(d){dialog.el.find('.jcm-dg-submit,.jcm-dg-cancel').removeAttr('disabled');if(d.status==200)
{var msg=_this.lang.get('followed_status');_el.addClass('_on').removeClass('_off');if(d.hash!=1)
{_el.attr('data-hash',d.hash);}
dialog.el.find('.jcm-dg-content').empty().append(msg);dialog.el.find('.jcm-dg-submit').remove();window.setTimeout(function(){dialog.off();},3000);}else if(d.status==400)
{dialog.el.find('.jcm-dg-content').empty().append(d.error);dialog.el.find('.jcm-dg-submit').remove();}},'json');}});}}).on('click','.jcm-task-collapse,.jcm-task-expand',function(){var _el=$(this).closest('.jcm-block');_el.toggleClass('jcm-collapse');_el.toggleClass('jcm-expand');}).on('click','.jcm-toggle-all',function(){_this.box.find('.jcm-block').removeClass('jcm-collapse jcm-expand').addClass($(this).hasClass('_on')?'jcm-collapse':'jcm-expand');$(this).toggleClass('_on _off');}).on('click','.jcm-dropdown-toggle',function(e){var _el=$(this).parent();_el.toggleClass('active');}).on('click','.jcm-map-dest',function(e){e.preventDefault();var _el=$(this),location=_el.attr("data-location").split(",");dialogMap=new _this.dialog({caption:_el.text(),content:'<div class="mapContent">'+_this.lang.get('please_wait')+'</div>',submitLabel:false,submitfn:function(dialog)
{},cancelfn:function(dialog)
{},loadfn:function(dialog)
{window.setTimeout(function(){var mapLoader=new google.maps.Map(dialog.el.find('.mapContent')[0],{center:new google.maps.LatLng(location[1],location[0]),zoom:13}),html='<div class="infowindow-content">';html+='<img src="" width="16" height="16" class="_icon" alt="">';html+='<span class="_name"  class="title"></span><br>';html+='<span class="_address"></span></div>';dialog.el.find('.jcm-dg-content').prepend(html);var infowindow=new google.maps.InfoWindow(),infowindowContent=dialog.el.find('.infowindow-content');infowindow.setContent(infowindowContent[0]);var marker=new google.maps.Marker({map:mapLoader,anchorPoint:new google.maps.Point(0,-29)});var marker_loc=new google.maps.LatLng(location[1],location[0]);marker.setPosition(marker_loc);marker.setVisible(true);infowindowContent.find('._name').text(_el.text());infowindowContent.find('._address').text(_el.attr("data-address"));infowindowContent.find('._icon').attr("src",decodeURIComponent(_el.attr("data-img")));infowindow.open(mapLoader,marker);},300);}});}).on('click','.jcm-files-attached ._detail',function(){$(this).toggleClass('_off').toggleClass('_on');});$(document).click(function(e){if($(e.target).closest('.jcm-dropdown').length)
{var _el=$(e.target).closest('.jcm-dropdown');_this.box.find('.jcm-dropdown.active').not(_el).removeClass('active');}else{_this.box.find('.jcm-dropdown.active').removeClass('active');}});_this.sharefn();var jcmrs=function()
{_this.box.width()>450?_this.box.removeClass('jcm-xsmall'):_this.box.addClass('jcm-xsmall');var plyrs=null;if(plyrs!=null)clearInterval(plyrs);plyrs=setInterval(function(){if(!$('.jcm-player').length)return;$('.jcm-player').each(function(){var pel=$(this);pel.find('.jcm-player-main').css('height',(pel.width()*9/16-1)+'px');pel.find('.jcm-player-main').css('background-image','url('+pel.find('.jcm-player-main').attr('data-image')+')');pel.find('.jcm-player-main').click(function(){if($(this).hasClass('active'))return;$(this).addClass('active');pel.find('.jcm-player-main').css('background-image','');pel.find('.jcm-player-main').append('<iframe width="853" height="480" src="'+pel.find('.jcm-player-main').attr('data-embed')+'" frameborder="0" allowfullscreen></iframe>');});});},1000);};$(window).resize(function(){jcmrs();});jcmrs();(function(){function CustomEvent(event,params){params=params||{bubbles:false,cancelable:false,detail:undefined};var evt=document.createEvent('CustomEvent');evt.initCustomEvent(event,params.bubbles,params.cancelable,params.detail);return evt;}
CustomEvent.prototype=window.Event.prototype;window.CustomEvent=CustomEvent;})();if(settings.refresh>0)
{_this.box.find('.jcm-refresh').addClass('active');var timeSub=settings.refresh*60;window.setInterval(function(){if(timeSub<=0)
{timeSub=settings.refresh*60;var _config={timestamp:0,timestamp_offset:_this.timestamp.hasOwnProperty(0)?_this.timestamp[0]:_this.config.timestamp,sort:'desc',page_comment:1};_this.box.find('.jcm-refresh').addClass('_loading');_this.reload(_config,function(d){_this.timestamp[0]=d.timestamp;if(!_this.box.find('.jcm-root').length)
{_this.box.find('#jcm-comments').append('<ul class="jcm-root"></ul>');}
_this.box.find('.jcm-root').prepend(d.html);_this.tmpCache={};_this.box.find('.jcm-refresh').removeClass('_loading');});}
var time_m=parseInt(timeSub/60),time_s=timeSub-time_m*60;var time_fm=(time_m<10?'0'+time_m.toString():time_m)
+':'
+(time_s<10?'0'+time_s.toString():time_s);_this.box.find('.jcm-refresh-sub').text(time_fm);timeSub-=1;},1000);}
var __jumpToCmid=function(id){_this.box.find('.jcm-block._light').removeClass('_light');_this.box.find('.jcm-block._blue').removeClass('_blue');if($('#comment-'+id).length)
{let elCm=$('#comment-'+id),elCmTo=function(){$('html, body').animate({scrollTop:elCm.offset().top-100},300,function(){elCm.addClass('_light');});};if(settings.openform!='0'){setTimeout(function(){elCmTo();},1000);}else{elCmTo();}
return;}
var _config={timestamp:_this.timestamp.hasOwnProperty(0)?_this.timestamp[0]:_this.config.timestamp,parent_id:0,timestamp_offset:0,cmid:id,unwrap:0};_this.reload(_config,function(d){_this.box.find('#jcm-comments').empty().append(d.html);$('html, body').animate({scrollTop:_this.box.find("#comment-"+id).offset().top-100},500,function(){_this.box.find("#comment-"+id).addClass('_light');});});};$(document).on('click','a[data-jcm-self=1]',function(e){e.preventDefault();var wlCmid=$(this).attr('data-cmid');__jumpToCmid(wlCmid);});window.setInterval(function(){var wl=$('a').filter(function(){if(typeof $(this).attr('data-jcm-self')!='undefined')return false;if(/^https?\:\/\//.test($(this).attr('href')))
{var wUrl=new URL($(this).attr('href'));if(/\#comment-[1-9][0-9]*$/.test(wUrl.hash)&&wUrl.host==window.location.host)return true;return false;}else{return/\#comment-[1-9][0-9]*$/.test($(this).attr('href'));}});if(!wl.length)return;var wlCid=[];wl.attr('data-jcm-self',0);wl.each(function(){var wlAll=$(this).attr('href').match(/\#comment-([1-9][0-9]*)$/);wlCid.push(wlAll[1]*1);$(this).attr('data-cmid',wlAll[1]*1);});if(!wlCid.length)return;$.post(_this.helper.url({task:'item.cin'}),{cid:wlCid.join(','),key:_this.config.key},function(d){if(d.status!=200)return;$.each(d.data,function(kj,vj){if(vj.sf==1)$('a[data-jcm-self][data-cmid='+vj.id+']').attr('data-jcm-self',1);});},'json');},100);if(/\#comment-[1-9][0-9]*$/.test(window.location.hash)){var wlAll=window.location.hash.match(/\#comment-([1-9][0-9]*)$/);__jumpToCmid(wlAll[1]*1);}};this.reload=function(extend,callback,failureCb)
{var _config=$.extend(true,{},_this.config);if(typeof extend=='object')
{$.each(extend,function(k,v)
{_config[k]=extend[k];});}
delete _config.box;delete _config.request;$.get(_this.helper.url({task:'items.reload'}),_config,function(d){if(typeof d!='object'||d.status==400)
{if(typeof failureCb=='function')
failureCb(d);return false;}
if(typeof callback=='function')
callback(d);$(window).trigger('resize');},'json');};this.paginationEvent=function(ctrEl,pageEl,cmList)
{var _way=ctrEl.hasClass('_page_next')?'next':'previous',_limit=pageEl.attr('data-limit')*1,_page=pageEl.attr('data-page')*1,_total=pageEl.attr('data-total')*1,_pid=pageEl.attr('data-pid')*1,_cmCount=cmList.children('.jcm-block').length;ctrEl.click(function(e){e.preventDefault();if(ctrEl.hasClass('jcm-loading'))return;cmList.find('>li.hide').removeClass('hide');if(ctrEl.hasClass('jshow'))return;var _pageCurr=_cmCount/_limit>parseInt(_cmCount/_limit)?parseInt(_cmCount/_limit)+1:parseInt(_cmCount/_limit);var _config={parent_id:_pid,page_comment:_way=='next'?_page+1:(_page-_pageCurr)};ctrEl.addClass('jcm-loading');_this.reload(_config,function(d){ctrEl.removeClass('jcm-loading');if(_way=='next')
{_page+=1;if(_page>=_total)
{ctrEl.remove();}
cmList.append(d.html);}else{if(_config.page_comment==1)
{ctrEl.remove();}
cmList.prepend(d.html);_cmCount+=_limit;}},function(d){ctrEl.removeClass('jcm-loading');});});};this.paginationChild=function()
{if(!_this.box.find('.jcm-childs').not('._page').length)return false;_this.box.find('.jcm-childs').not('._page').each(function(){var _el=$(this);_el.addClass('_page');if(!_el.next('.jcm-pagination-data').length)
return true;var _pageEl=_el.next('.jcm-pagination-data'),_pageTotal=_pageEl.attr('data-total')*1,_pageLimit=_pageEl.attr('data-limit')*1,_pageActive=_pageEl.attr('data-page')*1,lengthCm=_el.children('.jcm-block').length;if(_pageTotal>1&&_pageLimit*_pageActive>lengthCm)
{var _ctrEl=$('<a href="javascript:void(0)" class="_page_previous">'+_this.lang.get('show_previous_comments')+'</a>');_el.before(_ctrEl);_this.paginationEvent(_ctrEl,_pageEl,_el);}
if(_pageTotal>_pageActive)
{var _ctrEl=$('<a href="javascript:void(0)" class="_page_next">'+_this.lang.get('show_more_reply')+'</a>');_el.after(_ctrEl);_this.paginationEvent(_ctrEl,_pageEl,_el);if((config.id<1||(config.id>0&&!_el.find('>#comment-'+config.id).length))&&_el.find('>li').length>settings.preview)
{_el.find('>li').slice(settings.preview).addClass('hide');}}else{if((config.id<1||(config.id>0&&!_el.find('>#comment-'+config.id).length))&&_el.find('>li').length>settings.preview)
{var _ctrEl=$('<a href="javascript:void(0)" class="_page_next jshow">'+_this.lang.get('show_more_reply')+'</a>');_el.after(_ctrEl);_this.paginationEvent(_ctrEl,_pageEl,_el);_el.find('>li').slice(settings.preview).addClass('hide');}}});};this.paginationRoot=function()
{var urlRoot=null,loadPage=function(page,cb)
{var _config={timestamp:_this.timestamp.hasOwnProperty(0)?_this.timestamp[0]:_this.config.timestamp,parent_id:0,timestamp_offset:0,page_comment:page,unwrap:0};if(_this.tmpCache.hasOwnProperty(page))
{_this.box.find('#jcm-comments').empty().append(_this.tmpCache[page]);_this.box.find('.jcm-root-page a').each(function(){var page=$(this).attr('data-page')*1,newUrl=urlRoot.replace(/page_comment=[1-9][0-9]*/,'page_comment='+page);$(this).attr('href',newUrl);});return;}
_this.reload(_config,function(d){_this.tmpCache[page]=d.html;_this.box.find('#jcm-comments').empty().append(d.html);if(urlRoot!=null)
{_this.box.find('.jcm-root-page a').each(function(){var page=$(this).attr('data-page')*1,newUrl=urlRoot.replace(/page_comment=[1-9][0-9]*/,'page_comment='+page);$(this).attr('href',newUrl);});}
if(typeof cb=='function'){cb();}else{$('html, body').animate({scrollTop:$('#jcm-comments').offset().top-100},300);}});};if(_this.config.page_comment==1)
{if(!settings.cache)
{_this.config.timestamp=parseInt(new Date().getTime()/1000);loadPage(1,function(){$('#jcm-comments').removeClass('hide hidden');});}}
_this.box.on('click','.jcm-root-page a',function(e){e.preventDefault();var _el=$(this),page=_el.attr('data-page')*1,url=_el.attr('href');if(urlRoot==null)urlRoot=url;if(_el.parent().hasClass('a-selected'))return false;_el.parent().siblings().removeClass('a-selected');_el.parent().addClass('a-selected');loadPage(page);window.history.pushState({etype:'jcm',page:page},'',url);});window.onpopstate=function(e){if(e.state&&e.state.etype=='jcm'){loadPage(e.state.page);}
if(e.state==null)
{}};};this.init=function()
{if(_this.box==null||!_this.box.length)
{console.log("Error: No comment box found.");return false;}
if(settings.hasOwnProperty('translate'))
{_this.lang.load(settings.translate);}
if(/\#comment-[1-9][0-9]*$/.test(window.location.hash)){var wlAll=window.location.hash.match(/\#comment-([1-9][0-9]*)$/);config.id=wlAll[1]*1;}
_this.box.on('emoji',function(){if(!_this.emoji.loaded)
{_this.emoji.loaded=true;_this.emoji.init();}});var curl=window.location.href.replace(window.location.hash,'');if(curl.indexOf(settings.url)==-1)
{settings.url=curl.replace(/(\?|\&)?page_comment\=[0-9]*/g,'');_this.box.find('.page-button a').each(function(){var _page=$(this).attr('data-page'),_newUrl=settings.url+(settings.url.indexOf('?')==-1?'?':'&')+'page_comment='+_page;$(this).attr('href',_newUrl);});}
_this.events();_this.tpl.form=_this.box.find("#jcm-form").clone();_this.createFormEvents(_this.box.find("#jcm-form"));$(window).on('jcmQuote',function(e,text){$('#jcm-form .jcm-textarea').html('<div data-tag="quote" data-area="self">'+text+'</div><div>...</div>');$('#jcm-form').toggleClass('active');$('#jcm-form .jcm-textarea').focus();});_this.paginationRoot();if(config.id>0)
{let fff=function(){$('html, body').animate({scrollTop:_this.box.find("#comment-"+config.id).offset().top-100},500,function(){_this.box.find("#comment-"+config.id).addClass('_light');});};window.setTimeout(function(){fff();$(window).on('load',function(){fff();});},2000);}
var hlDelay=null;$('body').click(function(e){if(hlDelay!=null)clearTimeout(hlDelay);hlDelay=setTimeout(function(){if($(e.target).closest('.jcm-block').length)
{var el=$(e.target).closest('.jcm-block');if(!el.hasClass('_light')&&!el.hasClass('_blue'))
{_this.box.find('.jcm-block').removeClass('_light _blue');}}},100);});if(config.awe.v=="v4")
{var aj=function(){$('#jlexcomment, .jcm-dialog').find('.far, .fas').removeClass('far fas').addClass('fa');var ic_maps={'fa-map-marker-alt':'fa-map-marker','fa-grin-hearts':'fa-smile-o','fa-arrow-alt-circle-down':'fa-arrow-circle-down'};$.each(ic_maps,function(o,n){$('.'+o).removeClass(o).addClass(n);});}
aj();$(document).ajaxComplete(function(){aj()});}
if(config.awe.src=="local"&&config.awe.v=="v5")
{var aj=function(){$('#jlexcomment, .jcm-dialog').find('.far').removeClass('far').addClass('fas');}
aj();$(document).ajaxComplete(function(){aj()});}};};
