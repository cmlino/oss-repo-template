# Lab 8

## Example 0
Docker is running.
<img src="example00.PNG">

## Example 1
### Running the Ubuntu Container
<img src="example01_1.PNG">

### Installing Vim
Vim was installed in the `/root` directory and was used to create `test.txt`.
<img src="example01_2.PNG">

### Installing Cowsay
This is output when `cowsay "moo!" is run.
<img src="example01_3.PNG">

## Example 2
### Rocketchat
The following screenshot contains the set up of the RocketChat database as an instance of mongo, which is then linked to the mongo instance. The screenshot also shows a list of the running containers and examples of stopping and removing containers. The list of images is shown, and the image of ubuntu is also removed.
<img src="example02.PNG">

Here is an image of RocketChat in my local browser:
<img src="example02_2.PNG">

## Example 3
Here is the Dockerfile:
<img src="example03_a.PNG">

I built the Dockerfile, and ran the container and opened the port for the web server:
<img src="example03.PNG">

Here is the web server:
<img src="example03_1.PNG">


## Example 4
### Image creation
I created the Dockerfile:
<img src="example04_1.PNG">

I created the docker image using the command `docker build -t message app .`:
<img src="example04_2.PNG">

I list all images available on the Docker host:
<img src="docker_images.PNG">

Docker-compose being built and run:
<img src="example04_3.PNG">
<img src="example04_4.PNG">

The build was successful. I added "hola" and "hello" to the list of messages. Here is a screenshot of the text `como_estas` being added to the list of messages and a list of all the messages that were added. 
<img src="example04_5.PNG">

The following screenshot shows the `como_estas` message getting modified to be `estoy_bien`. The next commands delete `estoy_bien` from the list, and then show the list of remaining messages.
<img src="example04_7.PNG">