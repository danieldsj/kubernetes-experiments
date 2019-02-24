#!/bin/bash
POD=$(kubectl get pods -o custom-columns=name:.metadata.name -l app=stateful-site | tail -1)
NAMESPACE="default"
kubectl cp index.html $NAMESPACE/$POD:/usr/share/nginx/html/index.html
