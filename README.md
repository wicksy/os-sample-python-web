# os-sample-python-web
Sample Hello World Python Web Application for Red Hat OpenShift

To build and deploy in OpenShift:
```
$ oc new-app python:2.7~https://github.com/wicksy/os-sample-python-web.git --name=hello-py
```

To verify deployment:
```
$ curl http://$(oc get svc | awk '/^hello-py/ {print $2}'):8080
Hello, World!
$
```
