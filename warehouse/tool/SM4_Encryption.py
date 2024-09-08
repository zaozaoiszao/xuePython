from gmssl import sm4
import os
# 生成16字节的随机字节序列  
key = os.urandom(16)  
print("密钥为:",key)

# 密钥和明文（注意：密钥长度必须是16字节）  

plaintext = br'Hello, SM4 Encryption!'

# 创建一个SM4加密器
try:
    cipher = sm4.CryptSM4()
    cipher.set_key(key, sm4.SM4_ENCRYPT)
except:
    print("注意：密钥长度必须是16字节")
    exit()

# 加密
ciphertext = cipher.crypt_ecb(plaintext)  
print("Ciphertext:", ciphertext.hex())  

# 解密
cipher.set_key(key, sm4.SM4_DECRYPT)  
decryptedtext = cipher.crypt_ecb(ciphertext)
print(decryptedtext.decode())  