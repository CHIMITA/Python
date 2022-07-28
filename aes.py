from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64


# bytes형만 처리 가능 - encode를 통해 bytes로 변환
# 암호화를 위해 사용할 key는 32바이트
# hashlib을 이용하여 랜덤으로 얻은 바이트를 32바이트로 변환

# AES를 이용 암호화하려면, 암호화의 대상인 value가 16, 32, 64, 128, 256 바이트의 블록들이어야 한다.
# 위와 같이 암호화 대상인 value를 16, 32, 64, 128, 256 바이트의 블록들로 만드는 것을 padding이라고 한다.
# 내장된 pad 모듈을 이용하여 암호화를 하려는 value를 블록들로 변경한다.

def encrypt(data: dict):
    encrypt_data = {}

    # password 와 salt 는 임의값
    key = hashlib.pbkdf2_hmac(hash_name='sha256', password=b'wins', salt=b'$efgh#', iterations=10000)

    # 암호화를 위한 AES 객체 생성
    aes = AES.new(key, AES.MODE_ECB)

    # 암호화를 위한 블럭 생성
    block_size = 16

    # 암호화
    value = value.encode('utf8')  # bytes인코딩
    padded_value = pad(value, block_size)  # 블록 사이즈 맞추기(패딩)

    # base64 인코딩을 한 후 utf8 디코딩을 하는 이유는
    # 암호화된 값을 string 형태로 자유롭게 사용하기 위해서 (ex 데이터 전달 or 이동)
    # base64 인코딩 없이 utf8 디코딩을 하게 되면 디코딩 에러 발생
    encrypt_data[key] = base64.b64encode(aes.encrypt(padded_value)).decode('utf8')

    return encrypt_data


def decrypt(data: dict):
    data = {}

    # password 와 salt 는 임의값
    key = hashlib.pbkdf2_hmac(hash_name='sha256', password=b'abcd', salt=b'$efgh#', iterations=10000)

    # 복호화를 위한 AES 객체 생성
    aes = AES.new(key, AES.MODE_ECB)

    # 복호화
    block_size = 16
    for key, encrypted_value in data.items():
        # base64로 디코딩을 하면 데이터타입이 byte가 된다.
        decrypted_value = aes.decrypt(base64.b64decode(encrypted_value))  # 복호화
        unpadded_value = unpad(decrypted_value, block_size)  # 암호화 할 때 붙였던 pad 떼어내기
        data[key] = unpadded_value.decode('utf8')
        
    return data

msg = str(input("암호화할 문자를 입력하세요 : "))

#data[key] = {msg}

encrypt()
decrypt()