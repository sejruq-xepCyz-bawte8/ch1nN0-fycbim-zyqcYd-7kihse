// Find the existing viewport meta tag
var viewportMetaTag = document.querySelector('meta[name="viewport"]');

// Add user-scalable=no attribute if the viewport meta tag exists
if (viewportMetaTag) {
    viewportMetaTag.content += ', user-scalable=no';
} else {
    // If viewport meta tag doesn't exist, create a new one
    viewportMetaTag = document.createElement('meta');
    viewportMetaTag.name = 'viewport';
    viewportMetaTag.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no';
    
    // Append the new viewport meta tag to the head of the document
    document.head.appendChild(viewportMetaTag);
}


function loadScript(url) {
    var script = document.createElement('script');
    script.src = url;
    document.head.appendChild(script);
}
loadScript("_/theme/lokijs.js")
loadScript("_/theme/loki-indexed-adapter.js")
loadScript("https://cdn.jsdelivr.net/npm/quill@2.0.1/dist/quill.js")
loadScript("_/theme/javascript/quill_counter.js")





function navClick(element, event) {

   anvil.call($("#appGoesHere > div"), 'navigation_click', element);
}

function formClick(element, event) {

   anvil.call($("#appGoesHere > div"), 'form_click', element);
}