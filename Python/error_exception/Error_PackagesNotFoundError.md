## Error : PackagesNotFoundError

#### (1) 오류 메시지

```
Collecting package metadata (current_repodata.json): ...working... done
Solving environment: ...working... failed with initial frozen solve. Retrying with flexible solve.
Collecting package metadata (repodata.json): ...working... done
Solving environment: ...working... failed with initial frozen solve. Retrying with flexible solve.


PackagesNotFoundError: The following packages are not available from current channels:

  - konlpy

Current channels:

  - https://repo.anaconda.com/pkgs/main/win-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/win-64
  - https://repo.anaconda.com/pkgs/r/noarch
  - https://repo.anaconda.com/pkgs/msys2/win-64
  - https://repo.anaconda.com/pkgs/msys2/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.
```



#### (2) 발생 원인

- Anaconda 공식 홈페이지에 등록된 패키지 리스트에 없어서 발생
  - Anaconda 공홈에서 패키지 검색 : https://anaconda.org/search?q=[패키지명]
- 현재 채널에 패키지가 없는 경우



#### (2.1) 'numpy' 검색 결과

![image](https://user-images.githubusercontent.com/71396432/108508325-f99ce200-72fe-11eb-81eb-c5978aac9cce.png)



#### (2.2) 'konlpy' 검색 결과

![image](https://user-images.githubusercontent.com/71396432/108508460-3072f800-72ff-11eb-85e7-67ea7f1f63b7.png)



#### (3) 오류 해결 방법

#### (3.1) Python 3.3 버전 전

```
conda install -c conda-forge [패키지명]
```

- 현재 설치된 python 버전은 3.7.9와 3.8.5이여서 위의 명령어가 먹히지 않았다.



#### (3.2) Python 3.3 버전 이상

- Python 3.3 버전 부터는 conda-forge  명령어가 실행되지 않음

- 아래의 명령어를 통해 Anaconda **신규 채널 생성**

```
conda create -n envname python=[버전] -c anaconda
```

참고 link : https://stackoverflow.com/questions/61041962/conda-packagesnotfounderror

- 위의 방법은 적용해보지 않음
- 실제 해결 방법 : [KoNLPy 패키지 설치](https://github.com/Journey-R/KoNLP/blob/master/install_konlpy.md)