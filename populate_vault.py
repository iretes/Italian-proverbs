import pandas as pd
import argparse

# parse command line arguments
parser = argparse.ArgumentParser(description='Populate Vault')
parser.add_argument(
    '--dataset',
    action='store',
    type=str,
    required=True,
    help="Path to the dataset."
)
parser.add_argument(
    '--vault',
    action='store',
    type=str,
    required=True,
    help="Path to the vault directory."
)
args = parser.parse_args()
dataset_path = args.dataset
vault_dir = args.vault

# load dataset
data = pd.read_csv(dataset_path, header=None, names=['proverbio', 'tags'])

# create a file for each proverb
for index, row in data.iterrows():
    with open(f'{vault_dir}/{row["proverbio"]}.md', 'w') as f:
        for tag in row['tags'].split(';'):
            f.write(f'[[{tag.strip()}]]\n')
            break

# create a file for each tag
tags = data['tags'].str.get_dummies(sep=';')
for tag in tags.columns:
    with open(f'{vault_dir}/{tag}.md', 'w') as f:
        f.write(f'#topic\n')
    break