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

function navClick(element, event) {
    // Prevent default link behavior event.preventDefault();
    // Stop any other event handlers from firing event.stopImmediatePropagation();

   // Your code here
   console.log("Event fired once" , element);

   // Correcting the reference to the clicked element
   anvil.call($("#appGoesHere > div"), 'navigation_click', element);
}
