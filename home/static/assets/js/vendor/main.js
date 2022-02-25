$(function () {
    var $pswp = $('.pswp')[0],
        image = [],
        getItems = function () {
            var items = [];
            $('.lightboximages a').each(function () {
                var $href = $(this).attr('href'),
                    $size = $(this).data('size').split('x'),
                    item = {
                        src: $href,
                        w: $size[0],
                        h: $size[1]
                    }
                items.push(item);
            });
            return items;
        }
    var items = getItems();

    $.each(items, function (index, value) {
        image[index] = new Image();
        image[index].src = value['src'];
    });
    $('.prlightbox').on('click', function (event) {
        event.preventDefault();

        var $index = $(".active-thumb").parent().attr('data-slick-index');
        $index++;
        $index = $index - 1;

        var options = {
            index: $index,
            bgOpacity: 0.9,
            showHideOpacity: true
        }
        var lightBox = new PhotoSwipe($pswp, PhotoSwipeUI_Default, items, options);
        lightBox.init();
    });
});