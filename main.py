import pubchempy as pcp
import pandas as pd

data_list = []

cid_range = range(1, 500)

for cid in cid_range:
    try:
        compound = pcp.Compound.from_cid(str(cid))

        smiles = compound.isomeric_smiles
        xlogp = compound.xlogp
        solubility = None

        data_list.append({
            'CID': cid,
            'SMILES': smiles,
            'XLogP': xlogp,
            'Solubility': solubility
        })

        print(f"Fetched data for CID: {cid}")

    except Exception as e:
        print(f"An error occurred for CID: {cid}. {e}")

df = pd.DataFrame(data_list)

df.to_csv('pubchem_data.csv', index=False)