# coding:    utf-8
# author:    leviolet
# license:   MIT
# version:   Python 3.8+

#踢开Python2
def kick_py2():
    import sys
    if(sys.version[0] != '3' and int(sys.version[2]) < 8):
        print("需要Python3.8+")
        exit(5)
kick_py2()


from sympy import *
import math

n  = 0xa1d4d377001f1b8d5b2740514ce699b49dc8a02f12df9a960e80e2a6ee13b7a97d9f508721e3dd7a6842c24ab25ab87d1132358de7c6c4cee3fb3ec9b7fd873626bd0251d16912de1f0f1a2bba52b082339113ad1a262121db31db9ee1bf9f26023182acce8f84612bfeb075803cf610f27b7b16147f7d29cc3fd463df7ea31ca860d59aae5506479c76206603de54044e7b778e21082c4c4da795d39dc2b9c0589e577a773133c89fa8e3a4bd047b8e7d6da0d9a0d8a3c1a3607ce983deb350e1c649725cccb0e9d756fc3107dd4352aa18c45a65bab7772a4c5aef7020a1e67e6085cc125d9fc042d96489a08d885f448ece8f7f254067dfff0c4e72a63557
e1 = 0xf4c1158f
c1 = 0x2f6546062ff19fe6a3155d76ef90410a3cbc07fef5dff8d3d5964174dfcaf9daa003967a29c516657044e87c1cbbf2dba2e158452ca8b7adba5e635915d2925ac4f76312feb3b0c85c3b8722c0e4aedeaec2f2037cc5f676f99b7260c3f83ffbaba86cda0f6a9cd4c70b37296e8f36c3ceaae15b5bf0b290119592ff03427b80055f08c394e5aa6c45bd634c80c59a9f70a92dc70eebec15d4a5e256bf78775e0d3d14f3a0103d9ad8ea6257a0384091f14da59e52581ba2e8ad3adb9747435e9283e8064de21ac41ab2c7b161a3c072b7841d4a594a8b348a923d4cc39f02e05ce95a69c7500c29f6bb415c11e4e0cdb410d0ec2644d6243db38e893c8a3707
e2 = 0xf493f7d1
c2 = 0xd32dfad68d790022758d155f2d8bf46bb762ae5cc17281f2f3a8794575ec684819690b22106c1cdaea06abaf7d0dbf841ebd152be51528338d1da8a78f666e0da85367ee8c1e6addbf590fc15f1b2182972dcbe4bbe8ad359b7d15febd5597f5a87fa4c6c51ac4021af60aeb726a3dc7689daed70144db57d1913a4dc29a2b2ec34c99c507d0856d6bf5d5d01ee514d47c7477a7fb8a6747337e7caf2d6537183c20e14c7b79380d9f7bcd7cda9e3bfb00c2b57822663c9a5a24927bceec316c8ffc59ab3bfc19f364033da038a4fb3ecef3b4cb299f4b600f76b8a518b25b576f745412fe53d229e77e68380397eee6ffbc36f6cc734815cd4065dc73dcbcb

if(gcd(e1,e2) != 1):
    exit(2)

# 扩展欧几里得算法 矩阵形式
#   求出化简矩阵B
A = Matrix([
    [e1,e2],
    [1,0],
    [0,1]
])
B = A
while(B[0] != 1 and B[1] != 1):
    if B[1] > B[0]:
        k = - B[1] // B[0] + 1
        B = B * Matrix([
            [1,k],
            [0,1]
        ])
    else:
        k = - B[0] // B[1] + 1
        B = B * Matrix([
            [1,0],
            [k,1]
        ])
print(B)

#   根据B得出s1,s2
s1 = 0
s2 = 0
if(B[0] == 1):
    s1 = B[2]
    s2 = B[4]
else:
    s1 = B[3]
    s2 = B[5]
#坑爹的类型转换
s1 = int(s1)
s2 = int(s2)

print([s1,s2])

if(e1*s1 + e2*s2 != 1):
    print("出错")
    exit(3)

#求出m
m = (pow(c1,s1,n) * pow(c2,s2,n)) % n #或者 (pow(c1,s1) * pow(c2,s2)) % n
print(m)

#转化为字符，并除去前面多余的0和后面64个混淆字符
r = m.to_bytes(512,'big')
flag = r.strip(b"\x00")[:-64]
print(flag)