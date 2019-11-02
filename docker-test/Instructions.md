# Install docker

Install docker, create a group `docker` and add your user to this group.
Run `sudo systemctl start docker` (or equivalent).
Log out and log in again.

# Build & run the container

Clone the repo, go inside. Run:

```
docker build . -t factorial
docker run -i -t factorial
```

After the second command starts, type a number and you will get the value of the factorial of the entered number.

