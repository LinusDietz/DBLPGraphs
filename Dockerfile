# FROM directive instructing base image to build upon
FROM python:3-onbuild

# COPY startup script into known file location in container
COPY src/start.sh /src/start.sh

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["src/start.sh"]
# done!