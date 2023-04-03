## Create project directory
~~~bash
mkdir ~/MLOps_parser && cd ~/MLOps_parser
git clone git@github.com:RizhovDenis/MLOps-Production-parser.git
python3 -m venv proj_venv
source proj_venv/bin/activate && cd ~/MLOps_parser
pip install -r requirements.txt
~~~
## Prepare database
~~~bash
alembic upgrade head
~~~
## Run project
~~~bash
python setup.py
~~~
