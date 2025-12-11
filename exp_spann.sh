#!/bin/bash
for cache_size in 4096; do
    for nprobe in 8 16 32 64 128 256 512 1024 2048 4096 8192 16384; do
        for num_concurrent_queries in 1 4 16 64; do
            echo "${cache_size} ${nprobe} ${num_concurrent_queries}" >> spann_results.txt
            for l in 1 2 3 4 5; do
                echo "${cache_size} ${nprobe} ${num_concurrent_queries}"
                ./indexsearcher \
                    -i /tmp/vector_data/test_vectors.bin \
                    -x sptag_index_gist_no_replica \
                    -k 10 \
                    -d 960 \
                    -v Float \
                    -f Default \
                    -t "${num_concurrent_queries}" \
                    -r /tmp/vector_data/gt.bin \
                    -df /tmp/vector_data/train_vectors.bin \
                    -tk 10 \
                    -ec true \
                    -cc "${cache_size}M" \
                    BuildSSDIndex.SearchInternalResultNum="${nprobe}" \
                    BuildSSDIndex.MaxDistRatio=8.0 \
                    BuildSSDIndex.MaxCheck=16384 \
                    BuildSSDIndex.ResultNum=10 \
                    BuildSSDIndex.InternalResultNum=32 \
                    BuildSSDIndex.HashTableExponent=4 \
                    BuildSSDIndex.SearchPostingPageLimit=12 \
                &>> spann_results.txt
                wait
            done
        done
    done
done