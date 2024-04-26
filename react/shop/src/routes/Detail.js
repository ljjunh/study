import { Container, Row, Col } from "react-bootstrap";
import { useParams } from "react-router-dom";
const Detail = (props) => {
  let { id } = useParams();
  // 유저가 URL파라미터에 입력한거 가져오려면 useParams()
  return (
    <Container>
      <Row>
        <Col md={6}>
          <img
            src="https://codingapple1.github.io/shop/shoes1.jpg"
            width="100%"
          />
        </Col>
        <Col md={6}>
          <h4>{props.shoes[id].title}</h4>
          <p>{props.shoes[id].content}</p>
          <p>{props.shoes[id].price}원</p>
          <button className="btn btn-danger">주문하기</button>
        </Col>
      </Row>
    </Container>
  );
};
export default Detail;
