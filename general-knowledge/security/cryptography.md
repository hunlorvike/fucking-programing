## **🚀 "GIẢI MÃ" CRYPTOGRAPHY TRONG C#: "VŨ KHÍ" BẢO MẬT CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một lĩnh vực cực kỳ quan trọng và thú vị:
Cryptography (Mật mã học) trong C# .NET. Nghe có vẻ "cao siêu" nhưng thực ra rất gần gũi và cần thiết cho dân code chúng
mình đấy. Mình sẽ cố gắng giải thích dễ hiểu nhất có thể, kèm theo ví dụ thực tế để các bạn dễ hình dung nhé! Let's go!

### **I. CRYPTOGRAPHY LÀ GÌ? (BẢO VỆ DỮ LIỆU NHƯ THẾ NÀO?)**

* **Cryptography (Mật mã học):** Là môn khoa học nghiên cứu cách bảo vệ thông tin (chữ, số, file, ...) bằng cách mã
  hóa (encryption) và giải mã (decryption).
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn viết thư bằng một ngôn ngữ bí mật: chỉ những ai có "chìa khóa" mới đọc được nội dung.
* **Lợi ích:**
    * **Bảo mật:** Dữ liệu không bị lộ khi bị đánh cắp.
    * **Xác thực:** Xác định đúng người gửi/nhận.
    * **Toàn vẹn:** Đảm bảo dữ liệu không bị thay đổi.
    * **Không thể chối bỏ:** Người gửi không thể chối bỏ việc đã gửi thông tin.

### **II. CÁC THUẬT TOÁN CRYPTOGRAPHY PHỔ BIẾN (NHỮNG "CÔNG CỤ" BẢO MẬT)**

1. **AES (Advanced Encryption Standard):** Thuật toán mã hóa đối xứng (dùng chung khóa), dùng để bảo vệ dữ liệu.
2. **RSA (Rivest-Shamir-Adleman):** Thuật toán mã hóa bất đối xứng (dùng cặp khóa public/private), dùng để mã hóa, ký
   số.
3. **SHA (Secure Hash Algorithm):** Thuật toán băm (hashing), tạo "dấu vân tay" cho dữ liệu (không thể đảo ngược).
4. **HMAC (Hash-based Message Authentication Code):** Xác thực thông điệp dựa trên hàm băm.

### **III. CRYPTOGRAPHY TRONG C# .NET (THAO TÁC VỚI CÁC "CÔNG CỤ")**

#### **1. Mã Hóa Đối Xứng (SYMMETRIC):**

* Dùng chung 1 khóa để mã hóa và giải mã (nhanh nhưng khóa phải bí mật).
* **Ví dụ (AES):**

```csharp
using System;
using System.IO;
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

#### **2. Mã Hóa Bất Đối Xứng (ASYMMETRIC):**

* Dùng 2 khóa:
    * **Khóa công khai (Public Key):** Để mã hóa (chia sẻ thoải mái).
    * **Khóa riêng (Private Key):** Để giải mã (giữ bí mật).
* **Ví dụ (RSA):**

```csharp
using System;
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

#### **3. Chữ Ký Số (DIGITAL SIGNATURE):**

* Dùng khóa riêng để tạo chữ ký, khóa công khai để xác minh (đảm bảo tính toàn vẹn và xác thực).
* **Ví dụ (RSA):**

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

### **IV. QUẢN LÝ KHÓA (LƯU TRỮ CHÌA KHÓA CẨN THẬN)**

1. **Khóa đối xứng:** Phải bảo vệ khóa cẩn thận (lưu trữ an toàn, tránh lộ).
2. **Khóa bất đối xứng:** Khóa công khai chia sẻ thoải mái, khóa riêng bảo mật kỹ càng.
3. **Azure Key Vault:** Dùng dịch vụ đám mây để quản lý khóa an toàn hơn.

```csharp
using Azure.Identity;
using Azure.Security.KeyVault.Secrets;
using System.Threading.Tasks;

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

### **V. BẢO MẬT VÀ HIỆU SUẤT (KHÔNG CHỈ BẢO VỆ, MÀ CÒN PHẢI CHẠY NHANH)**

* **Bảo mật:** Tránh lưu khóa trong code, dùng các công cụ quản lý khóa an toàn.
* **Hiệu suất:** Cần cân nhắc chọn thuật toán mã hóa phù hợp, tối ưu hóa code để không làm chậm ứng dụng.

### **VI. CÔNG CỤ HỖ TRỢ (NHỮNG "TRỢ THỦ" ĐẮC LỰC)**

* **Azure Key Vault:** Quản lý khóa cho ứng dụng đám mây.
* **AWS KMS:** Quản lý khóa trên Amazon Web Services.
* **HashiCorp Vault:** Mã nguồn mở, quản lý khóa, chứng chỉ.

### **VII. KẾT LUẬN (TỔNG KẾT)**

Cryptography là một lĩnh vực quan trọng giúp bảo vệ dữ liệu của bạn. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về
nó và có thể áp dụng vào dự án của mình. Chúc các bạn code thành công và luôn bảo mật! 😎
