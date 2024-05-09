var chetemeDBadapter = new LokiIndexedAdapter('cheteme');

//chetemeDBadapter.deleteDatabase('cheteme.db');\n\
var chetemeDB = new loki('cheteme.db', { adapter: chetemeDBadapter });
var TemplateColl = chetemeDB.addCollection("Template");

var awesomeColl = chetemeDB.addCollection("Awesome", {unique: ['bg']});
var keywordsColl = chetemeDB.addCollection("Keywords", {unique: ['bg']});

var genresColl = chetemeDB.addCollection("Genres", {unique: ['gid']});




//chetemeDB.loadDatabase(function(result)\
//  console.log('loadDatabase', result);\n//});\n</script>