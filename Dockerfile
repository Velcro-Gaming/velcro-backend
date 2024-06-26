# Pull base image
FROM python:3.6-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and Set work directory
RUN mkdir /usr/src/velcro/
WORKDIR /usr/src/velcro

# Copy and Install dependencies
COPY requirements.txt /usr/src/velcro/
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    && pip install -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

# Copy project
COPY . /usr/src/velcro/
