From python

#using python image from docker hub
WORKDIR /harshcode

# creating and changing folder in docker image
COPY automate.py /harshcode/
CMD [ "python", "automate.py"]

#run the python code while creating container
