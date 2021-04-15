NAME=baidu-search-top
TAG := latest
IMAGE=$(NAME):$(TAG)
LATESTIMAGE=$(NAME):latest

define buildFunction
 docker build -t $(1) .
endef

image:
	$(call buildFunction, $(IMAGE))
