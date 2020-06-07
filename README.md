I came across an episode of silicon valley where “gilfoyle” creates a chatbot to talk to “Dinesh“, after that moment I realized what if I can do the same with my friends, can they differentiate between me and the chatbot, so to answer this question I have to build the bot. Finally, I built one that can talk to my friends and family members on whatsapp, the model is build using sequence to sequence model.

## Step 1:

Download whatsapp chat file or whatsapp chat history

## Step 2:
Go to data>chatapp and store whatsapp chat in txt format.<br/>
Edit dataset_create.py and change "chat file name" to your whatsapp chat file name.<br/>
Change "user name in your chat file" to the required username which is there on your chat file.

## Step 3:
Execute dataset_create.py

##### python dataset_create.py
A data.txt file is created

## Step 4:
Execute data.py
##### python data.py

## Step 5:
Execute main.py
##### python main.py
This will start training of your chat bot

## Step 6:
Go to connection.py and chage username to the name of the person you want to chat, the name should be same as on whatsapp.<br/>
Execute connection.py<br/>
scan the QR code and write any arbitary number on the termial or any medium for executing code, this will start the chatbot.

## Result:
![Alt text](data/result.jpeg?raw=true "Result")

