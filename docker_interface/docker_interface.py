from io import BytesIO
import docker
import yaml

DOCKERFILE_SRC = """
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 && apt-get clean

CMD ls
"""

client = docker.from_env()
events = client.events()
image, build_log = client.images.build(fileobj=BytesIO(DOCKERFILE_SRC.encode()))
print(image)
container = client.containers.run(image=image, detach=True)
print(container.id)
while True:
    event = yaml.load(events.next().decode(), Loader=yaml.SafeLoader)
    actor = event["Actor"]
    attributes = actor["Attributes"]
    if event["Type"] == "container" and event["Action"] == "die":
        print(event)
        print(actor)
        print(attributes)
        break
