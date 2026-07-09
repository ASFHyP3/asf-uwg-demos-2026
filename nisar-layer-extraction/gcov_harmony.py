import harmony

harmony_client = harmony.Client(env=harmony.Environment.PROD)

request = harmony.Request(
    collection=harmony.Collection(id="NISAR_L2_GCOV_BETA_V1"),
    granule_name="NISAR_L2_PR_GCOV_008_145_D_054_2005_QPDH_A_20251226T061551_20251226T061609_X05010_N_P_J_001",
    variables=[
        "/science/LSAR/GCOV/grids/frequencyB/VVVV",
    ],
)

job_id = harmony_client.submit(request)
print(job_id)
