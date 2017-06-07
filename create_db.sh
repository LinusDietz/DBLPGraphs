#promt for password
echo "### SETUP CONTAINER    ###"
echo "Provide a password for the docker user."
stty_orig=`stty -g` # save original terminal setting.
stty -echo          # turn-off echoing.
read passwd         # read the password
stty $stty_orig

# build image
echo "### BUILDING CONTAINER ###"
docker build -t dblpgraphs-db --build-arg dbpw=$passwd .
echo "### RUNNING DATABASE CONTAINER  ###"
docker run -td --rm -p 5432:5432 -v $PWD/src:/usr/src/dblpgraphs -v /usr/src/resources --name dblpgraphs-db-instance dblpgraphs-db ./populate_db