# Chapter 3
## Exercise
1. 상태, 행동, 보상을 확인하기 위한 자신만의 예제 3개를 MDP 구조에 맞추어 고안하라. 가능하면 3개 예제를 서로 `다르게` 만들어라. MDP 구조는 추상적이고 유동적이며, 많은 다양한 방식으로 적용될 수 있다. 최소한 한 개의 예제에서 MDP 구조는 추상적이고 유동적이며, 많은 다양한 방식으로 적용될 수 있다. 최소한 한 개의 예제에서 MDP의 구조적 한계를 어떤 방식으로든 확장하라.
>

2. 모든 목표 지향적 학습 문제를 유용하게 나타내는 데 있어 MDP 구조가 적합한가? MDP 구조가 적합하지 않은 명확한 문제를 생각해 볼 수 있는가?
>

3. 차를 운전하는 문제를 생각해 보자. 우리 몸이 차와 접촉하는 부분인 가속기, 운전대, 브레이크를 기준으로 행동을 정의할 수 있다. 더 바깥쪽으로 나아가서 타이어의 토크를 행동으로 생각해서, 타이어의 고무가 도로 면과 만나는 지점을 행동으로 정의할 수도 있다. 또는 더 안쪽으로 들어와서 우리 뇌가 우리 몸과 만나는 지점에서, 즉 갈비뼈를 제어하기 위한 근육의 미세한 움직임을 행동으로 정의할 수도 있다. 아니면 아주 놓은 수준에서 보면 차를 '어디로' 몰아야 할지 선택하는 것이 행동이 될 수도 있다. 무엇이 적정한 수준이며, 어디에 에이전트와 환경 사잉의 경계선을 긋는 것이 바람직할까? 한 경계선이 다른 경계선보다 더 바람직하다고 할 수 있는 기준은 무엇일까? 한 경계선을 다른 것보다 더 선호하는 근본적인 이유가 있을까? 아니면 아무런 선호 없이 그냥 선택하는 것일까?
>

4. 전이 확률 <img src="/rl-introduction-2nd-edit/tex/27f85042b2e9be54d56179a2dd20c45a.svg?invert_in_darkmode&sanitize=true" align=middle width=88.69078679999998pt height=24.7161288pt/>에 대해 예제 3.3에 나온 표와 유사한 표를 만들어라. 그 표에는 <img src="/rl-introduction-2nd-edit/tex/6f9bad7347b91ceebebd3ad7e6f6f2d1.svg?invert_in_darkmode&sanitize=true" align=middle width=7.7054801999999905pt height=14.15524440000002pt/>, <img src="/rl-introduction-2nd-edit/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/>, <img src="/rl-introduction-2nd-edit/tex/ac5fc6bb75d77e4b6a16e3a7946496b3.svg?invert_in_darkmode&sanitize=true" align=middle width=11.49544109999999pt height=24.7161288pt/>, <img src="/rl-introduction-2nd-edit/tex/89f2e0d2d24bcf44db73aab8fc03252c.svg?invert_in_darkmode&sanitize=true" align=middle width=7.87295519999999pt height=14.15524440000002pt/>, <img src="/rl-introduction-2nd-edit/tex/27f85042b2e9be54d56179a2dd20c45a.svg?invert_in_darkmode&sanitize=true" align=middle width=88.69078679999998pt height=24.7161288pt/>를 위한 열이 있어야 하고, <img src="/rl-introduction-2nd-edit/tex/14c39a9a3baf9c383416a0397c86091a.svg?invert_in_darkmode&sanitize=true" align=middle width=118.82757974999998pt height=24.7161288pt/>을 만족하는 모든 순서쌍 <img src="/rl-introduction-2nd-edit/tex/2e2229748ecb39fedc7d1588664c0bc9.svg?invert_in_darkmode&sanitize=true" align=middle width=71.28802559999998pt height=24.7161288pt/> 각각에 대해 하나의 행이 있어야 한다.
>

5. `3.1`절의 방정식들은 연속된 경우에 대한 것이라서 에피소딕 작업에 적용하려면 (아주 조금) 수정할 필요가 있다. 식 3.3의 수정된 버전을 제시함으로써 필요한 수정이 무엇인지 알고 있음을 보여라.

* 식 3.3: 모든 <img src="/rl-introduction-2nd-edit/tex/ea17b6fc02340f2b2ffd6a680fc5c50c.svg?invert_in_darkmode&sanitize=true" align=middle width=108.68642399999999pt height=24.65753399999998pt/> 에 대해 <img src="/rl-introduction-2nd-edit/tex/154c92b0592ac187131448ec45854e35.svg?invert_in_darkmode&sanitize=true" align=middle width=215.67675195pt height=24.7161288pt/>

>

6. 막대 균형 잡기 작업을 에피소딕 작업으로 다루지만 할인도 이용한다고 가정해 보자. 실패에 대한 보상은 -1이고 그 밖의 보상은 0이다. 이때 매 순간의 이득은 무엇인가? 이 이득은 할인을 이용한 연속적인 작업 형식에서의 이득과 어떻게 다른가?
>

7. 미로를 달리는 로봇을 설계한다고 가정해 보자. 미로를 탈출하면 로봇에게 +1의 보상을 주고 그 밖의 보상은 0을 주기로 결정했다고 해 보자. 이 작업은 자연스럽게 여러 개의 에피소드, 즉 미로를 달리는 연속적인 시도로 나누어지는 것처럼 보인다. 그래서 이 작업을 보상의 총합에 대한 기대값(식 3.7)을 최대화하는 것을 목표로 하는 에피소딕 작업으로 다루기로 결정했다고 해 보자. 잠깐 동안 로봇을 학습시킨 후에도 로봇이 미로를 탈출하는 데 있어 개선되는 모습을 보이지 못한다고 해 보자. 무엇이 잘못되었는가? 로봇에게 이루고자 하는 것이 무엇인지 효과적으로 전달했는가?

* 식 3.7: <img src="/rl-introduction-2nd-edit/tex/d12b3d69581e6856099257d2acc5abcf.svg?invert_in_darkmode&sanitize=true" align=middle width=266.9271264pt height=22.465723500000017pt/>
>

8. <img src="/rl-introduction-2nd-edit/tex/cd1e5bc22b389e724ed3c1c236dadbdb.svg?invert_in_darkmode&sanitize=true" align=middle width=52.346134499999984pt height=21.18721440000001pt/>이고 다음과 같이 보상이 주어진다고 가정해 보자.
    \begin{equation}R_{1}=-1, R_{2}=2, R_{3}=6, R_{4}=3, R_{5}=2\end{equation}
이때 <img src="/rl-introduction-2nd-edit/tex/8c4e06d0ac7cab63d8cb5e513560b16a.svg?invert_in_darkmode&sanitize=true" align=middle width=42.02615174999998pt height=22.465723500000017pt/>이다. <img src="/rl-introduction-2nd-edit/tex/9fce4f2c1c76c301d82c8c4d3060fc1c.svg?invert_in_darkmode&sanitize=true" align=middle width=103.910697pt height=22.465723500000017pt/>는 얼마인가? 힌트: 거꾸로 접근하라.    
>

9. <img src="/rl-introduction-2nd-edit/tex/a17536fdefed1ff20eae25df5c427e53.svg?invert_in_darkmode&sanitize=true" align=middle width=52.346134499999984pt height=21.18721440000001pt/>이고, 보상의 나열은 첫 항만 <img src="/rl-introduction-2nd-edit/tex/3e4eca8e7a2fdf160a39329136a0d9f4.svg?invert_in_darkmode&sanitize=true" align=middle width=49.99277579999999pt height=22.465723500000017pt/>이고 이후로는 모두 7이라고 가정해 보자. <img src="/rl-introduction-2nd-edit/tex/b598a01b0b2876cf6751005227ef9149.svg?invert_in_darkmode&sanitize=true" align=middle width=19.477190699999987pt height=22.465723500000017pt/>과 <img src="/rl-introduction-2nd-edit/tex/a9f4e880a8d38544547b331b0137079e.svg?invert_in_darkmode&sanitize=true" align=middle width=19.477190699999987pt height=22.465723500000017pt/>은 얼마인가?
>

10. 식 3.10의 두 번째 부등식을 증명하라.
* 식 3.10: <img src="/rl-introduction-2nd-edit/tex/0b11dbaaab0260ba096c4ee816a0f2a1.svg?invert_in_darkmode&sanitize=true" align=middle width=151.29447629999999pt height=27.91243950000002pt/>

>
    