import pandas as pd
from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule

data_list = []

for mol in molecule.all()[:500]:

    # Check if molecule_properties exist for the molecule
    if 'molecule_properties' in mol and mol['molecule_properties']:
        data_dict = {}

        data_dict['molecule_chembl_id'] = mol.get('molecule_chembl_id')
        data_dict['canonical_smiles'] = mol.get('molecule_structures', {}).get('canonical_smiles')
        data_dict['alogp'] = mol['molecule_properties'].get('alogp')
        data_dict['aromatic_rings'] = mol['molecule_properties'].get('aromatic_rings')
        data_dict['full_molformula'] = mol['molecule_properties'].get('full_molformula')
        data_dict['full_mwt'] = mol['molecule_properties'].get('full_mwt')
        data_dict['hba'] = mol['molecule_properties'].get('hba')
        data_dict['hbd'] = mol['molecule_properties'].get('hbd')

        data_list.append(data_dict)

df = pd.DataFrame(data_list)

df.to_csv('chembl_data.csv', index=False)
