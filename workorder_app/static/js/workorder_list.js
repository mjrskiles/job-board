// Wait until the document is ready before trying to parse it
$(document).ready(function() {
    var TABLE_SELECTOR = '#table';
    var TABLE_CONTAINER_SELECTOR = '#workorder-table';
    
    function loadNext() {
        var nextPage = $(TABLE_SELECTOR).attr('data-next-page');
        if (nextPage && shouldPage) {
            $.get('?ajax=true&page=' + nextPage, function(data) {
                var tableContainer = $(TABLE_CONTAINER_SELECTOR);
                tableContainer.empty();
                tableContainer.append(data);
            });
        }
        else {
            console.log("Couldn't get next page");
        }
    }

    var refreshRate = $(TABLE_SELECTOR).data('refresh-rate');
    setInterval(loadNext, refreshRate);
});

/*
 * Listeners
 */
var shouldPage = true;
var isFullScreen = false;

function fullScreen() {
    var el = document.documentElement;
    if (isFullScreen) {
        if (document.exitFullscreen) {
            document.exitFullscreen();
          } else if (document.mozCancelFullScreen) { /* Firefox */
            document.mozCancelFullScreen();
          } else if (document.webkitExitFullscreen) { /* Chrome, Safari and Opera */
            document.webkitExitFullscreen();
          } else if (document.msExitFullscreen) { /* IE/Edge */
            document.msExitFullscreen();
          }
    } else {
        var fs = el.requestFullscreen
          || el.webkitRequestFullScreen
          || el.mozRequestFullScreen
          || el.msRequestFullscreen;
        fs.call(el);
    }
    isFullScreen = !isFullScreen;
    $('#fullscreen-toggle').button('toggle');
}

function togglePaging() {
    shouldPage = !shouldPage;
}
