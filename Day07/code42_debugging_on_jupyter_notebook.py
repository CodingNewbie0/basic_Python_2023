# %% [markdown]
# # 주피터 노트북 사용법 학습
# ## 마크다운, 파이썬 셀을 추가
# - 현재 셀 앞에 셀 추가 : a
# - 현재 셀 뒤에 셀 추가 : b
# - 현재 셀을 마크다운으로 변경 : 포커스(커서가 깜빡거리지 않는)만 있는 상태 m
# - 현재 센을 코드 셀로 변경 : 포커스 상태 y

# %%
# 최초 작성된 Pyfhon 셀

# %% [markdown]
# ## 파이썬 셀 실행
# - 셀 실행 : Ctrl + Enter
# - 셀 실행후, 다음 셀로 이동(다음 셀 없으면 생성) : Shift + Enter
# - 셀 실행, 다음셀 생성 : Alt + Enter
# - 주석 처리 : ctrl + / 또는 Ctrl + K,C

# %%
print('Hello, jupyter!!')
# print('Hello, jupyter!!')


# %% [markdown]
# ## 디버깅!!
# 아무리 강조해도 지나치지 않습니다.

# %%
arr = [1, '2', True, 'hello', 3.141596585]

for i in arr:
    print(i)

# %% [markdown]
# ## 함수 디버깅

# %%
def plus(x, y):
    val = x + y
    return val

def div(x, y):
    val = x / y,
    return val
    
print('더하기')
print(plus(10, 4))

# %%

print('나누기')
# print(plus(10, 0))

print(arr)
arr
