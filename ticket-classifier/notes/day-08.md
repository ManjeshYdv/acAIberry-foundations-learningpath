# Day 03: Manage Processes with jobs, ps, pgrep, top, htop, kill, and fg

**Sun Sep 06**

**Time spent: 02:05 PM to 3:25 PM**

## Commands I practiced

```text
sleep 300 &
jobs
ps aux
pgrep 
top 
htop
kill
fg
```

## Task result

**`sleep 300 &`** = started a `sleep` process in the background so the terminal could still be used.
**`jobs`** = checked the background job and confirmed that `sleep 300` was running.
**`ps`** = checked the processes associated with the current terminal and found the `sleep` process with PID **1891130**.
**`ps aux`** = checked a larger list of processes running on the system and observed CPU and memory usage for each process.
**`pgrep`** = searched for running processes by their name and returned their PID. I also used `pgrep -a` and `pgrep -af` to see more information about the matching processes.


## Proof

Commit, file, screenshot, command output, or URL:

```text
$ sleep 300 & echo "hello manjesh"
[1] 1891130
hello manjesh

$ jobs
[1]+  Running                 sleep 300 &

$ ps
PID       TTY          TIME CMD
1621487   pts/5    00:00:00 bash
1891130   pts/5    00:00:00 sleep
1892244   pts/5    00:00:00 ps
```

The `sleep` process was also visible in the `ps au` output with PID **1891130**, using **0.0% CPU** and **0.0% MEM**.

I also practiced:

```text
$ pgrep python
1304257

$ pgrep -a python
1304257 /home/manjesh/.local/bin/python3.11 ...

$ pgrep -af python
1992 /usr/bin/python3 ...
261205 ... python-env-tools ...
1734510 ... streamlit ...
```
![alt](day-08.md)

## Can I explain it without AI?

* [✓] Yes
* [ ] Not yet; repeat this day
