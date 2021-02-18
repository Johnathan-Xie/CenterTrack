import os
from tqdm import tqdm

root_folder = '/Users/johnathanxie/Documents/GitHub/CenterTrack/data/nuscenes'
main_folder = 'v1.0-trainval01_keyframes'

for i in os.listdir(root_folder):
    if (not ('keyframes' in i)) or (i == main_folder): continue
    print(i)
    for j in os.listdir(os.path.join(root_folder, i, 'samples')):
        if not os.path.isdir(os.path.join(root_folder, i, 'samples', j)): continue
        print(j)
        from_folder = os.path.join(root_folder, i, 'samples', j)
        to_folder = os.path.join(root_folder, main_folder, 'samples', j)
        for k in tqdm(os.listdir(from_folder)):
            os.system('mv %s %s' % (os.path.join(from_folder, k), to_folder))