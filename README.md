# Cerbos Python Demo

Make sure your environment has the dependencies in `requirements.txt` installed before running.

Depending on your configuation, you may want to change the port number in the cerbos library in `cerbos/__init__.py`

Policies to use with your cerbos server are tin the `policy` folder.

To start the Cerbos server:
* Make sure you have access to JFrog repository by running: 
  
   `echo YOUR_API_KEY | docker login pkg.cerbos.dev -u YOUR_USERNAME --password-stdin`
* Run `./start.sh` in the `cerbos-bin` folder.

