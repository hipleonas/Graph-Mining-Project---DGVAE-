# Graph-Mining-Project---DGVAE-

This repository contains the implementation of DGVAE - Disentangled Graph Variational Auto-Encoder for Multimodal Recommendation with Interpretability

The original source code can be found at this link: https://github.com/enoche/DGVAE 


How to use the repostory:
Bước 1: Clone Repo về 
Bước 2: Do tập dữ liệu dataset quá lớn nên không thể commit được lên trên repo như vậy nên
cần truy cập dữ liệu vào link drive sau đây: https://drive.google.com/drive/folders/1eCvCmemwKBYNRHT3e0iPZCf2WM1v2Abz
Bước 3: Sau khi đã tải về dữ liệu baby từ drive rùi thì cho dữ liệu baby vào folder data

## Chú ý: lúc tải về chỉ cần copy các file vào folder baby tạo sẵn trên đây là được

## How to run the priginal repository

It is recommended to use WSL before using the repository

### Step 1: Create a virtual environment

+ Create a virtual environment in WSL using miniconda: conda create -n your-env-name python=3.8 -y

+ Activate your virtual environment: conda activate your-env-name 

### Step 2: Adding necessary packages, it is recommended to NOT use the command pip install -r requirements.txt, instead try to install the packages using manual pip install command belows

+ pip install numpy scipy tqdm

+ Install Pytorch GPU RTX 4060 (CUDA 12.1) : pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121. 

### Step 3: Run The Repository

+ Finally, start the repo using: ./run-baby.sh


 