export POSTGRES_VERSION=14
sudo apt-get update && \
sudo apt-get install -y \
    postgresql-server-${POSTGRES_VERSION}-dev \
    libpython3-dev \
    libclang-dev \
    cmake \
    pkg-config \
    libssl-dev \
    clang \
    build-essential \
    libopenblas-dev \
    python3-dev

git clone https://github.com/postgresml/postgresml && \
cd postgresml && \
git submodule update --init --recursive && \
cd pgml-exten