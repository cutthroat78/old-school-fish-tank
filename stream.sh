#!/bin/bash
echo Key?
read key
docker run -d --restart unless-stopped --privileged --name $key fish/fish $key
