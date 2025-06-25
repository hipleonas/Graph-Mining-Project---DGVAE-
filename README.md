# Graph-Mining-Project---DGVAE-

Đây là repo chứ source code cho project DGVAE

CÁch sử dụng Repo :
Bước 1: Clone Repo về 
Bước 2: Do tập dữ liệu dataset quá lớn nên không thể commit được lên trên repo như vậy nên
cần truy cập dữ liệu vào link drive sau đây: https://drive.google.com/drive/folders/1eCvCmemwKBYNRHT3e0iPZCf2WM1v2Abz
Bước 3: Sau khi đã tải về dữ liệu baby từ drive rùi thì cho dữ liệu baby vào folder data

## Chú ý: lúc tải về chỉ cần copy các file vào folder baby tạo sẵn trên đây là được

## Cách chạy Repo

Khuyến khích sử dụng WSL / ubuntu để tiện sử dụng repo

Bước 1: Tạo môi trường ảo

+ Tạo môi trường ảo trên WSL - sử dụng miniconda: conda create -n your-env python=3.8 -y

+ kích hoạt môi trường ảo: conda activate your-env (your-env là tên môi trường ảo mà mình muốn đặt! có thể đổi)

Bước 2: Thêm các gói thư viện vào, khuyên khích không gọi lệnh pip install -r requirements.txt mà hãy install các thư viện một cách thủ công

+ pip install numpy scipy tqdm

+ Cài PyTorch hỗ trợ GPU RTX 4060 (CUDA 12.1) : pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121.  chỗ này hãy linh động cho môi trường pytorch của máy mình

Bước 3: chạy repo: ./run-baby.sh


 