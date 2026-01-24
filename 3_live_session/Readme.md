## creating endpoint for CURD
* so for that we will make two folder 
1. Resources , 2. services -> this for way to splits diff functionality

* resouces will capture the http request ;; it will parser it and it will take care of sending data back to the client
-> we have auth_resource.py -> we should have "/login" and '/register'

-> better to use blueprints


* services will interact with database