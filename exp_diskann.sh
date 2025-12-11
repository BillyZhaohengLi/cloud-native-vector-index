#!/bin/bash
for cache_size in 4096; do
    for search_len in 10 20 40 80 160 320 640; do
        for num_concurrent_queries in 1 4 16 64; do
            echo "${cache_size} ${search_len} ${num_concurrent_queries}" >> diskann_results.txt
            for l in 1 2 3 4 5; do
                echo "${cache_size} ${search_len} ${num_concurrent_queries}"
                /tmp/hsap/hsap/build/src/ds/vector_search/diskann/tools/_build/search_disk_index \
                    --data_type float \
                    --dist_fn l2 \
                    --index_path_prefix /tmp/hsap/dikann_index_gist/dikann_index_gist \
                    --result_path /tmp/vector_data/diskann_gist_result \
                    ./ \
                    --query_file /tmp/vector_data/test_vectors.bin \
                    --recall_at 10 \
                    --search_list "${search_len}" \
                    --gt_file /tmp/vector_data/gt.bin \
                    -W 16 \
                    -T "${num_concurrent_queries}" \
                    &>> diskann_results.txt
                wait
            done
        done
    done
done