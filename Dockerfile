## FROM --platform=linux/amd64 python:3.11.3-slim-bullseye 
FROM python:3.11.3-slim-bullseye 

RUN apt update && \
    apt install -y sudo

RUN apt install -y curl

# Add non-root user
ARG USERNAME=nonroot
RUN groupadd --gid 1000 $USERNAME && \
    useradd --uid 1000 --gid 1000 -m $USERNAME

RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

## Make sure to reflect new user in PATH
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
USER $USERNAME

RUN curl -sSL https://install.python-poetry.org | python3 -
