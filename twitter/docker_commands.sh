# setup project folder
cd mintycarlo-encounter-notes/
cd 06_data_pipeline/
mkdir tweet_collector


# create the Dockerfile
cd tweet_collector
nano Dockerfile
cd ..
cat tweet_collector/Dockerfile

# create the requirements.txt
cd tweet_collector
nano requirements.txt

# build the dockerfile
cd ..
docker build -t tweet_collector_image ./tweet_collector 

# run the tweet collector image with volume mapping
docker run -it -v $PWD/tweet_collector:/app/ --name tweet_collector_container tweet_collector_image 

# create a app.py
nano tweet_collector/app.py

# start the container and check if it running through
docker start -i tweet_collector_container

# list all containers
docker container ls --all

# list all images
docker images

# remove a container
docker container rm modest_carson
