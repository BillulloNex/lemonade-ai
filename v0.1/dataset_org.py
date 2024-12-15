from pathlib import Path
import json
# Define the directory path
dataset_dir = Path('datasets/choice-75')

# List all CSV files in the directory
csv_files = list(dataset_dir.glob('*.json'))

datasets = []
# Print each CSV file
for csv_file in csv_files:
    with open(csv_file, 'r') as file:
        data = json.loads(file.read())
        situation = {}
        situation['options'] = {}
        situation['scenarios'] = []
        situation['goal'] = data['goal']
        situation['step'] = data['branching_info']['branching_step']
        situation['options']['1'] = data['branching_info']['option 1']
        situation['options']['2'] = data['branching_info']['option 2']
        situation['options']['0'] = 'neither option are applicable for the current situation'
        scenarios = data['branching_info']['freeform_ra']
        for scenario in scenarios:
            example = {}
            example['context'] = scenario[0]
            example['answer'] = scenario[1]
            example['difficulty'] = scenario[2]
            situation['scenarios'].append(example)

        datasets.append(situation)

        # Save the datasets to a JSON file
        output_file = 'datasets/choice-75/recompiled_dataset.json'
        with open(output_file, 'w') as f:
            json.dump(datasets, f, indent=4)
