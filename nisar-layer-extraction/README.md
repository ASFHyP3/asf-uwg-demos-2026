# Nisar GCOV Layer Extraction

## Locally

Download a GCOV locally
- use h5py to open the file
- load the file into memory (numpy)
- Save it to raster using gdal

## Earthdata Search

To extract go to [earthdata search](https://search.earthdata.nasa.gov/search?q=GCOV)

- We are going to look at the collection `NISAR_L2_GCOV_BETA_V1`
- To only find quad pol granules where going to use a granule wildcard search
- Under `Granule ID(s)` put `NISAR_L2_PR_GCOV*QPDH*N_P_J_001`
- Find a `GCOV` and add it to your project
- Click customize with haromny, then select net2cog
- Select a variable `science/LSAR/GCOV/grids/frequencyB/HHHH`
![Layer Selection](screenshots/layer-extraction-earthdata-search.png)
- Select `GEOTIFF` as an output format
- Click `Download Data`
- Wait for the Harmony job to finish
![Download Status Page](screenshots/download-status.png)
- Download the files by clicking on the link or using `Earthdata Download`

## Harmony Py

harmony-py is used to programatically submit Harmony jobs

```
```
