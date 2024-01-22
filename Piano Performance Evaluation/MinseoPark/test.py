import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import time


# 그래프 초기 설정
plt.ion()

# 그래프 생성
fig, ax = plt.subplots()

# 사각형을 저장할 리스트
rectangles = []

# 초기 시간 설정
start_time = time.time()

while True:
    # 현재 시간에서 시작 시간을 빼서 x 좌표 생성
    x = time.time() - start_time
    y = random.randint(0, 127)

    # 사각형의 위치 및 크기 설정
    rect = patches.Rectangle((x, y), 0.2, 0.2, linewidth=1, edgecolor='r', facecolor='none')

    # 사각형을 리스트에 추가
    rectangles.append(rect)

    # 그래프 업데이트
    ax.clear()

    # 저장된 모든 사각형을 그래프에 추가
    for r in rectangles:
        ax.add_patch(r)

    # 그래프 축 설정 (예: 가장 오래된 데이터부터 현재까지)
    ax.set_xlim(0, x)
    ax.set_ylim(0, 127)

    # 그래프 보여주기
    plt.show()
    plt.pause(0.1)
