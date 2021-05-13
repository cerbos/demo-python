docker run -i -t -p 9998:9998 \
  -v $(pwd)/config:/config \
  -v $(pwd)/policy:/policy \
  pkg.cerbos.dev/containers/cerbos:0.0.0-alpha10 \
  server --config=/config/conf.yaml

