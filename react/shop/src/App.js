import "./App.css";
import { Navbar, Nav, Container } from "react-bootstrap";
import { useState, createContext } from "react";
import data from "./data.js";
import { Routes, Route, useNavigate } from "react-router-dom";
import Detail from "./pages/Detail.js";
import axios from "axios";
import Cart from "./pages/Cart.js";

export const Context1 = createContext();

function App() {
  const [shoes, setShoes] = useState(data);
  const [count, setCount] = useState(2);
  const [stock, setStock] = useState([10, 11, 12]);

  const nav = useNavigate();
  return (
    <div className="App">
      <Navbar bg="light" variant="light">
        <Container>
          <Navbar.Brand href="#home">ShoeShop</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link
              onClick={() => {
                nav("/");
              }}
            >
              Home
            </Nav.Link>
            <Nav.Link
              onClick={() => {
                nav("/cart");
              }}
            >
              Cart
            </Nav.Link>
          </Nav>
        </Container>
      </Navbar>

      <Routes>
        <Route
          path="/"
          element={
            <div>
              {" "}
              <div className="main-bg"></div>
              <div className="container">
                <div className="row">
                  {shoes.map((item, idx) => {
                    return <Card key={item.id} shoes={item} i={idx + 1} />;
                  })}
                </div>
              </div>
              <button
                onClick={() => {
                  if (count > 3) {
                    alert("상품 더 없음");
                    return;
                  }
                  axios
                    .get(
                      `https://codingapple1.github.io/shop/data${count}.json`
                    )
                    .then((res) => {
                      setShoes([...shoes, ...res.data]);
                      console.log(count);
                    })
                    .catch((err) => {
                      console.error(err);
                    });
                }}
              >
                버튼
              </button>
            </div>
          }
        />
        <Route
          path="/detail/:id"
          element={
            <Context1.Provider value={{ stock, shoes }}>
              <Detail shoes={shoes} />
            </Context1.Provider>
          }
        />
        <Route path="/cart" element={<Cart />} />
      </Routes>
    </div>
  );
}

function Card(props) {
  return (
    <div className="col-md-4">
      <img
        src={`https://codingapple1.github.io/shop/shoes${props.i}.jpg`}
        width="80%"
      />
      <h4>{props.shoes.title}</h4>
      <p>{props.shoes.content}</p>
    </div>
  );
}

export default App;
