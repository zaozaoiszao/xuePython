from gmssl import sm4
import os
# 生成16字节的随机字节序列  
random_bytes = os.urandom(16)  
print("密钥为:",random_bytes)

# 现在random_string_16_chars是一个由16个随机选择的ASCII可打印字符组成的字符串  
# 但请注意，这个字符串在UTF-8编码下的字节长度可能大于16
# 密钥和明文（注意：密钥长度必须是16字节）  
key = random_bytes
print(key)
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
