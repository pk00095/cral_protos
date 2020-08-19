import pdb 
from pipeline_pb2 import Status, Pipeline

from dataset_pb2 import DatasetVersionMeta, TfrecordMeta, TaskType
from dataset_pb2 import ObjectDetectionDataFormat
from dataset_pb2 import DatasetMeta, HashEntry


pipeline = Pipeline()

# add data includes conerting to common format, generating csv and versioning the data

#add data
pipeline.add_data = Status.RUNNING
dataset_meta = DatasetMeta()

dataset_meta.task_type = TaskType.OBJECT_DETECTION
dataset_meta.object_detection = ObjectDetectionDataFormat.PASCALVOC
dataset_meta.train_set_size = 1000
dataset_meta.test_set_size = 500
dataset_meta.num_classes = 5
dataset_meta.version = 0


#version data
data_version_meta = DatasetVersionMeta()

trainset_hash = HashEntry()
trainset_hash.filename = 'train.csv'
trainset_hash.hash = 'yyyyyyyyyyyyyyyyyy'

data_version_meta.train_set_hash.CopyFrom(trainset_hash)

testset_hash = HashEntry()
testset_hash.filename = 'test.csv'
testset_hash.hash = 'yyyyyyyyyyyyyyyyyy'

data_version_meta.test_set_hash.CopyFrom(testset_hash)

data_version_meta.train_set_version = 0
data_version_meta.test_set_version = 0

pipeline.dataset_meta_info.Clear()
pipeline.dataset_meta_info.MergeFromString(dataset_meta.SerializeToString())
pipeline.dataset_version_info.MergeFromString(data_version_meta.SerializeToString())

pipeline.add_data = Status.COMPLETED



#lock_data includes creating tfrecords from csv files and versioning them
pipeline.lock_data = Status.RUNNING
tfrecord_meta = TfrecordMeta()

_NUM_SHARDS = 4
tfrecord_meta.num_shards = _NUM_SHARDS

for i in range(_NUM_SHARDS):
    tfr_hash = tfrecord_meta.train_set.add()
    tfr_hash.filename = f"{i+1:05d}-of-{_NUM_SHARDS:05d}.tfrecord"
    tfr_hash.hash = "xxxxxxxxxxxxxxxxxxx"

tfrecord_meta.train_set_hash = 'xyxyxyxyxyxyxyxy'
tfrecord_meta.test_set_hash = 'yyyyxxxxyyyyxxxx'

tfrecord_meta.train_set_version = 0
tfrecord_meta.test_set_version = 0

#assign tfrecord_meta
pipeline.tfrecord_meta_info.Clear()
pipeline.tfrecord_meta_info.MergeFromString(tfrecord_meta.SerializeToString())
pipeline.lock_data = Status.COMPLETED

print(pipeline)

print("***********************")
print(pipeline.UnknownFields())

# if __name__ == '__main__':
#     parse()
