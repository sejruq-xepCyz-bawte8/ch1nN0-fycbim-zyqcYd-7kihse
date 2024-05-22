if (!document.querySelector('#editor').__quill) {
    var quill = new Quill('#editor', {
        theme: 'snow',
        formats: ['italic', 'bold', 'header', 'align', 'blockquote' ],
        modules: {
                        counter: {
                                  container: '#counter',
                                  unit: 'word'
                                },
                        toolbar: '#toolbar',
                  }
    });
}

// Prevent zooming on touch events outside the editable content
document.addEventListener('touchstart', function(event) {
    // Check if the touch event occurred outside the editable content
    var target = event.target;
    if (!target.closest('#editable-content') && target.isContentEditable === false) {
        // Prevent default touch behavior (zooming)
        //event.preventDefault();
    }
}, { passive: false });


