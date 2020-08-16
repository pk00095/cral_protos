import dataset_pb2


def create():
    pass

    data = dataset_pb2.tfrecord_meta()

    data.num_shards=4
    data.train_set_hash = 'bla'
    data.test_set_hash = 'bla'



    for i in range(data.num_shards):
        train_shard = data.train_set.add()
        train_shard.filename = f'tfrecord-{i}'
        train_shard.hash = 'blu-bl'

    # print(data)

    with open('demo.pb', 'wb') as f:
        f.write(data.SerializeToString())


def parse():
    with open('demo.pb', 'rb') as f:
        data = dataset_pb2.tfrecord_meta()
        data.ParseFromString(f.read())

    # print(data)

    for tfrecords in data.train_set:
        print(tfrecords.filename, tfrecords.hash)

    print(data.test_set)


if __name__ == '__main__':
    parse()
