JS = """
var ls = {}, keys = Object.keys(localStorage);
for (var i = 0; i < keys.length; i++) {
    var key = keys[i];
    ls[key] = localStorage.getItem(key);
}
return ls;
"""