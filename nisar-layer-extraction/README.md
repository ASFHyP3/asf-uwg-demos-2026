# Nisar GCOV Layer Extraction

This tutorial will go over extracting single layers as geotiffs from Nisar [Geocoded Polarimetric Covariance (GCOV)](https://nisar-docs.asf.alaska.edu/gcov/) products. GCOV products are natively stored in [HDF5](http://nisar-docs.asf.alaska.edu/data-format/) format.

## Extract Layers Locally

The process for opening and extracting layers from nisar files can be found in [Local Nisar Layer Extraction](local-nisar-layer-extraction.ipynb) notebook

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

`harmony-py` is used to programatically submit Harmony jobs. [Nisar Layer Extraction](nisar-layer-extraction.ipynb) shows the basic workflow. More examples can be found at [harmony-py docs](https://github.com/nasa/harmony-py). If you want another view of your harmony jobs you can use the [Workflow UI](https://harmony.earthdata.nasa.gov/workflow-ui)
