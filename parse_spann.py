from collections import defaultdict

recalls = defaultdict(float)
qpses = defaultdict(float)
bandwidths = defaultdict(float)
p95 = defaultdict(float)
p99 = defaultdict(float)
meanio = defaultdict(float)
qpses_count = defaultdict(int)
minio = defaultdict(float)
maxio = defaultdict(float)
dram_hits = defaultdict(float)
hits = defaultdict(float)
reqs = defaultdict(float)
data = defaultdict(float)

cpus_count = defaultdict(int)
cpus = defaultdict(float)

num_queries=10000

with open("spann_results.txt", "r") as file:
    lines = file.readlines()
    cur_config = ""
    for line in lines:
        if len(line.split()) == 3 and line.split()[0].isdigit():
            cur_config = line.strip()
        elif "[1] 0-1000" in line and len(line.split()) > 12:
            qpses[cur_config] += float(line.split()[7])
            # qpses[cur_config] = max(qpses[cur_config], float(line.split()[7]))
            recalls[cur_config] += float(line.split()[6])
            bandwidths[cur_config] += (float(line.split()[18]) / 1024 / 1024 / (num_queries / float(line.split()[7])))
            p95[cur_config] += float(line.split()[5])
            p99[cur_config] += float(line.split()[4])
            meanio[cur_config] += float(line.split()[9])
            minio[cur_config] += float(line.split()[10])
            maxio[cur_config] += float(line.split()[11])
            dram_hits[cur_config] += (float(line.split()[14])) / float(line.split()[17])
            hits[cur_config] += (float(line.split()[14]) + float(line.split()[15])) / float(line.split()[17])
            reqs[cur_config] += float(line.split()[17])
            data[cur_config] += float(line.split()[18])
            qpses_count[cur_config] += 1

print("CacheSize,nprobe,numthreads,recall,qps,bandwidth,p95,p99,meanio,minio,maxio,hitrate,reqs,totaldata")
for key, value in qpses_count.items():
    if qpses_count[key] > 0:
        print(f"{key.split()[0]},{key.split()[1]},{key.split()[2]},"
              f"{recalls[key] / qpses_count[key]:.4f},{qpses[key] / qpses_count[key]:.4f},"
              f"{bandwidths[key] / qpses_count[key]:.4f},"
              f"{p95[key] / qpses_count[key]:.3f},"
              f"{p99[key] / qpses_count[key]:.3f},"
              f"{meanio[key]/ qpses_count[key]:.0f},"
              f"{minio[key] / qpses_count[key]:.0f},"
              f"{maxio[key] / qpses_count[key]:.0f},"
              f"{dram_hits[key] / qpses_count[key]:.4f},"
              f"{hits[key] / qpses_count[key]:.4f},"
              f"{reqs[key] / qpses_count[key]:.0f},"
              f"{data[key] / qpses_count[key]:.0f}")

# print("qpses")
# for key, value in qpses.items():
#     if qpses_count[key] > 0:
#         print(f"{key} {value / qpses_count[key]:.2f}")
#     else:
#         print(f"{key} 0.00")

# print("bandwidths")
# for key, value in bandwidths.items():
#     if qpses_count[key] > 0:
#         print(f"{key} {value / qpses_count[key]:.2f}")
#     else:
#         print(f"{key} 0.00")

# print("p95")
# for key, value in p95.items():
#     if qpses_count[key] > 0:
#         print(f"{key} {value / qpses_count[key]:.3f}")
#     else:
#         print(f"{key} 0.00")

# print("p99")
# for key, value in p99.items():
#     if qpses_count[key] > 0:
#         print(f"{key} {value / qpses_count[key]:.3f}")
#     else:
#         print(f"{key} 0.00")

# print("meanio")
# for key, value in p99.items():
#     if qpses_count[key] > 0:
#         print(f"{key} {value / qpses_count[key]:.3f}")
#     else:
#         print(f"{key} 0.00")
