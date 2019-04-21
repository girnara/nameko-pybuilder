TAG ?= latest

# docker

run-wheel-builder:
	docker run --rm \
		-v "$$(pwd)":/application -v "$$(pwd)"/wheelhouse:/wheelhouse \
		nameko-example-builder;

build-image:
	docker build -t girnara/nameko-gateway:$(TAG) -f docker.run .

push-image:
	docker push girnara/nameko-gateway:$(TAG)
