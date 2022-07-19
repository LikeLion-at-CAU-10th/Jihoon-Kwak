저번 세션에서 만들었던 PROFILE로 진행하지 않고 새로 record라는 model을 만든 후에 
diary라는 model을 만들어 diary가 record를 상속받는 model로 설정하였습니다.

<img width="671" alt="detailPOST" src="https://user-images.githubusercontent.com/101690974/179668397-6cb2ec41-2354-43c4-b0ea-fb00a01ff63b.PNG">
이건 post man을 활용하여 detail을 전송한 결과입니다 raw의 body로 보냈을 때는 계속 알수없는 오류가 발생하여 postman에서 제공해주는 form으로
전송하였더니 잘 되었습니다

<img width="670" alt="deatilADMIN" src="https://user-images.githubusercontent.com/101690974/179668356-167af64c-b642-4734-af39-4312497c458c.PNG">
admin에 들어가보니 방금 보낸 detail이 잘 전송되었음을 알 수 있었습니다.
