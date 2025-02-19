##  COMS 7900 Docker/YAML Assignment (KQV Group)

This github includes the code for our Docker/YAML group assignment for COMS 7900.  The following files are included:

* Dockerfile: instructions for building the Docker image (think of this like a script)
* app.py: code that performs the addition opperation (what is actually running)
* requirements.txt: pip install requirements; any libraries required
* templates: html for webpage

### How to run

1. Make a YAML file (named docker-compose.yml) with this content:

   <clipboard-copy for="code-block"></clipboard-copy>
<pre id="code-block">
<code>
version: '3.9'

services:
   kqv_service:
      build:
         context: https://github.com/abigamkelly/KQV_YAML.git    
      container_name: kqv_yaml
      ports:
         - "9001:9001"

</code>
</pre>

2. Open the terminal
3. Change current directory to where the docker-compose.yml file is located
4. Type the following command to build and run the container: **docker compose up -d**
5. Open the browser and type the following in the search bar: **localhost:9001**
6. Follow the prompts on the webpage
7. To stop to container, open the command line and type the following command: **docker container stop CONTAINER_ID**
