
/***!  Script Declaration  !***/

jQuery.thankyou=function thankyou(data,yrvoteimgclass){setTimeout(function(){var itrating=jQuery(data).find("#yrvote:first");if(itrating.length>0){yrvoteimgclass.find(".yrvote-star").off("click").off("hover");yrvoteimgclass.parents(".yrvote_box").html(itrating);}},1000);};
