// 1. Date 객체를 생성하는 방법
let date1 = new Date(); // new키워드와 함께 객체를 생성하는걸 생성자라고 함
// console.log(date1); // Sat Apr 06 2024 21:00:23 GMT+0900 (한국 표준시)
// let date2 = new Date("1996/06/10/10:10:10");
// 대쉬, 닷, 슬래시 가능
// 시간은 : 콜론으로 표현
let date2 = new Date(1996, 6, 10, 10, 10, 10);
// 문자열 말고도 ,콤마로 구문해서 표시하는것도 가능
// console.log(date2);

// 2. 타임 스탬프
// 특정 시간이 "1970.01.01 00시 00분 00초"로 부터 몇 ms가 지났는지 의미하는 숫자값
let ts1 = date1.getTime();
let date4 = new Date(ts1);
console.log(ts1);
console.log(date4);

// 3. 시간 요소들을 추출하는 방법
let year = date1.getFullYear();
let month = date1.getMonth() + 1;
let date = date1.getDate();

let hour = date1.getHours();
let minute = date1.getMinutes();
let seconds = date1.getSeconds();
console.log(year, month, date, hour, minute, seconds);
// 자바스크립트의 월은 0부터 시작

// 4. 시간 수정하기
date1.setFullYear(2023);
date1.setMonth(0); //0부터 시작하기때문에 0를 넣으면 1월로 셋팅
date1.setDate(20);

date1.setHours(23);
date1.setMinutes(59);
date1.setMinutes(59);
console.log(date1);

// 5. 시간을 여러 포맷으로 출력하기
console.log(date1.toDateString()); // 날짜만 출력
console.log(date1.toLocaleString()); // 현지화된 포멧으로 출력
