(6/26)
과제 1일차
![image](https://user-images.githubusercontent.com/101690974/175804159-99b5a31b-4046-4f58-a391-7017e4c2d0b0.png)
일단 html홈페이지에 구조가 이상하게 나타났다.

![image](https://user-images.githubusercontent.com/101690974/175803853-9406554c-91f2-4d62-aa37-1be6b3ecd0e7.png)

post요청을 보내니 서버에서 403메세지가 나온다.

![image](https://user-images.githubusercontent.com/101690974/175804212-1487eefc-db3a-458f-a47a-e8d098d4965d.png)
postman으로 확인했을 때도 get은 계속 HELLO WORLD가 나오고

![image](https://user-images.githubusercontent.com/101690974/175804235-96766d22-a082-402e-915a-2a52aae1feae.png)
post를 보내니까 이상한 코드가 나온다.


(6/28)
과제 2일차
1일차에 postman에서 발생하였던 csrf오류는 setting.py에서 해당 부분을 주석 처리함으로 해결 할 수 있었다. 이후 조금씩 코드 수정을 해서 post맨을 이용해서 원하는 post와 json데이터가 get 되는 것을 확인할 수 있었다.

![KakaoTalk_20220627_143136931](https://user-images.githubusercontent.com/101690974/176085306-5e28ef9c-8e8f-4365-9c89-28f5b3dc45c4.png)

![KakaoTalk_20220627_150250436](https://user-images.githubusercontent.com/101690974/176085265-805e17e1-a6eb-44b9-ae65-8eec72ff38ba.png)
