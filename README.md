# Automatic_TimeTable_Maker :clipboard:

<!--### 대학교 시간표 자동 완성 프로그램-->

## Index
  - [Overview](#overview) 
  - [Getting Started](#getting-started)
  - [Authors](#authors)
  - [License](#license)

## Overview
대학생들은 매 학기를 시작하기 전 필수로 수강신청을 거치게 된다. 본 수강신청 전 학교에서 공개한 강의 계획서를 보면서 자신만의 기준에서 가장 best인 시간표를 만들기 위해 많은 경우의 수를 계산하곤 한다. 본인의 경우에는 일단 강의계획서를 보면서 가장 듣고 싶은 과목과 대체 과목 혹은 들어보고 싶은 과목들을 일단 모두 선택한 후 수업시간이 겹치는 과목들을 하나씩 제거하면서 최적의 시간표를 만들어 낸다. 

또한, 최근에 대면수업이 다시 재개되면서 공강 일수 및 점심시간 확보 등이 시간표를 짜는데 중요한 요소로 고려되곤 한다.

본인의 소속 학교 수강신청의 경우 원하는 과목을 체크하고 저장 버튼 하나만 누르면 수강신청이 완료되지만 대부분 학교의 수강신청은 자신이 사전에 매긴 우선순위에 따라 과목 당 하나씩 클릭을 눌러 과목 신청을 한다. 즉, 수강신청 전까지 best 시간표 도출 및 과목 당 우선순위도 따져야 한다. 

이러한 번거로움을 해결하기 위해 본 프로젝트에서는 자신이 사전에 정한 과목의 정보를 모두 입력해놓고 자신이 원하는 조건(피하고 싶은 교시, 원하는 공강날짜, 점심시간 확보)를 개인의 기준에 따라 입력하면 가장 best 조합의 시간표 과목 및 시간표 내에서의 과목 우선순위를 도출해낸다.

즉, 해당 프로그램을 통해 대학생들은 매 학기마다 시간표를 짜는 번거로움을 해결할 수 있다.

### 사용된 기술
- Flask framework
- python
- html
- css

### 화면 구성
|app.py|URL|TEMPLATES|
|-------|-----|--------|
|main(메인 페이지)|localhost:5000|main.html|
|select(과목입력 및 조건선택)|localhost:5000/select|select.html|
|result(조합 완료 페이지)|localhost:5000/result|result.html|

### 업로드 파일 설명
|폴더명|설명|
|-----|-----|
|.vscode||
|__ pycache __||
|static||
|static - img||
|static - css||
|templates||

|파일명|설명|
|-----|----|
|.gitignore||
|License||
|README.md||
|app.py||

### 전반적인 프로그램 개요 설명
1. main page
2. select page
3. result page

## Getting Started
**click `Use this template` and use this template!**
<!--
### Depencies
 Write about need to install the software and how to install them 
-->
### Installing
<!-- A step by step series of examples that tell you how to get a development 
env running

Say what the step will be

    Give the example

And repeat

    until finished
-->
1. Click `Use this template` button 
2. Create New Repository
3. Update Readme and Others(Other features are noted in comments.)

프로젝트를 처음 사용하기 위해 필요한 내용 포함
- 프로젝트를 설치, 사용하기 위해 필요한 전제조건이 있는가
- 어떻게 설치, 사용, 테스트하는가
- 설치 가이드 문서는 어디에 있는가
<!--
## Deployment
 Add additional notes about how to deploy this on a live system
 -->

## Authors
  - **Jieun Im** - <jieun776121@gmail.com>

## License

```
Copyright 2022 ImJieunn

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
