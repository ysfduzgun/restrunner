import sys
sys.path.append("../.")

from restrunner import RestRunner

app = RestRunner()
app.set("port", 8000)
app.set("debug", True)
print(app.config('port'))
app.run()

## todo: data folder creating 
## todo: templates tasks.json and commands.json