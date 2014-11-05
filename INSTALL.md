# DBLPGraphs Installation #
This manual is intended for **Arch Linux**. Still, it should be pretty similar in other distributions. 

1) Install dependencies (Assuming you are on a vanilla Arch Linux.)

    # pacman -S archlinux-keyring # necessary on old virtual machines
    # pacman -Suy # system update
    # pacman -S wget python2 python2-django python2-numpy graphviz unzip # actual dependencies

1/a) Optional: Set correct charset and locales.

    # localectl set-locale LANG=en_US.UTF-8
    # echo "en_US.utf8" >> /etc/locale.conf
    # echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    # locale-gen

3) Get the files and create the installation directory

    $ cd /tmp/
    $ wget https://github.com/lynyus/DBLPGraphs/archive/master.zip
    $ unzip DBLPGraphs-master.zip
    $ mkdir /var/www # Or any other directory
    $ cp -r DBLPGraphs-master/src/* /var/www/


4/a) Run the update script

    $ cd /var/www/dblpGraphs/dblpGraphs/
    $ ./updateXML.sh # downloads the XML-Files from DBLP
    $ cd ..

4/b) Run the development server

    $ python2 manage.py runserver 0.0.0.0:8000

Open the service at the correct port in your browser (localhost:8000). Now you should see in your console that the service is starting to parse the *dblp.xml* file. This may take up to 10 minutes. When ready you can see the main page of DBLPGraphs in your web browser.
