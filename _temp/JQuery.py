from anvil.js.window import jQuery as jQ



def clean():
    jQ('#anvil-header').remove()
    jQ('#anvil-badge').remove()
    #jQ('#loadingSpinner').remove()
    #jQ('#error-indicator').remove()
    jQ('html').removeClass()