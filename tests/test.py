import sys
sys.path.append("src/")

from restrunner import RestRunner

app = RestRunner()
app.set("debug", True)
app.run()


# app.set("port", 8000)
# app.set("debug", False)
# app.set("host", "0.0.0.0")
# print(app.config('port'))
#app.set("data_folder", "/tmp")
## todo: data folder creating 
## todo: templates tasks.json and commands.json