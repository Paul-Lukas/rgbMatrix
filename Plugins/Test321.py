from ..basePlugin import BasePlugin


class Testris(BasePlugin):
    def __init__(self, app, output):
        super().__init__(app, output)
        self.pluginName = "Testris"
        self.version = "pre 0.1"
        
    def button(self):
        self.out.fill_all((34, 100, 66))
        self.out.submit_all()
        
    def run(self):
        pass

    def input(self, inp):
        randomVar = inp.get("Wert")

    def get_html(self):
        return """<h1 onclick="startPlugin()">Testi</h1>

<script>
function startPlugin() {
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", "/plugin/{{ start_id}}/input?Wert=1", false ); // false for synchronous request
	xmlHttp.send( null );
}
</script>"""
     
        

