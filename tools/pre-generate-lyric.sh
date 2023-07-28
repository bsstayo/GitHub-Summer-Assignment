#!/bin/bash

MD=SuperShy.md

apt-get install git-lfs 
git lfs install
git lfs track "*.png"

touch $MD

echo "# Title: SUPER SHY by newjeans  " >> $MD
git add $MD && git commit -m "feat: 타이틀 추가"

echo "![supershy album](./supershy)  " >> $MD
git add $MD && git commit -m "feat: 앨범 커버 추가"

echo "I'm super shy, super shy  " >> $MD
git add $MD && git commit -m "feat: 첫번째 가사줄 추가"

echo "But wait a minute while I make you mine, make you mine  " >> $MD
git add $MD && git commit -m "feat: 두번째 가사줄 추가"

echo "떨리는 지금도 you're on my mind all the time  " >> $MD
git add $MD && git commit -m "feat: 세번째 가사줄 추가"

echo "I wanna tell you but I'm super shy, super shy  " >> $MD
git add $MD && git commit -m "feat: 네번째 가사줄 추가"

echo "I'm super shy, super shy  " >> $MD
git add $MD && git commit -m "feat: 다섯번째 가사줄 추가"

echo "But wait a minute while I make you mine, make you mine  " >> $MD
git add $MD && git commit -m "feat: 여섯번째 가사줄 추가"

echo "떨리는 지금도 you're on my mind all the time  " >> $MD
git add $MD && git commit -m "feat: 일곱번째 가사줄 추가"

echo "I wanna tell you but I'm super shy, super shy  " >> $MD
git add $MD && git commit -m "feat: 여덟번째 가사줄 추가"

echo "I wanna tell you but I'm super shy, super shy  " >> $MD
git add $MD && git commit -m "feat: 여덟번째 가사줄 추가"

echo "And I wanna go out with you, where you wanna go? (Huh?)  " >> $MD
git add $MD && git commit -m "feat: 아홉번째 가사줄 추가"

echo "Find a lil' spot, just sit and talk  " >> $MD
git add $MD && git commit -m "feat: 열번째 가사줄 추가"

echo "Looking pretty, follow me, 우리 둘이 나란히  " >> $MD
git add $MD && git commit -m "feat: 열한번째 가사줄 추가"

echo "보이지? 내 눈이 갑자기 빛나지 when you say I'm your dream  " >> $MD
git add $MD && git commit -m "feat: 열두번째 가사줄 추가"

echo "You don't even know my name, do you?  " >> $MD
git add $MD && git commit -m "feat: 열세번째 가사줄 추가"

echo "You don't even know my name, do you?  " >> $MD
git add $MD && git commit -m "feat: 열네번째 가사줄 추가"

echo "누구보다도 I'm super shy, super shy  " >> $MD
git add $MD && git commit -m "feat: 열세번째 가사줄 추가"

echo "But wait a minute while I make you mine, make you mine  " >> $MD
git add $MD && git commit -m "feat: 열다섯번째 가사줄 추가"

echo "떨리는 지금도 you're on my mind all the time  " >> $MD
git add $MD && git commit -m "feat: 열여섯째 가사줄 추가"

echo "I wanna tell you but I'm super shy, super shy  " >> $MD
git add $MD && git commit -m "feat: 열일곱째 가사줄 추가"