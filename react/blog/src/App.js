//array,object state변경하는법 까지 들었음
//Component 들으면 됨

/* eslint-disable */
// import해놓고 안쓰는거나 선언해놓고 안쓰는 변수들 warning으로 알려주는건데 귀찮아서 일단 끔

import "./App.css";
import { useState } from "react";

function App() {
  const [title, setTitle] = useState([
    "남자 코트 추천",
    "강남 우동맛집",
    "파이썬독학",
  ]);
  // useState에 ['기본값', 함수]들어있고 Destructuring문법으로
  // const [a, b] 에 기본값과 함수를 넣어주는거임
  // 왜 let놔두고 state를 써야함?
  // let은 변경되더라도 리렌더링이 안되는데, state는 변경될때마다 html전체가 자동으로 리렌더링 됨
  const [like, setLike] = useState([0, 0, 0]);

  // 동적인 UI만드는 step
  // 1. html css로 미리 디자인 완성
  // 2. UI의 현재 상태를 state로 저장
  // 3. state에 따라 UI가 어떻게 보일지 작성
  let [modal, setModal] = useState(false);

  // map함수
  // 1.왼쪽 array 자료길이만큼 내부코드 실행해줌
  // 2. return문에 있는걸 array로 담아서 반환해줌
  // 3. 유용한 파라미터 2개(배열값, 인덱스)사용 가능
  let [idx, setIdx] = useState(0);
  return (
    <div className="App">
      <div className="black-nav">
        <h4>ReactBlog</h4>
      </div>
      <button
        onClick={() => {
          let copy = [...title];
          copy.sort();
          setTitle(copy);
        }}
      >
        가나다순정렬
      </button>

      <button
        onClick={() => {
          // state변경 함수는 기존state와 신규 state가 다른 경우에만 변경을 해줌
          // 참조형객체는 얕은복사를 하면 주소값을 복사해와서 새로운값을 변경하면 원본도 변경됨
          // 그래서 새로운 값을 변경하고 state변경함수에 넣으면 기존state값도 바껴있어서 결국 기존state==신규state라서
          // 변경을 안해줌
          // 해결방법은 spread나 다른 deepcopy로 원본데이터를 깊은복사해서 변경 후에 state변경 함수에 넣어줘야함
          let copy = [...title];
          copy[0] = "여자 코트 추천";
          setTitle(copy);
        }}
      >
        버튼
      </button>

      {/* <div className="list">
        <h4>
          {title[0]}
          <span onClick={likeUp}>👍</span>
          {like}
        </h4>
        <p>2월 17일 발행</p>
      </div>
      <div className="list">
        <h4>{title[1]}</h4>
        <p>2월 17일 발행</p>
      </div>
      <div className="list">
        <h4
          onClick={() => {
            setModal(!modal);
          }}
        >
          {title[2]}
        </h4>
        <p>2월 17일 발행</p>
      </div> */}

      {title.map(function (a, i) {
        return (
          <div className="list" key={i}>
            <h4
              onClick={() => {
                setModal(!modal);
                setIdx(i);
              }}
            >
              {title[i]}
              <span
                onClick={() => {
                  let copy = [...like];
                  copy[i]++;
                  setLike(copy);
                }}
              >
                👍
              </span>
              {like[i]}
            </h4>
            <p>2월 17일 발행</p>
          </div>
        );
      })}
      {modal ? <Modal title={title} setTitle={setTitle} idx={idx} /> : null}
    </div>
  );
}
// props
// props전송은 부모->자식만 가능(불륜, 패륜 금지)
// 1. 부모 -> 자식 state 전송하는 법
// 2. <자식컴포넌트 작명={state이름}>
// 3. props 파라미터 등록 후 porps.작명

function Modal(props) {
  return (
    <div className="modal" style={{ background: props.color }}>
      <h4>{props.title[props.idx]}</h4>
      <p>날짜</p>
      <p>상세내용</p>
      <button>글수정</button>
    </div>
  );
}

export default App;
