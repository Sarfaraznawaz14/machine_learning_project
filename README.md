# machine_learning_project

### software and account requirement

1. [github account](https://github.com/)
2. [heroku account](https://devcenter.heroku.com/articles/heroku-cli)
3. [VS CODE IDE]
4. [GIT CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
5. [GIT DOCUMENTATION](https://git-scm.com/docs)

Creating conda environment

'''
conda create -p venv python==3.7 -y
'''
'''conda activate venv/ or conda activate venv'''

'''
pip install -r requirements.txt
'''

to add files to git

'''
git add . or git add filename
'''

Note: to ignore file or folder from git we can write name of file/folder in .gitignore file

to check the git status

'''
git status
'''

to check all version by git 
'''
git log
'''

to create version/commit all the changes to git

'''
git commit -m "message"
'''

to send version/changes to github

'''
git push origin main
'''

to check remote url

'''
git remote -v
'''

heroku email = nawazme.rymec@gmail.com
heroku api key = copy from heroku
heroku application name = ml-project

BUILD DOCKER IMAGE

'''
docker build -t <image_name>:<tagname> .
'''

Note: Image name must be lowercase, and tag name as latest

to list docker image

'''
docker images
'''
to run the docker image

'''
docker run -p 5000:5000 -e PORT=5000 <image_ID>
'''

note: image id will be found when we list docker images

to check running container in docker

'''
docker ps
'''

to stop docker container

'''
docker stop <container_id>

'''