# How to run

Put in one single input file as argument.

Python locally:

```python src/app.py sample_data/data_set_full.csv```

## IExec local test run:

`docker build . --tag kx-ruptures`

`mkdir /tmp/iexec_in`
`mkdir /tmp/iexec_out`
 Paste your datafile to /tmp/iexec_in

 Or run:

 `curl -o /tmp/iexec_in/inputFile https://ipfs.io/ipfs/QmeCGCQXYeTKrpG2qVmvRzsQLdXDWatVYErojByr5vJC7t`

iExec
```
docker run \
    -v /tmp/iexec_in:/iexec_in \
    -v /tmp/iexec_out:/iexec_out \
    -e IEXEC_IN=/iexec_in \
    -e IEXEC_OUT=/iexec_out \
    -e IEXEC_INPUT_FILE_NAME_1=inputFile \
    -e IEXEC_NB_INPUT_FILES=1 \
    kx-ruptures:latest
```


```
docker run --rm \
    -v /tmp/iexec_in:/iexec_in \
    -v /tmp/iexec_out:/iexec_out \
    -e IEXEC_IN=/iexec_in \
    -e IEXEC_OUT=/iexec_out \
    kx-ruptures:latest https://ipfs.io/ipfs/QmeCGCQXYeTKrpG2qVmvRzsQLdXDWatVYErojByr5vJC7t
    ```
