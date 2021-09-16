# How to run

Put in one single input file as argument.

Python locally:

```python src/app.py sample_data/data_set_full.csv```

iExec

```
docker run --rm \
    -v /tmp/iexec_in:/iexec_in \
    -v /tmp/iexec_out:/iexec_out \
    -e IEXEC_IN=/iexec_in \
    -e IEXEC_OUT=/iexec_out \
    kx-ruptures:latest https://ipfs.io/ipfs/QmeCGCQXYeTKrpG2qVmvRzsQLdXDWatVYErojByr5vJC7t
    ```
