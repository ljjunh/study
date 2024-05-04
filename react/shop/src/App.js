import "./App.css";
import { Navbar, Nav, Container, Row, Col } from "react-bootstrap";
import bg from "./img/bg.png";
import { useEffect, useState } from "react";
import data from "./data";
import Card from "./components/Card";
import Detail from "./routes/Detail";
import Cart from "./routes/Cart";
import axios from "axios";
import {
  Routes,
  Route,
  Link,
  useNavigate,
  Outlet,
  useParams,
} from "react-router-dom";
import { useQuery } from "react-query";

function App() {
  // localStorage 사용
  // array / object -> JSON변환은 JSON.stringify()
  // JSON -> array / object -> JSON.parse()
  // let obj = { name: "kim" };
  // localStorage.setItem("data", JSON.stringify(obj));
  // let tmp = localStorage.getItem("data");
  // console.log(tmp);
  // 이렇게 편법으로 array나 object넣으면 꺼낼때 json으로 꺼내짐 ex) {"name":"kim"}
  // tmp.name 이런식으로 접근 불가능해서 다시 array/object로 바꿔줘야됨
  // console.log(JSON.parse(tmp));

  useEffect(() => {
    if (localStorage.getItem("watched")) {
      return;
    } else {
      localStorage.setItem("watched", JSON.stringify([]));
    }
  }, []);

  let [shoes, setShoes] = useState(data);
  const [stock, setStock] = useState([10, 11, 12]);
  let navigate = useNavigate();
  const [btnCnt, setBtnCnt] = useState(0);
  const [loading, setLoading] = useState(false);

  //useQuery 장점
  // 1. 성공/실패/로딩중 쉽게 파악 가능
  // 2. 틈만나면 자동으로 refetch 해줌
  // 3. 실패시 retry 알아서 해줌
  // 4. state공유 안해도 됨
  //    자식컴포넌트에서 데이터를 쓰고싶으면 똑같이 axios로 요청해주면 됨
  //    같은 요청이면 알아서 두번요청 안하고 한번만 해줌
  // 5. ajax결과 캐싱 가능
  let result = useQuery("작명", () => {
    return (
      axios.get("https://codingapple1.github.io/userdata.json").then((res) => {
        return res.data;
      }),
      { stableTime: 2000 } // refetch되는 간격 설정가능
      //2초안에는 다시 refetch 되지 않음
    );
  });

  return (
    <div className="App">
      <Navbar bg="light" variant="light">
        <Container>
          <Navbar.Brand href="#home">ShoeShop</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link
              onClick={() => {
                navigate("/");
              }}
            >
              Home
            </Nav.Link>
            <Nav.Link
              onClick={() => {
                navigate("/cart");
              }}
            >
              Cart
            </Nav.Link>
            <Nav.Link
              onClick={() => {
                navigate("/about");
              }}
            >
              About
            </Nav.Link>
          </Nav>
          <Nav className="ms-auto">
            {result.isLoading && "로딩중"}
            {result.error && "에러남"}
            {result.data && result.data.name}
          </Nav>
        </Container>
      </Navbar>

      <Routes>
        <Route
          path="/"
          element={
            <>
              <div
                className="main-bg"
                style={{ backgroundImage: `url(${bg})` }}
              ></div>

              <Container>
                <Row>
                  {shoes.map((arr, idx) => {
                    return <Card arr={arr} idx={idx} />;
                  })}
                </Row>
              </Container>

              {btnCnt < 3 ? (
                <button
                  onClick={() => {
                    setLoading(true);
                    setBtnCnt(btnCnt + 1);
                    axios
                      .get(
                        `https://codingapple1.github.io/shop/data${
                          btnCnt + 1
                        }.json`
                      )
                      .then((res) => {
                        setLoading(false);
                        let copy = [...shoes, ...res.data];
                        setShoes(copy);
                      })
                      .catch((error) => {
                        setLoading(true);
                        console.log(error);
                      });
                  }}
                >
                  버튼
                </button>
              ) : null}
              {loading ? <div>로딩중입니다</div> : null}
            </>
          }
        />
        <Route path="/detail/:id" element={<Detail shoes={shoes} />} />
        {/* /detail/뒤에는 동적으로 변하는 값을 받기위해 :사용  뒤의 id는 가독성과 명확성을 위해 씀 식별자의 역할이라서 대부분 id를 씀*/}
        <Route path="/cart" element={<Cart />} />
      </Routes>
    </div>
  );
}

export default App;
