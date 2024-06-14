import { useReducer } from "react";

// reducer : 변환기
// 상태를 실제로 변화시키는 변환기 역할
function reducer(state, action) {
  // 액션 객체가 많아지면 if문 대신 switch문 사용
  switch (action.type) {
    case "INCREASE":
      return state + action.data;
    case "DECREASE":
      return state - action.data;
    default:
      return state;
  }
}

const Exam = () => {
  // dispatch : 상태변화가 있어야 한다는 사실을 알리는, 발송하는 함수
  // 첫번째 인자 : 상태를 변환시키는 함수(reducer function), 두번째 인자 : state의 초기값
  const [state, dispatch] = useReducer(reducer, 0);

  const onClickPlus = () => {
    // 인자 : 상태가 어떻게 변화되길 원하는지 객체로(액션객체)
    dispatch({
      type: "INCREASE",
      data: 1,
    });
  };

  const onClickMinus = () => {
    dispatch({
      type: "DECREASE",
      data: 1,
    });
  };
  return (
    <div>
      <h1>{state}</h1>
      <button onClick={onClickPlus}>+</button>
      <button onClick={onClickMinus}>-</button>
    </div>
  );
};
export default Exam;
