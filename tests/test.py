import sys
sys.path.append("../src/.")
print(sys.path)

from restrunner import RestRunner

app = RestRunner()
app.set("port", 8000)
app.set("debug", False)
app.set("host", "0.0.0.0")
#app.set("data_folder", "/tmp")
app.run()

## todo: data folder creating 
## todo: templates tasks.json and commands.json