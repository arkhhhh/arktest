FROM busybox

RUN mkdir /app
WORKDIR /app

CMD ["echo abc"]
