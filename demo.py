import pdb 
from pipeline_pb2 import Status, Pipeline

from dataset_pb2 import DatasetVersionMeta, TfrecordMeta, TaskType
from dataset_pb2 import ObjectDetectionDataFormat
from dataset_pb2 import DatasetMeta


pipeline = Pipeline()

#add data
pipeline.add_data = Status.RUNNING
dataset_meta = DatasetMeta()

dataset_meta.task_type = TaskType.OBJECT_DETECTION
dataset_meta.object_detection = ObjectDetectionDataFormat.PASCALVOC
dataset_meta.train_set_size = 1000
dataset_meta.test_set_size = 500
dataset_meta.num_classes = 5
dataset_meta.version = 0

#assign dataset_meta
pipeline.dataset_meta_info.CopyFrom(dataset_meta)
pipeline.add_data = Status.COMPLETED

#version data

#lock_data
pipeline.lock_data = Status.RUNNING
tfrecord_meta = TfrecordMeta()

_NUM_SHARDS = 4
tfrecord_meta.num_shards = _NUM_SHARDS

for i in range(_NUM_SHARDS):
    tfr_hash = tfrecord_meta.train_set.add()
    tfr_hash.filename = f"{i}-of{_NUM_SHARDS}.tfrecord"
    tfr_hash.hash = "xxxxxxxxxxxxxxxxxxx"

#assign tfrecord_meta
pipeline.tfrecord_meta_info.CopyFrom(tfrecord_meta)
pipeline.lock_data = Status.COMPLETED

print(pipeline)

# if __name__ == '__main__':
#     parse()
