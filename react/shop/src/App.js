import "./App.css";
import { Navbar, Nav, Container, Row, Col } from "react-bootstrap";
import bg from "./img/bg.png";
import { useState } from "react";
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

function App() {
  let [shoes, setShoes] = useState(data);
  const [stock, setStock] = useState([10, 11, 12]);
  let navigate = useNavigate();
  const [btnCnt, setBtnCnt] = useState(0);
  const [loading, setLoading] = useState(false);
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
