function loadScript(url) {
    var script = document.createElement('script');
    script.src = url;
    document.head.appendChild(script);
}
loadScript("_/theme/lokijs.js")
loadScript("_/theme/loki-indexed-adapter.js")


var chetemeDBadapter = new LokiIndexedAdapter('cheteme');
chetemeDBadapter.deleteDatabase('cheteme.db');
var chetemeDB = new loki('cheteme.db', { adapter: chetemeDBadapter });
chetemeDB.loadDatabase(function(result) {
  console.log('done', result);
});
