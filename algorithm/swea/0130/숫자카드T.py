T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 숫자 카드의 개수
    numbers = input() # 숫자 카드들이 주어지는데, 공백없이 입력

    # 개수를 세는거니까, 카운팅 배열
    counts = [0] * 10

    # numbers 문자열을 순회하면서 글자 하나를 떼어 오고
    # 그 글자를 숫자로 바꾼 후에 카운팅
    for number in numbers:
        # 떼어온 글자를 숫자로 바꾸고, 등장 회수 1 증가
        counts[int(number)] += 1

    # 최대값 구하기, 가장 많이 등장한 숫자가 몇이고, 몇개인지
    # 가장 많이 등장한 숫자가 여러개일 경우 그 중에서 큰거 선택
    max_count = 0 # 최대 등장 횟수
    max_number = 0 # 가장 큰 수
    
    # 0부터 9까지 숫자 중에 누가 가장 많이 등장 했는지 구하기
    for i in range(len(counts)):
        # 내가 지금까지 알던 최대 등장 횟수보다
        # 이번에 새로 발견한 숫자 i의 등장 횟수가 크다면
        # 새로운 i의 값으로 최대값 변경
        # 등호를 추가하면 같은 등장 횟수를 가진 카드 중에 더 큰 숫자 사용 가능
        if counts[i] >= max_count:
            max_count = counts[i]
            max_number = i
    print(f"#{tc} {max_number} {max_count}")