import os
from tqdm import tqdm

path = "/home/haichao/data/tar"
savepth = "/home/haichao/data/vifi/outdoor"
filelist = os.listdir(path)

for p in tqdm(filelist):
    sav = os.path.join(savepth, p.split(".")[0])
    try:
        os.makedirs(sav)
    except:
        pass
    # os.system(f"tar --use-compress-program=pigz -xvpf {os.path.join(path,p)} -C {sav}")
    os.system(f'tar --use-compress-program="pigz -k -p12" -xvpf {os.path.join(path,p)} -C {sav} --exclude=Dist/* --exclude=Depth/* --exclude=RGB_anonymized/* --exclude=RGB_anonymized/*') # ./Dist  ./Depth ./RGB_anonymized

    # 20210907_143435 20210907_144603.tar.gz