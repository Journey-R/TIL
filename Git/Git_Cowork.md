# 협업자 추가

### (0) 협업자 추가 전

- master : 해당 repository 생성/관리자
  - 가능 : `clone`, `push`, `pull`
- slave : 해당 repository 사용자
  - 가능 : `clone`, `pull`
  - 불가능 : `push`



### (1) 협업자 추가 : master

1. Github 로그인
2. 해당 repository 이동
3. Settings
4. Manage access
5. Invite a collaborator
6. 협업자 추가(메일/이름)



### (2) 협업자 추가 : slave

1. 협업자 초대 메일에서 `수락`

- 수락 후에는 `push` 가능

---



# 협업 시나리오

## 1. 동기적 작업 : `push` & `pull`

- 동시 작업 불가(unsynchronize)

- branch 갯수 1개
  - 동시 작업이 불가능한 이유



### (1) 작업 순서 

- slave가 최초 : 원격 저장소 -> local : `git clone`

```shell
$ git clone https://github.com/Ryu-dot-line/collabo
```



- local -> 원격 저장소

```shell
$ git add file.md
$ git commit -m "commit msg"
$ git push origin master
```



- 원격 저장소 -> local : `git pull`

```shell
$ git pull origin master
```



## 2. 비동기적 작업 : `branch`

- 동시 작업 가능
- 테스트 가능
  - 원본 branch 외의 테스트 branch 통해 Test
  - 테스트 branch에서의 작업들은 **master(원본)에는 영향을 주지 않는다.**

- master : 원본 branch

  - 원본 branch은 사용자가 임의로 변경 가능하지만, master가 암묵적 원본

  

### (1) 현재 저장소에 있는 branch 목록 : `git branch`

```shell
$ git branch

# commit 목록 있을 경우에만 출력됨
* master
```



### (2) 현재 저장소에 branch 추가 :  `git branch [브랜치명]`

```shell
$ git branch Test

$ git branch
  Test
* master	# '*'이 있는 쪽이 현재 branch

* ~/branch (master)	# '(master)' : 현재의 branch
```



### (3) 특정 branch로 이동 : `git checkout [브랜치명]`

```shell
$ git checkout Test
Switched to branch 'Test'	# 'Test' branch로 이동

# branch 목록 및 현재의 branch 확인
$ git branch
* Test
  master
  
* ~/branch (Test)	# '(Test)' : 현재의 branch

$ git log
commit 0fabf23492ea0a2c7a1c88bb194f540d24697b29 (HEAD -> Test)	# commit 당시의 branch
Author: Ryu <*@gmail.com>
Date:   Wed Sep 16 14:48:40 2020 +0900
```

- `checkout` : 특정 버전으로 이동할 때도 쓰임



### (4) branch 삭제 : `git branch -d [브랜치명]`



### (5) branch 병합 : `git merge [합칠 브랜치명] `

- 대상 브랜치를 병합

- **★중요** : 주가 되는 브랜치로 이동★

- master가 test를 병합 -> master merge Test

- 순서

  1. 주가 되는 branch로 이동(master로 이동)   ★**중요**★

     ```shell
     $ git checkout master
     ```

  2. 병합

     ```shell
     $ git merge Test
     ```

  3. 옵션 : 테스트 branch 삭제 (테스트 branch 필요없을 경우)

     ```shell
     $ git branch -d Test
     ```



### (6) 특정 브랜치에 push : `git push [저장소명][브랜치명]`

- 최초의 `push` : branch 생성 및 push
- 그 이후의 `push` : push만

```shell
$ git push origin Test
```



- 원격저장소 페이지에서 `push` 결과 확인
  1. 원격저장소
  2. <> Code
  3. 하위의 brach 갯수 확인
  4. 하위의 브랜치명이 있는 콤보박스에서 해당 브랜치 선택
  5. master 브랜치와 Test 브랜치와의 차이점 확인 가능



### (6) 각자의 변화를 master에 반영 요청(Github) : `compare & pull request`

- compare & pull request
  - 각자의 변경사항을 반영 요청
  - 팀원1
- Pull requests
  - 각자의 변화를 master에 반영(`pull`/ `merge`) 시켜달라고 요청 (`request`)
  - 순서
    1. 해당 request로 이동
    2. Files chaned : 변경사항에 대한 리뷰 달 수 있음(라인별 리뷰도 가능)
    3. Conversation : 팀원들의 리뷰/코멘트 확인 및 최종 merge

- 일반적인 merge 권한
  - 팀장, pl, pm 등



### (9) Git-flow 참고

- 출처
  - 우아한형제들 기술 블로그 (https://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html)
  - https://nvie.com/posts/a-successful-git-branching-model/



- master : 제품으로 출시될 수 있는 브랜치
- develop : 다음 출시 버전을 개발하는 브랜치
- feature : 기능을 개발하는 브랜치
- release : 이번 출시 버전을 준비하는 브랜치
- hotfix : 출시 버전에서 발생한 버그를 수정 하는 브랜치

![우아한형제들 git-flow](https://woowabros.github.io/img/2017-10-30/git-flow_overall_graph.png)



### (7) cherry-pick

- 브랜치의 특정 파일/폴더만 병합



## 3. 다른 사용자의 원격저장소를 자기 원격저장소에 복제 : `fork`

- 순서

  1. 다른 사용자의 원격저장소의 프로젝트 -> 내 원격저장소로 복제


  2. clone 후 push 가능

  3. push 후 원본 사용자에게 pull request 요청 가능

  



