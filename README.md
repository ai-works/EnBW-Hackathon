# EnBW-Hackathon
## Organizer Hackathon Website
https://www.enbw.com/hackathon/home/
## Setup
### Get the code and change to repository directory
```
git clone https://github.com/alexgawrilow/EnBW-Hackathon.git
cd EnBW-Hackathon
```
### (If not done) Install python package `virtualenv`
https://virtualenv.readthedocs.io/en/latest/installation/
### Create and activate virtual environment
The virtual environment is called `venv` and should be created in the repository.
```
virtualenv venv
source venv/bin/activate
```
### Install necessary python packages
```
pip install -r requirements.txt
```
### Install ipython kernel for Jupyter Notebook
```
ipython kernel install --user --name=EnBW_kernel
```
Select this kernel when working with Jupyter Notebook.
## Workflow
### After installing python packages
Add name of packages to requirements.txt.
```
pip freeze > requirements.txt
```
Don't forget to push the changes to that file.

## Link collection
https://github.com/opencv/opencv/tree/master/data/haarcascades

Tutorial für cv dnn
https://www.arunponnusamy.com/yolo-object-detection-opencv-python.html
https://github.com/arunponnusamy/object-detection-opencv
weights:
https://pjreddie.com/media/files/yolov3.weights

XML-Dateien für Haar Cascade zum Downloaden
http://alereimondo.no-ip.org/OpenCV/34/



