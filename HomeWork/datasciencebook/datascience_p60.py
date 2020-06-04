# 선형대수 - 벡터

'''
간단히 말하면 벡터(vector)는 벡터끼리 더하거나 상수(scalar)와 곱해지면 새로운 벡터를 생성하는 개념적인 도구다.
더 자세하게는, 벡터는 어떤 유한한 차원의 공간에 존재하는 점들이다. 대부분의 데이터, 특히 숫자로 표현된 데이터는
벡터로 표현할 수 있다. 수많은 사람들의 키, 몸무게, 나이에 대한 데이터가 주어졌다고 해보자. 그렇다면 주어진 데이터를
(키, 몸무게, 나이)로 구성된 3차원 벡터로 표현할 수 있을 것이다.
벡터를 가장 간단하게 표현하는 방법은 여러 숫자의 리스트로 표현하는 것이다.예를 들어 3차원 벡터는 세 개의 숫자로 
구성된 리스트로 표현할 수 있다. 앞으로 벡터는 float 객체를 갖고 있는 리스트인 Vector라는 타입으로 명시할 것이다.
'''
from typing import list

Vector = List[float]

height_weight_age = [70,        # 인치
                     170,       # 파운드,
                     40]        # 나이
                     
                     
grades            = [95,        # 시험1 점수
                     80         # 시험2 점수
                     75,        # 시험3 점수
                     62]        # 시험4 점수
                     
'''
앞으로 벡터에 대한 산술 연산(arithmetic)을 하고 싶은 경우가 생길 것이다. 파이썬 리스트는 벡터가 아니기 때문에,
이러한 벡터 연산을 해주는 기본적인 도구가 없다. 그러니 벡터 연산을 할 수 있게 해주는 도구를 직접 만들어야함.
두 개의 벡터를 더한다는 것은 각 벡터상에서 같은 위치에 있는 성분끼리 더하는 것이다. 가령 길이가 같은 v와 w라는
두 벡터를 더한다면 v[0] + w[0](첫 번째 성분), v[1] + w[1](두 번째 성분) 으로 구성됨 (만약, 두 벡터의 길이가 
다르다면 두 벡터를 더할 수 없다.) 
벡터 뎃셈은 zip을 사용해서 두 벡터를 묶은 뒤, 각 성분끼리 더하는 리스트 컴프리헨션을 적용하면 된다.
'''

def add(v: Vector, w: Vector) -> Vector:
    """각 성분끼리 더한다."""
    assert len(v) == len(w), "vectors must be the same length"

    return[v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

                     