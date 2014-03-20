    $(document).ready(function() {
        $("figure.shop-product-image").parent().mouseenter(function() {
            $(this).children().next().animate({
                opacity: "toggle"
            }, 400);
        });
        $("figure.shop-product-image").parent().mouseleave(function() {
            $(this).children().next().animate({
                opacity: "toggle"
            }, 400);
        });
    });