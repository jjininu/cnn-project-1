# this is to create env and install all the req, instaid of running pip install on terminal
# echo is just to print a massage 
# creating such script with python script can result an issue , so thats why shell script is used
# it has to be run in gitbash terminal

echo [$(date)]: "START" 
echo [$(date)]: "creating env with python 3.8 version" 
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activating the environment" 
source activate ./env
echo [$(date)]: "installing the dev requirements" 
pip install -r requirements_dev.txt
echo [$(date)]: "END" 