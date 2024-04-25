import "./App.css";
import { Navbar, Nav, Container, Row, Col } from "react-bootstrap";
import bg from "./img/bg.png";
import { useState } from "react";
import data from "./data";
import ColTag from "./components/ColTag";
function App() {
  let [shoes, setShoes] = useState(data);
  return (
    <div className="App">
      <Navbar bg="light" variant="light">
        <Container>
          <Navbar.Brand href="#home">ShoeShop</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Cart</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      <div className="main-bg" style={{ backgroundImage: `url(${bg})` }}></div>

      <Container>
        <Row>
          {shoes.map((arr, idx) => {
            return <ColTag shoes={shoes} idx={idx} />;
          })}
        </Row>
      </Container>
    </div>
  );
}

export default App;
