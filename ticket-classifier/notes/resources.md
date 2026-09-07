## System Resource Check

Today I checked the system resources of my PC and recorded the results in this file.

### Disk space

I used `df -h .` to check the available disk space for the current project.

* Total: 353G
* Used: 329G
* Available: 5.6G
* Usage: 99%

The project itself is not using much space, but the overall root filesystem is almost full.

### Project size

I used:

```bash
du -sh .
```

The total size of the project is **6.5M**.

I then used `du -h --max-depth=1 . | sort -h` to see which top-level directory was using the most space.

The largest directories were:

* `.git` — 3.4M
* `ticket-classifier` — 2.9M

So, `.git` is currently the largest top-level directory in the project.

### Memory

I checked the memory with `free -h`.

* Total RAM: 14Gi
* Used: 9.5Gi
* Free: 2.8Gi
* Available: 5.2Gi
* Swap: 4.0Gi total, 3.7Gi used

### System load

I used `uptime` to check the system load.

* Uptime: 3 hours 37 minutes
* Users: 1
* Load average: 0.31 (1 min), 0.72 (5 min), 2.37 (15 min)

### CPU

I used `lscpu` and `nproc` to check the CPU information.

My CPU is an **AMD Ryzen 7 7700 8-Core Processor**.

* Physical cores: 8
* Threads per core: 2
* Logical CPUs: 16
* Architecture: x86_64

`nproc` also returned **16**, confirming the number of available logical CPUs.

### GPU

My PC has an **NVIDIA GeForce RTX 5060**. I used `nvidia-smi` to inspect it without changing any settings.

* GPU memory: 15MiB / 8151MiB
* GPU utilization: 0%
* Temperature: 34°C
* Power usage: 6W / 155W
* Driver version: 595.84
* CUDA version: 13.2

At the time I checked, the GPU was basically idle. Only the Xorg process was using a small amount of GPU memory.

### Commands I used



