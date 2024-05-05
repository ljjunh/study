import "./App.css";
import Viewer from "./components/Viewer";
import Controller from "./components/Controller";
import { useState, useEffect, useRef } from "react";
import Even from "./components/Even";
function App() {
  const [cnt, setCnt] = useState(0);
  const [input, setInput] = useState("");
  const isMount = useRef(false);
  // 1. 마운트 : 탄생
  useEffect(() => {
    console.log("mount");
  }, []); //useEffect에 빈배열을 넣으면 mount될 때 한번만 실행됨

  // 2. 업데이트 : 변화, 리렌더링
  useEffect(() => {
    console.log("update");
  }); // useEffect 두번째 인자로 아무것도 안넣으면 mount될때, update될때 모두 콜백함수 실행

  // 3. mount시점을 제외하고, 진짜 업데이트때만 실행하고싶으면
  // 컴포넌트가 마운트 되었는지 안되었는지를 체크하는 변수를 useRef로 만들고 초기값 false를 준다
  // 컴포넌트가 마운트 될때 isMount는 false니까 if문에 걸리고 true로 바뀐뒤 return으로 종료하면
  // 그 다음 진짜 update에는 if문에 걸리지 않고 나머지 코드가 실행된다.
  useEffect(() => {
    if (!isMount.current) {
      isMount.current = true;
      return;
    }
    console.log("realUpdate");
  });

  const onClickButton = (value) => {
    setCnt(cnt + value);
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
        ></input>
      </section>
      <section>
        <Viewer cnt={cnt} />
        {cnt % 2 === 0 ? <Even /> : null}
      </section>
      <section>
        <Controller onClickButton={onClickButton} />
      </section>
    </div>
  );
}

export default App;
