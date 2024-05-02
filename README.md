# DSCI351_Project

The API keys used to run the project on the local server, along with the DynamoDB account used for the project have been disabled. In addition, the MongoDB database used was on our local server, and for these reasons the code won't run given a download of the files. To have it run:

Install the following packages:
pip3 install pymongo
pip3 install deepface
pip3 install vosk
pip3 install pyaudio
pip3 install boto3
pip3 install openAI
pip3 install customtkinter

Create API keys for the following:
OpenAI
DynamoDB, and create the necessary database

Create a local MongoDB database for questions

Finally, ensure that the cv2 instance is correctly connecting to your webcam. To do this, change the value in the cv2.capture(x) section in main
