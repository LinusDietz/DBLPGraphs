#promt for password
echo "### SETUP CONTAINER    ###"
echo "Provide a password for the docker user."
stty_orig=`stty -g` # save original terminal setting.
stty -echo          # turn-off echoing.
read passwd         # read the password
stty $stty_orig

# build image
echo "### BUILDING CONTAINER ###"
docker build -t dblpgraphs --build-arg dbpw=$passwd .
echo "### RUNNING CONTAINER  ###"
docker run --rm -p 8000:8000 -v $PWD/src:/usr/src/dblpgraphs -v /usr/src/resources --link dblpgraphs-db-instance:dblpgraphs-db-instance --name dblpgraphs-client-instance dblpgraphs ./start.sh
