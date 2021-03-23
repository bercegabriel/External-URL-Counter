# External-URL-Counter

External-URL-Counter is a python script that parses html files from your project and generate a properties json file for DxPlatform.

## Motivation

The reason for this project is to analyze html files and count the number of external links which can be introduced in file by different tags: href, src, srcset, cite and data. 

## Requirements

You must have [<b>PYTHON</b>](https://www.python.org/downloads/) and <b>tkinter</b> package installed.Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tkinter.
```bash
pip install tkinter
```

## Installation

### Local

You can download a zip archive with python script or you can clone the project.
<br>Download zip archive:
![alt text](https://user-images.githubusercontent.com/49149499/112225282-3416d900-8c35-11eb-836b-b6ae2b2125c8.png)
<br>In order to clone the project you must have the [git](https://git-scm.com/downloads) installed. After that you must open a git cmd and type the following command:
```bash
git clone https://github.com/bercegabriel/External-URL-Counter.git
```
### Docker

You can also get this project as a Docker container from [DockerHub](https://hub.docker.com/layers/142688222/alexandrasanda/plugincounter/latest/images/sha256-b7ecc0dcd7d16f5e8cf64a1d84f6ffd4fd686bf55fb328df97cc51bec4183fc6?context=explore).

To get the container:
```bash
docker pull alexandrasanda/plugincounter:latest
```

## Usage

### Local

If you download zip archive or cloned the project, you must go from cmd in directory where is the project and run:
```bash
python plugin.py
```
An user interface will appear and you must push the browse button in order to choose a project. After that you must push save button and wait until json file is generated. The output file will be genrated in your project directory.
![alt text](https://user-images.githubusercontent.com/49149499/112227654-a937dd80-8c38-11eb-942d-f7506b88c1a6.png)

### Docker

To run the container use the command below:
```bash
docker run -v "path to your project directory":"./plugincontainer/projectFolder" -v "path to directory in which you wish to see results/results":"./plugincontainer/results" alexandrasanda/plugincounter
```

## Output file

The output file will have a structure like:<br>
![alt text](https://user-images.githubusercontent.com/49149499/112228228-a689b800-8c39-11eb-835a-c1466ab4568d.png)

## Results
If you upload output file in DX Platform, you can see the following results:<br>
![alt text](https://user-images.githubusercontent.com/49149499/112228638-47787300-8c3a-11eb-9df5-39eb8d66a354.png)
![alt text](https://user-images.githubusercontent.com/49149499/112228727-6971f580-8c3a-11eb-8094-5e5a571881c8.png)

### Note
Be sure that in your project exists html files to avoid generating an empty json file.

## Contributing
We are not open to collaborations with other developers.

## License
Distributed under the [Apache License 2.0](LICENSE)
