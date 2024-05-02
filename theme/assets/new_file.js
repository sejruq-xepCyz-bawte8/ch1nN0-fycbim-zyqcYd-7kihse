
  function loadScript(url) {
    var script = document.createElement('script');
    script.src = url;
    document.head.appendChild(script);
}
loadScript("_/theme/lokijs.js")
loadScript("_/theme/loki-indexed-adapter.js")




  var chDBadapter = new LokiIndexedAdapter('cheteme');
  chDBadapter.deleteDatabase('cheteme.db')
  var chDB = new loki('cheteme.db', { adapter: chDBadapter });

  chDB.loadDatabase(function(result) {
  console.log('done');
});

  chDBadapter.deleteDatabase('test')
