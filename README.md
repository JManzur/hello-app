# hello-app

A simple Python Flask apps that you can use for demo purposes.

```bash
while true; do echo -n; k exec -it hello-app -- curl localhost:8883/status | jq -r; sleep 1; done
```

If you want to use this app to test horizontal pod autoscaler, you can use the following endpoint to stress the CPU:

```bash
while true; do echo -n; curl -s localhost:8883/stress | jq -r; sleep 0.001; done
```

The `/stress` endpoint run a math calculation that will stress the CPU.

Also, both `/status` and `/stress` endpoint will return the pod name, so you can demostrate that the request is load balanced between the pods.