# Cerbos Python Demo

Make sure you have Python 3.9 and your environment has the dependencies in `requirements.txt` installed before running.

Depending on your configuration, you may want to change `CERBOS_URL` in `main.py`.

Policies to use with your Cerbos server are in the `cerbos-bin/policy` folder.

* Start the Cerbos server
    ```sh
    ./cerbos-bin/start.sh
    ```
* In another terminal window, create a new virtual environment to run `./main.py` and start the demo
    ```sh
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ./main.py
    ```
* Try deleting the `condition` block attached to the `direct_manager` derived role (line 23-28 in `cerbos-bin/policy/derived_roles_1.yml`) and running `./main.py` again. Amanda, who was previously disallowed from viewing or approving Harry’s leave requests should now be allowed to do those actions. 


## Demo Video
Watch the demo with commentary:
<a href="https://www.loom.com/share/0425d8a075804d528185ad2ba30817b3">
    <p>Cerbos Python Demo (github) - Watch Video</p>
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/0425d8a075804d528185ad2ba30817b3-with-play.gif">
  </a>
