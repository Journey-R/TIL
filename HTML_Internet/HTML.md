# HTML 

- Hypertext Markup Language
- 전 세계 웹페이지 분석 결과 정리 - 사용 빈도수 높은 태그 등 
  - https://www.advancedwebranking.com/html/
- 사용 빈도수 높은 태그

![image](https://user-images.githubusercontent.com/71396432/104194634-e9265b80-5464-11eb-8cb7-342fcf87bce0.png)





---



## tag > html 문서 기본 태그

- **html**
  - head, body를 감싸는 태그
  - `<!doctype html>` 다음에 위치함



- **head**

  - body 태그를 설명하는 태그

    

    - title (head 하위)

      - 웹 페이지 제목

        

    - meta (head 하위)

      - 속성
        - charset : 인코딩 방식 



- **body**
  - 본문



```html
<!DOCTYPE html>
<html>

<head>
    <title>WEB1 - html</title>
    <meta charset = "utf-8">
</head>

<body>
	<h1>HTML이란 무엇인가?</h1>

    <p>Hypertext Markup Language(HTML) is the standard markup language for <b>creating web pages</b> and web application.</p>
</body>

</html>
```



## tag > text

- strong (= b)

  - 글자 굵게

    ```html
    HTML is the standard markup language for <b>creating web pages</b> and web application.
    ```

    - HTML is the standard markup language for <b>creating web pages</b> and web application.

  - strong

    ```html
    HTML is the standard markup language for <strong>creating web pages</strong> and web application.
    ```

    - HTML is the standard markup language for <strong>creating web pages</strong> and web application.

  

- u

  - 밑줄

    ```html
    HTML is the standard markup language for <b>creating <u>web</u> pages</b> and web application.
    ```

    - HTML is the standard markup language for <b>creating <u>web</u> pages</b> and web application.



- h1~h6 

  - 제목
  - 자동 개행

  ```html
  <h1>This is heading 1</h1>
  <h2>This is heading 2</h2>
  <h3>This is heading 3</h3>
  <h4>This is heading 4</h4>
  <h5>This is heading 5</h5>
  <h6>This is heading 6</h6>
  ```

  <h1>This is heading 1</h1>

  <h2>This is heading 2</h2>

  <h3>This is heading 3</h3>

  <h4>This is heading 4</h4>

  <h5>This is heading 5</h5>

  <h6>This is heading 6</h6>



## tag > 개행 / 단락, 문단

- br

  - 개행

  ```html
  Hypertext Markup Language(HTML) is the standard markup language for <b>creating web pages</b> and web application.<br>
  Hypertext Markup Language(HTML) is the standard markup language for <strong>creating <u>web</u> pages</strong> and web application.
  ```

  Hypertext Markup Language(HTML) is the standard markup language for <b>creating web pages</b> and web application.<br>

  Hypertext Markup Language(HTML) is the standard markup language for <strong>creating <u>web</u> pages</strong> and web application.



- p

  - 단락, 문단

  ```html
  <p>Hypertext Markup Language(HTML) is the standard markup language for <b>creating web pages</b> and web application.</p>
  Hypertext Markup Language(HTML) is the standard markup language for <strong>creating <u>web</u> pages</strong> and web application.
  ```

  <p>Hypertext Markup Language(HTML) is the standard markup language for <b>creating web pages</b> and web application.</p>
  Hypertext Markup Language(HTML) is the standard markup language for <strong>creating <u>web</u> pages</strong> and web application.



## tag > 이미지

- img

  - 속성

    - src : 이미지 주소(웹 페이지 주소, 로컬 주소)
    - width : 너비(기본 단위 : 픽셀)
      - px, % 등

    ```html
    <img src = "coding.jpg" width = "100%">
    ```

    



## tag > 목록

- li
  - list
  - ul, ol 태그의 자식 태그



- ul (Unordered List)

  - li 태그의 부모 태그, 범위
  - 순번 없음

  ```html
  <ul>
  	<li>HTMl</li>
  	<li>CSS</li>
  	<li>JavaScript</li>
  </ul>
  ```

<ul>
	<li>HTMl</li>
	<li>CSS</li>
	<li>JavaScript</li>
</ul>



- ol (Orderd List)

  - li 태그의 부모 태그, 범위
  - 순번 있음

  ```html
  <ol>
  	<li>HTMl</li>
  	<li>CSS</li>
  	<li>JavaScript</li>
  </ol>
  ```

<ol>
	<li>HTMl</li>
	<li>CSS</li>
	<li>JavaScript</li>
</ol>



## tag > a

- a (anchor)
  - link 
  - 속성
    - href
      - 참조 링크 주소
    - target
      - 연결 페이지 open 형식
        - _self : 현재 창에서 open (default)
        - _blank : 새창에서 open
        - _parent : 부모(상위 레벨) 창에서 open(부모가 없으면 _self와 동일)
        - _top : 가장 상위 창에서 open(전체 브라우저 창에서 & 부모가 없으면 _self와 동일)
        - frame name : 지정된 프레임 안에서 open
    - title
      - 툴팁





---



## HTML의 중요성

- 검색 엔진을 통한 검색시, 헤더 태그 사용 여부에 따른 차이

  - `<h1>`~`<h6>` 태그 사용 vs 미사용
    - 화면을 예쁘게 꾸미기 위해 페이지의 제목을 이미지로 대체하거나 `<h숫자>`태그 외의 다른 태그 사용시, 검색 결과 정렬에서 하위에 노출된다.

  