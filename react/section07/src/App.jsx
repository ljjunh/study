import "./App.css";
import Viewer from "./components/Viewer";
import Controller from "./components/Controller";
import Even from "./components/Even";
import { useState, useEffect, useRef } from "react";
function App() {
  const [count, setCount] = useState(0);
  const [input, setInput] = useState("");
  const isMount = useRef(false);
  // 1. 마운트 : 탄생
  useEffect(() => {
    console.log("mount");
  }, []);
  // 콜백함수를 넣은 뒤 deps로는 빈 배열을 넣으면 됨
  // useEffect는 deps의 값이 변경되어야만 실행되기 때문에
  // deps값을 넣지 않으면, 콜백함수는 컴포넌트가 처음 mount 된 후에는 실행되지 않음

  // 2. 업데이트 : 변화, 리렌더링
  useEffect(() => {
    if (!isMount.current) {
      isMount.current = true;
      return;
    }
    console.log("update");
  });
  // 첫번째 인수로 콜백함수를 넣고, 두번째 deps는 생략
  // deps를 생략하면 콜백함수는 마운트 될 때 한번 실행되고
  // 컴포넌트가 리렌더링 될 때마다(업데이트) 실행됨
  // mount 시점도 제외하고 업데이트될때만 실행하고 싶으면
  // 컴포넌트가 마운트 되었는지 체크하는 변수를 useRef로 사용

  // 3. 언마운트 : 죽음
  // components폴더 안의 Even컴포넌트에 정의

  // useEffect
  // 첫번째 인수 콜백함수, 두번째 인수 배열
  // 두번째인수로 들어간 배열이 바뀌면 첫번째 인수로 들어간 콜백함수가 실행됨
  // 두번째 인수로 들어간 배열에 의존하기때문에 의존성 배열, deps(dependency array)라고 부름
  // 이렇게 state가 변경될때마다 특정작업을 할꺼면 그냥 setSate뒤에 쓰면 되지 않나? 라고 생각할 수 있는데
  // setState는 비동기 요청이라서 언제 끝날지 몰라서 꼬일수도 있음
  // useEffect(() => {
  //   console.log(`count: ${count} / input: ${input}`);
  // }, [count, input]);

  const onClickButton = (value) => {
    setCount(count + value);
  };
  return (
    <div className="App">
      <h1>Simple Counter</h1>
      <section>
        <input
          value={input}
          onChange={(e) => {
            setInput(e.target.value);
          }}
        />
        {input}
      </section>
      <section>
        <Viewer count={count} />
        {count % 2 === 0 && <Even />}
      </section>
      <section>
        <Controller onClickButton={onClickButton} />
      </section>
    </div>
  );
}

export default App;
