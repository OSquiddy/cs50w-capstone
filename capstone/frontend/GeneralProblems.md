### Deploying to Production

I'm creating a list of the different issues I faced in trying to get this project deployed to a remote server, and stuff I learned along the way.

**NGINX**

NGINX is a major pain in the ass. Lots of possible configurations and no one wants to explain how things work. Here is what I've learned so far.

- Once you install nginx on the server you can find its config files at the `/etc/nginx` folder.
- `/etc` folder doesn't show up on entering the `ls` command. Nor does it show up when using `sudo` before the `ls`. (Need to find out why that is)
- `etc/nginx` has a file called *nginx.conf*. This is the main file that contains all the configurations. All other files that we create are imported as smaller modules/parts into this main file.
- There are two main folders where config files can be created. They are **conf.d** and **sites-available**. There are 2 more directories called **modules-available** and **modules-enabled**, but I'm not sure what these do. Will have to research later.
- **sites-available** has a **default** config file. This is the initial config module that is created when nginx is first installed. It is recommended not to modify this. Instead we should disable this file and use a custom created file. This is because anytime you update nginx, this file could be overwritten and you'd lose all your config settings
- To use a file as our config we copy it from the **sites-available** directory to the **sites-enabled** directory. This can be done manually, but a far better way of doing this is by creating a symbolic link. What this does is essentially link one file to another so that any changes made in the first file are reflected in the second. Not sure why we don't directly create one file in the **sites-enabled** folder and just use that. Things to look at later
- The command to create a symbolic link is: `sudo ln -s <location-of-first-file> <location-of-second-file>`. If the second file does not already exist, this command creates it at that location.
    - `sudo` stands for *SuperUser Do*. Basically provides admin rights (Do whatever a super user would be able to do)
    - `ln` - Stands for Link.
    - `-s` - Stands for symbolic (I assume. Need to see what other flags are there)
    - `<location-of-first-file>` - Here it will be the file in the *sites-available* directory. So `/etc/nginx/sites-available/<filename>`. <filename> can end with .conf or not, it doesn't seem to matter (Need to verify that)
    - `<location-of-second-file>` - Here it will be the file in the *sites-enabled* directory. So `/etc/nginx/sites-enabled/<filename>`
- Once the config file is created/modified, nginx can be restarted/reloaded with either of the following commands:
    - `sudo systemctl restart nginx`
    - `sudo service restart nginx` - If you're using a Linux Distribution without **systemd**
    - `sudo /etc/init.d/nginx restart` - For very old versions of Linux
    - `sudo nginx -s reload` - Reloads nginx

Problems:
- Navigating to any url apart from '/' is not working. 
- Styling for admin panel and django-drf is not working.

If static files aren't being served look in the `/var/log/nginx` folder. Read the contents of *error.log*. If there is a status code 404, then then nginx is unable to locate the file. Either the file doesn't exist at all or you're looking in the wrong location. It'll most likely be the second option.

If you're getting a status code of 403, (like I was), then that means that you're most likely at the correct location but you're unable to access the file. In my case, an *error 13: Permission denied* was being logged to the file. NGINX was unable to navigate to where the files were being kept because it did not have the permissions to do so.

By default, it seems as though NGINX scripts(?) run as the **www-data** user. To check if a user/group is able to access a particular file/folder run the following command: `sudo -u username stat <path>`. (For a group, use the -g flag, and enter groupname). If the user/group is unable to access the location the *Permission denied* error will show up.

I ran `ls -lah` to see the list of files and directories along with the user and group info and saw that both were set to *ubuntu*. Instead of changing the owner to *www-data* for all files and directories (which could be possible. Gotta test it out), I just added *www-data* to the *ubuntu* group, since it had all the permissions required. The command to add an existing user to another group is `sudo usermod -a -G <group-you-want-to-add-to> <username>`. On restarting nginx, the Django css files were being served successfully 


**Gunicorn**

Gunicorn configuration was not as tough as NGINX's (thankfully), but there were a few areas where I got stuck and those need to be highlighted.

- There are apparently 2 ways of running gunicorn. It can be run as a socket file or on a port. The guide I followed showed the first version so I'll link that (here)[https://arctype.com/blog/install-django-ubuntu/]
- For some reason I did not have to create the *gunicorn.service* and *gunicorn.socket* files at `/etc/systemd/system` from scratch. They were already there, and filled (altough the username it picked up was *omar* which is weird since there was no user with that name on this instance. Maybe it took my name from the oracle account? Need to test further)
- *gunicorn.socket* did not require any changes. It was the same as in the guide
- *gunicorn.servie* required some changes.
    - I initially changed the User from *root* to *ubuntu* (More on this later)
    - WorkingDirectory = This is changed to the django project folder (project, not app). So in this case it was `/home/ubuntu/cs50w/cs50w-capstone/capstone/backend`
    - ExecStart = This needs the path of the gunicorn executable. Since it was installed in the python virtual env, we need to look through the binaries (bin) folder there. For this project it was `/home/ubuntu/cs50w/cs50w-capstone/capstone/backend/python-3.8-venv/bin/gunicorn`. I made an error in this path which was hard to trakc (More on this later)
    - django_project.wsgi:application - This needs the name of the folder (Main Django application) that contains the **wsgi.py** file. It does not need the entire path again, since we've set the path in the WorkingDirectory. So all we needed for this project was `capstone.wsgi:application`
- Once all this is done, we need to set permissions for the directory that contains the sqlite file, and for the file itself
- Restart the daemon, and restart gunicorn. Also enable it to start automatically

Problems faced: Permissions for the directory need to be explicitly set from outside the directory. And it doesn't translate to the contents of the directory. Had this issue for a long time. 2 things are absolutely mandatory. The directory and the sqlite file, both need to have read/write permissions. The owner and the group must also be the same as what is in the gunicorn.service file. System logs can be read at `/var/log` by typing in the command `cat system`.
