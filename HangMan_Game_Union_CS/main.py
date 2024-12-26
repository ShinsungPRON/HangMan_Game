#행맨 게임
# 이 코드 기반으로 만들었습니다. 어떻게 작동하는지 참고하세요.

import random # random 라이브러리를 import한다.

print("Developer : union-cs")

words = ['shinsung', 'pron', 'highschool', 'hungry', 'thirsty', 'hangman', 'hello', 'goodbye'] # words라는 리스트에 단어들을 채워넣는다.

word_random = random.choice(words) # 리스트에 있는 단어 중 하나를 랜덤으로 골라낸다.
guessed_word = [] # 입력한 글자들을 저장하는 리스트를 만든다.
tries = 8 # 총 8번의 기회를 준다.
hidden_word = ["_"] * len(word_random) # 선택된 단어를 단어의 길이에 맞게 '_'로 출력해서 보여준다.

print("Welcome to the Hangman Game!")
print("Prove that you are a Shinsung High School student by guessing the correct answer.")
print("Guess the word")

while tries > 0: # tries (기회)가 0보다 클 동안 (즉 기회가 남아있을 동안)
  print("\nCurrent State: " + " ".join(hidden_word)) # 현재 상태를 보여준다. '______' 이런 형식으로 보여지며, 단어를 맞추면 '___d____' 이렇게 변한다.
  print(f"Remaining tries: {tries}") # 남은 기회를 보여준다.

  guess = input("Enter the letter! : ").lower() # 글자 하나를 input으로 받는다. 유저가 대문자로 적어내서 발생하는 오류를 방지하기 위해 .lower()로 모두 소문자로 바꾸었다.

  if  guess in guessed_word: # 만약 이미 입력했던 글자를 또 입력했다면
    print("Ah, you already entered that... Enter another one")
  elif guess in word_random: # 만약 입력한 글자가 정해진 글자에 들어있는 글자라면
    print(f"GOOD. {guess} is included")
    guessed_word.append(guess) # 맞춘 글자를 리스트에 넣는다.

    for i in range(len(word_random)): # 해당 단어의 길이만큼 반복한다.
      if word_random[i] == guess: # 입력한 글자가 단어에 포함된 위치를 찾는다.
        hidden_word[i] = guess # 해당 위치에 맞춘 글자를 표시한다.

  else: # 그 외에 글자를 틀렸다면,
    print(f"YOUR ABSOLUTLY WRONG!! {guess} is not included")
    guessed_word.append(guess) # 틀린 글자를 리스트에 넣는다.
    tries -= 1 # 기회를 1 차감한다.

  if "_" not in hidden_word: # 만약 모든 글자를 전부 맞췄다면,
    print("\nCongratulations! Your very smart =) Shinsung Highschool student confirmed. This is your answer : " + word_random)
    break # 게임을 끝낸다.

if tries == 0: # 만약 주어진 기회를 모두 소진했다면,
  print("Too bad. Maybe your not smart enough, haha")
  print(f"The answer was {word_random}. hehe")
