import os
import azure.storage.blob

def get_container():
    url = os.environ['CONTAINER_URL']
    return azure.storage.blob.ContainerClient.from_container_url(url)

def print_directory(container):
    for blob in container.list_blobs():
        print(f'{blob.size:>20} {blob.name}')

def read_lasfile(container, filename):
    blob_client = container.get_blob_client(filename)
    data = blob_client.download_blob().content_as_bytes()
    lines = []
    for line in data.splitlines():
        lines.append(line.decode("ascii", errors='ignore'))
    return lines

def print_header_section(lines):
    for line in lines:
        if line.startswith('~A'):
            break
        print(line)

def print_data_section(lines):
    idx = 0
    for line in lines:
        if line.startswith('~A'):
            break
        idx += 1
    for line in lines[idx+1:]:
        print(line)

def main():
    container = get_container()
    #print_directory(container)

    lasfile = '31_5-7 Eos/07.Borehole_Seismic/TZV_TIME_SYNSEIS_2020-01-17_2.LAS'
    lines = read_lasfile(container, lasfile)
    print_header_section(lines)
    print_data_section(lines)

if __name__ == '__main__':
    main()
