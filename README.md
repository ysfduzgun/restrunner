# lider-repoman-api
Pardus repository and package management !
This project was created for Liderahenk Central Management System. It will be designed to be easily used from Liderahenk Web Panel.

Planned features:
* Completely restfull
* Ability to work asynchronously
* View all task history
* Live monitoring of the status of ongoing tasks(streaming log)
* Cloning Pardus official repos
* Creating personal repos
* Adding, deleting and updating packages to this created repo
* Merge this personal repository created with Pardus repository
* Publishing these repositories
* Take snapshots of repositories
* Restore from snapshots

Testing:
```
pip install flask-restful
git clone
cd lider-repoman-api
python3 src/server.py
```

```bash
yusuf@TPX1C:~$ curl http://127.0.0.1:5000/commands
{
    "log_list": "ls ../log/",
    "uptime": "uptime",
    "tmp_folder_list": "ls /tmp/"
}
yusuf@TPX1C:~$ curl http://127.0.0.1:5000/run/log_list
"ls ../log/"
yusuf@TPX1C:~$ curl http://127.0.0.1:5000/run/test_cmd
{
    "message": "Command test_cmd doesn't exist"
}
yusuf@TPX1C:~$ curl http://127.0.0.1:5000/test
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```