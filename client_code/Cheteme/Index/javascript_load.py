from ..Helpers.Javascript import script_to_head_load

scripts = [
"_/theme/javascript/init.js",
"https://kit.fontawesome.com/dcfe5f394f.js",
"https://cdn.jsdelivr.net/npm/quill@2.0.1/dist/quill.js",
"_/theme/javascript/init_viewport.js",
"_/theme/javascript/lokijs.js",
"_/theme/javascript/loki-indexed-adapter.js",
"_/theme/javascript/quill_counter.js",
]



def load_all_js_scripts() -> None:
    for script in scripts:
        script_to_head_load(script)
