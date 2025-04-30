/**
 * @extensione  YRVote Plugin for Marlev Template ONLY!
 * @author      Lev Milicenco
 * @copyright   (c) Marlev.it - Itroom SRLS - 2016. All rights reserved.
 * @license     GNU General Public License version 2 or later; see LICENSE.txt
 */

jQuery.star_to_default = function star_to_default(w_class, timer) {
    setTimeout(function () {
        jQuery(w_class).removeClass("offhover onhover");

    }, timer);
};



jQuery.onhover_rating = function hover_rating(element) {

    jQuery(element).parent().find(".star-hovered").removeClass("star-hovered").promise().done(function () {
        jQuery(element).addClass("star-hovered");

    });

    var num = jQuery(element).data("vote");
    var timer = 0;
    jQuery(element).parent().find(".yrvote-star").each(function () {
        var t_this = jQuery(this).find("span");
        var get_num = jQuery(this).data("vote");
        var active = jQuery(this).parent().data("active");
        var off = jQuery(this).parent().data("off");
        if (get_num <= num) {

            if (!jQuery(t_this).hasClass("onhover")) {

                setTimeout(function () {
                    jQuery(t_this).removeClass("offhover").addClass("onhover");

                }, timer);

                timer = timer + 100;
            }
        } else {

            jQuery(t_this).addClass("offhover").removeClass("onhover");

        }
    });
};

jQuery.ratting_to_default = function ratting_to_default(element) {
    var ratting = jQuery(element).parents(".yrvote_box").data("rating").toString().split(".");

    if (parseInt(ratting[1]) > 0) {
        ratting = parseInt(ratting[0]) + 1;
    } else {
        ratting = parseInt(ratting[0]);
    }

    var hovered_element = jQuery(element).find(".star-hovered");
    var hovered = jQuery(hovered_element).data("vote");

    var timer = 0;
    if (hovered >= ratting) {
        for (var i = hovered; i > 0; i = i - 1) {
            var w_class = jQuery(element).find(".yrstar-" + i).find("span");
            jQuery.star_to_default(w_class, timer);
            timer = timer + 100;

        }
    } else {
        for (var i = hovered; i < 6; i = i + 1) {
            var w_class = jQuery(element).find(".yrstar-" + i).find("span");
            jQuery.star_to_default(w_class, timer);
            timer = timer + 100;

        }
    }
    jQuery(element).find(".star-hovered").removeClass("star-hovered");
};






jQuery(document).ready(function () {

    jQuery(".yrvote-star").hover(function () {
        clearTimeout(window.yrovote_todefault);
        jQuery.onhover_rating(this);
    });




    jQuery(".yrvoteimg").mouseleave(function () {
        if (jQuery(this).find(".star-hovered").length) {

            var element = jQuery(this);
            window.yrovote_todefault = setTimeout(function () {
                jQuery.ratting_to_default(element);
            }, 400);
        }
    });



    // jQuery(".yrvoteimg").each(function () {
    //     var w = 0;
    //     jQuery(this).find(".fa").each(function () {
    //         w = jQuery(this).width() + w;
    //     });
    //     jQuery(this).css({"width": w + w});
    //     jQuery(this).parent().find(".yrvotetotal").css({"width": w + w});
    // });


});
