# Cloud-Native Vector Search: A Comprehensive Performance Analysis
Repository for Cloud-Native Vector Index VLDB 2026 EA&amp;B submission

## Datasets
We use 4 open-source datasets in our benchmarking. GIST1M and DEEP10M can be downloaded as hdf5 files from the [ANN Benchmarks][https://github.com/erikbern/ann-benchmarks] repository; MSSPACE10M and DEEP1B can be downloaded from links provided in the [Neurips'23 BigANN Competition][https://github.com/harsha-simhadri/big-ann-benchmarks] repository:
- [GIST1M][http://ann-benchmarks.com/gist-960-euclidean.hdf5]
- [DEEP10M][http://ann-benchmarks.com/deep-image-96-angular.hdf5]
- [MSSPACE10M][https://github.com/harsha-simhadri/big-ann-benchmarks/blob/36f6c737d3c67fa2d3336897cb6bd55c874ee9f1/benchmark/datasets.py#L478]
- [DEEP1B][hhttps://github.com/harsha-simhadri/big-ann-benchmarks/blob/36f6c737d3c67fa2d3336897cb6bd55c874ee9f1/benchmark/datasets.py#L312]

## Index Build
We build indexes locally. SPANN and DiskANN indexes for each dataset are built using the `./indexbuilder` and `./build_disk_index` executables using parameters specified in our paper, respectively.

## Cloud Storage
We use ByteDance's [Volcano Engine TOS][volcengine.com/docs/6349/148775?lang=en] as our remote storage. Locally-built indexes are uploaded to remote storage via the TOS cli tool (`tosutil.zip`) found in this repository:

```
./tosutil cp file_url tos://bucket[/key]
```

## Running Experiments 
To run experiments, invoke the `exp_diskann.sh` and `exp_spann.sh` scripts with the appropriate search parameters. These scrips will in turn invoke the indexes' search executables (`./indexsearcher` and `./search_disk_index`), while writing the raw output logs to a text file on disk. 

The `parse_diskann.py` and `parse_spann.py` scripts can then be used to convert these raw logs to CSV files containing relevant metrics for each search parameterization (e.g., recall, QPS, remote storage mean I/O, p99 query latency). The average is reported for search parameterizations with multiple runs.