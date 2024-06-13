import "./App.css";
import HookExam from "./components/HookExam";
// 컴포넌트 리랜더링 상황
// 자신이 관리하는 state값 변경시
// 자신이 제공받는 props값 변경시
// 부모 컴포넌트가 리렌더링 될때

function App() {
  return (
    <>
      <HookExam />
    </>
  );
}

export default App;
