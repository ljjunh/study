import "./App.css";
import Header from "./components/Header"; // Header.jsx를 가져오기 vite에서는 확장자 생략 가능
import Main from "./components/Main";
import Footer from "./components/Footer";
function App() {
  return (
    <>
      <Header />
      <Main />
      <h1>안녕 리액트!</h1>
      <Footer />
    </>
  );
}

export default App;
