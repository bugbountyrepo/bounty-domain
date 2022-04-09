import os
from xml import dom
import zipfile

output = os.listdir('output')

with open('results.txt', 'w') as result:
    for i in output:
        with open(f'output/{i}') as f:
            lines = f.readlines()
            for l in lines:
                result.writelines(l)
        print(f'{i} == Done')
        print()
    print('Copied all the files')


# with zipfile.ZipFile(f'zip/{z}',"r") as zip_ref:
    #     zip_ref.extractall("output")
