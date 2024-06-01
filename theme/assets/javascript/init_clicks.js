function navClick(element, event) {
    anvil.call($("#appGoesHere > div"), 'navigation_click', element.id);
 }
 
 function formClick(element, event) {
    anvil.call($("#appGoesHere > div"), 'form_click', element.id);
 }