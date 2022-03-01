import os
import azure.storage.blob

def get_container():
    url = os.environ['CONTAINER_URL']
    return azure.storage.blob.ContainerClient.from_container_url(url)

def get_list_of_lasfiles(container):
    files = []
    for blob in container.list_blobs():
        if blob.name.endswith('.LAS'):
            files.append(blob.name)
    return files

def print_list_of_lasfiles(container):
    for name in get_list_of_lasfiles(container):
        print(name)

def read_lasfile(container, filename):
    blob_client = container.get_blob_client(filename)
    data = blob_client.download_blob().content_as_bytes()
    lines = []
    for line in data.splitlines():
        lines.append(line.decode("ascii", errors='ignore'))
    return lines

def main():
    container = get_container()
    #print_list_of_lasfiles(container)
    filename = "31_5-7 Eos/07.Borehole_Seismic/TZV_TIME_SYNSEIS_2020-01-17_2.LAS"
    lines = read_lasfile(container, filename)
    for line in lines:
        print(line)

if __name__ == '__main__':
    main()


