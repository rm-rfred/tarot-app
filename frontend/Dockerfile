FROM node:18.12.1

ENV GENERATE_SOURCEMAP=false \
    WDS_SOCKET_PORT=10131

WORKDIR /app

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
