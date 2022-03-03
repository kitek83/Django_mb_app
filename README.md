#Django_mb_app.
In this repository I built, tested, and deployed first database-driven app(Django_mb_app).
I showed how to create database model Post, update it with Admin panel and then display the content from
the Admin Panel on the Web Page: https://immense-meadow-12420.herokuapp.com/.


#Deployment and launching to Heroku:
Logging in... done
Logged in as krzysztofkozak833@gmail.com
PS C:\Django\mb> heroku create
Creating app... done, ⬢ immense-meadow-12420
https://immense-meadow-12420.herokuapp.com/ | https://git.heroku.com/immense-meadow-12420.git
PS C:\Django\mb> heroku config: set DISABLE_COLLECTSTATIC=1
 »   Warning: config: is not a heroku command.
Did you mean config? [y/n]:
 »   Error: Run heroku help config for a list of available commands.
PS C:\Django\mb> heroku config:set DISABLE_COLLECTSTATIC=1
Setting DISABLE_COLLECTSTATIC and restarting ⬢ immense-meadow-12420... done, v3
DISABLE_COLLECTSTATIC: 1
PS C:\Django\mb> git push heroku main
Enumerating objects: 29, done.
Counting objects: 100% (29/29), done.
Delta compression using up to 8 threads
Compressing objects: 100% (23/23), done.
Writing objects: 100% (29/29), 101.24 KiB | 6.75 MiB/s, done.
Total 29 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Building on the Heroku-20 stack
remote: -----> Determining which buildpack to use for this app
remote: -----> Python app detected
remote: -----> Using Python version specified in Pipfile.lock
remote: cp: cannot stat '/tmp/build_36c5d042/requirements.txt': No such file or directory
remote: -----> Installing python-3.9.10
remote: -----> Installing pip 21.3.1, setuptools 57.5.0 and wheel 0.37.0
remote: -----> Installing dependencies with Pipenv 2020.11.15
remote:        Installing dependencies from Pipfile.lock (5835e3)...
remote: -----> Installing SQLite3
remote: -----> Skipping Django collectstatic since the env var DISABLE_COLLECTSTATIC is set.
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 78.5M
remote: -----> Launching...
remote:        Released v6
remote:        https://immense-meadow-12420.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/immense-meadow-12420.git
 * [new branch]      main -> main
PS C:\Django\mb>
