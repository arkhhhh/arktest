import os
from kubernetes import client, config
from kubernetes.client import V1Job, V1PodTemplateSpec, V1Container, V1ObjectMeta, V1JobSpec
from kubernetes.client.rest import ApiException

def create_job(api_instance, job_name, namespace="default"):
    # Define job specifications
    job = V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=V1ObjectMeta(name=job_name),
        spec=V1JobSpec(
            template=V1PodTemplateSpec(
                metadata=V1ObjectMeta(labels={"app": job_name}),
                spec=client.V1PodSpec(
                    containers=[V1Container(name="botrunrun", image="your-image-here", args=["/bin/bash", "-c", "echo 'Running botrunrun job...'"])],
                    restart_policy="Never"
                ),
            ),
            backoff_limit=4  # Number of retries if the job fails
        ),
    )

    try:
        api_instance.create_namespaced_job(namespace=namespace, body=job)
        print(f"Job '{job_name}' created successfully!")
    except ApiException as e:
        print(f"Exception when creating job: {e}")

def main():
    # Load the kube config from environment or default locations
    try:
        config.load_incluster_config()  # If running inside the cluster
    except:
        config.load_kube_config()  # If running locally

    # Get the Kubernetes API client
    api_instance = client.BatchV1Api()

    # Create the job
    create_job(api_instance, job_name="botrunrun", namespace="dev")

if __name__ == "__main__":
    main()

