# Cerbos Python Demo

Make sure you have Python 3.9 and your environment has the dependencies in `requirements.txt` installed before running.

Depending on your configuration, you may want to change `CERBOS_URL` in `main.py`.

Policies to use with your Cerbos server are in the `cerbos-bin/policy` folder.

* Login to the container registry  
    ```sh
    echo YOUR_API_KEY | docker login pkg.cerbos.dev -u YOUR_USERNAME --password-stdin
    ```
* Start the Cerbos server
    ```sh
    ./cerbos-bin/start.sh
    ```
* In another terminal window, run `./main.py` to start the demo
* Try deleting the `condition` block attached to the `direct_manager` derived role (line 23-28 in `cerbos-bin/policy/derived_roles_1.yml`) and running `./main.py` again. Amanda, who was previously disallowed from viewing or approving Harry’s leave requests should now be allowed to do those actions. 


