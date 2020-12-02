# Git Error

### warning: LF will be replaced by CRLF

-  원인 : OS마다 개행 문자가 달라고 발생하는 오류

  - Windows : CR(Carriage-Return, \r), LF(Line Feed, \n) 사용
  - Linux, Mac : LF(Line Feed, \n) 만 사용

- 해결

  - Windows 

  ```shell
  git config --global core.autocrlf true
  ```

  - Linux, Mac

  ```shell
  git config --global core.autocrlf input
  ```



---



