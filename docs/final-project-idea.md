# Final Project Idea

Final Project를 위해 아이디어를 모아봅시다! 💡🚀🤯💪 

## #1 What's your ETA? ⏰
### 1. 설명
What's your ETA(Estimated Time of Appraisal)는 글로벌 시대에 맞춰 편리한 PR을 도와줍니다.<br/>
전세계 어디에 있든, 팀원의 시간을 비교하여 대략 어느 시점에 PR을 확인할 수 있는지 제공합니다.

>ex) John: New York, USA / Lily: London, UK / Minsu: Seoul, South Korea
>각 도시/국가들은 다음과 같은 시간대를 사용합니다:<br/>
>New York: EST(GMT-5)/EDT(GMT-4)<br/>
>London: GMT(GMT+0)/BST(GMT+1)<br/>
>Seoul: KST(GMT+9)<br/>
>
>썸머 타임을 적용하는 국가들과 그렇지 않는 국가들이 있기 때문에 협업에 있어 시간차를 이해하기란 매우 어렵습니다.
>
>우선, 보통의 사람들은 주 5일 근무를 하고, 출근을 하자마자 PR을 확인하지 않을 수도 있으니 각자 오전 11시 즈음에 확인한다고 가정합니다.<br/>
>그리고 만약 John이 2023년 8월 11일 17시 30분에 PR을 올렸다고 가정을 해봅시다.<br/>
>그러면 Lily는 2023/08/11/ 22:30, Minsu는 2023/08/12 06:30입니다.<br/>
>둘 다 이미 퇴근을 해서 집에서 편안한 휴식을 취하고 있거나, 주말의 달콤한 늦잠을 만끽하고 있을 수 있습니다.<br/>
>이 때 제작된 깃허브 액션이 아래와 같이 코멘트를 남겨줍니다:<br/>
> ```
> Lily's Time: 2023/Aug/11 22:30 (Estimated: +60.5 hours)
> Minsu's Time: 2023/Aug/12 06:30 (Estimated: +52.5 hours)
> ```

### 2. 제출형식
깃허브 액션 + 파이썬 파일 등

### 3. 테크 스택
- GitHub Actions
- Python
- Docker

## #2 Simple Server Monitoring Action 
### 1. 설명
대규모 트래픽을 담당하는 서비스는 대부분 실시간으로 서버의 상황을 모니터링하는것이 가능하고 자체적인 복구 솔루션을 가지고 있습니다. 반면에 개인 프로젝트로 만든 서비스나 소규모 트래픽을 예상하고 만든 서비스인 경우는 실시간 서버 모니터링까지 구현하지 않는것이 대부분입니다. 하지만 소규모 서비스라 하더라도 사용자가 서비스를 요청했을때, 만약 서버에 문제가 생겨 응답하지 않는다면 서비스에 대한 신뢰도의 큰 하락으로 이어질 수 있습니다. <br/>
따라서 깃허브 액션을 통해 일정시간마다 서버에 요청을 보내 서버의 상황을 확인할 수 있다면 소규모 서비스들은 매우 적은 노력과 비용으로 서버 모니터링 시스템을 구현할 수 있습니다.

작동 예시 <br/>
한시간마다 요청을 보낸다고 할경우.. <br/>
깃허브 액션 -->(http 기반 요청)--> 서비스 <br/>
if(응답이 온경우) -> job done <br/>
else -> slack 알림 메시지 (서버에 문제가 생겼습니다) > job done
### 2. 제출형식
- github action
- python script 
### 3. 테크스택
- Gihub Actions
- Python
- Slack WebHook
- Shell Script?