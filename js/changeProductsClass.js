    $(document).ready(function() {
        $("figure.shop-category-image").parent().mouseenter(function() {
            $(this).children().next().animate({
                opacity: "toggle"
            }, 400);
        });
        $("figure.shop-category-image").parent().mouseleave(function() {
            $(this).children().next().animate({
                opacity: "toggle"
            }, 400);
        });
    });