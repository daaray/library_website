/*
 * Get libal id for the page.
*/
function getLibCalId() {
    var libcalid = $('#current-hours').data('libcalid');
    $.ajax({
        dataType: 'json',
        url: '/json-hours/?fallback=true',
        async: false,
        success: function (data) {
            fallback = data.llid;
        }
    });
    if (libcalid == '') {
        return fallback;
    } 
    return libcalid;
}

/*
 * Ajax call to libcal. Renders hours in the header. 
 */
function renderHours(libcalid){
    json = $.getJSON('/json-hours/?libcalid='.concat(encodeURIComponent(libcalid)), function(data) {
        var innerJson = JSON.parse(data.all_building_hours);
        var currentLlid = data.llid;
        var html ='';
        var currentHoursHtml = '';

        // Build the html
        $.each(innerJson, function(keystr, val){
            var key = JSON.parse(keystr);
            var llid = innerJson[key][0];
            var hours = innerJson[key][1];

            if (llid != currentLlid) {
                html += '<li><a href="#">' + hours + '</a></li>';
            } else {
                // Render the current building hours as selected
                var currentHoursHtml = '<span>' + hours  + '</span>';
                $('#current-hours-target').replaceWith(currentHoursHtml);
            }
        });

        // Render the hours dropdown
        $('#hours-dropdown').prepend(html); 
    });
}

/*
 * Ajax call to workshops and events feed.
 */
function renderEvents() {
    var feed = $('#events').data('events'); // Already encoded
    var eventsHtml = '';
    if (feed) {
        json = $.getJSON('/json-events/?feed='.concat(feed), function(data) {
            var innerJson = data['events'];
            $.each(innerJson, function(key, val){
                var title = innerJson[key][0];
                var url = innerJson[key][1];
                var date = innerJson[key][2];
                var time = innerJson[key][3];
                eventsHtml += '<p><a id="event-header" href="' + url + '">' + title + '</a><br/><span class="event-date">' + date + '</span> | ' + time; 
            });
            $('#events-target').replaceWith(eventsHtml);
        });
    }
}

/*
 * Ajax call to wordpress for news.
 */
function renderNews() {
    var feed = $('#news-target').data('news-feed'); // Already encoded
    var newsHtml = '';
    if (feed) {
        json = $.getJSON('/json-news/?feed='.concat(feed), function(data) {
            var innerJson = data['news'];
            var has_stories = innerJson.length > 0;
            if (has_stories) {
                $('#news-header').removeClass('hidden');
            }
            $.each(innerJson, function(key, val){
                var title = innerJson[key][0];
                var tag = innerJson[key][2];
                var desc = innerJson[key][3];
                var link = innerJson[key][1];
                var css = innerJson[key][4];
                var img = innerJson[key][5];
                newsHtml += '<div class="newsblock col-xs-12 col-sm-6 col-md-3">'
                newsHtml += '<figure class="embed"><div class="figure-wrap">'
                newsHtml += '<a href="' + link + '"><img class="img-responsive" src="' + img + '"></a></div>'
                newsHtml += '<figcaption class="' + css + '">' + tag + '</figcaption></figure>'
                newsHtml += '<a href="' + link + '"><h5>' + title + '</h5></a>'
                newsHtml += '<p>' + desc + '<br><a href="' + link + '">Read more...</a></p>'
                newsHtml += '</div>'
            });
            $('#news-target').replaceWith(newsHtml);
        });
    }
}
    

$(document).ready(function(){

    /* 
     * Collection browse pages "Limit to digital materials" button. 
     */

    // hide the submit button if javascript is enabled. 
    $('#checkboxdigital').closest('form').find('input[type="submit"]').hide();
    // when the checkbox is clicked, submit the form automatically. 
    $('#checkboxdigital').change(function() {
        $(this).closest('form').submit();
    });

    /*
     * Search Widget, Catalog search, Begins-With searches.
     */

    // If this script is running (i.e., JavaScript is enabled) add dropdown elements for browses. 
    $('#search_widget_catalog_search').each(function() {
        var select = $(this).find('select[name="type"]');
        select.append('<option value="browse_title">Title begins with</option><option value="browse_journal">Journal begins with</option><option value="browse_lcc">Call Number begins with</option>');
    });

    // Modify browses before the form is submitted.
    $('#search_widget_catalog_search').submit(function() {
        // If the field pulldown's value begins with "browse_"...
        var type = $(this).find('select[name="type"]').val();
        if (type.substring(0, 7) == 'browse_') {
            // Make a new hidden element called "source" for everything after "browse_". 
            $('#search_widget_catalog_search').append('<input name="source" type="hidden" value="' + type.substring(7) + '"/>');
            // Remove the original "type" element.
            $(this).find('select[name="type"]').remove();
            // Change the name of the text input from "lookfor" to "from". 
            $(this).find('input[name="lookfor"]').attr('name', 'from');
            // Change the action of the form so it points to the browse result pages. 
            $(this).attr('action', 'https://catalog.lib.uchicago.edu/vufind/Alphabrowse/Home');
        }
    });

    // Render news html
    renderNews()

    // Render hours html in the header
    renderHours(getLibCalId());

    // Render events widget html in the right sidebar
    renderEvents();

    /*
     * Lightbox
     */
    $(document).delegate('*[data-toggle="lightbox"]', 'click', function(event) {
        event.preventDefault();
        $(this).ekkoLightbox();
    });

});
