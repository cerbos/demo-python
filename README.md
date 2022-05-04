# Cerbos Python Demo

Run the following command to try out the demo:

```shell
./pw demo
```

The demo script (`main.py`) starts a new Cerbos container with the policies from the `policies` directory and sends requests for a set of different principals and resources to demonstrate how policy evaluation works.

Try deleting the `condition` block attached to the `direct_manager` derived role (line 23--28 in `policies/derived_roles_1.yml`) and running `./pw demo` again. Amanda, who was previously disallowed from viewing or approving Harry’s leave requests should now be allowed to do those actions. 


## Demo Video
Watch the demo with commentary:
<a href="https://www.loom.com/share/0425d8a075804d528185ad2ba30817b3">
    <p>Cerbos Python Demo (GitHub) - Watch Video</p>
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/0425d8a075804d528185ad2ba30817b3-with-play.gif">
  </a>

## Playground
Launch the policy from this demo in the playground. Play with it to see how Cerbos behaves.
<P><a href="https://play.cerbos.dev/p/UWG3inHjwrFhqkv60dec623G9PoYlgJf"><img src="https://github.com/cerbos/express-jwt-cerbos/blob/main/docs/launch.jpg"></a></p>
