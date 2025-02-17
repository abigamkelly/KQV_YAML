##  COMS 7900 Docker/YAML Assignment (KQV Group)

This github includes the code for our Docker/YAML group assignment for COMS 7900.  The following files are included:

* Dockerfile: instructions for building the Docker image (think of this like a script)
* app.py: code that performs the addition opperation (what is actually running)
* requirements.txt: pip install requirements; any libraries required
* templates: html for webpage

### How to run

1. Make a YAML file with this content:

   '''<YAML>
   version: '3.8'

   services:
   
     kqv_service:
     
       build:
       
         context: https://github.com/abigamkelly/KQV_YAML.git    
         
       container_name: test-flask
       
       ports:
       
         - "9001:9001"'''
