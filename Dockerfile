# Reproducible-build image for the STL generators. Pins python + libs to
# match the sandbox that produced the STLs in stl/. Default arch is amd64
# (linux/x86_64) because that's what the original sandbox ran; Apple
# Silicon hosts run this under Rosetta emulation.
#
#   docker build --platform=linux/amd64 -t geodesic-build .
#
#   # verify the checked-in stl/ against a fresh build:
#   docker run --rm --platform=linux/amd64 geodesic-build
#
#   # regenerate stl/ in the host tree (bind-mount the repo):
#   docker run --rm --platform=linux/amd64 -v "$PWD":/repo geodesic-build build

ARG PLATFORM=linux/amd64
FROM --platform=$PLATFORM python:3.11.15-slim-bookworm

# Silence trimesh's to_planar deprecation nag in build output.
ENV PYTHONWARNINGS="ignore::DeprecationWarning"

# libgomp1 for manifold3d's OpenMP runtime.
RUN apt-get update && apt-get install -y --no-install-recommends libgomp1 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /repo

COPY scripts/requirements.txt scripts/requirements.txt
RUN pip install --no-cache-dir -r scripts/requirements.txt

COPY . .

ENTRYPOINT ["scripts/docker-entrypoint.sh"]
CMD ["verify"]
