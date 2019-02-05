// Wait until the document is ready before trying to parse it
$(document).ready(function() {
    var TABLE_SELECTOR = '#table';
    var TABLE_CONTAINER_SELECTOR = '#workorder-table';
    
    function loadNext() {
        var nextPage = $(TABLE_SELECTOR).attr('data-next-page');
        if (nextPage) {
            $.get('?ajax=true&page=' + nextPage, function(data) {
                var tableContainer = $(TABLE_CONTAINER_SELECTOR);
                tableContainer.empty();
                tableContainer.append(data);
                console.log("Refreshed table async.")
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

function fullScreen() {
    document.documentElement.requestFullscreen();
}