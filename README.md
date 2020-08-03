# fastapi-async-blobs

This is a short test to **list BLOBs from Azure storage** using [FastAPI](https://fastapi.tiangolo.com/) and...

* the **synchronous** Python SDK from Azure vs.
* the **asynchronous** Python SDK from Azure.

The app is deployed at Heroku: https://fastapi-async-blobs.herokuapp.com/

The implementation is straightforward, see [main.py](main.py).


## Performance comparison

I used the small tool [hey](https://github.com/rakyll/hey) to compare how the two 
endpoints react to "heavy" load:

### Typical results for the **async** endpoint:
```
$ ./hey_linux_amd64 -c 10 -n 50 https://fastapi-async-blobs.herokuapp.com/async

Summary:
  Total:	18.1493 secs
  Slowest:	6.1439 secs
  Fastest:	1.0707 secs
  Average:	2.5444 secs
  Requests/sec:	2.7549
  
  Total data:	745600 bytes
  Size/request:	14912 bytes

Response time histogram:
  1.071 [1]   |■■■
  1.578 [16]  |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  2.085 [5]   |■■■■■■■■■■■■■
  2.593 [7]   |■■■■■■■■■■■■■■■■■■
  3.100 [6]   |■■■■■■■■■■■■■■■
  3.607 [4]   |■■■■■■■■■■
  4.115 [7]	  |■■■■■■■■■■■■■■■■■■
  4.622 [0]   |
  5.129 [1]   |■■■
  5.637 [2]   |■■■■■
  6.144 [1]   |■■■
```
When I tried this several times I got a **responses per second** value of 2-3.


### Typical results for the **sync** endpoint:
```
$ ./hey_linux_amd64 -c 10 -n 50 https://fastapi-async-blobs.herokuapp.com/sync

Summary:
  Total:	22.7028 secs
  Slowest:	7.4702 secs
  Fastest:	1.3497 secs
  Average:	4.0661 secs
  Requests/sec:	2.2024
  
  Total data:	745600 bytes
  Size/request:	14912 bytes

Response time histogram:
  1.350 [1]	|■■■■
  1.962 [5]	|■■■■■■■■■■■■■■■■■■■■■■
  2.574 [4]	|■■■■■■■■■■■■■■■■■■
  3.186 [6]	|■■■■■■■■■■■■■■■■■■■■■■■■■■■
  3.798 [6]	|■■■■■■■■■■■■■■■■■■■■■■■■■■■
  4.410 [9]	|■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  5.022 [1]	|■■■■
  5.634 [6]	|■■■■■■■■■■■■■■■■■■■■■■■■■■■
  6.246 [8]	|■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  6.858 [2]	|■■■■■■■■■
  7.470 [2]	|■■■■■■■■■
```

When I tried this several times I see a **responses per second** of 2-2.5.
