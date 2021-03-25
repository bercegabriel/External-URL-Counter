# set base image
FROM python:3.9.1

# set the working directory in the container
WORKDIR /plugincontainer

# copy the content of the local src directory to the working directory
COPY plugin.py .

# command to run on container start
CMD [ "python", "plugin.py" ]