function sbThumbnailGallery(gallery) {
    var imageId = 0;
    var imageThumbId = 0;
    var currentImage = 1;
    var animating = false;
    var autoRotate = true;
    var interval = 8000;
    $(gallery + ' #sbThumbnailGalleryImages figure').each(function() {
        imageId = imageId + 1;
        $(this).attr('data-image-id', imageId);
    });
    $(gallery + ' #sbThumbnailGalleryThumbs figure').each(function() {
        imageThumbId = imageThumbId + 1;
        $(this).attr('data-image-thumb-id', imageThumbId);
    });
    if (Modernizr.csstransitions) {
        selectCurrentImage();
    } else {
        $(gallery + ' #sbThumbnailGalleryImages figure[data-image-id="' + currentImage + '"]').addClass('current');
        $(gallery + ' #sbThumbnailGalleryThumbs figure[data-image-thumb-id="' + currentImage + '"]').addClass('current');
    }

    function selectCurrentImage() {
        if (Modernizr.csstransitions) {
            $(gallery + ' #sbThumbnailGalleryImages figure.current').removeClass('current');
            $(gallery + ' #sbThumbnailGalleryThumbs figure.current').removeClass('current');
            $(gallery + ' #sbThumbnailGalleryImages figure[data-image-id="' + currentImage + '"]').addClass('current');
            $(gallery + ' #sbThumbnailGalleryThumbs figure[data-image-thumb-id="' + currentImage + '"]').addClass('current');
        } else {
            animating = true;
            $(gallery + ' #sbThumbnailGalleryThumbs figure.current').removeClass('current');
            $(gallery + ' #sbThumbnailGalleryThumbs figure[data-image-thumb-id="' + currentImage + '"]').addClass('current');
            $(gallery + ' #sbThumbnailGalleryImages figure[data-image-id="' + currentImage + '"]').addClass('next-image');
            $(gallery + ' #sbThumbnailGalleryImages figure.current').fadeOut(function() {
                $(this).removeClass('current');
                $(gallery + ' #sbThumbnailGalleryImages figure.next-image').addClass('current').removeClass('next-image');
                animating = false
                $(gallery + ' #sbThumbnailGalleryImages figure').attr('style', '');
            });
        }
    }
    $(gallery + ' #sbThumbnailGalleryThumbs figure').click(function() {
        if (!animating) {
            clearInterval(slideInterval);
            currentImage = $(this).attr('data-image-thumb-id');
            selectCurrentImage();
        }
    });
    $(gallery + ' #sbThumbnailGalleryNavigation a').click(function(e) {
        if (!animating) {
            clearInterval(slideInterval);
            var displayImageId;
            if ($(this).hasClass('next-image')) {
                if (currentImage + 1 > imageId) {
                    displayImageId = 1;
                } else {
                    displayImageId = currentImage + 1;
                }
            } else {
                if (currentImage - 1 == 0) {
                    displayImageId = imageId;
                } else {
                    displayImageId = currentImage - 1;
                }
            }
            currentImage = displayImageId;
            selectCurrentImage();
        }
        e.preventDefault();
    });
    if (autoRotate) {
        var slideInterval = setInterval(autoRotateSlides, interval);
    }

    function autoRotateSlides() {
        currentImage = currentImage + 1;
        if (currentImage > imageId) {
            currentImage = 1;
        }
        selectCurrentImage();
    }
    $(window).load(function() {
        $('.full-banner .image-gallery-images').fadeIn(300, function() {
            $('.full-banner').removeClass('loading');
        });
    });
    $(gallery).imagesLoaded(function() {
        var containerHeight = $('.image-gallery-images').height();
        $(gallery).animate({
            height: containerHeight
        }, 500, function() {
            $(this).find('.image-gallery-images').animate({
                opacity: 1
            }, 500)
            $(gallery).removeClass('loading').attr('style', '');
        });
    });
}
