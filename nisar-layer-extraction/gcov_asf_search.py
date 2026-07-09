import asf_search as asf
import pprint

opts = asf.ASFSearchOptions(**{
    "maxResults": 250,
    "granule_list": [
        "NISAR_L2_PR_GCOV*QPDH*N_P_J_001"
    ],
    "processingLevel": [
        "GCOV"
    ],
    "dataset": [
        "NISAR"
    ],
    "productionConfiguration": [
        "PR"
    ]
})

results = asf.search(opts=opts)
pprint.pp(results.geojson())
