import os
import azure.storage.blob

def get_container():
    url = os.environ['CONTAINER_URL']
    return azure.storage.blob.ContainerClient.from_container_url(url)

def print_directory(container):
    for blob in container.list_blobs():
        print(f'{blob.size:>20} {blob.name}')

def main():
    container = get_container()
    print_directory(container)

if __name__ == '__main__':
    main()
