RestRunner
=====

A tool for run linux command with flask rest api.

```
virtual env
source env/bin/activate
cd env && mkdir test
cd test && touch test.py
pip install RestRunner
```

test.py
```py
from restrunner import RestRunner

app = RestRunner()
app.set("debug", True)
# app.set("port", 8000)
# app.set("host", "0.0.0.0")
# app.set("data_folder", "/tmp/")
# print(app.config('port'))
app.run()
```

```
python test.py
```

gel all command
http://127.0.0.1/commands <br>
run test1 command
http://127.0.0.1/commands/run/test1
