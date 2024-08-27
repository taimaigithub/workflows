# Sử dụng Python 3.8 làm image base
FROM python:3.8

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements.txt vào container
COPY app/requirements.txt /app/requirements.txt

# Cài đặt các thư viện Python cần thiết
RUN pip install -r requirements.txt
RUN pip install watchdog
RUN pip install pytest  # Cài đặt thêm pytest

# Sao chép tất cả mã nguồn vào container
COPY app/ /app

# Thiết lập lệnh mặc định để chạy pytest
CMD ["pytest"]
