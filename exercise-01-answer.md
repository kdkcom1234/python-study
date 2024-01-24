알겠습니다. 각 문제에 대한 해답을 제공하겠습니다. 단, 파이썬 문법과 기능을 활용하는 다양한 방법이 있을 수 있으므로 제시하는 해답은 한 가지 예시일 뿐임을 알려드립니다.

1. 변수 x와 y의 합 출력하기:
   ```python
   x = 5
   y = 3
   print(x + y)
   ```

2. 문자열 s의 길이 출력하기:
   ```python
   s = "Hello, Python!"
   print(len(s))
   ```

3. 두 정수의 곱 반환하는 함수:
   ```python
   def multiply(a, b):
       return a * b
   ```

4. 리스트에서 짝수만 선택하기:
   ```python
   numbers = [1, 2, 3, 4, 5]
   even_numbers = [num for num in numbers if num % 2 == 0]
   ```

5. 양수/음수 판별 함수:
   ```python
   def check_number(n):
       if n > 0:
           return "양수"
       elif n < 0:
           return "음수"
       else:
           return "0"
   ```

6. 문자열이 회문인지 판별하는 함수:
   ```python
   def is_palindrome(s):
       return s == s[::-1]
   ```

7. 0부터 10까지 출력하는 반복문:
   ```python
   for i in range(11):
       print(i)
   ```

8. 튜플 요소들의 합 계산하기:
   ```python
   t = (1, 2, 3)
   total = sum(t)
   ```

9. 딕셔너리에서 'name' 키의 값 출력하기:
   ```python
   person = {'name': 'Alice', 'age': 25}
   print(person['name'])
   ```

10. 소수 판별 함수:
    ```python
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    ```

11. 리스트 요소 두 배로 만들기:
    ```python
    a = [1, 2, 3]
    a = [x * 2 for x in a]
    ```

12. 두 문자열 결합 함수:
    ```python
    def concatenate(str1, str2):
        return str1 + str2
    ```

13. 짝수/홀수 판별 조건문:
    ```python
    n = 4
    if n % 2 == 0:
        print("짝수")
    else:
        print("홀수")
    ```

14. 1부터 100까지의 합 계산하기:
    ```python
    total = sum(range(101))
    ```

15. 리스트에서 최댓값과 최솟값 찾기:
    ```python
    numbers = [1, 2, 3, 4, 5]
    max_value = max(numbers)
    min_value = min(numbers)
    ```

16. 문자열에서 모음 개수 세기:
    ```python
    def count_vowels(s):
        vowels = 'aeiou'
        return sum(1 for char in s if char in vowels)
    ```

17. 정수 n의 팩토리얼 계산하기:
    ```python
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    ```

18. 리스트 역순으로 만들기:
    ```python
    numbers = [1, 2, 3, 4, 5]
    numbers.reverse()
    ```

19. 딕셔너리에 키와 값 추가하기:
    ```python
    dictionary = {}
    key = 'new_key'
    value = 'new_value'
    dictionary[key] = value
    ```

20. 0부터 입력한 숫자까지의 짝수 합 출력하기:
    ```python
    n = int(input("숫자를 입력하세요: "))
    total = sum(i for i in range(0, n+1,

 2))
    print(total)
    ```

21. 튜플의 첫 번째와 마지막 요소 반환하기:
    ```python
    def first_last(t):
        return t[0], t[-1]
    ```

22. 문자열을 거꾸로 반환하는 함수:
    ```python
    def reverse_string(s):
        return s[::-1]
    ```

23. 리스트에서 중복 요소 제거하기:
    ```python
    numbers = [1, 2, 2, 3, 4, 4, 5]
    unique_numbers = list(set(numbers))
    ```

24. 두 숫자 중 큰 숫자 반환하기:
    ```python
    def max_number(a, b):
        return max(a, b)
    ```

25. 1부터 10까지 출력하는 while 반복문:
    ```python
    i = 1
    while i <= 10:
        print(i)
        i += 1
    ```

26. 딕셔너리의 키와 값 출력하기:
    ```python
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")
    ```

27. 문자열에서 각 문자의 출현 횟수 세기:
    ```python
    def count_characters(s):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        return count
    ```

28. 10개의 숫자 중 최댓값 찾기:
    ```python
    numbers = [int(input("숫자를 입력하세요: ")) for _ in range(10)]
    print("최댓값:", max(numbers))
    ```

29. 리스트 요소를 문자열로 결합하기:
    ```python
    def join_list(lst):
        return ''.join(map(str, lst))
    ```

30. 이름과 나이를 딕셔너리에 저장하기:
    ```python
    person = {}
    person['name'] = input("이름을 입력하세요: ")
    person['age'] = int(input("나이를 입력하세요: "))
    ```

이 해답들은 기본적인 파이썬 프로그래밍 기술을 보여줍니다. 각 문제에 대한 해답은 다양한 방식으로 작성될 수 있으며, 이는 그 중 하나의 예시일 뿐입니다.