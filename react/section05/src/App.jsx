import "./App.css";
import Header from "./components/Header"; // Header.jsx를 가져오기 vite에서는 확장자 생략 가능
import Main from "./components/Main";
import Footer from "./components/Footer";
import Button from "./components/Button";
function App() {
  const buttonProps = {
    text: "메일",
    color: "red",
    a: 1,
    b: 2,
    c: 3,
  };
  return (
    <>
      <Button {...buttonProps} />
      <Button text={"카페"} />
      <Button text={"블로그"}>
        <Header />
      </Button>
    </>
  );
}

export default App;
