# ViFiDataSetPreProcessing

Download Vi-Fi Multi-modal Dataset from this [page](https://drive.google.com/drive/folders/1Zd1j5b9bDyyKyh7QGE9EoZr2IcF50las) or [Google Drive](https://drive.google.com/drive/folders/1Zd1j5b9bDyyKyh7QGE9EoZr2IcF50las)

use extract_vifi_zip.py to unzip the vi-fi multimodal dataset without large image files.

Use extract_bbx_wireless_fromvifi function in preprocess_vifi_dataset.py to extract the trajectories, imu, GPS, and other sensor data, and save each video's data into pickle file. 
Use load_savedbbx to cut the data into sequences for training.
