# Cerbos Python Demo

<img src="https://github.com/cerbos/cerbos/blob/main/docs/supplemental-ui/logo.png?raw=true" alt="Cerbos" width="87" height="100"/>

This project demonstrates how to work with [Cerbos](https://github.com/cerbos/cerbos) in Python projects.

It shows how Cerbos enforces access rules on a holiday request created by an employee named Harry.

## Requirements
- Minimum Python version supported by this demo is 3.10
- Your Cerbos server is up and running (check how to run a [binary](https://docs.cerbos.dev/cerbos/latest/installation/binary.html), [container](https://docs.cerbos.dev/cerbos/latest/installation/container.html) or [Helm chart](https://docs.cerbos.dev/cerbos/latest/installation/helm.html))

⚠️ If you're completely new to Cerbos make sure to check the _[How it works](https://cerbos.dev/how-it-works)_ videos!  ⚠️


## Run the demo

Make sure that the `console` / `terminal` tab you're using is positioned in the root of this `demo-python` repository.

Run the following command to launch the demo:
```shell
./pw demo
```

That's all!

The demo script (`main.py`) starts a new Cerbos container with the policies from the `policies` directory and sends requests for a set of different principals and resources to demonstrate how policy evaluation works.

Now try deleting the `condition` block attached to the `direct_manager` derived role (line 23-28 in [derived_roles_1.yml](policies/derived_roles_1.yml)) and run the `./pw demo` command again.

Amanda, who was previously disallowed from viewing or approving Harry’s leave requests should now be allowed to do those actions.

Do you understand why?

Read more about Cerbos on our comprehensive [documentation](https://docs.cerbos.dev) or join the friendly [Cerbos Slack Community](https://join.slack.com/t/cerboscommunity/shared_invite/zt-1qlny60no-E8jLaLZSu08_ZhzORQOEOA) to ask questions.

Feel free to get creative and edit [policies](policies) to test how even more complex use-cases would turn out.

## Demo Video
Watch the demo with commentary:
<a href="https://www.loom.com/share/0425d8a075804d528185ad2ba30817b3">
    <p>Cerbos Python Demo (GitHub) - Watch Video</p>
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/0425d8a075804d528185ad2ba30817b3-with-play.gif">
  </a>

## Playground
Launch the policy from this demo in the playground. Play with it to see how Cerbos behaves.
<P><a href="https://play.cerbos.dev/p/UWG3inHjwrFhqkv60dec623G9PoYlgJf"><img src="https://github.com/cerbos/express-jwt-cerbos/blob/main/docs/launch.jpg"></a></p>