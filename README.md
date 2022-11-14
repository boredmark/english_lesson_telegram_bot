# Telelgram bot(pet project✨)
## Bot for studing english

## Features

- The bot shows how to use the word in the sentence
- The bot has different levels of difficulty, and the ability to change them
- The bot detect users and current level of user


## Installation


#### Install and run localy:

```sh
git clone
# clone this repo

cd <PATH>
# move to project root directory

pip3 install -r requirements.txt 
# install requirements

export TOKEN=<your bot token> 
# to start the bot, you need to pass token to the environment

python3 run main.py

```

#### Install and run with Docker:

```sh
git clone
# clone this repo

cd <PATH>
# move to project root directory

docker build -t <REPOSITORY>:<TAG> . 
# build docker image for this bot pass REPOSITORY and TAG for comfortable run

docker run -e TOKEN=<your bot token> <REPOSITORY>:<TAG>
# create and run your docker Container with bot passing your bot token to environment 
```

 





  

