# Cryptography trong C# .NET

## Mục Lục

1. [Tổng quan về Cryptography](#1-tổng-quan-về-cryptography)
   - [Cryptography là gì?](#cryptography-là-gì)
   - [Lợi ích của Cryptography](#lợi-ích-của-cryptography)
   - [Các thuật toán Cryptography phổ biến](#các-thuật-toán-cryptography-phổ-biến)
2. [Các loại Cryptography trong C# .NET](#2-các-loại-cryptography-trong-c-net)
   - [Symmetric Key Cryptography](#symmetric-key-cryptography)
   - [Asymmetric Key Cryptography](#asymmetric-key-cryptography)
   - [Hashing](#hashing)
   - [Digital Signatures](#digital-signatures)
3. [Sử dụng Cryptography trong ASP.NET Core](#3-sử-dụng-cryptography-trong-aspnet-core)
   - [Mã hóa với AES](#mã-hóa-với-aes)
   - [Mã hóa với RSA](#mã-hóa-với-rsa)
   - [Tạo và xác minh chữ ký số](#tạo-và-xác-minh-chữ-ký-số)
4. [Quản lý khóa trong Cryptography](#4-quản-lý-khóa-trong-cryptography)
   - [Khóa đối xứng](#khóa-đối-xứng)
   - [Khóa công khai và khóa riêng](#khóa-công-khai-và-khóa-riêng)
   - [Key Vault trong .NET](#key-vault-trong-net)
5. [Bảo mật và hiệu suất trong Cryptography](#5-bảo-mật-và-hiệu-suất-trong-cryptography)
6. [Công cụ hỗ trợ trong môi trường Production](#6-công-cụ-hỗ-trợ-trong-môi-trường-production)
7. [Kết luận](#kết-luận)

---

### 1. Tổng quan về Cryptography

#### Cryptography là gì?

Cryptography (Mật mã học) là một lĩnh vực trong khoa học máy tính và toán học nghiên cứu các phương pháp để bảo vệ thông tin trong các giao dịch. Cryptography bao gồm việc mã hóa, giải mã dữ liệu và các kỹ thuật bảo mật khác nhằm đảm bảo tính riêng tư, xác thực và tính toàn vẹn của dữ liệu.

#### Lợi ích của Cryptography

- **Bảo mật thông tin**: Đảm bảo rằng thông tin chỉ có thể được truy cập và đọc bởi những người được phép.
- **Xác thực danh tính**: Xác nhận danh tính của người gửi và người nhận, giúp ngăn chặn các cuộc tấn công giả mạo.
- **Tính toàn vẹn của dữ liệu**: Đảm bảo rằng dữ liệu không bị thay đổi hoặc làm giả trong quá trình truyền tải.
- **Không thể phủ nhận**: Đảm bảo rằng người gửi không thể từ chối việc gửi một thông điệp hoặc thực hiện một giao dịch.

#### Các thuật toán Cryptography phổ biến

- **AES (Advanced Encryption Standard)**: Thuật toán mã hóa đối xứng được sử dụng rộng rãi trong bảo mật dữ liệu.
- **RSA (Rivest-Shamir-Adleman)**: Thuật toán mã hóa bất đối xứng phổ biến với khả năng mã hóa và ký số.
- **SHA (Secure Hash Algorithm)**: Thuật toán băm (hashing) để tạo ra các giá trị băm duy nhất từ dữ liệu đầu vào.
- **HMAC (Hash-based Message Authentication Code)**: Kỹ thuật xác thực thông điệp dựa trên hàm băm.

### 2. Các loại Cryptography trong C# .NET

#### Symmetric Key Cryptography

Cryptography với khóa đối xứng sử dụng một khóa duy nhất cho cả việc mã hóa và giải mã dữ liệu. Thuật toán AES là ví dụ điển hình của mã hóa đối xứng.

- **Ưu điểm**: Hiệu suất cao, mã hóa và giải mã nhanh chóng.
- **Nhược điểm**: Việc bảo vệ khóa là rất quan trọng vì nếu khóa bị lộ, dữ liệu có thể bị giải mã.

#### Asymmetric Key Cryptography

Cryptography với khóa bất đối xứng sử dụng một cặp khóa: khóa công khai (public key) để mã hóa dữ liệu và khóa riêng (private key) để giải mã. RSA là thuật toán phổ biến trong mã hóa bất đối xứng.

- **Ưu điểm**: Đảm bảo tính bảo mật cao hơn vì khóa công khai có thể được chia sẻ công khai mà không lo ngại bị lộ khóa riêng.
- **Nhược điểm**: Quá trình mã hóa và giải mã thường chậm hơn so với mã hóa đối xứng.

#### Hashing

Hashing là quá trình chuyển đổi dữ liệu đầu vào thành một giá trị băm có độ dài cố định. Các thuật toán hash như SHA-256 thường được sử dụng để kiểm tra tính toàn vẹn của dữ liệu.

- **Ưu điểm**: Mã hóa một chiều, không thể giải mã lại, giúp bảo vệ thông tin như mật khẩu.
- **Nhược điểm**: Không thể khôi phục dữ liệu từ giá trị băm, chỉ có thể so sánh với giá trị băm đã biết.

#### Digital Signatures

Chữ ký số là một ứng dụng của mã hóa bất đối xứng, dùng để xác thực người gửi và đảm bảo tính toàn vẹn của dữ liệu. Thông qua việc sử dụng khóa riêng để ký và khóa công khai để xác minh, chữ ký số giúp đảm bảo rằng dữ liệu không bị thay đổi và người gửi là hợp lệ.

- **Ưu điểm**: Bảo vệ dữ liệu khỏi bị thay đổi và xác nhận danh tính người gửi.
- **Nhược điểm**: Yêu cầu quản lý khóa riêng và khóa công khai.

### 3. Sử dụng Cryptography trong ASP.NET Core

#### Mã hóa với AES

Mã hóa với AES trong C# sử dụng lớp `Aes` từ thư viện `System.Security.Cryptography`. Ví dụ mã hóa và giải mã dữ liệu:

```csharp
using System.Security.Cryptography;
using System.Text;

public class AesExample
{
    public static string Encrypt(string plainText, string key)
    {
        using (Aes aesAlg = Aes.Create())
        {
            aesAlg.Key = Encoding.UTF8.GetBytes(key);
            aesAlg.IV = new byte[16]; // Initialization Vector

            ICryptoTransform encryptor = aesAlg.CreateEncryptor(aesAlg.Key, aesAlg.IV);
            using (MemoryStream msEncrypt = new MemoryStream())
            using (CryptoStream csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write))
            {
                using (StreamWriter swEncrypt = new StreamWriter(csEncrypt))
                {
                    swEncrypt.Write(plainText);
                }
                return Convert.ToBase64String(msEncrypt.ToArray());
            }
        }
    }

    public static string Decrypt(string cipherText, string key)
    {
        using (Aes aesAlg = Aes.Create())
        {
            aesAlg.Key = Encoding.UTF8.GetBytes(key);
            aesAlg.IV = new byte[16];

            ICryptoTransform decryptor = aesAlg.CreateDecryptor(aesAlg.Key, aesAlg.IV);
            using (MemoryStream msDecrypt = new MemoryStream(Convert.FromBase64String(cipherText)))
            using (CryptoStream csDecrypt = new CryptoStream(msDecrypt, decryptor, CryptoStreamMode.Read))
            using (StreamReader srDecrypt = new StreamReader(csDecrypt))
            {
                return srDecrypt.ReadToEnd();
            }
        }
    }
}
```

#### Mã hóa với RSA

Mã hóa với RSA trong C# sử dụng lớp `RSACryptoServiceProvider`. Dưới đây là ví dụ mã hóa và giải mã với RSA:

```csharp
using System.Security.Cryptography;
using System.Text;

public class RsaExample
{
    public static string Encrypt(string plainText, RSAParameters publicKey)
    {
        using (RSACryptoServiceProvider rsa = new RSACryptoServiceProvider())
        {
            rsa.ImportParameters(publicKey);
            byte[] dataToEncrypt = Encoding.UTF8.GetBytes(plainText);
            byte[] encryptedData = rsa.Encrypt(dataToEncrypt, false);
            return Convert.ToBase64String(encryptedData);
        }
    }

    public static string Decrypt(string cipherText, RSAParameters privateKey)
    {
        using (RSACryptoServiceProvider rsa = new RSACryptoServiceProvider())
        {
            rsa.ImportParameters(privateKey);
            byte[] dataToDecrypt = Convert.FromBase64String(cipherText);
            byte[] decryptedData = rsa.Decrypt(dataToDecrypt, false);
            return Encoding.UTF8.GetString(decryptedData);
        }
    }
}
```

#### Tạo và xác minh chữ ký số

Dưới đây là ví dụ về việc tạo và xác minh chữ ký số sử dụng RSA:

```csharp
using System.Security.Cryptography;
using System.Text;

public class DigitalSignatureExample
{
    public static string CreateSignature(string data, RSAParameters privateKey)
    {
        using (RSACryptoServiceProvider rsa = new RSACryptoServiceProvider())
        {
            rsa.ImportParameters(privateKey);
            byte[] dataBytes = Encoding.UTF8.GetBytes(data);
            byte[] signedData = rsa.SignData(dataBytes, CryptoConfig.MapNameToOID("SHA256"));
            return Convert.ToBase64String(signedData);
        }
    }

    public static bool VerifySignature(string data, string signature, RSAParameters publicKey)


 {
        using (RSACryptoServiceProvider rsa = new RSACryptoServiceProvider())
        {
            rsa.ImportParameters(publicKey);
            byte[] dataBytes = Encoding.UTF8.GetBytes(data);
            byte[] signatureBytes = Convert.FromBase64String(signature);
            return rsa.VerifyData(dataBytes, CryptoConfig.MapNameToOID("SHA256"), signatureBytes);
        }
    }
}
```

### 4. Quản lý khóa trong Cryptography

#### Khóa đối xứng

Khóa đối xứng là một khóa duy nhất dùng để mã hóa và giải mã dữ liệu. Điều quan trọng là bảo vệ khóa này trong môi trường an toàn, tránh lộ ra ngoài. Các phương pháp lưu trữ an toàn khóa đối xứng có thể bao gồm sử dụng các công cụ quản lý khóa hoặc lưu trữ trong các dịch vụ đám mây bảo mật.

#### Khóa công khai và khóa riêng

Khóa công khai và khóa riêng được sử dụng trong mã hóa bất đối xứng (ví dụ: RSA). Khóa công khai có thể được chia sẻ công khai, trong khi khóa riêng cần được bảo vệ nghiêm ngặt. Sử dụng các dịch vụ như **Key Vault** của Azure giúp bảo mật và quản lý các khóa này hiệu quả.

#### Key Vault trong .NET

**Azure Key Vault** là một dịch vụ của Microsoft Azure giúp lưu trữ và bảo vệ các khóa mã hóa và thông tin nhạy cảm. Bạn có thể tích hợp Azure Key Vault với ứng dụng ASP.NET Core để quản lý khóa một cách an toàn.

```csharp
// Cài đặt package Azure.Identity và Azure.Security.KeyVault.Secrets
public class KeyVaultExample
{
    public async Task<string> GetSecretAsync(string secretName)
    {
        var client = new SecretClient(new Uri("https://your-keyvault-name.vault.azure.net/"), new DefaultAzureCredential());
        KeyVaultSecret secret = await client.GetSecretAsync(secretName);
        return secret.Value;
    }
}
```

### 5. Bảo mật và hiệu suất trong Cryptography

- **Bảo mật**: Đảm bảo bảo vệ khóa riêng và dữ liệu nhạy cảm. Cần tránh lưu trữ khóa trong mã nguồn hoặc cơ sở dữ liệu không an toàn.
- **Hiệu suất**: Cryptography có thể ảnh hưởng đến hiệu suất của ứng dụng, đặc biệt khi sử dụng các thuật toán bất đối xứng. Vì vậy, cần cân nhắc kỹ lưỡng trong việc lựa chọn thuật toán mã hóa và tối ưu hóa các phép toán mật mã.

### 6. Công cụ hỗ trợ trong môi trường Production

- **Azure Key Vault**: Cung cấp dịch vụ quản lý khóa và chứng chỉ cho các ứng dụng đám mây.
- **AWS KMS**: Dịch vụ của Amazon Web Services để quản lý và bảo vệ khóa mã hóa.
- **HashiCorp Vault**: Công cụ mã nguồn mở để quản lý khóa, chứng chỉ và mật khẩu bảo mật.

### 7. Kết luận

Cryptography là yếu tố quan trọng trong việc bảo mật dữ liệu và giao dịch trực tuyến. Trong ASP.NET Core, các công cụ và thư viện hỗ trợ cryptography mạnh mẽ giúp bảo vệ thông tin và đảm bảo tính toàn vẹn của dữ liệu. Việc quản lý khóa và bảo mật hiệu quả sẽ đảm bảo tính an toàn cho hệ thống và người dùng.
