def get_current_namespace():
    current_namespace = open("/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()
    return current_namespace