# **Luồng Deploy ứng dụng .NET trên Server Linux với Docker Compose (bao gồm DB và Redis)**

### **1. Chuẩn bị Server Linux**

#### **Bước 1: Cài đặt Docker và Docker Compose**

Đảm bảo Docker và Docker Compose đã được cài đặt trên server Linux. Nếu chưa, chạy các lệnh sau trên Ubuntu:

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
```

Kiểm tra phiên bản Docker và Docker Compose:

```bash
docker --version
docker compose version
```

---

### **2. Chuẩn bị mã nguồn ứng dụng .NET**

#### **Bước 2: Clone mã nguồn ứng dụng**

Clone mã nguồn ứng dụng .NET từ repository Git của bạn vào server Linux:

```bash
git clone https://github.com/yourusername/your-dotnet-app.git /opt/mydotnetapp
cd /opt/mydotnetapp
```

---

### **3. Tạo Dockerfile cho ứng dụng .NET**

#### **Bước 3: Tạo Dockerfile**

Tạo file `Dockerfile` trong thư mục gốc của ứng dụng (nếu chưa có):

```bash
nano Dockerfile
```

Nội dung `Dockerfile`:

```dockerfile
# Stage 1: Build .NET application
FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS build
WORKDIR /src

# Copy và restore project
COPY *.sln .
COPY web/*.csproj ./web/
COPY core/*.csproj ./core/
COPY infrastructure/*.csproj ./infrastructure/
COPY tests/*.csproj ./tests/

RUN dotnet restore "web/web.csproj"

# Copy toàn bộ mã nguồn và build
COPY . .
WORKDIR /src/web
RUN dotnet publish "web.csproj" -c Release -o /app/publish --no-restore

# Stage 2: Tạo final image
FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine AS final
WORKDIR /app
COPY --from=build /app/publish .

ENV ASPNETCORE_ENVIRONMENT=Production
ENV ASPNETCORE_URLS=http://+:80

EXPOSE 80

ENTRYPOINT ["dotnet", "web.dll"]
```

---

### **4. Tạo file `docker-compose.yml`**

#### **Bước 4: Tạo file `docker-compose.yml`**

Tạo file `docker-compose.yml` trong thư mục `/opt/mydotnetapp`:

```bash
nano docker-compose.yml
```

Nội dung `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .  # Build ứng dụng .NET từ Dockerfile
    restart: always
    ports:
      - "8080:80"
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      - ASPNETCORE_ENVIRONMENT=Production
      - ASPNETCORE_URLS=http://+:80
      - ConnectionStrings__DefaultConnection=Server=db;Database=${POSTGRES_DB};User=${POSTGRES_USER};Password=${POSTGRES_PASSWORD}
      - Redis__Configuration=redis:6379
    networks:
      - app-network

  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - app-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7
    restart: always
    volumes:
      - redis_data:/data
    command: redis-server --save 60 1 --loglevel warning
    networks:
      - app-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  db_data:
  redis_data:

networks:
  app-network:
    driver: bridge
```

---

### **5. Tạo file `.env` cho biến môi trường**

#### **Bước 5: Tạo file `.env`**

Tạo file `.env` trong thư mục `/opt/mydotnetapp` để lưu trữ các biến môi trường:

```bash
nano .env
```

Nội dung file `.env`:

```ini
POSTGRES_USER=user
POSTGRES_PASSWORD=secure_password
POSTGRES_DB=daiminh
```

---

### **6. Triển khai ứng dụng bằng Docker Compose**

#### **Bước 6: Chạy Docker Compose**

Trong thư mục `/opt/mydotnetapp`, chạy lệnh sau để triển khai ứng dụng:

```bash
sudo docker compose up -d
```

- **`-d`**: Chạy ở chế độ nền (detached).
- Docker Compose sẽ tự động build ứng dụng .NET từ `Dockerfile`, đồng thời khởi động PostgreSQL và Redis.

---

### **7. Kiểm tra và giám sát**

#### **Bước 7: Kiểm tra Logs**

Kiểm tra logs của các service:

```bash
sudo docker compose logs web
sudo docker compose logs db
sudo docker compose logs redis
```

#### **Bước 8: Truy cập ứng dụng**

Truy cập ứng dụng qua trình duyệt tại địa chỉ:  
`http://<server-ip>:8080`

---

### **8. Tắt hoặc xóa ứng dụng**

#### **Tắt ứng dụng:**

```bash
sudo docker compose down
```

#### **Xóa toàn bộ dữ liệu và ứng dụng:**

```bash
sudo docker compose down -v
```

---

### **Tóm tắt các bước triển khai:**

1. **Cài đặt Docker và Docker Compose** trên server Linux.
2. **Clone mã nguồn ứng dụng** từ Git repository.
3. **Tạo Dockerfile** để build ứng dụng .NET.
4. **Tạo file `docker-compose.yml`** để định nghĩa các service: web, db, redis.
5. **Tạo file `.env`** để quản lý biến môi trường.
6. **Chạy Docker Compose** để triển khai ứng dụng.
7. **Kiểm tra logs** và truy cập ứng dụng qua trình duyệt.

